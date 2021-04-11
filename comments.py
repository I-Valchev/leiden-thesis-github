from collections import defaultdict

from utils import Query
from utils.API import API
from utils.FileLoader import FileLoader

api = API()
pull_requests = FileLoader.load('pull-requests.json')

repos = defaultdict(list)
for pr in pull_requests:
    if not pr['repo_name'] or not pr['number']:
        continue
    repos[pr['repo_name']].append(pr['number'])

comments = []
for i, repo in enumerate(repos):
    print("{:}/{:} ({:.2f}%)" .format(i, len(repos), (i / len(repos)*100)))
    try:
        # Omit the empty instances
        if not repos[repo]:
            continue
        [keys, query] = Query.getCommentsForRepo(repo, repos[repo])
        prComments = api.asArray(query, keys)
        comments += prComments

        if i % 1000 == 0:
            FileLoader.save('comments.json', comments)
    except:
        pass

FileLoader.save('comments.json', comments)

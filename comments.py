from utils import Query
from utils.API import API
from utils.FileLoader import FileLoader

api = API()
pull_requests = FileLoader.load('pull-requests.json')

comments = []
for i, pr in enumerate(pull_requests):
    print(i)
    # if i > 10:
    #     break

    # Omit the empty instances
    if not pr['repo_name']:
        continue
    [keys, query] = Query.getCommentsForOrgAndPr(pr['repo_name'], pr['number'])
    prComments = api.asArray(query, keys)
    comments += prComments

FileLoader.save('comments.json', comments)

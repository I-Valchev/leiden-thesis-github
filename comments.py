from utils import Query
from utils.API import API
from utils.FileLoader import FileLoader

api = API()
pull_requests = FileLoader.load('pull-requests.json')

comments = []

for pr in pull_requests:
    [keys, query] = Query.getCommentsForOrgAndPr(pr['repo_name'], pr['number'])
    comments = api.asArray(query, keys)
    comments.append(comments)

FileLoader.save('comments.json', comments)

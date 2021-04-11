from utils import Query
from utils.API import API
from utils.FileLoader import FileLoader


api = API()
orgs = FileLoader.load('orgs-community-size-2020.json')

pull_requests = []

for org in orgs:
    [keys, query] = Query.getPRsForOrg(org['org'])
    orgPRs = api.asArray(query, keys)
    pull_requests.append(orgPRs)

FileLoader.save('pull-requests.json', pull_requests)

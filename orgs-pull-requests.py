"""
Extracts all Pull Request numbers for the orgs
listed in data/orgs-community-size-2020.json.
Saves the output to data/pull-requests.json
"""

from utils import Query
from utils.API import API
from utils.FileLoader import FileLoader

api = API()
orgs = FileLoader.load('orgs-community-size-2020.json')

pull_requests = []

for org in orgs:
    [keys, query] = Query.getPRsForOrg(org['org'])
    orgPRs = api.asArray(query, keys)
    pull_requests += orgPRs

FileLoader.save('pull-requests.json', pull_requests)

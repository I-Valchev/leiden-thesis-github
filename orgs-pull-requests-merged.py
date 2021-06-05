"""
Extracts all organisations that are
listed in orgs-community-size-2020.json, finds
all merged Pull Requests in 2020.
Saves the output to data/pull-requests-status.json
"""

from utils import Query
from utils.API import API
from utils.FileLoader import FileLoader

api = API()
orgs = FileLoader.load('orgs-community-size-2020.json')

pull_requests = []

for org in orgs:
    [keys, query] = Query.getMergedPRsFrOrg(org['org'])
    orgPRs = api.asArray(query, keys)
    pull_requests += orgPRs

FileLoader.save('pull-requests-merged.json', pull_requests)

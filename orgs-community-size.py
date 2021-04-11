"""
Get the orgs with the largest communities in 2020.
Save them to data/orgs-community-size-2020.json
"""
from utils import Query
from utils.API import API
from utils.FileLoader import FileLoader

api = API()

[keys, query] = Query.getOrgs()

orgs = api.asArray(query, keys)
FileLoader.save('orgs-community-size-2020.json', orgs)

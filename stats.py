from utils.FileLoader import FileLoader
from utils.Plotter import Plotter
import pandas as pd

# orgs = FileLoader.load('orgs-community-size-2020.json')
prs = FileLoader.load('pull-requests.json')
prsMerged = FileLoader.load('pull-requests-merged.json')
# c = FileLoader.load('comments.json')
# cc = FileLoader.load('comments-clean.json')
ca = FileLoader.load('comments-analysis.json')

# print("====================")
# print("Organisations: " + str(len(orgs)))
# print("Pull Requests: " + str(len(prs)))
# print("All comments: " + str(len(c)))
# print("Clean comments: " + str(len(cc)))
# print("Comments analysis: " + str(len(ca)))
# print("====================")

''' Parse the data frames '''
commentsDf = pd.json_normalize(ca)
prsDf = pd.json_normalize(prs)
prsMergedDf = pd.json_normalize(prsMerged)
prsDf = pd.merge(prsDf, prsMergedDf, how='left', left_on=['repo_name', 'number'], right_on=['repo_name', 'number'])
prsDf['is_merged'] = prsDf['merged_at'].isnull() == False

plotter = Plotter(commentsDf, prsDf)

#
# plotter.negMeanByCommunity()
# plotter.neuMeanByCommunity()
# plotter.posMeanByCommunity()

# plotter.totalNegVsMerged()

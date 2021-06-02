from utils.FileLoader import FileLoader
from utils.Plotter import Plotter
import pandas as pd

# orgs = FileLoader.load('orgs-community-size-2020.json')
# prs = FileLoader.load('pull-requests.json')
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

# commentsDf = pd.json_normalize(ca)
#
# plotter = Plotter(commentsDf)
#
# plotter.negMeanByCommunity()
# plotter.neuMeanByCommunity()
# plotter.posMeanByCommunity()

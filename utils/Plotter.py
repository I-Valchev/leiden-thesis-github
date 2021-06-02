import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, commentsDf):
        self.commentsDf = commentsDf

    def mean(self):
        print("MEAN:")
        print("Mean comments neg. " + str(self.commentsDf['analysis.neg'].mean()))
        print("Mean comments neu. " + str(self.commentsDf['analysis.neu'].mean()))
        print("Mean comments pos. " + str(self.commentsDf['analysis.pos'].mean()))

    def median(self):
        print("MEDIAN:")
        print("Median comments neg. " + str(self.commentsDf['analysis.neg'].median()))
        print("Median comments neu. " + str(self.commentsDf['analysis.neu'].median()))
        print("Median comments pos. " + str(self.commentsDf['analysis.pos'].median()))

    def mode(self):
        print("MODE:")
        print("Median comments neg. " + str(self.commentsDf['analysis.neg'].mode()))
        print("Median comments neu. " + str(self.commentsDf['analysis.neu'].mode()))
        print("Median comments pos. " + str(self.commentsDf['analysis.pos'].mode()))

    def oneEmotionOnly(self):
        print("ONE EMOTION ONLY:")
        fully_neg = len(self.commentsDf.loc[self.commentsDf['analysis.neg'] == 1.0])
        fully_neu = len(self.commentsDf.loc[self.commentsDf['analysis.neu'] == 1.0])
        fully_pos = len(self.commentsDf.loc[self.commentsDf['analysis.pos'] == 1.0])
        print("100% comments neg. {:d} ({:f}%)".format(fully_neg, fully_neg * 100 / len(self.commentsDf)))
        print("100% comments neu. {:d} ({:f}%)".format(fully_neu, fully_neu * 100 / len(self.commentsDf)))
        print("100% comments pos. {:d} ({:f}%)".format(fully_pos, fully_pos * 100 / len(self.commentsDf)))

    def negMeanByCommunity(self):
        negMeanByCommunity = self.commentsDf.groupby('repo_name')['analysis.neg'].mean()
        negMeanByCommunityPlot = negMeanByCommunity.plot(title="Comments neg. mean by community")
        negMeanByCommunityPlot.set_xlabel('Repository')
        negMeanByCommunityPlot.set_ylabel('Mean neg. display of emotion')

        print("NEU MEAN BY COMMUNITY:")
        print("Variance:")
        print(negMeanByCommunity.var())
        print("Std. dev.")
        print(negMeanByCommunity.std())

        # don't close the plots when the script ends.
        plt.show(block=True)

    def neuMeanByCommunity(self):
        neuMeanByCommunity = self.commentsDf.groupby('repo_name')['analysis.neu'].mean()
        neuMeanByCommunityPlot = neuMeanByCommunity.plot(title="Comments neu. mean by community")
        neuMeanByCommunityPlot.set_xlabel('Repository')
        neuMeanByCommunityPlot.set_ylabel('Mean neu. display of emotion')

        print("NEU MEAN BY COMMUNITY:")
        print("Variance:")
        print(neuMeanByCommunity.var())
        print("Std. dev.")
        print(neuMeanByCommunity.std())

        # don't close the plots when the script ends.
        plt.show(block=True)

    def posMeanByCommunity(self):
        posMeanByCommunity = self.commentsDf.groupby('repo_name')['analysis.neu'].mean()
        posMeanByCommunityPlot = posMeanByCommunity.plot(title="Comments pos. mean by community")
        posMeanByCommunityPlot.set_xlabel('Repository')
        posMeanByCommunityPlot.set_ylabel('Mean pos. display of emotion')

        print("POS MEAN BY COMMUNITY:")
        print("Variance:")
        print(posMeanByCommunity.var())
        print("Std. dev.")
        print(posMeanByCommunity.std())

        # don't close the plots when the script ends.
        plt.show(block=True)

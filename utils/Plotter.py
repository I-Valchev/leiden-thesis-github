import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, commentsDf, prsDf):
        self.commentsDf = commentsDf
        self.prsDf = prsDf

        commentsByPR = self.commentsDf.groupby(['repo_name', 'number'], as_index=False)['analysis.neg'].mean()
        commentsByPR = commentsByPR.rename(columns={'analysis.neg': 'meanNeg'})
        self.prsWithComments = self.prsDf.merge(commentsByPR, how='left', left_on=['repo_name', 'number'],
                                           right_on=['repo_name', 'number'])

        self.percentiles = [0, 0.05, 0.25, 0.50, 0.75, 0.85, 0.90, 0.95, 0.98, 1]

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

        print("NEG MEAN BY COMMUNITY:")
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

    def totalNegVsMerged(self):
        totalNegVsMerged = self.prsWithComments[['is_merged', 'meanNeg']].groupby('is_merged')['meanNeg'].mean()

        plot = totalNegVsMerged.plot(title="Total mean neg. compared to merge status", kind='bar')
        for p in plot.patches:
            plot.annotate(str(p.get_height()), xy=(p.get_x(), p.get_height()))

        plot.set_ylabel('Mean neg. display of emotion')
        plt.show(block=True)

    def totalNegVsMergeTime(self):
        data = self.prsWithComments.loc[
            self.prsWithComments['merged_at'].notnull()
            &
            self.prsWithComments['meanNeg'].notnull()
        ]

        data['merge_time'] = data['merged_at'] - data['created_at']
        data = data[['merge_time', 'meanNeg']]

        plot = data.plot(title='Total neg. vs merge time', x='merge_time', y='meanNeg', style='o')
        plt.show(block=True)

        quantiles = data.quantile(self.percentiles).unstack().plot(title="Mean neg quantiles")
        plt.show(block=True)


    def meanNegDensityMergedPRs(self):
        data = self.prsWithComments.loc[
            self.prsWithComments['merged_at'].isnull()
            &
            self.prsWithComments['meanNeg'].notnull()
        ]

        data = data[['meanNeg']]

        plot = data.plot.density(title='Mean neg. density for merged PRs')
        plt.show(block=True)

    def meanNegDensityUnmergedPRs(self):
        data = self.prsWithComments.loc[
            self.prsWithComments['merged_at'].notnull()
            &
            self.prsWithComments['meanNeg'].notnull()
        ]

        data = data[['meanNeg']]

        plot = data.plot.density(title='Mean neg. density for unmerged PRs')
        plt.show(block=True)
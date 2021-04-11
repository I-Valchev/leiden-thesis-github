from utils.FileLoader import FileLoader
from utils.SentimentAnalyser import SentimentAnalyser

comments = FileLoader.load('comments-clean.json')
analyser = SentimentAnalyser()

analysed_comments = []
for i, comment in enumerate(comments):
    # if i > 100:
    #     continue
    comment['analysis'] = analyser.analyse(comment['body'])
    analysed_comments.append(comment)

FileLoader.save('comments-analysis.json', analysed_comments)

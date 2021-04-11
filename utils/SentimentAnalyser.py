import nltk

nltk.download('vader_lexicon', quiet=True)
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class SentimentAnalyser:
    def __init__(self):
        self.analyser = SentimentIntensityAnalyzer()

    def analyse(self, sentence):
        return self.analyser.polarity_scores(sentence)

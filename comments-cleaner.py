from utils.Cleaner import Cleaner
from utils.FileLoader import FileLoader

comments = FileLoader.load('comments.json')

cleaner = Cleaner()

comments = cleaner.filterIncompleteComments(comments)
comments = list(map(cleaner.cleanCommentBody, comments))

FileLoader.save('comments-clean.json', comments)

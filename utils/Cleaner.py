import re

from bs4 import BeautifulSoup
from markdown import markdown


class Cleaner:
    def filterIncompleteComments(self, comments):
        return [comment for comment in comments if 'repo_name' in comment and 'number' in comment and 'body' in comment]

    def cleanCommentBody(self, comment):
        comment['body'] = comment['body']\
                            .replace('\t', ';')\
                            .replace('\n', '.')\
                            .replace('\\n', '')\
                            .replace('\\r', '')
        comment['body'] = self.cleanMarkdown(comment['body'])
        return comment

    def cleanMarkdown(self, markdown):
        return self.markdown_to_text(markdown)

    def markdown_to_text(self, markdown_string):
        # md -> html -> text since BeautifulSoup can extract text cleanly
        html = markdown(markdown_string)

        # remove code snippets
        html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
        html = re.sub(r'<code>(.*?)</code >', ' ', html)

        # extract text
        soup = BeautifulSoup(html, "html.parser")
        text = ''.join(soup.findAll(text=True))

        return text

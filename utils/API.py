import json
import requests

class API:
    def __init__(self):
        self.url = 'https://gh-api.clickhouse.tech/play?user=play'

    def request(self, data):
        return requests.post(self.url, data)

    def asJson(self, data, keys):
        return json.dumps(self.asArray(data, keys))

    def asArray(self, data, keys):
        response = self.request(data)
        rows = response.text.split('\n')

        return [self.parseToArrayRow(row, keys) for row in rows]

    @staticmethod
    def parseToArrayRow(row, keys):
        values = row.split('\t')
        return dict(zip(keys, values))

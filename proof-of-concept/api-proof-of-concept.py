
import requests

url = 'https://gh-api.clickhouse.tech/play?user=play'

data = "select * from github_events where event_type = 'PullRequestReviewCommentEvent' order by created_at desc limit 10;"

x = requests.post(url, data)

print(x.text)


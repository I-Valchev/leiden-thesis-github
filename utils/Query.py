
def getPRsForOrg(org):
    return [["repo_name","number"], """
        SELECT repo_name, number
        FROM github_events
        WHERE LOWER(SUBSTRING(repo_name, 1, POSITION(repo_name, '/'))) IN ('%s') AND event_type = 'PullRequestEvent' AND action = 'opened';
        """ % org]

def getOrgs():
    return [['org', 'authors', 'pr_authors', 'issue_authors', 'comment_authors', 'review_authors', 'push_authors'], """
        SELECT
            lower(substring(repo_name, 1, position(repo_name, '/'))) AS org,
            uniq(actor_login) AS authors,
            uniqIf(actor_login, event_type = 'PullRequestEvent') AS pr_authors,
            uniqIf(actor_login, event_type = 'IssuesEvent') AS issue_authors,
            uniqIf(actor_login, event_type = 'IssueCommentEvent') AS comment_authors,
            uniqIf(actor_login, event_type = 'PullRequestReviewCommentEvent') AS review_authors,
            uniqIf(actor_login, event_type = 'PushEvent') AS push_authors
        FROM github_events
        WHERE event_type IN ('PullRequestEvent', 'IssuesEvent', 'IssueCommentEvent', 'PullRequestReviewCommentEvent', 'PushEvent') AND (created_at BETWEEN '2020/01/01' AND '2020/12/31')
        GROUP BY org
        ORDER BY authors DESC
        LIMIT 50
        """]


def getCommentsForOrgAndPr(repo, pr):
    # @todo: Implement query for getting all comments for a repo and PR number.
    return None
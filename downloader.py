from login import login


def search_tweets(query, ):
    api = login()
    results = api.search_tweets(query)
    return results

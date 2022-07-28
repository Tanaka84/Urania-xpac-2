def search_tweets(API_call, query, id=""):
    api = API_call
    results = api.search_tweets(query, max_id=id, tweet_mode="extended")
    return results


def find_last_id(API_search):
    return API_search[-1].id

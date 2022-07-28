import tweepy as tw


def login():
    API_key = ""
    API_key_secret = ""
    bearer_token = ""
    client_key = ""
    client_secret = ""

    auth = tw.OAuth1UserHandler(
        API_key, API_key_secret, client_key, client_secret)
    api = tw.API(auth, wait_on_rate_limit=True)
    return api

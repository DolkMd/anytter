import tweepy

def get_client(api_key: str, api_secret: str, access_token: str, access_token_secret: str) -> tweepy.API:
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['xxx'], cfg['yyy'])
  auth.set_access_token(cfg['zzz'], cfg['aaa'])
  return tweepy.API(auth)

def main():
 
  cfg = { 
    "consumer_key"        : "xxx",
    "consumer_secret"     : "yyy",
    "access_token"        : "zzz",
    "access_token_secret" :  "aaa", 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  print(success)



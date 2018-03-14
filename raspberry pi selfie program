import os
import time
import tweepy
consumer_key = '5PJ0jQh8b6MztpbsXu0tu0cZC'
consumer_secret = 'VAvy9tnSi8bZi2mraZ3vhUxsjCejicwdY6tDM8bHLZV9hs41RQ'
access_token = '968403081451974656-uypjoGaQOIyr4gAMAEP0caWm7HnvPZd'
access_token_secret = 'z0vmgA8qwrysaPqNc4bcBiyZXmjqtCOqK4rqrzEBZBJsR'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
b=1
a=0
while a<=2 :
    img="/home/cs2017b105/Desktop/img"+str(b)+".jpg"
    cmd="fswebcam -F 3 --fps 20 -r 800*600 "+img
    os.system(cmd)
    print ("pic taken")
    api.update_with_media(img, status="Nice one")
    print("wait for 5 seconds selfiiii!")
    time.sleep(5)
    a+=1
    b+=1
    print("success")


import tweepy
import time
import re

API_key = "KgsyftScD209RPHk4ViKgIJpq"
secret_key = "efxLhVofdVMgY7jpWjxuiyoOwfrOPpQoa6oLBlLIk0SSWxZu4r"
Access_token = "148141056-d8IZJpFmiTxfGki20FINycObVib0tL7xUZTwQKOe"
Access_token_secret = "3lfqxG7zNvlYADdGBjUwsgYENQ2VXUY3MTa27L0bxCFnm"



def check_mentions(api, keywords, since_id):
    print("Checking")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        
        if any(keyword in tweet.text.lower() for keyword in keywords):
            start = re.search(r"\d", tweet.text).start()
            if start is not None:
                end = re.match('.+([0-9])[^0-9]*$', tweet.text).start(1)
                print("Bingo")             
                api.update_status(status="@{} {}".format(tweet.user.screen_name, eval(tweet.text[start:end+1])), in_reply_to_status_id=tweet.id)
    
    return new_since_id


# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_key, secret_key)
auth.set_access_token(Access_token, Access_token_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
    
since_id = 1  
while(True):
    since_id = check_mentions(api, ["calculate"], since_id)
    time.sleep(30)



    
#api.update_status(status = "your message here", in_reply_to _status_id = tweet.id_str)

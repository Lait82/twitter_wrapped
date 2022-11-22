import tweepy
import utils
import best_friends
import curses
import tw_statistics as ts
from dotenv import load_dotenv
import json
import os
import time

# Functions
def authenticate_api():
    try:
        # Authenticate to Twitter
        load_dotenv()

        auth = tweepy.OAuthHandler(os.getenv("TW_API_KEY"), os.getenv("TW_API_KEY_SECRET"))
        auth.set_access_token(os.getenv("TW_ACCESS_TOKEN"), os.getenv("TW_ACCESS_TOKEN_SECRET"))
        api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
        return api
    except Exception as e:
        print(e)
        print("Authentication Error")

def fetch_last_year_tweets(user, api):
    try:
        timeline_params = {
            "user_id":user['id'], 
            "include_rts":False, 
            "count":200,
            "trim_user": True,
        }
        flag = True
        all_tweets = []
        last_tw = None
        while(flag):
            if(last_tw):
                if("max_id" in timeline_params and timeline_params['max_id'] == int(last_tw['id_str'])):
                    break # Exception to reach as far as the endpoint allows (3200 tweets. Which are like 8 tweets a day... Definitely someone who has to grab the shovel. )
                timeline_params['max_id'] = int(last_tw['id_str'])

            try:
                tweets = api.user_timeline(**timeline_params)
            except Exception as e:
                print("error al traer los tweets, intentando de nuevo en 2 seg")
                print(e)
                time.sleep(3)
                continue

            
            tweets = [{
                "created_at":tweet["created_at"], 
                "text":tweet["text"],
                "id_str":tweet["id_str"],
                "favorite_count":tweet["favorite_count"],
                "retweet_count":tweet["retweet_count"],
                "user_mentions":tweet["entities"]["user_mentions"]
                } for tweet in tweets]
            
            last_tw = tweets[len(tweets)-1]
            last_tw_date = utils.get_date(last_tw['created_at'])
            
            if(last_tw_date.year == 2021):
                tweets = filter(lambda tw: utils.get_date(tw['created_at']).year == 2022, tweets)
                flag = False

            all_tweets = [*all_tweets, *tweets]

            print("last 200 tweets retrieved, last in: {0}".format(last_tw['created_at']))
            time.sleep(0.5) # Para que la api no se ponga rompehuevos
        # END WHILE

        utils.write_to_file(all_tweets, "all_tweets.json")
        return all_tweets
    except Exception as e:
        print(e)

def main():
    # all_tweets = client.get_all_tweets_count(query="", start_time=1666248774)
    try:
        api = authenticate_api()

        user = api.get_user(screen_name="manuqooi")
        timeline_params = {
            "user_id":user['id'], 
            "include_rts":False,
            "trim_user": True,
            "count": 200
        }
        # tweets = api.user_timeline(**timeline_params)

        # tweets = [{
        #         "created_at":tweet["created_at"], 
        #         "text":tweet["text"],
        #         "id_str":tweet["id_str"],
        #         "favorite_count":tweet["favorite_count"],
        #         "retweet_count":tweet["retweet_count"]
        #         } for tweet in tweets]

        # with open('sample.json', 'r', encoding='utf-8') as sample:
        #     # sample.write(json.dumps(tweets))
        #     sample = json.load(sample)
        #     # sample = json.load(sample)
        #     print("llega")
        #     best_friends.get_best_friends(sample)


        # print(tweets)

        # tweets = fetch_last_year_tweets(user, api)
        with open("all_tweets.json", "r", encoding="utf-8") as tweets:
            tweets = json.load(tweets)
            bfs = best_friends.get_best_friends(tweets, 4)
            print(bfs)



        # curses.get_top_3_curses()
        # print(get_curse_words())
        # rts = ts.get_tw_interaction_count("RTS")
        # most_liked_pictures = ts.get_most_liked_pics(3)
        
        # print(most_liked_pictures)

        

        # print(tweets)

        
    except Exception as e:
        print(e)

if(__name__ == "__main__"):
    main()
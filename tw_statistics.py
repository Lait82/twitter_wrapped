import json
import functools as fn
import re

def get_tw_interaction_count(interaction_type="LIKES"):
    try:
        with open('all_tweets.json', 'r', encoding='utf-8') as tweets:
            tweets = json.load(tweets)
            if(interaction_type == "LIKES"):
                tw_interaction = "favorite_count"
            elif(interaction_type == "RTS"):
                tw_interaction = "retweet_count"
            else:
                raise KeyError("That interaction {0} does not exist.".format(interaction_type))
                
                
            interaction_count = fn.reduce(lambda accum, tw: accum + tw[tw_interaction], tweets, 0)
            return(interaction_count)

    except Exception as e:
        print(e)

def  get_most_liked_pics(limit):
    try:
        with open("all_tweets.json", 'r', encoding='utf-8') as tweets:
            tweets = json.load(tweets)
            pic_links = {}
            for tweet in tweets:
                pic_link = re.findall("(https:\/\/t\.co\/+[a-zA-Z0-9]+)", tweet['text'])
                if len(pic_link):
                    pic_links[pic_link[-1]] = tweet['favorite_count'] + (pic_links[pic_link[0]] if pic_link[0] in pic_links else 0)
        pic_links = { pl: pic_links[pl] for pl in pic_links if pic_links[pl] > 0}
        pic_links = sorted(pic_links.items(), key=lambda pl: -pl[1])
        if limit:
            pic_links = pic_links[0:limit]
        return pic_links
    except Exception as e:
        print("There was problems while getting the most liked pictures")
        print(e)
        
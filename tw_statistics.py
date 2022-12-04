import json
import functools as fn
import re
import curses as cr
import best_friends as bf

def get_tw_interaction_count(tweets = None, interaction_type="LIKES") -> int:
    try:
        if(not tweets):
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

def get_most_liked_pics(tweets = None, limit = None):
    try:
        if not tweets:
            with open("all_tweets.json", 'r', encoding='utf-8') as tws:
                tweets = json.load(tws)

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







def get_all_statistics(tweets):
    rts = get_tw_interaction_count(tweets, "RTS")
    likes = get_tw_interaction_count(tweets, "LIKES") 

    top_3_curses = cr.get_top_3_curses(tweets)
    curses_count = cr.get_curses_count(tweets)

    top_3_friends = bf.get_best_friends(tweets, 3)
    top_liked_pics = get_most_liked_pics(tweets, 4)
    return {
        "rts_count": rts,
        "likes_count": likes, 
        "top_3_curses": top_3_curses, 
        "curses_count": curses_count, 
        "top_3_friends": top_3_friends, 
        "top_liked_pics": top_liked_pics
    }
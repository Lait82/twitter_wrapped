import json

def load_curses_counter(tweets = False) -> dict:
    try:
        curses_list = []
        
        with open("curses.json", "r", encoding="utf-8") as curses:
            curses_list = json.load(curses)
        
        curses_counter = {c: 0 for c in curses_list }
        # print("empieza con estas malas palabras: ")
        # print(curses_list)
        # print(curses_counter)

        if(not tweets):
            with open("all_tweets.json", "r", encoding="utf-8") as tweets:
                tweets = json.load(tweets)
        
        for tweet in tweets:
            for curse in curses_list:
                curses_counter[curse] += 1 if curse in tweet['text'] else 0

        return(curses_counter)
            
    except Exception as e:
        print("There was an error loading bad words")
        print(e)

def get_top_3_curses(tweets = False) -> dict:
    try:
        # curses_counter, curses_list = load_curses_list()
        curses_counter = load_curses_counter(tweets)

        curses_counter_items = curses_counter.items()

        # curses_list = sorted(curses_list, key=lambda bw: -curses_counter[bw])
        curses_counter_items = sorted(curses_counter_items, key=lambda cci: -cci[1])

        # print("la 3 puteadas que mas usaste fueron: ")
        # print(curses_counter_items[0][0])
        # print(curses_counter_items[1][0])
        # print(curses_counter_items[2][0])
        
        # print("y las usaste un total de {0}, {1} y {2} respectivamente".format(
        #     curses_counter_items[0][1],
        #     curses_counter_items[1][1],
        #     curses_counter_items[2][1],
        # ))
        return {
            curses_counter_items[0][0]: curses_counter_items[0][1], 
            curses_counter_items[1][0]: curses_counter_items[1][1], 
            curses_counter_items[2][0]: curses_counter_items[2][1], 
        }
    except Exception as e:
        print("There was an error getting the most used curse")
        print(e)

def get_curses_count(tweets = False):
    try:
        curses_counter = load_curses_counter(tweets)

        total_curses_counter = sum( cc for _, cc in curses_counter.items())

        return total_curses_counter
    except Exception as e:
        print("Error when trying to get curses count")
        print(e)
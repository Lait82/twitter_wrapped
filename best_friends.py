def get_best_friends(all_tweets, limit = None):
    try:
        mentioned_users_count = {}
        for tweet in all_tweets:
            for user_mention in tweet['user_mentions']:
                mentioned_users_count[user_mention['screen_name']] = 1 + (mentioned_users_count[user_mention['screen_name']] 
                if user_mention['screen_name'] in mentioned_users_count 
                else 0)

        mentioned_users_count = mentioned_users_count.items()
        mentioned_users_count = sorted(mentioned_users_count, key=lambda mui: -mui[1])
        
        print(mentioned_users_count)
        if(limit):
            return(mentioned_users_count[0:limit])
        return(mentioned_users_count)
            
    except Exception as e:
        print("Error while getting best friends from tweets")
        print(e)

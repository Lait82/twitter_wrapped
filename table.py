from datetime import datetime
import json

dt = datetime.strptime("Sun Nov 20 06:25:04 +0000 2022", "%a %b %d %H:%M:%S %z %Y")
print(dt.year)

allt = []
tweets = [{
    "test": 123,
    "teest": 345
},
{
    "test": 11323,
    "teest": 34515
}]
allt = [*allt, *tweets]
allt = [*allt, *tweets]
allt = [*allt, *tweets]

print(allt)

# with open('tw-data.json', 'a+', encoding='utf-8') as tw_data:
#     try:
#         tw_data.write(json.dumps(tweets))
#         # print(tweets)
#         print("Successful json dump of tweets")
#     except Exception as e:
#         print("There was an error while dumping the tweets to the json file")
#         print(e)
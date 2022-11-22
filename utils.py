from datetime import datetime
import json

def get_date(date_string):
    try:
        dt = datetime.strptime(date_string, "%a %b %d %H:%M:%S %z %Y")
        return dt
    except Exception as e:
        print("There was an error while parsing the created_at date")

def write_to_file(tweets, file_name = "tw-data.json"):
    with open(file_name, 'a+', encoding='utf-8') as tw_data:
        try:
            tw_data.write(json.dumps(tweets))
            # print(tweets)
            print("Successful json dump of {0} tweets".format(len(tweets)))
        except Exception as e:
            print("There was an error while dumping the tweets to the json file")
            print(e)
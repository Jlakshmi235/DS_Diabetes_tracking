import json
import pandas as pd

line_str = '/Users/Jayalakshmi/Desktop/tweets/output.json'

array=[]

with open(line_str) as f:
    for line in f:
    	array.append(line)


#removing new lines from the json file
array = [x for x in array if x != '\n']

json_array=[]
x=len(array)
for i in range (0,x):
	data = json.loads(array[i])
	json_array.append(data)

#removing unnecessary attributes
for row in json_array:
	
	del row['contributors']
	del row['id']
	del row['id_str']
	del row['source']
	del row['truncated']
	del row["in_reply_to_status_id"]
	del row["in_reply_to_status_id_str"]
	del row["in_reply_to_user_id"]
	del row["in_reply_to_user_id_str"]
	del row["in_reply_to_screen_name"]
	del row["is_quote_status"]
	del row["retweet_count"]
	del row["favorite_count"]
	del row["favorited"]
	del row["retweeted"]
	#del row["possibly_sensitive"]
	del row["filter_level"]
	del row["timestamp_ms"]
	del row["user"]
	del row["entities"]["urls"]
	del row["entities"]["user_mentions"]
	del row["entities"]["symbols"]
	del row["geo"]
	del row["coordinates"]




df = pd.DataFrame(json_array)

#removing unnecessary attributes
df = df.drop('display_text_range', 1)
df = df.drop('extended_tweet', 1)
df = df.drop('retweeted_status', 1)
df = df.drop('extended_entities', 1)
df = df.drop('possibly_sensitive', 1)
df = df.drop('quoted_status', 1)
df = df.drop('quoted_status_id', 1)
df = df.drop('quoted_status_id_str', 1)

df = df[df.lang=="en"]
df = df.drop('lang', 1)

#segregating tweets with geo info
geo_tweets = df[df.place.isnull()==False]
df = df.drop('place', 1)



#separating retweets
retweet = (df.loc[df['text'].str.startswith('RT', na=False)])

#separating non-retweets
nonRT = df[~df['text'].str.startswith('RT')]

text=nonRT['text']

print len(df)
print len(retweet)
print len (nonRT)
print len(geo_tweets)



#writing to txt for further analysis
text.to_csv('3.txt', encoding='utf8', index=False)
geo_tweets['place'].to_csv('3geo.txt', encoding='utf8', index=False)



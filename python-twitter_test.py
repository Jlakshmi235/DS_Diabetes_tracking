import twitter


# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key='QhwbJVdvDhe3pm7tDJYtyx5pc'
consumer_secret='o9EgcpYJXqOckTqdhPbslZCwZrFxNMOvHHW7c636gNFRwAyeSv'


# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token='708526515777105920-WjXVWk43VCEcPGaAG77tkf4hcOaeK8h'
access_token_secret='7UACHPXOO1hgl9ykyQMzrSIobLImvUcLdRC3LWMzpfmPW'

api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token, access_token_secret=access_token_secret)

# print statuses of a user
statuses = api.GetUserTimeline(screen_name='MDT_Diabetes')
# tweets were collected from other users like @WDD, @IntDiabetesFed, @diabeteshf, @MDT_Diabetes
for status in statuses:
	print status['text']


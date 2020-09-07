from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "762075386-hddiJG8pThN9sszp46hJxpmSkdREtADrTfCmvSuU" #"ENTER YOUR ACCESS TOKEN"
access_token_secret = "KaqjJiYG1IlppwmGYwUjf7eDR6eoJKD6Dw7AKsmSnnJjc" #"ENTER YOUR ACCESS TOKEN SECRET"
consumer_key = "Dw8ZJRGZ0sdjm530Tg60NUWvq" #"ENTER YOUR API KEY"
consumer_secret = "LQ8qu88jWG3LgIbpL4gcBWJZf8FLi12cAmK9HUcVYX1ZZ0KrXX" #"ENTER YOUR API SECRET"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['Online Games', 'MOBA', 'MMORPG', 'MMO',\
        'World of Warcraft', 'Elder Scrolls Online', 'Guild Wars 2', 'Final Fantasy 14', 'Black Desert Online', 'RuneScape',\
        'Dota 2', 'League of Legends', 'Area of Valor', 'Heros of the Strom'])
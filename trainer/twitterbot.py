from twython import Twython
import time
from auth import ( consumer_key, consumer_secret, access_token, access_token_secret)


twitter = Twython( #Imports login details from the twitter developers section which are stored in another file
    consumer_key, consumer_secret, access_token, access_token_secret
    )


verify = twitter.verify_credentials() #Checks that twitter has logged you in
print(twitter)
print(verify)


script = open('beemoviescript.txt', 'r') #Opens up a document stored, goes through the script line by line then tweets each line
while script:
    line = para.readlines()
    for x in line:
        twitter.update_status(status=x)
        print(x)
        time.sleep(30)



    

import fbchat
from fbchat import Client
from getpass import getpass
username = 'joefredgreenwood'
client = fbchat.Client(username, getpass())
no_of_friends = int(input('number of friends'))
messages=[]
f = open('beemoviescript.txt', 'r')
for x in f:
    word = x.split()
    for msg in word:
        messages.append(msg)
for i in range(no_of_friends):
    name = str(input('Name of friend'))
    friends = client.searchForUsers(name)
    friend = friends[0]
    for mesg in messages:            
        sent = client.send(fbchat.models.Message(mesg),friend.uid)
    if sent:
        print('msg go go go')
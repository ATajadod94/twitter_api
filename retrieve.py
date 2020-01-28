import TwitterAPI.TwitterAPI
import sqlite3
import constants

conn = sqlite3.connect('test1.db')
c = conn.cursor()

#create table
c.execute('''CREATE TABLE IF NOT EXISTS quotes
             (rollno integer , tweet text)''')

import csv


api = TwitterAPI.TwitterAPI(constants.consumer_key, constants.consumer_secret,
                            constants.access_token_key, constants.access_token_secret )

values = []
r = api.request('statuses/filter', {'track':'trump'})
with open('tweets.csv', 'w', newline='') as file:
    i = 1
    writer = csv.writer(file)
    for item in r.get_iterator():
        if 'text' in item:
            writer.writerow([i,item['text']])
            i += 1





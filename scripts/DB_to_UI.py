from cassandra.cluster import Cluster
from firebase import firebase
import datetime
import json


fire = firebase.FirebaseApplication('https://bitchynesstracker.firebaseio.com/')
#fire = firebase.FirebaseApplication('https://testbendroste.firebaseio.com/')	
cluster = Cluster(['172.31.38.201'], port=9042)
		
session = cluster.connect()
session.execute('use tracker')

today = datetime.date.today()

date_range = [0,0,0,0,0,0,0]
for j in range(0,7):
	time_range = datetime.timedelta(days = j)
	day = today - time_range
	str_day = datetime.date.__str__(day)
	date_range[j] = str_day[0:4] + str_day[5:7] + str_day[8:10] 
		

codes = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IND','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','ORE','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"] 

fire.delete("Bitchyness",None)

for i in range(0,50):
	state = codes[i]
	maxscore = 0
	tweetID = 0
	count = 0
	total_score = 0
	tweet_txt = ""
	for day in date_range:
		query = "select * from " + state + " where date = " + day
		rows = session.execute(query)
		for r in rows:
			if(r.sentiment > maxscore):
				maxscore = r.sentiment
				tweetID = r.tid
			
			total_score = total_score + r.sentiment
			count = count +1
	if(count > 0):
		average = total_score / count
	else:
		average = 0
	if(tweetID != 0):
		angryquery = session.prepare("select * from tweets where id_str = ?")
		tweet = session.execute(angryquery,[tweetID])
		for line in tweet:
			tweet_txt = line.text
	stateJson = {'abrev':state,'name':states[i], 'score':average, 'bitchtweet':tweet_txt}
	fire.post("Bitchyness",stateJson)

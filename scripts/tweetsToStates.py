from cassandra.cluster import Cluster
from watson_developer_cloud import ToneAnalyzerV3Beta
from credentials import watsonUser, watsonPassword
import datetime
import json
cluster = Cluster(['172.31.38.201'],port = 9042)
session = cluster.connect()
session.execute('USE Tracker')
tone_analyzer = ToneAnalyzerV3Beta(
		username = watsonUser,
		password = watsonPassword,
		version = '2016-02-11')	
		
count =0
now = datetime.datetime.now()
year = str(now.year)
month = now.month
if (month < 10):
	month = "0" + str(month)
day = now.day
if (day < 10):
	day = "0" + str(day)
currentDate = str(year) + str(month) + str(day)
queryHandle = session.prepare("SELECT * FROM Tweets WHERE created_at=?")
testdata = session.execute(queryHandle,[currentDate])

for data in testdata:
	if count < 10:
		contents = data.text
		geo = data.geo
		badDate = data.created_at
		tid = data.id_str
		date = int(badDate)
		sentimentData = tone_analyzer.tone(text=contents)
		anger=sentimentData["document_tone"]["tone_categories"][0]["tones"][0]["score"]
		disgust=sentimentData["document_tone"]["tone_categories"][0]["tones"][1]["score"]
		joy=sentimentData["document_tone"]["tone_categories"][0]["tones"][3]["score"]
		neuroticism=sentimentData["document_tone"]["tone_categories"][2]["tones"][4]["score"]
		sentimentScore = .4*anger + .7*disgust + .6*neuroticism - .35*joy
		if(sentimentScore < 0):
			sentimentScore = 0
		if(sentimentScore > 1):
			sentimentScore = 1
		locationTest = geo.count(",")
		if(locationTest == 1 ):
			geo2 = geo.split(',')
			location = geo2[1].replace(" ","")
			location = location[0:2]
			stateArray = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
			for state in stateArray:
				if location == state:
					if state == 'IN':
						location = 'IND'
					if state == 'OR':
						location = 'ORE'
					insertHandle = 'INSERT INTO ' + location +'(tID,date,sentiment) values (%s, %s, %s)'		
					session.execute(insertHandle,(tid,date,sentimentScore))

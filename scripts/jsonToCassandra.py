from sys import argv
from cassandra.cluster import Cluster
import json
script, filename = argv

cluster = Cluster(['172.31.38.201'],port=9042)
session = cluster.connect()
session.execute('USE Tracker')
''' Sample query syntax
testdata = session.execute('select * from CO')
for data in testdata:
	print(data.sentiment)
'''
#insertHandle = session.prepare('INSERT INTO tweets JSON ?')
with open (filename, 'r') as data:
		for line in data:
			count = line.count(" ---$%^--- ")
			parts = line.split(" ---$%^--- ")
			if(count == 3):
				badDate = parts[0]
				date= badDate[-4:]
				if "Jan" in badDate:
					date = date + "01"
				if "Feb" in badDate:
					date = date + "02"
				if "Mar" in badDate:
					date = date + "03"
				if "Apr" in badDate:
					date = date + "04"
				if "May" in badDate:
					date = date + "05"
				if "Jun" in badDate:
					date = date + "06"
				if "Jul" in badDate:
					date = date + "07"
				if "Aug" in badDate:
					date = date + "08"
				if "Sep" in badDate:
					date = date + "09"
				if "Oct" in badDate:
					date = date + "10"
				if "Nov" in badDate:
					date = date + "11"
				if "Dec" in badDate:
					date = date + "12"	
				date = date + badDate[8:10]
				contents = parts[1]
				id_str = parts[2]
				geo = parts[3]
				session.execute(
				"""
				insert into tweets(id_str,text,created_at,geo) values (%s,%s,%s,%s)
				""",
				(id_str,contents,date,geo)
				)
				'''
			line = line[1:-1]
			line2 = line.replace(" '",' "')
			line2 = line2.replace("{'",'{"')
			line2 = line2.replace("' ",'" ')
			line2 = line2.replace("',",'",')
			line2 = line2.replace(",'",',"')
			line2 = line2.replace("':",'":')
			line2 = line2.replace("'}",'"}')
			line2 = line2.replace("'","")
			#print line2
			session.execute(insertHandle, [line2])
			'''
			
			#session.execute(
			"""
			insert into Tweets JSON '{"tID": "Monkey", "contents": "This is a test tweet also","date": 20160331,"geolocation": "Boulder?"}'
			"""
			#)

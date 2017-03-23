# AngryLevelAnalyser

We use data from Twitter's public tweet stream to find a angry level for each state in the US, and we display this data in an interactive heat map through web interface. To do this, we stream Twitter's tweets at daily bases and take the data and classify it by state of origing using location tags attached to the tweets themselves. We extract the information we need and insert it into a Cassandra database hosted on AWS. Then for each tweet in our Cassandra database, it gets passed into the tone-analyzer from IBM's Watson Bluemix and we use the values of Joy, Anger, Disgust, and Neuroticism to create a angry level score for that tweet and insert this value into a new table in Cassandra. These values, categorized by state, are averaged into a heat map (see screenshot) that displays the level of angryness for each state as well as that state's angriest tweet of the week. The results can be viewed below.

Our instances was shut down after our class ends. When our instances were running, we processes up to 1000 tweets (free semtiment analysis limit)  everyday, and we analysed up to one month of data collected ( then our instance got shut down because we ran out of budget :( ). 


# Technology involved
NodeJS was used when we were using twitter's API to stream tweets, the data gets stored in Cassandra database in our AWS EC2 server. For front end we used Firebase. In In this project my focus is on the backend. I built the application streaming tweets through twitter API and processes the data , set up instances in EC2, and worked on the Cassandra database as well as the script. 

# Code Functionality Breakdown:
+ DB folder: Cassandra query to set up table
+ Node1 folder: twitter streaming bot, streaming and tempoarily buffer tweets
+ Script folder: main logic of the project
+ Web: web frontend 

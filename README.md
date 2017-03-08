# BitchynessTracker

This is our Big Data project for Big Data class at the University of Colorado Boulder.

We use data from Twitter's public tweet stream to find a bitchiness level for each state in the US. To do this, we take the data and classify it by state of origing using location tags attached to the tweets themselves. We extract the information we need and insert it into a Cassandra database hosted on AWS. We pass the text of these tweets into the tone-analyzer from IBM's Watson Bluemix and use the values of Joy, Anger, Disgust, and Neuroticism to create a bitchiness score for that tweet and insert this value into a new table in Cassandra. These values, categorized by state, are averaged into a heat map that displays the level of bitchiness for each state as well as that state's bitchiest tweet of the week. The results can be viewed below.

WARNING: The contents of the tweets displayed are uncensored and may contain inappropriate content. The views expressed in these tweets are not shared by us. 

http://cubigdataclass.github.io/BitchynessTracker/web/index.html

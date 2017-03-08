console.log('bot is starting');

var Twit=require('twit'); //import twit




//create an object of twitter 
var Twit = new Twit({

//  timeout_ms:           60*1000,  // optional HTTP request timeout to apply to all requests.
});
/*** Another way to get twitter information 
var config = require('./config');
var T = new Twit(config);
****/
//  search twitter for all tweets containing the word 'xxx' since --time of year ---

var params={
	q: 'Donald trump',
	count: 1
}

Twit.get('search/tweets', params, gotData);

function gotData(err, data, response) {
  //console.log(data);
  var tweets=data.statuses;
  for (var i=0; i < tweets.length; i++){
  	console.log(data);
  	//console.log(tweets[i].text);
  	//console.log('\n');
  	//console.log('\n');
  }
}

/*
var MyPost={ status: 'I am using tweeter API new'}
Twit.post('statuses/update', MyPost,  postData)

function postData(err, data, response) {

  console.log(data);
}
*/
 


/*
HttpResponse<JsonNode> response = UniresTwit.get("https://jamiembrown-tweet-sentiment-analysis.p.mashape.com/api/?text=I+love+Mashape!")
.header("X-Mashape-Key", "kQpgNyGgV7mshUv83x1y6U7QD7A7p1hGbSSjsn4XX0sxHcHVQr")
.header("Accept", "application/json")
.asJson();
*/


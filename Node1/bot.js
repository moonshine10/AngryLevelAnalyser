

var Twit=require('twit'); //import twit


var T = new Twit({

//  timeout_ms:           60*1000,  // optional HTTP request timeout to apply to all requests.
});

var counts=0;

 
stream.on('tweet', function (tweet) {

if(tweet.place !=null)
{

  if (counts<=10000)
  {
  counts++;
  console.log(tweet.created_at, "---$%^---", tweet.text,"---$%^---",tweet.id_str,"---$%^---",tweet.place.full_name);
  }
  else
  {
    throw new Error("Opps!! We just hit the tweets cap of 10,000");
  }

})





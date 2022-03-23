## What is Chaos Suppressor?
If you are tired of software engineer exaggerations on your Twitter timeline, this is for you.

Chaos automatically silences users who fall into your timeline every 15 minutes, according to the keywords we set. 

For example: "yazılımcı", "klavye", "sucuk"

## How can I use it?
Chaos Suppressor is a serverless application and we use AWS Chalice to run it.
 - Get a Twitter API key and secret from https://apps.twitter.com/
 - Set the Twitter API key and secret in the `twitter_api_key` and `twitter_api_secret` fields in the `config.json` file.
 - `pip install chalice`
 - Set your AWS account credentials in `.aws/credentials`
 - `chalice deploy` -> deploy to cloud
 - `chalice delete` -> delete from cloud

## Where can I find the mute list?
You can find the mute list in the `https://gist.github.com/kemalcanbora/fdff0cd956a9d30f2e136c0e3aa94e92` url.
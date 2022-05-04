
<p align="center">
  <img 
    width="450px"
    height="450px"
    src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/bb856fda-e64f-47dd-ae49-58db849d8812/d5ghpr6-7ea656b5-ab56-44ff-b30d-c7f54de552bf.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2JiODU2ZmRhLWU2NGYtNDdkZC1hZTQ5LTU4ZGI4NDlkODgxMlwvZDVnaHByNi03ZWE2NTZiNS1hYjU2LTQ0ZmYtYjMwZC1jN2Y1NGRlNTUyYmYuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.RttH0xQGVtrMb9PcwnOW_WgKFh2FibSY9D2n9CUtE3Y"
  >
</p>

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




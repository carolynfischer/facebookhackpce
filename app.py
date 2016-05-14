import json
from pprint import pprint

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/get_posts', methods=['POST'])
def get_posts():
    """Takes in JSON data of posts made to Middle School page & parses it.
    JSON format is a list of dicts, with each dict being 1 post."""

    # Keywords selected from: http://slate.me/KlDTQn
    
    keyword_weights = {
						'fucking': 1,
						'fucked':  1,
						'done with':  1,
						'drunk':  1,
						'shite':  1,
						'annoyed':  1,
						'freaking':  1,
						'pissed':  1,
						'crap':  1,
						'sucks':  1,

						'bullshit':4,
						'stressed': 4,
						'hate': 4,
						'stupid': 4,
						'frustrated':4, 
						'crappy': 4,
						'miserable': 4,
						'horrible': 4,
						'disappointed':4, 
						'fed up': 4,
						'sick of': 4,
						'for once':4,

						'leave me alone':7,
						'scared':  7,
						'unwanted': 7,
						'feeling sad': 7,
						'feeling depressed':7, 
						'helpless': 7,
						'crying': 7,
						'empty': 7,

						'kill': 10,
						'suicide':  10,
						'depressed':  10,
						'lonely':  10,
						'depression':  10,
						'dead':  10,
						'better off dead': 10, 
						'no one would miss me': 10, 
						'gun':  10,
						'jump off a bridge': 10 
    }

    keywords = set(keyword_weights.keys())

    # The Facebook API does not currently return data on "How I'm Feeling."
    # If this is available in the future, the script would search that data also.

    # data = json file POSTed from API call

    for each in data:
    	msg_words = each['message'].split(" ")
    
    for word in msg_words: 
    	if word in keywords:
    		# increment user's point count in database by each[word]


  	# {
	   # "data": [
	   #   {
	   #     "id": "546349135390552_1138601292831997", 
	   #     "message": "test", 
	   #     "from": {
	   #       "category": "Restaurant/cafe", 
	   #       "category_list": [
	   #         {
	   #           "id": "128673187201735", 
	   #           "name": "Coffee Shop"
	   #         }
	   #       ], 
	   #       "name": "Mahesh's Cafe", 
	   #       "id": "546349135390552"
	   #     }, 
	   #     "created_time": "2015-05-19T22:51:20+0000"
	   #   }, 

    return 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

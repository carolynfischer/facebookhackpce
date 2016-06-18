import json
from pprint import pprint

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/get_posts', methods=['GET', 'POST'])
def get_posts():
	""" Takes in JSON data of posts made to Middle School page & parses it. JSON format is a list of dicts, with each dict being 1 post."""
	a = "Hi filler"

	return True
    
def parse():
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
						'shit': 1,

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
    
	msg_words = msg_words.split(" ")
	# msg_words : is a list of the words in a single post	
    
	# msg : data structure to hold the set of keywords corresponding to one post
	# scores : scores
	msg = set(msg_words)
	score = 0
	for word in msg: 
		if word in keywords:
    		# increment user's score : Word count for this keyword * weight for this keyword
			score += msg_words.count(word) * keyword_weights[word]

	print score

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=8080)
	parse()

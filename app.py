import json

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()


@app.route('/get_posts', methods=['GET'])
def get_posts():
    '''Takes in JSON data of posts made to Middle School page & parses it.
    JSON format is a list of dicts, with each dict being 1 post.'''



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
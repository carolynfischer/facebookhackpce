import json
import requests
from pprint import pprint
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def respond_FB(sender_id, text):
    json_data = {
        "recipient": {"id": sender_id},
        "message": {"text": text + " to you!"}
    }
    params = {
        "access_token": ''
    }
    r = requests.post('https://graph.facebook.com/v2.6/me/messages', json=json_data, params=params)
    print(r, r.status_code, r.text)

@app.route('/auth')
def fb_webhook(methods=['GET', 'POST']):
    print request.args.get('hub.verify_token')
    if (request.args.get('hub.verify_token') == ''):
        return request.args.get('hub.challenge')
    return 'Error, wrong validation token'
        
@app.route('/get_posts', methods=['GET', 'POST'])
def get_posts():
    """Takes in JSON data of posts made to Middle School page & parses it.
    JSON format is a list of dicts, with each dict being 1 post."""

    #hackathonschool
    return True
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

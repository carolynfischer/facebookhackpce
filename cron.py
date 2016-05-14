import requests
import app
import json
import datetime
import dateutil.parser

ACCESS_TOKEN = '***REMOVED***'

def pull_posts():
    payload = {'method': 'get',
                'fields': 'id,message,from,to,created_time',
                'access_token': ACCESS_TOKEN
    }
    r = requests.get('https://graph.facebook.com/v2.6/hackathonschool/feed', params=payload)
    result = json.loads(r.text)['data']
    now = datetime.datetime.now()

    for post in result:
        if 'to' in post.keys():
            name = post['from']['name']
            user_id = post['id']
            message = post['message']
            time = dateutil.parser.parse(post['created_time'])
            print name, user_id, message, time
        
def send_message():
    url = 'https://graph.facebook.com/v2.6/me/messages'
    message_to_post = {'text': 'Please look out for your friend!'}
    payload = {'qs': {'access_token': '***REMOVED***'},
                'json': {
                    'recipient': {'id': '***REMOVED***'},
                    'message': message_to_post
                }
    }
    r = requests.post('https://graph.facebook.com/v2.6/hackathonschool/feed', params=payload)
    print r.text
    
if __name__ == '__main__':
    #pull_posts()
    send_message()
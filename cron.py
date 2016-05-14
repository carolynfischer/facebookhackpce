import requests
import app
import json
import datetime
import dateutil.parser
from twilio.rest import TwilioRestClient

ACCESS_TOKEN = '***REMOVED***'
account_sid = "***REMOVED***"
auth_token  = "***REMOVED***"
client = TwilioRestClient(account_sid, auth_token)

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
            
            if 'class' in message:
                send_sms(name, message)
                print "SENT A NOTIFICATION"
        
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
    
def send_sms(name, message):
    sms_input = "Please pay attention to and contact {}, they might be in need! \
    They just posted the following comment and it's concerning: {}.".format(name, message)
    message = client.messages.create(body=sms_input,
        to="***REMOVED***",    # Replace with your phone number
        from_="***REMOVED***") # Replace with your Twilio number
    print message

if __name__ == '__main__':
    pull_posts()
    #send_message()
    #send_sms()
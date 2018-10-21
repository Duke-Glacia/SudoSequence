from __future__ import print_function
from apiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools

def date_adder_exercise(disease,level,tolerance):
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('storage.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    GCAL = discovery.build('calendar', 'v3', http=creds.authorize(Http()))
        # PDT/MST/GMT-7]

    predicted_rate=10
    rate_of_change=(weght_list[-1]-weight_list[-8])/7

    if rate_of_change<predicted_rate:
        date_fluctuation=5
    elif rate_of_change>predicted_rate:
        data_fluctuation=-5


    
    if disease=="diabetes" and 0<tolerance<40:
        event = {
        'summary': "Tackle diabetes by running", #if disease=="diabetes"  else "Tackle hip problems by running more " if disease=="hip_problems",
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'To reduce your weight and combat diabetes',
        'start': {
            'dateTime': datetime.datetime.utcnow().isoformat() ,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': datetime.datetime.utcnow().isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=WEEKLY;COUNT='+str(x)
        ],
        'reminders': {
            'useDefault': True,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }
    elif disease=="diabetes" and 40<tolerance<80:
        event = {
        'summary': "Tackle diabetes by running", #if disease=="diabetes"  else "Tackle hip problems by running more " if disease=="hip_problems",
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'To reduce your weight and combat diabetes',
        'start': {
            'dateTime': datetime.datetime.utcnow().isoformat() ,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': datetime.datetime.utcnow().isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;INTERVAL=2;COUNT='+str(x)
        ],
        'reminders': {
            'useDefault': True,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }
    elif disease=="diabetes" and 80<tolerance:
        event = {
        'summary': "Tackle diabetes by running", #if disease=="diabetes"  else "Tackle hip problems by running more " if disease=="hip_problems",
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'To reduce your weight and combat diabetes',
        'start': {
            'dateTime': datetime.datetime.utcnow().isoformat() ,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': datetime.datetime.utcnow().isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT='+str(x)
        ],
        'reminders': {
            'useDefault': True,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }
    elif disease=="diabetes" and 80<tolerance:
        event = {
        'summary': "Tackle diabetes by running", #if disease=="diabetes"  else "Tackle hip problems by running more " if disease=="hip_problems",
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'To reduce your weight and combat diabetes',
        'start': {
            'dateTime': datetime.datetime.utcnow().isoformat() ,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': datetime.datetime.utcnow().isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT='+str(x)
        ],
        'reminders': {
            'useDefault': True,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }
    elif disease=="hip_problems" and 0<tolerance<40:
        event = {
        'summary': "Swimming", 
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'To reduce your weight and combat diabetes',
        'start': {
            'dateTime': datetime.datetime.utcnow().isoformat() ,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': datetime.datetime.utcnow().isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=WEEKLY;COUNT='+str(x)
        ],
        'reminders': {
            'useDefault': True,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }

    elif disease=="hip_problems" and 40<tolerance<80:
        event = {
        'summary': "Tackle diabetes by running", #if disease=="diabetes"  else "Tackle hip problems by running more " if disease=="hip_problems",
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'To reduce your weight and combat diabetes',
        'start': {
            'dateTime': datetime.datetime.utcnow().isoformat() ,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': datetime.datetime.utcnow().isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;INTERVAL=2,COUNT='+str(x)
        ],
        'reminders': {
            'useDefault': True,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }
    elif disease=="hip_problems" and 80<tolerance:
        event = {
        'summary': "Tackle diabetes by running", #if disease=="diabetes"  else "Tackle hip problems by running more " if disease=="hip_problems",
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'To reduce your weight and combat diabetes',
        'start': {
            'dateTime': datetime.datetime.utcnow().isoformat() ,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': datetime.datetime.utcnow().isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT='+str(x)
        ],
        'reminders': {
            'useDefault': True,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }
        }    

    e = GCAL.events().insert(calendarId='primary',
            sendNotifications=True, body=EVENT).execute()

print('''*** %r event added:
    Start: %s
    End:   %s''' % (e['summary'].encode('utf-8'),
        e['start']['dateTime'], e['end']['dateTime']))

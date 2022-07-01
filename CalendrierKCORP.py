from telnetlib import SE
from leaguepedia import response
import datetime
import Settings
from create_event import create_event
for k in range (len(response)):
    
    a= response[k]['title']
    x= a['DateTime UTC']+'.000000'
    x= datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f')
    Settings.start_time= x.isoformat()
    Settings.end_time= (x + datetime.timedelta(hours=1)).isoformat()
    Settings.summary = a['Team1']+ ' vs ' +a['Team2']
    print(Settings.start_time)
    print(Settings.end_time)
    print(Settings.summary)
    create_event()



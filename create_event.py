from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import Settings

def create_event():
   service = get_calendar_service()

   event_result = service.events().insert(calendarId='hni6nck8egtnc1irn3udh8m7e0@group.calendar.google.com',
       body={
           "summary": Settings.summary,
           "description": Settings.description,
           "colorId":0,
           "status": 'confirmed',
           "start": {"dateTime": Settings.start_time, "timeZone": 'Europe/Paris'},
           "end": {"dateTime": Settings.end_time, "timeZone": 'Europe/Paris'},
       }
   ).execute()

   print("created event")
   print("id: ", event_result['id'])
   print("summary: ", event_result['summary'])
   print("starts at: ", event_result['start']['dateTime'])
   print("ends at: ", event_result['end']['dateTime'])


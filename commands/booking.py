import os
import sys
from commands import event_listing as listings
USER_PATHS = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../'))
sys.path.insert(0, USER_PATHS)
import utilities as utils
        

def get_chosen_slot(events, username, uid):
    """
    Function will sort throught the list of open slots given as PARAM:
    If the event with UID given is valid the function will return true and the event details:
    :RETURN: BOOL(True if event is valid/False if invalid), DICT(Event details)
    """
    
    for event in events:
        if event['id'] == uid and len(event['attendees']) == 1:
            if "VOLUNTEER: " + str(username) in event['summary']:
                return False, {}
            return True, event
    return False, {}


def make_booking(username, uid, service_student, service_clinic):
    """
    Function will handle the logic for booking a empty slot.
    with a list of events, user input will be he index of the list -1, the event will be updated with the user added as an attendee.

    """
    slots, output = listings.list_personal_slots(service_clinic, True, False, username)
    if slots == []:
        return False, 'ERROR: This slot is unavailable'
    available, volunteered_event = get_chosen_slot(slots, username, uid)
    if not available:
        return False, 'ERROR: Cannot book chosen slot.'
    updated_event, unique_id = create_booking_body(volunteered_event, username)
    try:
        updated_event_response = service_clinic.events().update(calendarId='primary', eventId=unique_id, body=updated_event).execute()
        booker_accept_invite(service_clinic, unique_id, username, updated_event_response)
        return True, "Booking succesfully made! You're unique id is: "+ str(updated_event_response['id'])
    except:
        return False, "ERROR: An error has stopped the booking from being made.\nPlease try again."


def booker_accept_invite(service_clinic, unique_id, username, event):
    """
    Function will update the event with the user having already accepted the invite to the event.
    """
    event['attendees'][1]['responseStatus'] = 'accepted'
    service_clinic.events().update(calendarId='primary', eventId=unique_id, body=event).execute()


def create_booking_body(event, username):
    """
    Function will take a event object and sort the relevant data to create a body for the new booking.
    User will be added as an attendee and only relevant data will be taken from the event object for body.
    :RETURN: New event body will be returned with updated information.
    """
    event['attendees'].append({'email': username+'@student.wethinkcode.co.za'})

    blueprint = {
            'summary': event['summary'],
            'location': event['location'],
            'start': event['start'],
            'end': event['end'],
            'attendees':event['attendees'],
            'reminders': {
                'useDefault': True,
            },
     }
    return blueprint, event['id']
  


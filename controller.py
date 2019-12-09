import os
from datetime import date
from icalendar import Calendar, Event, vCalAddress, vText


def create_event():
    cal = Calendar()

    event = Event()

    event.add('summary', 'Out of Office')
    event.add('dtstart', date.today())
    event.add('dtend', date.today())

    event.add('description', 'I\'ll be out of office today.')

    organizer = vCalAddress('MAILTO:paulinakhew12345@hotmail.com')
    organizer.params['cn'] = vText('Paulina Khew')
    organizer.params['role'] = vText('Software Engineering Co-op')
    event['organizer'] = organizer
    event['location'] = vText('Out of Office')

    attendee = vCalAddress('MAILTO:paulinakhew12345@hotmail.com')
    attendee.params['ROLE'] = vText('REQ-PARTICIPANT')
    event.add('attendee', attendee, encode=0)

    cal.add_component(event)

    f = open('course_schedule.ics', 'wb')
    f.write(cal.to_ical())
    f.close()
    if os.path.isfile('course_schedule.ics'):
        return True
    return False


if __name__ == '__main__':
    create_event()

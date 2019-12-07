import os
from datetime import datetime
from docx import Document
from icalendar import Calendar, Event


def create_event():
    cal = Calendar()

    event = Event()

    event.add('summary','summary')
    event.add('dtstart', datetime.now())
    event.add('dtend', datetime.now())
    event.add('description', 'Activity')
    event.add('location', 'Room')
    cal.add_component(event)

    f = open('course_schedule.ics', 'wb')
    f.write(cal.to_ical())
    f.close()
    if os.path.isfile('course_schedule.ics'):
        return True
    return False


if __name__ == '__main__':
    create_event()
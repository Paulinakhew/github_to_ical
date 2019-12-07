from datetime import datetime
from docx import Document
from icalendar import Calendar, Event

if __name__ == '__main__':
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

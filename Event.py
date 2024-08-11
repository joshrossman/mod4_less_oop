#Problem Statement: Extend an existing Event class by adding a feature to 
# keep track of the number of participants. Implement a method add_participant
#  that increases the count and a method get_participant_count to retrieve the current count.

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []

    def add_participant(self, name):
        self.participants.append(name)

    def get_participant_count(self):
        print(f"There are currently {len(self.participants)} participants signed up for this event.")

events = []
while True:
    my_choice=input("What would you like to do?\n[1]Create a new event.\n[2]Add a paticipant to an event\n[3]List the number of people attending the event\n[4]Exit\n")
    if my_choice=="1":
        name=input("What is the name of this event?")
        date=input("What is the date of the event?")
        events.append(Event(name,date))
    elif my_choice=="2":
        event_name=input("Which event would you like to add a particpant to?")
        participant_name=input("What is the name of the new participant?")
        event_exists=False
        for event in events:
            if event_name.lower() == event.name.lower():
                event.add_participant(participant_name)
                event_exists=True
        if not event_exists:
            print(f"Sorry, we could not find event called {event_name}")
    elif my_choice=="3":
        event_name=input("Which event would you like to get a participant count for?")
        event_exists=False
        for event in events:
            if event_name.lower() == event.name.lower():
                event.get_participant_count() 
                event_exists=True  
        if not event_exists:
            print(f"Sorry, we could not find event called {event_name}")
    elif my_choice=="4":
        print("Have a great day!")
    else:
        print("This is not a valid response.")
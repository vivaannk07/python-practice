# Event Management System Python Code
class Event:
    def __init__(self,name, date, time, organiser):
        self.name = name
        self.date = date
        self.time = time
        self.organiser = organiser
        self.participants =[]
        self.activities = []    
    
    def display_event_details(self):
        print(f"Event Name: {self.name}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Organiser: {self.organiser.name}")
        print("Participants: ")
        for participant in self.participants:
            print(f"- {participant.name} (ID: {participant.id})")
        print("Activities: ")
        for activity in self.activities:
            print(f"- {activity.name}: {activity.description}")
    
    def add_participant(self,participant):
        self.participants.append(participant)
        return f"Participant {participant.name} with ID {participant.id} has been added"

    def add_activity(self,activity):
        self.activities.append(activity)
        return f"Activity {activity.name} has been added"
    
class Organiser:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact

class Participant:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Activity:
    def __init__(self, name, description):
        self.name = name
        self.description = description

org = Organiser("Raj Events", "9876542310")
e1 = Event("Music Concert", "20th April", "6pm", org)

while True:
    print("Event Management System")
    print("1. Add Participant")
    print("2. Add Activity")
    print("3. Display Event Details")
    print("4. Exit")

    choice = input("Enter your choice: ")
    
    if choice == '1':
        name = input("Enter participant name: ")
        id = input("Enter participant ID: ")
        participant = Participant(name, id)
        print(e1.add_participant(participant))
    elif choice =='2':
        name = input("Enter activity name: ")
        description =input ("Enter description")
        activity = Activity(name, description)
        print(e1.add_activity(activity))
    elif choice == '3':
        e1.display_event_details()
    elif choice == '4':
        print("Exiting")
        break
    else:
        print("Invalid choice")
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def open_seats(self):
        return self.capacity - len(self.passengers)
    def add_passengers(self, name):
        if not self.open_seats():
            return False
        #check for duplicate entry, very wonderful in form submission!
        else:
            self.passengers.append(name)
            return True
    
flight = Flight(3)
passengers = flight.passengers
names = ["Patrick", "Chekwube", "Patrick", "Extra"]
for person in names:
    print(f"Adding {person} to flight....")
    #Check for duplicate entry before adding
    if person in passengers:
        print("Cannot add duplicate entry")
    else:
        #Add the person
        if flight.add_passengers(person):
            print(f"{person} added to flight")
        else:
             print("Can not add further people to flight!")
        
    # if flight.add_passengers(person):
    #     print(f"Added {person} to flight")
    # else:
    #     print("Can not add further people to flight!")
        
print(f"{passengers}")
    

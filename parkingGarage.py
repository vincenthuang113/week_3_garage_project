# Start Your Code here

class Garage:
    def __init__(self):
        self.tickets = [1:10]
        self.parkingSpaces = [1:10]
        self.currentTicket = {}
    
    def takeTicket(self):
        ticket = int(input("Please take a ticket | 1,2,3,4,5,6,7,8,9,10 "))
        self.currentTicket[ticket] = ""
        self.tickets.remove(ticket)
        print(f"You took ticket no.{ticket}! ")

    def payForParking(self):
        pass

    def leavesGarage(self):
        pass
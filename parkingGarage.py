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
        while True:
            pay_ticket = int(input(f"Which ticket will you pay for? Enter '0' to quit: \n{self.currentTicket}"))
            if pay_ticket == 0:
                break
            elif pay_ticket in self.currentTicket.keys():
                pay_confirm = input("Enter any key to pay, or enter 'c' to cancel: ")
                if pay_confirm.lower() == "c":
                    continue
                else:
                    self.currentTicket[pay_ticket]: 'Paid'
                    print(f"Ticket no.{pay_ticket} has been paid! ")
                    break
            else:
                print("Invalid entry.")
    def leavesGarage(self):
        while True:
            leave_ticket = int(input(f"Which ticket will you pay for? Enter '0' to quit: \n{self.currentTicket}"))
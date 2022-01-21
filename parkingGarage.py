class Garage:
    def __init__(self):
        self.tickets = ['1','2','3','4','5','6','7','8','9','10']
        self.currentTicket = {}
    
    def takeTicket(self):
        while True:    
            print(self.tickets)
            ticket = input("Please take a ticket, or enter 'return' to go back: ")
            if ticket.lower() == 'return':
                break
            elif (ticket not in self.tickets):
                print("Invalid entry.")
            else:
                self.currentTicket[ticket] = 'Not paid'
                self.tickets.remove(ticket)
                print(f"You took ticket no.{ticket}! ")
                break

    def payForParking(self):
        while True:
            for key,value in self.currentTicket.items():
                print(f"{key}:{value}",end=" ")
            pay_ticket = input("Which ticket will you pay for? Enter 'return' to go back: ")
            if pay_ticket.lower() == 'return':
                break
            elif pay_ticket in self.currentTicket.keys():
                if self.currentTicket[pay_ticket] == 'Paid':
                    print("This ticket has been paid.")
                else:
                    pay_confirm = input("Enter any key to pay, or enter 'c' to cancel: ")
                    if pay_confirm.lower() == "c":
                        continue
                    else:
                        self.currentTicket[pay_ticket] = 'Paid'
                        print(f"Ticket no.{pay_ticket} has been paid! ")
                        break
            else:
                print("Invalid entry.")

    def leavesGarage(self):
        while True:    
            leave_ticket = input(f"Enter your ticket. Enter 'return' to go back: ")
            if leave_ticket.lower() == 'return':
                break
            elif leave_ticket in self.currentTicket.keys():
                if self.currentTicket[leave_ticket] == 'Paid':
                    del self.currentTicket[leave_ticket]
                    self.tickets.append(leave_ticket)
                    self.tickets.sort(key=int)
                    print("Have a nice day!")
                    break
                elif self.currentTicket[leave_ticket] == 'Not paid':
                    print("Please pay for this ticket.")
                else:
                    print("Invalid entry.")
            else:
                print("Invalid entry.")

    def run(self):
        while True:
            option = input(f"What would you like to do? Ticket | Pay | Leave | Quit \nSpots available: {len(self.tickets)}")
            if option.lower() == 'pay':
                self.payForParking()
            elif option.lower() == 'ticket':
                if len(self.tickets) == 0:
                    print("No tickets available.")
                else:
                    self.takeTicket()
            elif option.lower() == 'leave':
                self.leavesGarage()
            elif option.lower() == 'quit':
                break
            else:
                print("Invalid option.")

my_garage = Garage()
my_garage.run()
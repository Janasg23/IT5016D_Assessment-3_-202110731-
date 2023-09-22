# This program is a help desk ticketing system that allows users to submit tickets, respond to tickets, reopen tickets, and display statistics and tickets.

# This class represents a ticket.
class Ticket:
    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = self.generate_ticket_number()
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet provided"
        self.status = "Open"

#This method generates a ticket number.
    def generate_ticket_number(self):
        counter = 2000
        counter += 1
        return counter
    
#This method generates a new password.
    def request_password_change(self):
        if "Password Change" in self.description:
            new_password = f"{self.staff_id[:2]}{self.creator_name[:3]}"
            self.response = f"New password generated: {new_password}"
            print(f"New password generated: {new_password}")

#This method responds to a ticket.
class HelpDesk:
    def __init__(self):
        self.tickets = []
        self.closed_tickets = 0
        self.open_tickets = 0
        self.resolved_tickets = 0

#This method submits a ticket.
    def submit_ticket(self, staff_id, creator_name, contact_email, description):
        ticket = Ticket(staff_id, creator_name, contact_email, description)

#This method generates a new password.        
        if "Password Change" in description:
            ticket.request_password_change()

        self.tickets.append(ticket)
        self.open_tickets += 1

#This method responds to a ticket.
    def respond_to_ticket(self, ticket_number, response):
        for ticket in self.tickets:
            if ticket.ticket_number == ticket_number:
                ticket.response = response
                ticket.status = "Closed"
                if "Password Change" in ticket.description:
                    ticket.resolve_password_change()
                self.closed_tickets += 1
                self.open_tickets -= 1

#This method reopens a ticket.
    def reopen_ticket(self, ticket_number):
        for ticket in self.tickets:
            if ticket.ticket_number == ticket_number and ticket.status == "Closed":
                ticket.status = "Reopened"
                self.open_tickets += 1
                self.closed_tickets -= 1

#This method displays statistics.
    def display_statistics(self):
        print(f"Number of Tickets Submitted: {len(self.tickets)}")
        print(f"Number of Open Tickets: {self.open_tickets}")
        print(f"Number of Closed Tickets: {self.closed_tickets}")
        print(f"Number of Resolved Tickets: {self.resolved_tickets}")

#This method displays tickets.
    def display_tickets(self):
        for ticket in self.tickets:
            print("Ticket Number:", ticket.ticket_number)
            print("Name of Ticket's Creator:", ticket.creator_name)
            print("Staff ID:", ticket.staff_id)
            print("Email Address:", ticket.contact_email)
            print("Description of the Issue:", ticket.description)
            print("Response from IT Department:", ticket.response)
            print("Ticket Status:", ticket.status)
            print("\n")

support = HelpDesk()

#This method displays the menu.
while True:
    print("1. Submit Ticket")
    print("2. Respond to Ticket")
    print("3. Reopen Ticket")
    print("4. Display Statistics")
    print("5. Display Tickets")
    print("6. Quit")

    choice = input("Enter your choice: ")

#This method allows the user to submit a ticket.
    if choice == "1":
        while True:
            staff_id = input("Enter Staff ID: ")
            creator_name = input("Enter Ticket Creator Name: ")
            contact_email = input("Enter Contact Email: ")
            description = input("Enter Description of the Issue (Type 'Password Change' for a new password request): ")

            support.submit_ticket(staff_id, creator_name, contact_email, description)
            if "Password Change" in description:
                another_ticket = input("Do you want to submit another ticket? (Y / N): ")
                if another_ticket.lower() != "y":
                    break
            else:
                print("Ticket submitted successfully!")
                break

#This method allows the help desk to respond to a support ticket.
    elif choice == "2":
        ticket_number = int(input("Enter Ticket Number: "))
        response = input("Enter Response: ")
        support.respond_to_ticket(ticket_number, response)
        print("Response added successfully!")

#This method allows the help desk to reopen a support ticket.
    elif choice == "3":
        ticket_number = int(input("Enter Ticket Number to Reopen: "))
        support.reopen_ticket(ticket_number)
        print("Ticket reopened successfully!")

#This method allows the help desk to display statistics.
    elif choice == "4":
        support.display_statistics()

#This method allows the help desk to display tickets.
    elif choice == "5":
        support.display_tickets()

#This method allows the help desk to quit the program.
    elif choice == "6":
        break
#This method displays an error message if the user enters an invalid choice.
    else:
        print("Invalid choice. Please try again.")

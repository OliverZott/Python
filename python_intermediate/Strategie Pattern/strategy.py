import string
import random
from typing import List
from enum import Enum


def generate_id(length=8):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class Strategy(Enum):
    FIFO = 'fifo'
    FILO = 'filo'
    RND = 'random'


class SupportTicket:
    id: str
    customer: str
    issue: str

    def __init__(self, customer: str, issue: str) -> None:
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class CustomerSupport:
    tickets: List[SupportTicket] = []

    def create_ticket(self, customer: str, issue: str):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: str = "fifo") -> None:
        if len(self.tickets) == 0:
            print("No tickets to process.")
            return

        # Use switch-case instead maybe
        if processing_strategy == Strategy.FIFO:
            for ticket in self.tickets:
                self.process_ticket(ticket)
        elif processing_strategy == Strategy.FILO:
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)
        elif processing_strategy == Strategy.RND:
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
                self.process_ticket(ticket)
        else:
            raise Exception("Invalid processingstrategy!")

    @staticmethod
    def process_ticket(ticket: SupportTicket):
        print(f"Ticket {ticket.id} processed!")
        # return f"Ticket {ticket.id} processed!"


if __name__ == "__main__":

    cst = CustomerSupport()
    cst.create_ticket("Olli", "ticket nr 1")
    cst.create_ticket("Olli", "ticket nr 2")
    cst.create_ticket("Olli", "ticket nr 3")

    cst.process_tickets(Strategy.FIFO)

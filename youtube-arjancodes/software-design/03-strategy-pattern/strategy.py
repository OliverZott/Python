import string
import random
from typing import List
from enum import Enum
from abc import ABC, abstractmethod


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


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()


# Alternativly use revered(list) for iterator instead reversing the whole list!
class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy


class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy


class CustomerSupport:
    tickets: List[SupportTicket] = []

    def create_ticket(self, customer: str, issue: str):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy) -> None:

        ticket_list = processing_strategy.create_ordering(self.tickets)

        if len(ticket_list) == 0:
            print("No tickets to process.")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)

        # if processing_strategy is FILOOrderingStrategy:
        #     for ticket in self.tickets:
        #         self.process_ticket(ticket)
        # elif processing_strategy == Strategy.FILO:
        #     for ticket in reversed(self.tickets):   # used reversed iterator
        #         self.process_ticket(ticket)
        # elif processing_strategy == Strategy.RND:
        #     list_copy = self.tickets.copy()
        #     random.shuffle(list_copy)
        #     for ticket in list_copy:
        #         self.process_ticket(ticket)
        # else:
        #     raise Exception("Invalid processing strategy!")

    @staticmethod
    def process_ticket(ticket: SupportTicket):
        print(
            f"Ticket {ticket.id} processed: {ticket.issue} from {ticket.customer}")
        # return f"Ticket {ticket.id} processed!"


if __name__ == "__main__":
    cst = CustomerSupport()
    cst.create_ticket("Olli", "ticket nr 1")
    cst.create_ticket("Olli", "ticket nr 2")
    cst.create_ticket("Olli", "ticket nr 3")

    order_strat = FILOOrderingStrategy()
    cst.process_tickets(order_strat)

    cst.process_tickets(RandomOrderingStrategy())
    # cst.process_tickets(Strategy.FIFO)

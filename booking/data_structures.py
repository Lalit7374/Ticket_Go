# booking/data_structures.py

class TicketQueue:
    def __init__(self):
        self.queue = []

    def book_ticket(self, ticket):
        self.queue.append(ticket)

    def cancel_ticket(self):
        if self.queue:
            return self.queue.pop(0)  # Remove the first ticket from the queue
        return None

class CancellationStack:
    def __init__(self):
        self.stack = []

    def cancel_ticket(self, ticket):
        self.stack.append(ticket)

    def undo_cancel(self):
        if self.stack:
            return self.stack.pop()  # Undo the cancellation
        return None

class TicketHistoryLinkedList:
    def __init__(self):
        self.history = []

    def add_history(self, ticket):
        self.history.append(ticket)

    def get_all_history(self):
        return self.history

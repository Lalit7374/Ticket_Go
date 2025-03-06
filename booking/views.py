
from django.shortcuts import render
from .data_structures import TicketQueue, CancellationStack, TicketHistoryLinkedList


ticket_queue = TicketQueue()
cancellation_stack = CancellationStack()
ticket_history = TicketHistoryLinkedList()


ticket_id_counter = 1


def home(request):
    return render(request, 'booking/home.html')


def book_ticket(request):
    global ticket_id_counter
    if request.method == 'POST':
        
        passenger_name = request.POST.get('passenger_name')
        passenger_age = request.POST.get('passenger_age')
        travel_date = request.POST.get('travel_date')

        
        ticket_id = ticket_id_counter
        ticket_id_counter += 1
        ticket = f"Ticket-{ticket_id} - {passenger_name}, Age: {passenger_age}, Date: {travel_date}"

        
        ticket_queue.book_ticket(ticket)
        ticket_history.add_history(f"Booked {ticket}")

        
        return render(request, 'booking/book_ticket.html', {
            'ticket': ticket,
            'queue': list(ticket_queue.queue)
        })
    return render(request, 'booking/book_ticket.html')


def cancel_ticket(request):
    ticket = ticket_queue.cancel_ticket()
    if ticket:
        cancellation_stack.cancel_ticket(ticket)
        ticket_history.add_history(f"Cancelled {ticket}")
    return render(request, 'booking/cancel_ticket.html', {
        'canceled_ticket': ticket,
        'stack': cancellation_stack.stack
    })


def undo_cancel(request):
    ticket = cancellation_stack.undo_cancel()
    if ticket:
        ticket_queue.book_ticket(ticket)
        ticket_history.add_history(f"Rebooked {ticket}")
    return render(request, 'booking/undo_cancel.html', {
        'rebooked_ticket': ticket,
        'queue': list(ticket_queue.queue)
    })


def show_booked_ticket(request):
    
    booked_tickets = ticket_history.get_all_history()

    return render(request, 'booking/show_booked_ticket.html', {
        'booked_tickets': booked_tickets
    })

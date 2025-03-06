# Ticket_Go - Ticket Booking System

## Project Overview
Ticket_Go is a ticket booking system designed to allow users to book, cancel, and view tickets. It uses a variety of data structures to manage and optimize ticket operations, including queues for booking, stacks for cancellations, and linked lists to store booking history. 

This project is built using **Django** for the backend and **Python** for data structure management.

## Technologies Used
- **Python**: The primary programming language for implementing ticket booking logic and data structures.
- **Django**: The web framework used for building the backend and handling HTTP requests and responses.
- **Data Structures**: 
  - **Queue**: Used for managing ticket bookings in a First-Come-First-Serve (FIFO) manner.
  - **Stack**: Used for handling ticket cancellations and undoing cancellations (Last-In-First-Out).
  - **Linked List**: Used to store the history of ticket bookings, cancellations, and rebookings.
  
## Features
- **Booking Tickets**: Users can book tickets which are added to a queue.
- **Cancel Tickets**: Canceled tickets are added to a stack, with the ability to undo cancellations.
- **Ticket History**: The system keeps track of all bookings, cancellations, and rebookings using a linked list.
- **Undo Cancellation**: Users can undo cancellations, re-booking the most recently canceled ticket.

## Snapshot's of project
![image](https://github.com/user-attachments/assets/c0c3457a-47dd-4d28-8d4b-0d043e99c9af)

![image](https://github.com/user-attachments/assets/ae35a565-cce2-414d-9b1b-b6fced9ef94d) 

![image](https://github.com/user-attachments/assets/06608864-a675-429d-a16f-c8307b2d75c5)

![image](https://github.com/user-attachments/assets/4dec4e07-5f18-4c9f-86bb-92fe8a7f29fd)




### Clone the repository

To get started with this project, first clone the repository:

```bash
git clone https://github.com/Lalit7374/Ticket_Go.git

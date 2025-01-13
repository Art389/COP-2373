# The code is simply running tests to see how many buyers could buy the max amount of tickets (20 tickets).


def buy_tickets(remaining_tickets, simulated_input):
    while True:
        try:
            desired_tickets = int(next(simulated_input))
            print(f"How many tickets do you wanna buy? (Max 4, Available: {remaining_tickets}): {desired_tickets}")
            if desired_tickets < 1 or desired_tickets > 4:
                print("You can only buy 1-4 tickets.")
            elif desired_tickets > remaining_tickets:
                print(f"Only {remaining_tickets} tickets available.")
            else:
                return desired_tickets
        except ValueError:
            print("Enter a number.")
        except StopIteration:
            print("No simulated inputs available.")
            return 0

def cinema_ticket_presale(simulated_inputs):
    total_tickets = 20
    remaining_tickets = total_tickets
    total_buyers = 0

    print("The Cinema Ticket Pre-sale!")

    simulated_input_iter = iter(simulated_inputs)

    while remaining_tickets > 0:
        print(f"\nTickets remaining: {remaining_tickets}")
        tickets_bought = buy_tickets(remaining_tickets, simulated_input_iter)
        if tickets_bought == 0:
            break
        remaining_tickets -= tickets_bought
        total_buyers += 1
        print(f"You bought {tickets_bought} ticket(s). {remaining_tickets} ticket(s) remaining.")

    print("\nAll tickets sold!")
    print(f"Total buyers: {total_buyers}")

simulated_inputs = [3, 4, 5, 2, 4, 3] 
cinema_ticket_presale(simulated_inputs)

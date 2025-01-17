# This program allows each buyer to purchase up to 4 tickets and stops once all 20 tickets are sold.

# Function for one purchase.
def process_purchase(remaining_tickets, buyers):
    
    # Ask user for the number of tickets they want to buy.
    tickets_requested = int(input("Enter the number of tickets you want to purchase (max 4): "))

    # Checks to see if the request is valid.
    if 1 <= tickets_requested <= 4:
        if tickets_requested <= remaining_tickets:
            remaining_tickets -= tickets_requested
            buyers += 1
            print(f"You have purchased {tickets_requested} ticket(s).")
        else:
            print("Not enough tickets remaining.")
    else:
        print("You can only purchase between 1 to 4 tickets.")

    print(f"Tickets remaining: {remaining_tickets}")
    return remaining_tickets, buyers

# Function to manage the ticket pre-sale process.
def ticket_presale():
    total_tickets = 20  # Total tickets available to buy.
    remaining_tickets = total_tickets
    buyers = 0  # Accumulates the number of buyers.

    # Loop for tickets until all are sold.
    while remaining_tickets > 0:
        remaining_tickets, buyers = process_purchase(remaining_tickets, buyers)

    print(f"All tickets sold! Total buyers: {buyers}")

# Main execution.
ticket_presale()

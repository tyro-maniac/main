###################################################################################################################################
### Thank you for downloading the calculator! It works purely inside of the command line. It will ask you to                    ###
### input a party name, then it's vote count/percentage, and so on until you type "done", rather than a new party's name.       ###
### Make sure to run it inside of a code editor like Visual Studio Code, running it on it's own will cause it to immediately    ###
### close upon finishing the calculation!                                                                                       ###
###                                                                                                                             ###
### Enjoy and have fun creating!                                                                                                ###        
### -Tyro                                                                                                                       ### 
###################################################################################################################################

def dhondt(votes, total_seats):
    seats = {party: 0 for party in votes}

    for _ in range(total_seats):
        quotients = {party: votes[party] / (seats[party] + 1) for party in votes}
        winner = max(quotients, key=quotients.get)
        seats[winner] += 1

    return seats


if __name__ == "__main__":
    print("Enter parties and their vote counts or percentages.")
    print("Type 'done' when finished.\n")

    election_results = {}
    while True:
        party = input("Party name: ")
        if party.lower() == "done":
            break
        try:
            votes_input = input(f"Votes/Percentage for {party}: ")
            votes = float(votes_input.replace(",", "."))
        except ValueError:
            print("Invalid input. Try again.")
            continue
        election_results[party] = votes

    # Ask for the cutoff threshold
    try:
        cutoff_input = input("\nMinimum percentage to qualify (e.g., 5 for 5%): ")
        cutoff = float(cutoff_input.replace(",", "."))
    except ValueError:
        print("Invalid input. Using default cutoff of 0%.")
        cutoff = 0.0

    # Remove parties below the cutoff
    election_results = {party: v for party, v in election_results.items() if v >= cutoff}

    if not election_results:
        print("\nNo party meets the cutoff threshold!")
    else:
        try:
            total_seats = int(input("\nTotal number of seats: "))
        except ValueError:
            print("Invalid number of seats. Using default 130.")
            total_seats = 130

        allocation = dhondt(election_results, total_seats)

        print("\nSeat allocation results:")
        for party, seats in allocation.items():
            print(f"{party}: {seats}")
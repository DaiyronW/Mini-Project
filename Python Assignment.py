
#Daiyron Williams
#04 Jan 2024
#Travel Destination Code

def suggest_travel_destination():
    print("Welcome to the Travel Destination Suggester!")
    
    # Get user input for their preferred season
    while True:
        season = input("Enter your preferred season (spring, summer, fall, winter): ").lower()
        if season in ['spring', 'summer', 'fall', 'winter']:
            break
        else:
            print("Invalid input. Please enter a valid season.")

    # Determine travel destination based on the user's season preference
    if season == 'spring':
        print("Great choice! Spring is perfect for exploring cherry blossoms in Kyoto, Japan.")
    elif season == 'summer':
        print("Nice! Summer is ideal for a beach vacation in Bali, Indonesia.")
    elif season == 'fall':
        print("Awesome! Fall is the best time to witness the vibrant foliage in New England, USA.")
    elif season == 'winter':
        print("Excellent! Winter calls for a skiing adventure in the Swiss Alps, Switzerland.")

    # Ask the user if they want more suggestions
    while True:
        more_suggestions = input("Would you like more travel suggestions? (yes/no): ").lower()
        if more_suggestions in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if more_suggestions == 'yes':
        # Recursively call the function for more suggestions
        suggest_travel_destination()
    else:
        print("Thank you for using the Travel Destination Suggester!")

# Run the program
suggest_travel_destination()


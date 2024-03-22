import time
import random

def print_pause(message):
    print(message)
    #time.sleep(2)

def intro():
    print_pause("Welcome to 'Blind Date'!")
    print_pause("You've been set up on a blind date with a mystery person.")
    print_pause("You'll get to ask a series of questions to determine if you're compatible.")
    print_pause("Let's see if love is truly blind!")

def question_round(round_number):
    print_pause(f"\nRound {round_number}")
    print_pause("Choose a category to ask a question:")
    print_pause("1. Hobbies")
    print_pause("2. Favorite Foods")
    print_pause("3. Dream Vacation")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice in ['1', '2', '3']:
            break
        else:
            print_pause("Invalid choice. Please enter 1, 2, or 3.")

    if choice == '1':
        hobbyselection = input("Pick a selection from \nA.Working Out \nB.Traveling\nC.Binging Shows\nD.Trying New Restaurants")
        hobbystring = ""
        match hobbyselection.upper():
            case "A":
                hobbystring = "Working Out"
                print_pause("You chose 'Working Out'")
            case "B":
                hobbystring = "Traveling"
                print_pause("You chose 'Traveling'")
            case "C":
                hobbystring = "Binging Shows"
                print_pause("You chose 'Binging Shows'")
            case "D":
                hobbystring = "Trying New Restaurants"
                print_pause("You chose 'Trying New Restaurants'")
        hobbies = ['Working Out', 'Traveling', 'Binging Shows', 'Trying New Restaurants']
        hobby = random.choice(hobbies)
        print_pause(f"Your date says: 'I love {hobby}!'")
        if hobby == hobbystring:
            print_pause("Your date says: 'OMG! I love that too!'")
            return 1
        else:
            print_pause("Your date says: 'I don't love that!'")
            return 0
    elif choice == '2':
        foods = ['Pepperoni Pizza', 'Sushi', 'Birria Tacos', 'Pho']
        food = random.choice(foods)
        print_pause(f"Your date says: 'I can't resist {food}!'")
        return 1
    elif choice == '3':
        vacations = ['a tropical beach', 'a ski resort', 'a city adventure', 'a cozy cabin']
        vacation = random.choice(vacations)
        print_pause(f"Your date says: 'My dream vacation is {vacation}!'")
        return 0

def play_game():
    compatibility_score = 0
    intro()

    for round_number in range(1, 4):
        compatibility_score += question_round(round_number)

    print_pause(f"\nYour compatibility score is: {compatibility_score}")

    if compatibility_score >= 2:
        print_pause("Congratulations! You and your date are a match made in Heaven!")
    else:
        print_pause("Sorry, it seems like you and your date aren't quite compatible so you'll end up alone")

    play_again = input("\nDo you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        play_game()
    else:
        print_pause("Thanks for playing 'Blind Date'! Goodbye!")

play_game()
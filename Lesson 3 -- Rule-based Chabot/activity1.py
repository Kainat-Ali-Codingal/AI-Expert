import re
import random
import colorama
from colorama import Fore, init

init(autoreset=True)
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don’t programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# text.strip(): removes all trailing and leading whitespaces
# re.sub(r"\s+", " "): removes the occurance of one or more white spaces with a single space
def nomralize_user_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Displays a list of commands and features that TravelBot can handle.
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say ‘recommendation’)")
    print(Fore.GREEN + "- Offer packing tips (say ‘packing’)")
    print(Fore.GREEN + "- Tell a joke (say ‘joke’)")
    print(Fore.CYAN + "Type ‘exit’ or ‘bye’ to end.\n")

# Offers simple packing advice based on the destination and duration provided by the user.
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = nomralize_user_input(input(Fore.YELLOW + "You: "))

    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

# Prompt for Destination Type:
# Asks the user if they prefer beaches, mountains, or cities.
# Normalize and Check Input:
# The user’s answer is normalized and checked against the keys in the destinations dictionary.
# Random Suggestion:
# If the input matches a key, the bot picks a random destination from that category using random.choice().
# User Feedback Loop:
# If the user answers "yes", it confirms the suggestion.
# If the user answers "no" or gives an unrecognized answer, the function calls itself recursively to try again.
# Invalid Input Handling:
# If the preference isn’t in the dictionary, the bot informs the user it doesn’t have that type of destination.
# Show Help:
# After processing the recommendation, the show_help() function is called to remind the user of other available commands.
def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")

    preference = nomralize_user_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let’s try another.")
            recommend()  # Recursive call if the user rejects the suggestion

        else:
            print(Fore.RED + "TravelBot: I’ll suggest again.")
            recommend()  # Recursive call on unrecognized answer

    else:
        print(Fore.RED + "TravelBot: Sorry, I don’t have that type of destination.")
    show_help()

def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")


# Main chat gonna happrn here
def chat():
    print(Fore.CYAN + "Hello! I’m TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")
    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = nomralize_user_input(user_input)
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input or "packing" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")


## Calling main function start
## This gonna make sure this main function runs only when script runs, not when imported as a module
if __name__ == "__main__":
    chat()

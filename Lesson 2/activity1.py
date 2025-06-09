# Used for processing textual data, including sentiment analysis.
from textblob import TextBlob
# Imports the entire colorama library which is used to print colored text in the terminal.
import colorama
# Imports specific objects (Fore and Style) from the colorama module.
# Fore: Contains constants for text colors (e.g., Fore.RED, Fore.GREEN, etc.).
# Style: Contains constants for text style and resets (e.g., Style.RESET_ALL).
from colorama import Fore, Style

# colorama.init(autoreset=True) is used to automatically reset the text color after each print statement.
# Initializes colorama to enable colored text output in the terminal.
colorama.init(autoreset=True)

print(f"{Fore.CYAN}👋🎉 Welcome to Sentiment Spy! 🕵️{Style.RESET_ALL}")
#lower converts to lowercase, strip removes any starting or ending whitespaces
username = input(f"{Fore.CYAN}\nWhat's your name? {Style.RESET_ALL}").strip()
if not username:
    # Meaning if Username empty, assign mystery agent
    print(f"{Fore.RED}Ooooh, a Mystery Agent is among us... No worries, your identity and conversations are safe with me!{Style.RESET_ALL}")
    username = "Mystery"


# Let's say I want to maintain a chat history for the current run
# in each item, we will a tuple of sentence, polarity level, and sentiment type
history = []

print(f"{Fore.CYAN}\nHello, Agent {username}! 🤖")
print(f"I'm here to help you analyze the sentiment of your messages. Let's get started!")
print(f"Type {Fore.YELLOW} 'reset'{Fore.CYAN}, {Fore.YELLOW} 'history'{Fore.CYAN}, and {Fore.YELLOW} 'exit'{Fore.CYAN} to quit the chat at any time.\n")

while True:
    user_input = input(f"\n{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter a message.{Style.RESET_ALL}")
        continue

    # Check for special commands
    if user_input.lower() == "reset":
        history.clear()
        print(f"{Fore.CYAN}Chat history has been CLEARED!.{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not history:
            print(f"{Fore.CYAN}No chat history available.")
        else:
            print(f"{Fore.YELLOW}Chat History:{Style.RESET_ALL}")
            for idx, (sentence, polarity, sentiment) in enumerate(history):
                print(f"{Fore.RED}{idx+1}. {sentence} | Polarity: {polarity:.2F} | Sentiment: {sentiment}{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "exit":
        print(f"{Fore.CYAN}Goodbye, Agent {username}! Stay safe out there while I keep your conversations secure!{Style.RESET_ALL}")
        break

    # Processing simple user input
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity
    sentiment = "Neutral"
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"

    # Storing in history now
    history.append((user_input, polarity, sentiment))
    print(f"{Fore.CYAN}Sentiment Analysis Result:{Style.RESET_ALL}")
    print(f"\t{Fore.YELLOW}User Input: {user_input}{Style.RESET_ALL}")
    print(f"\t{Fore.YELLOW}Polarity: {polarity:.2f}{Style.RESET_ALL}")
    print(f"\t{Fore.YELLOW}Sentiment: {sentiment}{Style.RESET_ALL}")

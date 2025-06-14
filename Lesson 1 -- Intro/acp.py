# from textblob import TextBlob
# import colorama
# from colorama import Fore, Style
# colorama.init(autoreset=True)


# def print_colored(text, color):
#     """
#     Print text in a specified color.
    
#     Parameters:
#     text (str): The text to print.
#     color (str): The color to use (e.g., 'red', 'green', 'blue').
#     """
#     colors = {
#         'red': Fore.RED,
#         'green': Fore.GREEN,
#         'blue': Fore.BLUE,
#         'yellow': Fore.YELLOW,
#         'cyan': Fore.CYAN,
#         'magenta': Fore.MAGENTA,
#         'white': Fore.WHITE
#     }
    
#     if color in colors:
#         print(colors[color] + text + Style.RESET_ALL)
#     else:
#         print(text)  # Default to no color if the specified color is not found

# def main():
#     print_colored("Hello, World!", "green")



# # __name__ is a special variable that holds the name of the current module.
# # When a Python file is executed directly, __name__ is set to __main__.
# # When a file is imported as a module, __name__ is set to the module's name.
# # The if __name__ == '__main__': block ensures that the main function is only called when the script is run directly, not when it's imported into another script.
# if __name__ == '__main__':
#     main()



print("Hello! I am AI Bot. What's your name?")
name = input()
print(f"Nice to meet you, {name}!")

while True:
    print("How are you feeling today? (good/bad/okay)")
    mood = input().lower()

    if mood == "good":
        print("I'm glad to hear that! What made your day good?")
    elif mood == "bad":
        print("I'm sorry to hear that. Is there something you want to share?")
    elif mood == "okay":
        print("Got it. Sometimes 'okay' is just right.")
    else:
        print("I see. Sometimes it's hard to put feelings into words.")

    print("What is one thing you like to do in your free time?")
    hobby = input()
    print(f"That sounds fun! {hobby} is a great way to spend time.")

    print("Would you like to keep chatting? (yes/no)")
    choice = input().lower()

    if choice == "no":
        print(f"It was nice chatting with you, {name}. Goodbye!")
        break

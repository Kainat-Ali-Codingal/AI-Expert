# A basic chatbot using print and input commands
print("\n\nHey there! I'm a coding instructor. What's your name?")
name = input()
print(f"Nice to meet you, {name}!\n")


print("I'd love to know a little more about you before we start. Can you share how you're feeling today? (good/bad/upset/happy)")
mood = input()
if mood.lower() in ["good", "happy"]:
    print("That's great to hear! Let's make the most of our time together.")
elif mood.lower() in ["bad", "upset"]:
    print("I'm sorry to hear that. I hope coding can help take your mind off things.")
else:
    print("I can understand. Sometimes it's hard to put words to how we feel. Let's just focus on coding for now.")


print("\nOh! I'm afraid I'm late for a class. But catch you later? See you soon!\n\n")


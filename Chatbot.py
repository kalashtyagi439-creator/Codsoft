from datetime import datetime
import random

BOT_NAME = "KalashAI"

jokes = [
    "Why do programmers love Python? Because it makes coding feel like English!",
    "Debugging is like being a detective in a movie where you are also the culprit.",
    "I would tell you a coding joke, but it might not compile."
]

quotes = [
    "Success is the sum of small efforts repeated every day.",
    "Dream big, start small, act now.",
    "Consistency beats motivation."
]

print("=" * 50)
print(f"🤖 Welcome to {BOT_NAME}")
print("Type 'help' to see commands")
print("Type 'bye' to exit")
print("=" * 50)

while True:
    user = input("\nYou: ").strip().lower()

    if user in ["hi", "hello", "hey"]:
        print(f"{BOT_NAME}: Hello! Hope you're having a great day.")

    elif "name" in user:
        print(f"{BOT_NAME}: My name is {BOT_NAME}, your virtual assistant.")

    elif "time" in user:
        print(f"{BOT_NAME}: Current Time:",
              datetime.now().strftime("%I:%M:%S %p"))

    elif "date" in user:
        print(f"{BOT_NAME}: Today's Date:",
              datetime.now().strftime("%d-%m-%Y"))

    elif "joke" in user:
        print(f"{BOT_NAME}: {random.choice(jokes)}")

    elif "motivate" in user or "quote" in user:
        print(f"{BOT_NAME}: {random.choice(quotes)}")

    elif "attendance" in user:
        print(f"{BOT_NAME}: Attend classes regularly and maintain above 75% attendance.")

    elif "exam" in user:
        print(f"{BOT_NAME}: Start preparation early and practice previous year questions.")

    elif "library" in user:
        print(f"{BOT_NAME}: Library timing is generally 9 AM to 5 PM.")

    elif "calculator" in user:
        try:
            expression = input("Enter expression (Example: 10+20): ")
            result = eval(expression)
            print(f"{BOT_NAME}: Result = {result}")
        except:
            print(f"{BOT_NAME}: Invalid Expression!")

    elif user == "help":
        print("""
Available Commands:
• hi / hello
• name
• time
• date
• joke
• motivate
• attendance
• exam
• library
• calculator
• help
• bye
        """)

    elif user == "bye":
        print(f"{BOT_NAME}: Goodbye! Have a productive day.")
        break

    else:
        print(f"{BOT_NAME}: Sorry, I don't understand that command.")
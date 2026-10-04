import datetime
import random

fun_facts = [
    "A triangle has three sides.",
    "Python strings are sequences of characters.",
    "Seven days make a week.",
]
jokes = [
    "I'm so good at sleeping. \nI can do it with my eyes closed.",
    "Why was the math book worried? It had too many problems.",
]


def run_assistant():
    name = ""
    print("Welcome to the Command Assistant!")
    try:
        while True:
            choice = input(
                "\nHow can I help?\n 1. Time\n 2. Date\n 3. Remember a name\n"
                " 4. Recall the name\n 5. Fun fact\n 6. Joke\n 7. Quit\n"
            ).strip().lower()

            if choice in ("7", "quit", "exit"):
                print("Goodbye!")
                return
            if choice == "1":
                print(datetime.datetime.now().strftime("%H:%M"))
            elif choice == "2":
                print(datetime.datetime.now().strftime("%Y-%m-%d"))
            elif choice == "3":
                name = input("Type a name to remember: ").strip()
            elif choice == "4":
                print("The stored name is " + name if name else "No name is stored yet.")
            elif choice == "5":
                print(random.choice(fun_facts))
            elif choice == "6":
                print(random.choice(jokes))
            else:
                print("Unknown command. Choose 1 through 7, quit, or exit.")
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")


if __name__ == "__main__":
    run_assistant()

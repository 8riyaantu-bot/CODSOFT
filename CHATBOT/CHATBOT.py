def chatbot():
    print("Chatbot: Hello! I am your assistant 🤖")
    name = input("Chatbot: What is your name? ")
    print(f"Chatbot: Nice to meet you, {name}!")

    while True:
        user = input("You: ").lower()

        # Greetings
        if "hello" in user or "hi" in user:
            print(f"Chatbot: Hello {name}! 😊")

        # How are you
        elif "how are you" in user:
            print("Chatbot: I'm doing great! How about you?")

        # About chatbot
        elif "your name" in user:
            print("Chatbot: I am a rule-based AI chatbot.")

        # Joke
        elif "joke" in user:
            print("Chatbot: Why did the computer go to the doctor? Because it had a virus! 😂")

        # Help
        elif "help" in user:
            print("Chatbot: I can respond to greetings, jokes, and simple questions.")

        # Simple addition
        elif "add" in user:
            try:
                nums = user.split()
                a = int(nums[-2])
                b = int(nums[-1])
                print("Chatbot: Result =", a + b)
            except:
                print("Chatbot: Please enter like 'add 5 10'")

        # Exit
        elif "bye" in user:
            print(f"Chatbot: Goodbye {name}! 👋")
            break

        # Default
        else:
            print("Chatbot: Sorry, I didn't understand that. Try 'help'.")

chatbot()

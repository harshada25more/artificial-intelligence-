
print("ChatBot: Hello! I am your chatbot.")
print("ChatBot: You can talk with me.")
print("ChatBot: Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("ChatBot: Hey! How are you?")

    elif "your name" in user:
        print("ChatBot: My name is MiniBot!")

    elif "how are you" in user:
        print("ChatBot: I am doing great! How about you?")

    elif "good" in user:
        print("ChatBot: That's great! Keep smiling.")

    elif "sad" in user:
        print("ChatBot: Don't worry. Everything will be okay.")

    elif "study" in user:
        print("ChatBot: Keep learning! You are doing amazing.")

    elif "thank" in user:
        print("ChatBot: You're welcome!")

    elif user == "bye":
        print("ChatBot: Goodbye! Have a great day.")
        break

    else:
        print("ChatBot: Interesting! Tell me more.")

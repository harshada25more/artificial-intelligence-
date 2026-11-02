def chatbot(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you?"

    elif "name" in message:
        return "My name is Chatbot."

    elif "how are you" in message:
        return "I am fine, thank you!"

    elif "bye" in message:
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."


print("Chatbot: Hello! Type bye to exit.")

while True:
    user = input("You: ")
    response = chatbot(user)

    print("Chatbot:", response)

    if "bye" in user.lower():
        break
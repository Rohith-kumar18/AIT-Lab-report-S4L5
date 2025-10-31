
import openai
openai.api_key = "sk-T70IEYMFS8IUAT3BIDKFTVT7DUGBIYGE9YUBS7"

messages = []

system_msg = input("What type of chatbot would you like to create? ")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready! Type 'quit' to end the chat.\n")

while True:
    message = input("You: ")
    if message.lower() == "quit":
        break

    messages.append({"role": "user", "content": message})
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})

    print("\n"+ reply +"\n")

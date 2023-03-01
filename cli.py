import openai
import os


messages = [
    # system message first, it helps set the behavior of the assistant
    {"role": "system", "content": "You are a helpful assistant."},
]

while True:
    message = input("👨‍💻: ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        # doc is here https://platform.openai.com/docs/guides/chat/chat-vs-completions?utm_medium=email&_hsmi=248334739&utm_content=248334739&utm_source=hs_email
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    # get the reply
    reply = chat_completion.choices[0].message.content
    print(f"🤖: {reply}")
    messages.append({"role": "assistant", "content": reply})

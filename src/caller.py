from openai import OpenAI
import sys
import os
client = OpenAI()


def messageAI(user_input, system_input=""):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides short, direct responses about terminal commands. If the user asks about something else, respond concisely but appropriately. Keep responses to a single sentence"},
            {
                "role": "system", "content": f"{os.getcwd()} is the users current directory"
            },
            {
                "role": "user",
                "content": f"{user_input}"
            }
        ]
    )

    response = completion.choices[0].message.content
    print(" ".join(response.split("\n")))


def main(arg1):
    user_input = arg1
    messageAI(user_input)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide an argument")

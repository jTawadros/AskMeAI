from openai import OpenAI
import sys
import os
import re
client = OpenAI()


def messageAI(user_input):

    current_dir = os.getcwd()
    dir_contents = "\n".join(os.listdir())

    system_prompt = (
        "You are a helpful assistant that provides short, direct responses about terminal commands.\n"
        "If user asks about something other than terminal commands answer in short direct responses\n"
        "Keep responses to one sentence whenever possible\n"
        f"The user's current directory is {current_dir}.\n"
        f"The files that are in this directory are {dir_contents}"
    )
    _messages = [
        {
            "role": "system", "content": system_prompt
        },
        {
            "role": "user", "content": user_input
        }
    ]

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=_messages
    )

    clean_text = re.sub(r"'''(.*?)'''", "", completion.choices[0].message.content, flags=re.DOTALL).strip()
    print(clean_text)


def main(arg1):
    user_input = arg1
    messageAI(user_input)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide an argument")

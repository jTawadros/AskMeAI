from openai import OpenAI
import sys
import subprocess
import os
import re
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Path to your dedicated ask history file
HISTORY_FILE = os.path.expanduser("~/.ask_command_history")


def append_to_history(command):
    try:
        with open(HISTORY_FILE, "a") as f:
            f.write(command + "\n")
    except Exception as e:
        print(f"Warning: Could not update history file: {e}")


def get_command_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            lines = f.readlines()
        return "".join(lines[-100:]).strip()
    except Exception:
        return "No history available."


def messageAI(user_input):
    current_dir = os.getcwd()
    try:
        dir_contents = "\n".join(os.listdir())
    except Exception as e:
        dir_contents = "Unable to list directory contents."
    command_history = get_command_history()

    system_prompt = (
        "You are a terminal assistant that helps answer command-line queries and personal questions using only the context provided below. "
        "Your responses must be one concise sentence.\n\n"
        "Use the context below to answer questions about the user or command reminders."
        "Context:\n"
        f"Current Working Directory: {current_dir}\n\n"
        f"Directory Contents:\n{dir_contents}\n\n"
        f"Recent Terminal Commands:\n{command_history}\n"
    )

    _messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=_messages
    )

    clean_text = re.sub(
        r"'''(.*?)'''", "", completion.choices[0].message.content, flags=re.DOTALL).strip()
    print(clean_text)


def main(arg1):
    append_to_history(arg1)
    user_input = arg1
    messageAI(user_input)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Please provide an argument")


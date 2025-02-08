import sys
import requests
import re

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"


def clean_response(response):
    # Getting rid of <think>
    response = re.sub(r"<think>.*?</think>", "", response,
                      flags=re.DOTALL)  
    return response.strip()


def query_ollama(prompt):
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response_data = response.json()
        if "error" in response_data:
            return f"Ollama API Error: {response_data['error']}"

        clean_text = clean_response(response_data.get(
            "response", "No response received from Ollama."))
        return clean_text

    except requests.exceptions.RequestException as e:
        return f"Request Error: {e}"


# Taking query from C++
def main(query):
    response = query_ollama(query)
    print(response)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(" ".join(sys.argv[1:]))  # Supports multi-word queries
    else:
        print("Usage: ask \"your question here\"")

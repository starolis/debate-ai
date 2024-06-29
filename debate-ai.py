import os
from dotenv import load_dotenv
from anthropic import Anthropic
from openai import OpenAI

load_dotenv()

anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MAX_TOKENS = 500


class ConversationManager:
    def __init__(self, initial_topic):
        self.history = [{"role": "moderator", "content": initial_topic}]

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})

    def get_recent_history(self, n=4):
        return self.history[-n:]

    def get_last_message_content(self):
        return self.history[-1]["content"] if self.history else ""


def format_for_gpt(history, prompt):
    formatted = [
        {
            "role": "system",
            "content": (
                "You are participating in a debate. Be concise, witty, and "
                "respond to your opponent's points like an absolute savage."
            ),
        }
    ]
    for msg in history:
        if msg["role"] == "moderator":
            formatted.append({"role": "user", "content": msg["content"]})
        elif msg["role"] in ["GPT", "Claude"]:
            formatted.append({"role": "assistant", "content": msg["content"]})
    formatted.append({"role": "user", "content": prompt})
    return formatted


def format_for_claude(history, prompt):
    formatted = []
    for i, msg in enumerate(history):
        role = "user" if i % 2 == 0 else "assistant"
        formatted.append({"role": role, "content": msg["content"]})

    # If the last message is from the assistant, add the prompt as a user message
    if formatted and formatted[-1]["role"] == "assistant":
        formatted.append({"role": "user", "content": prompt})
    # If last message is from the user or empty, add an assistant message
    else:
        formatted.append(
            {"role": "assistant", "content": "I understand. Please continue."}
        )
        formatted.append({"role": "user", "content": prompt})

    return formatted


def get_gpt_response(conversation, prompt):
    try:
        messages = format_for_gpt(conversation.get_recent_history(), prompt)
        response = openai_client.chat.completions.create(
            model="gpt-4o", messages=messages, max_tokens=MAX_TOKENS
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error getting GPT response: {e}")
        return "I apologize, I'm having trouble formulating a response."


def get_claude_response(conversation, prompt):
    try:
        messages = format_for_claude(conversation.get_recent_history(), prompt)
        response = anthropic_client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=MAX_TOKENS,
            system=(
                "You are participating in a debate. Be concise, witty, and "
                "respond to your opponent's points like an absolute savage."
            ),
            messages=messages,
        )
        return response.content[0].text.strip()
    except Exception as e:
        print(f"Error getting Claude response: {e}")
        return "I apologize, I'm having trouble formulating a response."


def run_debate():
    topic = input("Enter the debate topic: ")
    conversation = ConversationManager(topic)
    speakers = ["GPT", "Claude"]

    round_number = 1
    while True:
        print(f"\nRound {round_number}")
        print(f"Moderator: {topic}")

        for i, speaker in enumerate(speakers):
            if i == 0:
                prompt = f"Respond to the moderator's topic: {topic}"
            else:
                prompt = f"Respond to your opponent's point: \
                    {conversation.get_last_message_content()}"

            if speaker == "GPT":
                response = get_gpt_response(conversation, prompt)
            else:
                response = get_claude_response(conversation, prompt)

            print(f"\n{speaker}:")
            print(response)
            conversation.add_message(speaker, response)

        moderator_input = input(
            "\nModerator (press Enter to continue, or type 'end' to finish): "
        )
        if moderator_input.lower() == "end":
            break
        elif moderator_input:
            topic = moderator_input
            conversation.add_message("moderator", moderator_input)

        round_number += 1
        speakers.reverse()


if __name__ == "__main__":
    run_debate()

import openai
import time

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",  # or use 'davinci' for GPT-3.5
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to Study Chatbot!")
    print("You can start asking questions about your studies. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Study Chatbot: Goodbye!")
            break

        # Add your custom study-related prompts here
        response = ask_gpt(user_input)

        print("Study Chatbot:", response)
        time.sleep(1)  # Optional: add a short delay to mimic natural conversation

if __name__ == "__main__":
    main()

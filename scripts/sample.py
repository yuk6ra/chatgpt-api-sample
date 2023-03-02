import os
import openai
import dotenv

dotenv.load_dotenv()

BLACK_FONT_COLOR = "\033[30m"
GREEN_FONT_COLOR = "\033[32m"

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPEN_AI_KEY")

while True:
    input_content = input(BLACK_FONT_COLOR + "You\t: ")
    
    if input_content.lower() == "end":
        break

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": input_content}]
    )

    openai_content = response['choices'][0]["message"]["content"]

    print(GREEN_FONT_COLOR + f"OpenAI\t: {openai_content.strip()}\n")
import os
import openai

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

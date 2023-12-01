import os
import asyncio
from OpenAI import AsyncOpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
  temperature=0.9,
  max_tokens=64,
  top_p=1,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)
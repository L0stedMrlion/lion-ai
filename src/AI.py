import openai

openai.api_key = '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'

prompt = "Translate the following English text to French:"

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=100
)

generated_text = response['choices'][0]['text']
print(generated_text)

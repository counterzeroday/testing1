import os
from openai import AzureOpenAI

endpoint = ""
subscription_key = ""
model_name = "gpt-4.1"
deployment = "gpt-4.1"


#subscription_key = "<your-api-key>"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

'''
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        },
'''

response = client.chat.completions.create(
    stream=True,
    messages=[
        {
            "role": "user",
            "content": "What are secure implementations on AI agent and Agentic AI?"            
        }        
    ],
    max_completion_tokens=800,
    temperature=1.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    model=deployment,
)

for update in response:
    if update.choices:
        print(update.choices[0].delta.content or "", end="")

client.close()

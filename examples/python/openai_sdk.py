# pip install openai
# One key for Claude, GPT, Grok, DeepSeek and GLM in the OpenAI Chat Completions format.
from openai import OpenAI

client = OpenAI(base_url="https://api.tkbk.online/v1", api_key="cr_your_key")
for model in ["claude-sonnet-5", "gpt-6.1-sol", "deepseek-v4-pro", "grok-4.7"]:
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Say hi in one word."}],
    )
    print(model, "->", resp.choices[0].message.content)

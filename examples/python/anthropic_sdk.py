# pip install anthropic
from anthropic import Anthropic

client = Anthropic(base_url="https://api.tkbk.online", api_key="cr_your_key")
msg = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(msg.content[0].text)

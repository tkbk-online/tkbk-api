# Anthropic Messages format
curl https://api.tkbk.online/v1/messages \
  -H "x-api-key: cr_your_key" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model": "claude-sonnet-5", "max_tokens": 256, "messages": [{"role": "user", "content": "Hello!"}]}'

# OpenAI Chat Completions format — any model of the catalog
curl https://api.tkbk.online/v1/chat/completions \
  -H "Authorization: Bearer cr_your_key" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-6.1-sol", "messages": [{"role": "user", "content": "Hello!"}]}'

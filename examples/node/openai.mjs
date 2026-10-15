// npm install openai
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.tkbk.online/v1", apiKey: process.env.TKBK_API_KEY });
const resp = await client.chat.completions.create({
  model: "claude-sonnet-5",
  messages: [{ role: "user", content: "Hello!" }],
});
console.log(resp.choices[0].message.content);

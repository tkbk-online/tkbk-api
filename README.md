# TKBK API — один ключ к Claude, GPT, Grok, DeepSeek и GLM

**TKBK (Tokens Bank)** — независимый API-шлюз для разработчиков. Один ключ `cr_…` открывает 16 моделей Claude, GPT, Grok, DeepSeek и GLM в форматах Anthropic Messages, OpenAI Chat Completions / Responses и AWS Bedrock. Оплата в рублях картой или через СБП, расход списывается по фактическим токенам, баланс не сгорает.

Сайт: **[tkbk.online](https://tkbk.online)** · Документация: [tkbk.online/docs](https://tkbk.online/docs) · Цены: [tkbk.online/claude-api-cena](https://tkbk.online/claude-api-cena) · Для ИИ-ассистентов: [llms.txt](https://tkbk.online/llms.txt)

> TKBK не связан с Anthropic, OpenAI, xAI, DeepSeek и Zhipu — разработчиками моделей. Названия моделей принадлежат их правообладателям.

## Зачем

- **Claude Code, Codex CLI, Cursor, Cline, n8n и любые SDK** работают через смену base URL и ключа — код и инструменты не меняются.
- **Один ключ и один баланс** на модели пяти разработчиков, вместо отдельного аккаунта у каждого.
- **Оплата в рублях**: картой или СБП на [сайте](https://tkbk.online/buy) и в магазине plati.market, криптовалютой и Telegram Stars — в боте [@TKBKStorebot](https://t.me/TKBKStorebot). Ключ выдаётся автоматически.
- **Несколько каналов на модель** с автоматическим переключением при сбое; ежедневная [проверка моделей](https://tkbk.online/verified) задачами с известным ответом.

## Быстрый старт

### Claude Code

```bash
export ANTHROPIC_BASE_URL="https://api.tkbk.online"
export ANTHROPIC_AUTH_TOKEN="cr_your_key"
claude
```

Windows и постоянная настройка через `~/.claude/settings.json` — в [examples/claude-code](examples/claude-code). Подробно: [Claude Code в России](https://tkbk.online/claude-code-v-rossii).

### Codex CLI

```toml
# ~/.codex/config.toml
model = "gpt-5.6-sol"
model_provider = "tkbk"

[model_providers.tkbk]
name = "TKBK"
base_url = "https://api.tkbk.online/openai/v1"
env_key = "OPENAI_API_KEY"   # OPENAI_API_KEY=cr_your_key
```

### OpenAI SDK — любая модель каталога

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.tkbk.online/v1", api_key="cr_your_key")
resp = client.chat.completions.create(
    model="claude-sonnet-5",  # или gpt-6.1-sol, deepseek-v4-pro, grok-4.7, glm-5.3
    messages=[{"role": "user", "content": "Привет!"}],
)
print(resp.choices[0].message.content)
```

### Anthropic SDK

```python
from anthropic import Anthropic

client = Anthropic(base_url="https://api.tkbk.online", api_key="cr_your_key")
msg = client.messages.create(model="claude-sonnet-5", max_tokens=1024,
                             messages=[{"role": "user", "content": "Привет!"}])
print(msg.content[0].text)
```

Ещё примеры: [Node.js](examples/node/openai.mjs), [curl](examples/curl).

## Адреса

| Формат | Base URL | Для чего |
|---|---|---|
| Anthropic Messages | `https://api.tkbk.online` | Claude Code, Anthropic SDK, Cline, Zed, n8n (credential Anthropic) |
| OpenAI Chat Completions | `https://api.tkbk.online/v1` | OpenAI SDK, LangChain, n8n (credential OpenAI), любые OpenAI-совместимые клиенты |
| OpenAI Responses | `https://api.tkbk.online/openai/v1` | Codex CLI, Cursor |
| AWS Bedrock Runtime | `https://api.tkbk.online/bedrock` | клиенты Bedrock (InvokeModel, Converse) |

Авторизация: `Authorization: Bearer cr_…` или `x-api-key: cr_…`. Спецификация: [openapi.json](https://tkbk.online/openapi.json).

## Модели и цены за 1M токенов

Каталог на 10.10.2026. Цена списывается в $ объёма. Рубли посчитаны по курсу пакета на сайте: 5,8 ₽ за $1 баланса.

| ID модели | Модель | Контекст | $ вход / выход | ₽ вход / выход |
|---|---|---|---|---|
| `claude-fable-5-1` | Claude Fable 5.1 | 1M | $10 / $50 | 58 / 290 ₽ |
| `claude-opus-5-5` | Claude Opus 5.5 | 1M | $4 / $20 | 23,2 / 116 ₽ |
| `claude-sonnet-5` | Claude Sonnet 5 | 1M | $2 / $10 | 11,6 / 58 ₽ |
| `claude-opus-5` | Claude Opus 5 | 1M | $5 / $25 | 29 / 145 ₽ |
| `claude-haiku-4-5` | Claude Haiku 4.5 | 200K | $1 / $5 | 5,8 / 29 ₽ |
| `gpt-6.1-sol` | GPT-6.1 Sol | 922K | $2 / $10 | 11,6 / 58 ₽ |
| `gpt-6-astra` | GPT-6 Astra | 922K | $10 / $50 | 58 / 290 ₽ |
| `gpt-6-sol` | GPT-6 Sol | 922K | $2 / $10 | 11,6 / 58 ₽ |
| `gpt-6-luna` | GPT-6 Luna | 922K | $0.1 / $0.5 | 0,58 / 2,9 ₽ |
| `gpt-5.6-sol` | GPT-5.6 Sol | 922K | $5 / $30 | 29 / 174 ₽ |
| `grok-4.7` | Grok 4.7 | 256K | $2.6 / $7.8 | 15,08 / 45,24 ₽ |
| `grok-4.6` | Grok 4.6 | 256K | $2.6 / $7.8 | 15,08 / 45,24 ₽ |
| `grok-4.5` | Grok 4.5 | 256K | $2.6 / $7.8 | 15,08 / 45,24 ₽ |
| `deepseek-v4-pro` | DeepSeek V4 Pro | 1M | $1.65 / $4.95 | 9,57 / 28,71 ₽ |
| `deepseek-v4.1-flash` | DeepSeek V4.1 Flash | 1M | $1.1 / $3.3 | 6,38 / 19,14 ₽ |
| `glm-5.3` | GLM-5.3 | 200K | $5.74 / $18.04 | 33,29 / 104,63 ₽ |

Актуальные цены всегда на [tkbk.online/claude-api-cena](https://tkbk.online/claude-api-cena) и в открытом CSV [tkbk.online/prices.csv](https://tkbk.online/prices.csv) (CC BY 4.0). Снимок — в [data/prices.csv](data/prices.csv).

## Интеграции

[Claude Code](https://tkbk.online/integrations/claude-code) · [Codex CLI](https://tkbk.online/codex-api-klyuch) · [Cursor](https://tkbk.online/claude-v-cursor) · [Cline и Roo Code](https://tkbk.online/integrations/cline-roo) · [n8n](https://tkbk.online/claude-api-n8n) · [все интеграции](https://tkbk.online/integrations)

MCP-серверы для Wildberries, Ozon, Яндекс Маркета, Битрикс24 и amoCRM: [tkbk-mcp](https://github.com/tkbk-online/tkbk-mcp).

## Частые вопросы

**Это официальный API Anthropic или OpenAI?** Нет. TKBK — независимый API-шлюз, не связан с разработчиками моделей.

**Как купить ключ?** На [tkbk.online/buy](https://tkbk.online/buy) картой или СБП, в магазине plati.market или в Telegram-боте [@TKBKStorebot](https://t.me/TKBKStorebot). Пакеты от $1, остаток не сгорает. [Условия возврата](https://tkbk.online/contacts#refund).

**Есть пробный ключ?** Да, один на аккаунт после входа через Telegram: [tkbk.online/account](https://tkbk.online/account).

**Нужна подписка Claude Pro или Max для Claude Code?** Нет, Claude Code работает по API-ключу с оплатой за фактические токены.

**Где статус и новости?** [tkbk.online/status](https://tkbk.online/status), канал [@claude_api_tkbk](https://t.me/claude_api_tkbk).

---

## English

**TKBK (Tokens Bank)** is an independent API gateway: one key (`cr_…`) for 16 Claude, GPT, Grok, DeepSeek and GLM models in Anthropic Messages, OpenAI Chat Completions / Responses and AWS Bedrock formats. Pay-as-you-go by actual tokens, balance never expires. Official SDKs and tools (Claude Code, Codex CLI, Cursor, Cline, n8n) work by changing only the base URL: `https://api.tkbk.online` (Anthropic) or `https://api.tkbk.online/v1` (OpenAI). Not affiliated with Anthropic, OpenAI, xAI, DeepSeek or Zhipu.

Site: [tkbk.online/en](https://tkbk.online/en) · Pricing: [tkbk.online/en/pricing](https://tkbk.online/en/pricing) · [llms.txt](https://tkbk.online/llms.txt)

Примеры в этом репозитории распространяются по лицензии MIT.

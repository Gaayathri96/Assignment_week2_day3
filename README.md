# Week 2 Day 3: LangChain + LangSmith tracing

`traced_app.py` sends 3 prompts to OpenAI through LangChain's `ChatOpenAI` (`gpt-4o-mini`) and prints each answer.
Tracing is switched on **only with environment variables**. The file has no tracing code in it.
It just calls `load_dotenv()` to read those variables from a `.env` file.

## Setup

Use Python 3.12 (`py -3.12 -m venv .venv`). Python 3.15 has no prebuilt wheels yet for `pyyaml`, `zstandard` and other dependencies. `tiktoken` is pinned to 0.12.0 because Windows Smart App Control blocks the newer DLL.

```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Turn tracing on

Create a `.env` file in the project folder. It is listed in `.gitignore`, so your keys are not committed.

```
OPENAI_API_KEY=sk-...
LANGSMITH_API_KEY=lsv2_...
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=caie-week2
# Only if your LangSmith account is in the EU region:
# LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com
```

Runs land in the project named by `LANGSMITH_PROJECT`, not in `default`.

## Run

```powershell
.venv\Scripts\activate
python traced_app.py | Tee-Object -FilePath output.txt
```

To see that the code doesn't change, set `LANGSMITH_TRACING=false` in `.env` and run it again.
The answers still print, but no new runs appear in LangSmith.

## Find the runs in LangSmith

1. Open https://smith.langchain.com, then **Tracing Projects**, then **caie-week2**.
2. You should see 3 root runs named `ChatOpenAI`, one per prompt.
3. Click one run. From there, write down the prompt sent, the response, the latency and the token counts.

## Results (run on 2026-11-17, earlier version of the app)

These results come from an earlier version of `traced_app.py`. That version used a prompt template with a system message (`prompt | llm | StrOutputParser()`) and logged to the project `week2-day3-traced-app`.
So its root runs are named `RunnableSequence`, and the prompt sent includes a system message. The current version sends each prompt directly, with no system message.

The project `week2-day3-traced-app` has 3 successful `RunnableSequence` root runs, one per prompt.
It also has 1 earlier `error` run, from a first attempt with an invalid OpenAI key.
The full console output is in [`output.txt`](output.txt).

Details of one run: the `ChatOpenAI` child run for prompt 3, model `gpt-4o-mini`, run ID `01a1eb02-f63f-70b5-8a2d-7c3a5c634a7a`.

| Field | Value |
|---|---|
| Exact prompt sent | **system:** `You are a concise, helpful assistant.`<br>**human:** `Write a haiku about debugging code late at night.` |
| Response | Flickering screen glows, / Silent whispers of the bugs, / Night's code dance unfolds. |
| Latency | 0.94 s |
| Token counts | 30 prompt + 21 completion = **51 total** |

A screenshot of the current code and its terminal output is in [`Code_run_output.png`](Code_run_output.png).

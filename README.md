# Week 2 Day 3: LangChain + LangSmith tracing

`traced_app.py` sends 3 prompts to OpenAI through LangChain's `ChatOpenAI` and prints each answer.
Tracing is switched on **only with environment variables**. The file has no tracing code in it.

## Setup

Use Python 3.11–3.13. Python 3.15 has no prebuilt wheels yet for `pyyaml`, `zstandard` and other dependencies.

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Turn tracing on (PowerShell, current session only)

```powershell
$env:OPENAI_API_KEY    = "sk-..."
$env:LANGSMITH_API_KEY = "lsv2_..."
$env:LANGSMITH_TRACING = "true"
$env:LANGSMITH_PROJECT = "week2-day3-traced-app"   # runs land here, not in "default"
# Only if your LangSmith account is in the EU region:
# $env:LANGSMITH_ENDPOINT = "https://eu.api.smith.langchain.com"
```

## Run

```powershell
python traced_app.py | Tee-Object -FilePath output.txt
```

To see that the code doesn't change, set `$env:LANGSMITH_TRACING = "false"` and run it again.
The answers still print, but no new runs appear in LangSmith.

## Find the runs in LangSmith

1. Open https://smith.langchain.com, then **Tracing Projects**, then **week2-day3-traced-app**.
2. You should see 3 root runs named `RunnableSequence`, one per prompt.
3. Click one run and open its `ChatOpenAI` child run. From there, write down:

| Field | Value |
|---|---|
| Exact prompt sent (system + human messages) | _fill in_ |
| Response | _fill in_ |
| Latency | _fill in_ |
| Token counts (prompt / completion / total) | _fill in_ |

Screenshots go in `screenshots/`.

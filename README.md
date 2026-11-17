# Week 2 Day 3: LangChain + LangSmith tracing

`traced_app.py` sends 3 prompts to OpenAI through LangChain's `ChatOpenAI` and prints each answer.
Tracing is switched on **only with environment variables**. The file has no tracing code in it.

## Setup

Use Python 3.12 (`py -3.12 -m venv .venv`). Python 3.15 has no prebuilt wheels yet for `pyyaml`, `zstandard` and other dependencies. `tiktoken` is pinned to 0.12.0 because Windows Smart App Control blocks the newer DLL.

```powershell
py -3.12 -m venv .venv
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

## Results (run on 2026-11-17)

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

Screenshots go in `screenshots/`.

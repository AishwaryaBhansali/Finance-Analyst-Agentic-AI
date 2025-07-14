# Finance Agentic AI

Finance Agentic AI is a multi-agent system that performs financial analysis and real-time web research using LLMs hosted on Groq. It is built using the `phi` framework, allowing autonomous agents to collaborate on tasks such as analyzing stock data and retrieving live news.

---

## Features

- Multi-agent architecture: Finance Agent + Web Search Agent
- Uses Groq-hosted LLaMA 3 models (8B or 70B)
- Financial data via YFinance: stock prices, company info, analyst recommendations
- Live web search using DuckDuckGo (via the `ddgs` package)
- Task delegation and reasoning between agents
- Structured output in markdown with tables and sources

---

## Example Query
"Summarize analyst recommendations and share the latest news for NVDA"


This triggers:
1. Financial analysis by the Finance Agent using YFinance
2. Web news search by the Web Search Agent
3. Combined, formatted response from the multi-agent system

---

## Getting Started

1. Clone the Repository
```bash
git clone https://github.com/yourusername/finance-agentic-ai.git
cd finance-agentic-ai

2. Create and Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Set Up Environment Variables
PHI_API_KEY=""
GROQ_API_KEY=""

Step 5: Run the Agent
python finance_agent.py

Step 6: To see the app view of the agent run - 
python playground.py

Project Structure - 
finance-agentic-ai/
├── finance_agent.py         # Main multi-agent script
├── playground.py            # App View of multi-agent script
├── requirements.txt         # Dependencies
├── .env.example             # Sample env file
├── README.md                # Documentation




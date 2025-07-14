from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools  # Finance data
from phi.tools.duckduckgo import DuckDuckGo  # Web search using ddgs
import openai
import os

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# ✅ Make sure you're using Groq's compatible model
model = Groq(id="llama3-70b-8192")  # more stable than meta-llama scout

# 🔍 Web Search Agent using updated ddgs backend (automatically used inside DuckDuckGo tool)
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search web for information",
    model=model,
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

# 📈 Finance Agent using yfinance
finance_agent = Agent(
    name="Finance Agent",
    role="Perform financial analysis",
    model=model,
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_info=True
        )
    ],
    instructions=["Use tables to show data"],
    show_tool_calls=True,
    markdown=True
)

# 🤝 Multi-modal Agent combining both sub-agents
multi_modal_agents = Agent(
    team=[web_search_agent, finance_agent],
    model=model,
    instructions=[
        "Always include sources",
        "Use tables to show data"
    ],
    show_tool_calls=True,
    markdown=True
)

# 🧠 Query Example
multi_modal_agents.print_response(
    "Summarize analyst recommendation and share the latest news for NVDA",
    stream=True
)

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools  # Finance data
from phi.tools.duckduckgo import DuckDuckGo  # Web search using ddgs
import openai
import os
from dotenv import load_dotenv
import phi 
from phi.playground import Playground, serve_playground_app 

load_dotenv()
phi.api = os.getenv("GROQ_API_KEY")

model = Groq(id="llama3-70b-8192")  # more stable than meta-llama scout

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


app = Playground(agents=[web_search_agent, finance_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
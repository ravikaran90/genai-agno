from agno.agent import agent
from agno.models.google import Gemini
from agno.models.openai import OpenAIChat
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

from dotenv import load_dotenv

load_dotenv()

agent=Agent(
  model=Gemini(id="gemini-2.0-flash")
  # model=OpenAIChat(id="gpt-4o")
  tools=[
    ReasoningTools(add_instructions=True)
    YFinanceTools(stock_price=True,analyst_recommendations=True,company_info=True,company_news=True)
  ],
  instructions=[
    "Use Tables to Display Data",
    "Only Output the report, not other text"
  ],
 markdown=True
)
agent.print.response(message:"Write a report on CISCO",stream=True,show_full_reasoning=True)

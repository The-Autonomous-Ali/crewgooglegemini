from crewai import Agent
import os
from tools import tool
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
# Call the gemini models

llm= ChatGoogleGenerativeAI(model='gemini-1.5-flash',
                            verbose=True,
                            temperature= 0.5,
                            google_api_key=os.getenv('GOOGLE_API_KEY'))


# Creating a senior research agent with the memory and verbose mode


news_researcher = Agent(
            role= "Senior Researchger",
            goal= "Uncover ground breaking technologies in {topic}",
            verbose = True,
            memory = True,
            backstory =(
                "Drive by curiosity, you're at the forefronts of"
                "innovative eager to explore and share knowledge that could change"
                "the world."
            ),
            tools=[tool],
            llm=llm,
            allow_delegation=True

)



# Creating a write ageny with custom tools responsible in writting news blogs
news_writer = Agent(
            role= "Writer",
            goal= "Narrate compelling tech stories about {topic}",
            verbose = True,
            memory = True,
            backstory =(
                "With a flair for simplifying complex topics, you craft"
                "engaging narraitve that captivates and educate, bring new"
                "discovies to light in an accessible manner"
            ),
            tools=[tool],
            llm=llm,
            allow_delegation=False

)




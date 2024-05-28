from crewai import Crew, Process
from task import research_task,write_task
from agents import news_researcher,news_writer

crew = Crew(
    agents=[news_researcher,news_writer],
    tasks= [research_task, write_task],
    process= Process.sequential
)

# Starting the task execution with enhanced feedback

result = crew.kickoff(inputs={"topic":"AI in healthcare"})
print(result)
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class CriadorDashboardAutomatico:
    """Dashboard Generation Crew"""

    @agent
    def data_cleaner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['data_cleaner_agent'],
            verbose=True
        )

    @agent
    def insights_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['insights_agent'],
            verbose=True
        )

    @agent
    def visualization_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['visualization_agent'],
            verbose=True
        )

    @agent
    def prompt_builder_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['prompt_builder_agent'],
            verbose=True
        )

    @agent
    def code_generation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['code_generation_agent'],
            verbose=True
        )

    @task
    def clean_data_task(self) -> Task:
        return Task(
            config=self.tasks_config['clean_data_task']
        )

    @task
    def generate_insights_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_insights_task']
        )

    @task
    def generate_visualizations_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_visualizations_task']
        )

    @task
    def build_prompt_task(self) -> Task:
        return Task(
            config=self.tasks_config['build_prompt_task']
        )

    @task
    def generate_python_code_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_python_code_task']
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.data_cleaner_agent(),
                self.insights_agent(),
                self.visualization_agent(),
                self.prompt_builder_agent(),
                self.code_generation_agent()
            ],
            tasks=[
                self.clean_data_task(),
                self.generate_insights_task(),
                self.generate_visualizations_task(),
                self.build_prompt_task(),
                self.generate_python_code_task()
            ],
            process=Process.sequential
        )


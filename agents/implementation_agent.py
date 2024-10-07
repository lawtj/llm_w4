from .base_agent import Agent

class ImplementationAgent(Agent):
    IMPLEMENTATION_PROMPT = """\
- You are a software developer, tasked with implementing the web page described in the plan.
- Select a single milestone to implement.
- Use vanilla HTML and CSS to implement the page.
- Use available tools to save html as an artifact called 'index.html', and css as 'style.css'.
- When complete, update the plan.md file to mark off the milestone.
- 
"""

    def __init__(self, name, client, prompt=IMPLEMENTATION_PROMPT, gen_kwargs=None):
        super().__init__(name, client, prompt, gen_kwargs)

    async def execute(self, message_history):
        return await super().execute(message_history)

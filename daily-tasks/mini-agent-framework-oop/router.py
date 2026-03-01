class Router:
    def __init__(self, agents):
        self.agents = {agent.name: agent for agent in agents}
    
    def show_agent(self):
        return list(self.agent.key())

    def execute(self, agent_name, data):
        agent_name = agent_name.lower()

        if agent_name not in self.agents:
            raise ValueError(
                f"Agent not found. Available: {list(self.agents.keys())}"
            )

        return self.agents[agent_name].run(data)
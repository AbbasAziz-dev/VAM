from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self, name):
        self.name = name.lower()

    @abstractmethod
    def run(self, data):
        pass


class CalcAgent(Agent):
    def run(self, data):
        try:
            return eval(data)
        except:
            return "Please enter a valid math expression"


class ProfessorAgent(Agent):
    def run(self, topic):
        topics = {
            "list": "A list stores multiple items in one variable.",
            "tuple": "A tuple is immutable.",
            "dictionary": "Stores key-value pairs."
        }
        return topics.get(topic, "Topic not found")
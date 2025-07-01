from langchain.schema import LLMResult
from langchain.llms import OpenAI

class NLPModule:
    def __init__(self):
        self.llm = OpenAI()

    def process_input(self, user_input):
        try:
            response = self.llm(user_input)
            return response
        except Exception as e:
            return f"Error processing input: {str(e)}"
from langchain.schema import LLMResult
from langchain.llms import OpenAI

class GenerativeModel:
    def __init__(self):
        self.llm = OpenAI()

    def generate_lesson_plan(self, topic, level):
        try:
            prompt = f"Create a lesson plan on {topic} for {level} level"
            response = self.llm(prompt)
            return response
        except Exception as e:
            return f"Error generating lesson plan: {str(e)}"

    def generate_exercise(self, topic, level):
        try:
            prompt = f"Create practice exercises on {topic} for {level} level"
            response = self.llm(prompt)
            return response
        except Exception as e:
            return f"Error generating exercise: {str(e)}"

    def generate_assessment(self, topic, level):
        try:
            prompt = f"Create an assessment on {topic} for {level} level"
            response = self.llm(prompt)
            return response
        except Exception as e:
            return f"Error generating assessment: {str(e)}"
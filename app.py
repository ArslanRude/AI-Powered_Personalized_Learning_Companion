from nlp_module import NLPModule
from generative_model import GenerativeModel
from memory_module import MemoryModule
import json

def main():
    try:
        # Initialize modules
        nlp = NLPModule()
        generator = GenerativeModel()
        memory = MemoryModule()

        # Load configuration
        with open('config.json', 'r') as f:
            config = json.load(f)

        # Start the application
        print("AI-Powered Personalized Learning Companion Started")
        while True:
            user_input = input("Enter your command: ")
            response = nlp.process_input(user_input)
            print(response)
    except Exception as e:
        print(f"Error: {str(e)}")
        return

if __name__ == '__main__':
    main()
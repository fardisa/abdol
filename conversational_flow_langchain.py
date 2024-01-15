```python
import os
from langchain import Langchain

class ConversationalFlowManager:
    def __init__(self):
        self.langchain_api_key = os.getenv('LANGCHAIN_API_KEY')
        self.langchain = Langchain(self.langchain_api_key)

    def handle_conversation(self, user_input):
        response = self.langchain.process_input(user_input)
        return response

    def manage_flow(self, user_input):
        response = self.handle_conversation(user_input)
        return response

if __name__ == "__main__":
    manager = ConversationalFlowManager()
    while True:
        user_input = input("User: ")
        response = manager.manage_flow(user_input)
        print("Bot: ", response)
```
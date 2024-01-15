```python
import os
from mistral_api import MistralAPI

class ChatbotMistralAI:
    def __init__(self):
        self.mistral_api_key = os.getenv('MISTRAL_API_KEY')
        self.mistral = MistralAPI(self.mistral_api_key)

    def process_message(self, message):
        response = self.mistral.process_message(message)
        return response

    def handle_conversation(self, conversation_id, message):
        response = self.mistral.handle_conversation(conversation_id, message)
        return response

    def end_conversation(self, conversation_id):
        self.mistral.end_conversation(conversation_id)

if __name__ == "__main__":
    chatbot = ChatbotMistralAI()
    message = "Hello, I need a service"
    response = chatbot.process_message(message)
    print(response)
```
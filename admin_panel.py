```python
import os
from dotenv import load_dotenv
from user_management import UserManager
from financial_management import FinancialManager
from integration_settings import IntegrationManager
from api_key_management import APIKeyManager
from secret_management import SecretManager

load_dotenv()

class AdminPanel:
    def __init__(self):
        self.user_manager = UserManager()
        self.financial_manager = FinancialManager()
        self.integration_manager = IntegrationManager()
        self.api_key_manager = APIKeyManager()
        self.secret_manager = SecretManager()

    def manage_users(self):
        print("Managing Users...")
        self.user_manager.manage_users()

    def manage_finances(self):
        print("Managing Finances...")
        self.financial_manager.manage_finances()

    def manage_integrations(self):
        print("Managing Integrations...")
        self.integration_manager.manage_integrations()

    def manage_api_keys(self):
        print("Managing API Keys...")
        self.api_key_manager.manage_api_keys()

    def manage_secrets(self):
        print("Managing Secrets...")
        self.secret_manager.manage_secrets()

if __name__ == "__main__":
    admin_panel = AdminPanel()
    admin_panel.manage_users()
    admin_panel.manage_finances()
    admin_panel.manage_integrations()
    admin_panel.manage_api_keys()
    admin_panel.manage_secrets()
```
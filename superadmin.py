```python
import os
from dotenv import load_dotenv
from admin_panel import AdminPanel

load_dotenv()

class SuperAdmin(AdminPanel):
    def __init__(self):
        super().__init__()
        self.superadmin_username = os.getenv("SUPERADMIN_USERNAME")
        self.superadmin_password = os.getenv("SUPERADMIN_PASSWORD")

    def create_superadmin(self):
        self.create_user(self.superadmin_username, self.superadmin_password, "superadmin")

    def manage_users(self, action, user_id=None, user_data=None):
        if action == "view":
            return self.view_users()
        elif action == "add":
            return self.add_user(user_data)
        elif action == "update":
            return self.update_user(user_id, user_data)
        elif action == "delete":
            return self.delete_user(user_id)

    def manage_finances(self, action, transaction_id=None, transaction_data=None):
        if action == "view":
            return self.view_transactions()
        elif action == "add":
            return self.add_transaction(transaction_data)
        elif action == "update":
            return self.update_transaction(transaction_id, transaction_data)
        elif action == "delete":
            return self.delete_transaction(transaction_id)

    def manage_integrations(self, action, integration_id=None, integration_data=None):
        if action == "view":
            return self.view_integrations()
        elif action == "add":
            return self.add_integration(integration_data)
        elif action == "update":
            return self.update_integration(integration_id, integration_data)
        elif action == "delete":
            return self.delete_integration(integration_id)

    def manage_api_keys(self, action, api_key_id=None, api_key_data=None):
        if action == "view":
            return self.view_api_keys()
        elif action == "add":
            return self.add_api_key(api_key_data)
        elif action == "update":
            return self.update_api_key(api_key_id, api_key_data)
        elif action == "delete":
            return self.delete_api_key(api_key_id)

    def manage_secrets(self, action, secret_id=None, secret_data=None):
        if action == "view":
            return self.view_secrets()
        elif action == "add":
            return self.add_secret(secret_data)
        elif action == "update":
            return self.update_secret(secret_id, secret_data)
        elif action == "delete":
            return self.delete_secret(secret_id)

if __name__ == "__main__":
    superadmin = SuperAdmin()
    superadmin.create_superadmin()
```
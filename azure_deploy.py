```python
import os
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient
from azure.common.credentials import ServicePrincipalCredentials

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Get environment variables
subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
tenant_id = os.getenv('AZURE_TENANT_ID')
client_id = os.getenv('AZURE_CLIENT_ID')
client_secret = os.getenv('AZURE_CLIENT_SECRET')
resource_group_name = os.getenv('AZURE_RESOURCE_GROUP_NAME')
app_service_plan_name = os.getenv('AZURE_APP_SERVICE_PLAN_NAME')
app_name = os.getenv('AZURE_APP_NAME')

# Create Azure credentials
credentials = ServicePrincipalCredentials(
    client_id=client_id,
    secret=client_secret,
    tenant=tenant_id
)

# Create Azure clients
resource_client = ResourceManagementClient(credentials, subscription_id)
web_client = WebSiteManagementClient(credentials, subscription_id)

# Create resource group
resource_client.resource_groups.create_or_update(resource_group_name, {'location': 'westus'})

# Create App Service plan
web_client.app_service_plans.create_or_update(
    resource_group_name,
    app_service_plan_name,
    {
        'location': 'westus',
        'sku': {
            'name': 'S1',
            'capacity': 1
        }
    }
)

# Create web app
web_client.web_apps.create_or_update(
    resource_group_name,
    app_name,
    {
        'location': 'westus',
        'server_farm_id': app_service_plan_name
    }
)

# Deploy code to web app
web_client.web_apps.create_or_update_source_control(
    resource_group_name,
    app_name,
    {
        'location': 'GitHub',
        'repo_url': 'https://github.com/yourusername/yourrepo',
        'branch': 'master',
        'is_manual_integration': True
    }
)
```
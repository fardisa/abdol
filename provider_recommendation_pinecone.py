```python
import os
import pinecone

# Load Pinecone API key from environment variables
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# Initialize Pinecone
pinecone.init(api_key=pinecone_api_key)

# Define the Pinecone index name
index_name = "service_providers"

# Create the Pinecone index if it doesn't exist
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name=index_name, metric="cosine", shards=1)

# Get a Pinecone index instance
index = pinecone.Index(index_name=index_name)

def add_provider_to_index(provider_id, provider_vector):
    """
    Add a service provider to the Pinecone index.
    """
    index.upsert(items={provider_id: provider_vector})

def remove_provider_from_index(provider_id):
    """
    Remove a service provider from the Pinecone index.
    """
    index.delete(ids=[provider_id])

def recommend_providers(user_vector, top_k=5):
    """
    Recommend service providers to a user based on their vector.
    """
    results = index.query(queries=[user_vector], top_k=top_k)
    return results.ids[0]

# Remember to deinitialize Pinecone when done
pinecone.deinit()
```
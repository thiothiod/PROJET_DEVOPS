from datetime import datetime
from elasticsearch import Elasticsearch, helpers

client = Elasticsearch(
    "https://searche-thioro-f3acc8.es.us-east-1.aws.elastic.cloud:443",
    api_key="VWhJQ1A1MEJZRm8ySVhvWE1iOEc6U0hHekRGcHN5TVVSQjRYSkoyU1o4dw=="
)

index_name = "national-parks"

docs = [
    {
        "@timestamp": datetime.utcnow().isoformat(),
        "level": "INFO",
        "service": "backend",
        "message": "Server started successfully"
    },
    {
        "@timestamp": datetime.utcnow().isoformat(),
        "level": "ERROR",
        "service": "backend",
        "message": "Database connection failed"
    },
]

actions = [{"_index": index_name, "_source": doc} for doc in docs]

helpers.bulk(client, actions, refresh="wait_for")
print("Documents reingested with created_at")
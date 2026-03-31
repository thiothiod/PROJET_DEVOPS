from datetime import datetime
from elasticsearch import Elasticsearch, helpers

client = Elasticsearch(
    "https://searche-thioro-f3acc8.es.us-east-1.aws.elastic.cloud:443",
    api_key="VWhJQ1A1MEJZRm8ySVhvWE1iOEc6U0hHekRGcHN5TVVSQjRYSkoyU1o4dw=="
)

index_name = "project-logs"

logs = [
    {"@timestamp": datetime.utcnow().isoformat(), "level": "INFO", "service": "backend", "message": "Server started"},
    {"@timestamp": datetime.utcnow().isoformat(), "level": "ERROR", "service": "backend", "message": "Database connection failed"},
    {"@timestamp": datetime.utcnow().isoformat(), "level": "WARN", "service": "frontend", "message": "Deprecated API call"},
]

actions = [{"_index": index_name, "_source": log} for log in logs]

helpers.bulk(client, actions, refresh="wait_for")
print("Logs ingérés avec @timestamp")
"""THIS IS FOR USING JUST THE REST API WITH REQUEST"""

import requests
from pprint import pprint
import os

API_URL = os.getenv('API_URL')
assert API_URL
API_KEY = os.getenv('API_KEY')
assert API_KEY

headers = {
    "x-api-key": API_KEY
}

# Create an index
INDEXES_URL = f"{API_URL}/indexes"
INDEX_NAME = "<MYINDEXNAME>" # Use a descriptive name for your index 
data = {
    "engine_id": "marengo",
    "index_options": ["visual", "conversation", "text_in_video"],
    "index_name": INDEX_NAME,
}
response = requests.post(INDEXES_URL, headers=headers, json=data)
INDEX_ID = response.json().get('_id')
print (f'Status code: {response.status_code}')
pprint (response.json())


# Upload a video
INDEX_TASK_URL = f"{API_URL}/indexes/tasks"
file_name = "<YOUR_FILE_NAME>" # Example: "test.mp4"
file_path = "<YOUR_FILE_PATH>" # Example: "/Downloads/test.mp4"
file_stream = open(file_path,'rb')
data = {
    "index_id": INDEX_ID, 
    "language": "en"
}
file_param=[('video_file', (file_name, file_stream, 'application/octet-stream'))]
response = requests.post(INDEX_TASK_URL, headers=headers, data=data, files=file_param)
TASK_ID = response.json().get('_id')
pprint (response.status_code)
pprint (response.json())


# Make a search request
SEARCH_URL = f"{API_URL}/search"
data = {
    "query": "car accidents", #search prompt
    "index_id": INDEX_ID,
    "search_options": ["visual"],
}
response = requests.post(SEARCH_URL, headers=headers, json=data)
pprint (response.status_code)
pprint (response.json())
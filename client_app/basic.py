import requests

endpoint = "http://localhost:8000/"
response = requests.get(endpoint, params={"name": "Hyacinth"}, json={"MATRI":"UBA19E0181"})   
# print(response.text)
# print(response.status_code)
print(response.json())
print(response.status_code)



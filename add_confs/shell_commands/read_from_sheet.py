import requests

url = "https://sheets.googleapis.com/v4/spreadsheets/12Lfm2VDyvlTfhiUtid23M4haJuQLMF-NMN9_vGAdx5o/values/B1"

querystring = {"key":"AIzaSyAfUwTtd6qYvMUXn2P7hnJ3e5T7xisogZY"}

response = requests.request("GET", url, params=querystring)

print(response.text)

json_data = response.json()
value = json_data["values"][0][0]

print(value)



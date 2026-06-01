import requests

# url = "http://localhost:8080/2015-03-31/functions/function/invocations"

url = "https://q2pqkne3aqfmdfau42dlljrs7q0hisgz.lambda-url.us-east-1.on.aws/"

data = {
    "name": "John"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Body:", response.json())

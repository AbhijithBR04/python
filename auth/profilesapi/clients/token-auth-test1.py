import requests

def client():

    token_h = "6fd304bd55cd9616756e0c3945e3f591aa7568a1"
    headers = {"Authorization":  token_h}

    # credentials = {"username": "admin", "password": "123"}
    # response = requests.post("http://localhost:8000/api/rest-auth/login/", data=credentials)

    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)

    print("status: " , response.status_code)
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()
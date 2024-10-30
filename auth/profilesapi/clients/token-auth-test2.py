import requests

def client():

    # token_h = "Token 640c2db3fafd2ad1f2e5c5e4ececb256c7fcdcef"
    # headers = {"Authorization": token_h}

    # response = requests.get("http://127.0.0.1:8000/api/profiles/",
                            # headers=headers)
    data = {
        "username": "resttest", 
        "email": "test@rest.com",
        "password1": "changeme123",
        "password2": "changeme123"
    }

    # Corrected registration endpoint
    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)

    print("Status Code: ", response.status_code)

    # Check for success and retrieve the token
    if response.status_code == 201:  # 201 Created indicates success in user registration
        try:
            response_data = response.json()
            token = response_data.get('key')  # Assuming the token is returned under 'key'
            print("Registration successful! Token:", token)
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON. Raw response content:")
            print(response.text)
    else:
        print("Registration failed.")
        try:
            response_data = response.json()
            print("Error details:", response_data)
        except requests.exceptions.JSONDecodeError:
            print("Failed to decode JSON. Raw response content:")
            print(response.text)

if __name__ == "__main__":
    client()
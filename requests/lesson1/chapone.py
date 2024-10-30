import requests

def main():
    response = requests.get("http://www.google.com")
    # response = requests.get("http://www.google.com/afafawffafw")
    print("HTTP Status Code: " ,response.status_code)
    # print("Headers: " ,response.headers)
    print("Content-Length: " ,response.headers['Content-Length'])

if __name__ == '__main__':
    main()
    

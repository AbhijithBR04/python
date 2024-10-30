import requests

def main():
    response = requests.get("https://dog.ceo/api/breeds/list?corgi")

    if response.status_code != 200 :
        print("Error fetching data:", response.status_code)
        raise Exception("Error fetching data:", response.status_code)

    data = response.json()
    print("data",data)
    print("HTTP Status Code: " ,response.status_code)


if __name__ == '__main__':
    main()
    

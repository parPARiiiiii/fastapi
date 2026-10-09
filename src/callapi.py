import requests

def get_ALL_items():
    url = 'http://127.0.0.1:8000/getItem/'

    response = requests.get(url)
    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()
        return response
    
#########################################
if __name__ == "__main__":
    result = get_ALL_items()
    print('result', result)
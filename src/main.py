# - coding: utf-8 -
import time
import os
import json
import requests
import math


class MusicSpy:
    url = 'https://music.2333.me/'
    headers = {'referer': 'https://music.2333.me/',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36',
               'x-requested-with': 'XMLHttpRequest'}
    services = ['netease', 'qq', 'kugou', 'kuwo', 'xiami', 'baidu', '1ting', 'migu', 'lizhi', 'qingting', 'ximalaya',
                'kg', '5singyc', '5singfc', 'soundcloud']

    @classmethod
    def __init__(cls, names, pic=False, lrc=False):
        ###
        cls.names = names
        cls.pic = pic
        cls.lrc = lrc
        cls.page = 1
        cls.service = cls.services[0]

    @classmethod
    def run(cls):
        if cls.names is None or not type(cls.names) is list:
            raise Exception('Names array is needed!')

        print('CG Music Crawler')
        print('1. Normal Mode()')
        print('2. Fast Mode(without annoying choices, straight download)')
        mode = input('input index to choose mode: ')
        while True:
            if mode is '1':
                for name in cls.names:
                    cls.search(name)
                break
            elif mode is '2':
                index = 0
                for service in cls.services:
                    print(str(index) + '. ' + service)
                    index += 1
                while True:
                    choose = int(input('input index to choose service: '))
                    if choose != 1 and choose != 2:
                        continue
                    else:
                        break

                start_time = time.time()
                service = cls.services[choose]
                for name in cls.names:
                    cls.fastmode(name, service)
                end_time = time.time()
                print('All download completed, total time: ' + str(math.floor(end_time - start_time)) + 's')
                break
            else:
                continue

    @classmethod
    def search(cls, name):
        cls.page = 1

        #### choose service part ######
        while True:
            print('-----------------------------------------')
            idx = 0
            for service in cls.services:
                print(str(idx) + '. ' + service)
                idx += 1
            try:
                service = int(input('Input index to choose service: '))
            except:
                continue
            if service >= len(cls.services) or service < 0:
                continue
            else:
                service = cls.services[service]
                break
        #### choose service part ######
        while True:
            print('-------------------------------------------')
            print('Searching at service: ' + service)
            datas = cls.crawling(name, service)
            print('Fetched contents: ')
            index = 0
            print(str(index) + '. ' + 'Pre page')
            for data in datas['data']:
                index += 1
                print(str(index) + '. ' + data['author'] + ' - ' + data['title'])
            index += 1
            nextpage = index
            print(str(index) + '. ' + 'Next page')
            index += 1
            try:
                choose = int(input('Input index to choose cmd: '))
            except:
                continue
            if choose < 0 or choose > nextpage:
                continue
            elif choose == 0:
                if cls.page > 1:
                    cls.page -= 1
                else:
                    continue
            elif choose == nextpage:
                cls.page += 1
                continue
            else:
                cls.download(datas['data'][choose-1])
                while True:
                    ch = input('1 for continue download, 2 for next song')
                    if ch is '1' or ch is '2':
                        break
                    else:
                        continue
                if ch is '1':
                    continue
                elif ch is '2':
                    break





    @classmethod
    def crawling(cls, name, service):
        res = requests.post(cls.url, data={'input': name, 'filter': 'name', 'type': service, 'page': cls.page},
                            headers=cls.headers)
        ret = json.loads(res.text)
        if ret['code'] is not 200:
            raise Exception('Crawling failed at name' + name + ';service: ' + service + ';err: ' + ret['error'])
        return ret

    @classmethod
    def fastmode(cls, name, service):
        datas = cls.crawling(name, service)
        cls.download(datas['data'][0])

    @classmethod
    def download(cls, data):
        fullpath = './Music/' + data['author'] + ' - ' + data['title'] + '.' + data['url'].split('.')[-1].split('?')[0]
        if not os.path.exists('./Music'):
            os.mkdir('./Music')
        if os.path.exists(fullpath):
            return
        response = requests.get(data['url'])
        with open(fullpath,
                  'wb') as f:
            f.write(response.content)


def main():
    ms = MusicSpy(['ho ho ho', 'hello'])

    ms.run()


if __name__ == '__main__':
    main()

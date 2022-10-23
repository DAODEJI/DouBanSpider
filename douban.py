# coding=utf-8
import requests
from lxml import etree


def url_generator():
    url = []
    for i in range(10):
        if i == 0:
            url.append('https://movie.douban.com/top250')
        else:
            url.append('https://movie.douban.com/top250?start={}&filter='.format(25 * i))
    return url


def main(url, headers):
    response = requests.get(url, headers=headers).text
    xp = etree.HTML(response)
    f = open("data.txt", "a", encoding="utf-8")
    for i in range(1, 26):
        test = []
        symbol = ','
        move_name = 'normalize-space(//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[1])'.format(i)
        style = 'normalize-space(//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/p[1]/text()[2])'.format(i)
        Director_starring = 'normalize-space(//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/p[1]/text()[1])'.format(i)
        score = 'normalize-space(//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/div/span[2]//text())'.format(i)
        result1 = xp.xpath(move_name)
        test.append(str(result1))
        result3 = xp.xpath(style)
        test.append(str(result3))
        result4 = xp.xpath(Director_starring)
        test.append(str(result4))
        result5 = xp.xpath(score)
        test.append(str(result5))
        f.write(symbol.join(test) + '\n')
    f.close()



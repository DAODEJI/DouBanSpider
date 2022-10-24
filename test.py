import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
re = requests.get('https://movie.douban.com/top250',headers=headers).text


xp = etree.HTML(re)
test2 = []
f = open("data.txt", "w", encoding="utf-8")
for i in range(1, 26):
    test = []
    symbol = ','
    move_name = 'normalize-space(//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[1]/a/span[1])'.format(i)
    style = 'normalize-space(//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/p[1]/text()[2])'.format(i)
    Director_starring = 'normalize-space(//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/p[1]/text()[1])'.format(i)
    score = 'normalize-space(//*[@id="content"]/div/div[1]/ol/li[{}]/div/div[2]/div[2]/div/span[2]//text())'.format(i)
    result1 = xp.xpath(move_name)
    a = str(result1)
    test.append(str(result1))
    result3 = xp.xpath(style)
    test.append(str(result3))
    result4 = xp.xpath(Director_starring)
    test.append(str(result4))
    result5 = xp.xpath(score)
    test.append(str(result5))
    test2.append(test)
    print(symbol.join(test2))
    f.write(symbol.join(test) + '\n')
f.close()

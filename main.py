from douban import url_generator
from douban import main
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (HTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
url = url_generator()
for i in url:
    time.sleep(0.5)
    main(url=i, headers=headers)


from douban import url_generator
from douban import main
import time

headers = {
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'

}
url = url_generator()
for i in url:
    time.sleep(0.5)
    main(url=i, headers=headers)

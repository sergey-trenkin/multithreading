import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

urls = [
  'http://www.python.org',
  'https://docs.python.org/3/',
  'https://docs.python.org/3/whatsnew/3.7.html',
  'https://docs.python.org/3/tutorial/index.html',
  'https://docs.python.org/3/library/index.html',
  'https://docs.python.org/3/reference/index.html',
  'https://docs.python.org/3/using/index.html',
  'https://docs.python.org/3/howto/index.html',
  'https://docs.python.org/3/installing/index.html',
  'https://docs.python.org/3/distributing/index.html',
  'https://docs.python.org/3/extending/index.html',
  'https://docs.python.org/3/c-api/index.html',
  'https://docs.python.org/3/faq/index.html',
  'https://sokolov.ru/jewelry-catalog/rings/signet_rings/'
]

start = time.time()
# with ThreadPoolExecutor(7) as executor:
#   for i in range(2):
#     executor.map(print, urls)
for i in range(14):
  print(urls[i])

end = time.time()
print(end - start)



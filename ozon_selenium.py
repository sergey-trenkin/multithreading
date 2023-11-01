import threading 
from selenium import webdriver 
from bs4 import BeautifulSoup as bs
import time  
  
class ScrapeThread(threading.Thread): 
    def __init__(self, url): 
        threading.Thread.__init__(self) 
        self.url = url 
  
    def run(self): 
        driver = webdriver.Chrome() 
        driver.get(self.url) 
        time.sleep(3)
        page_source = driver.page_source 
        driver.close() 
        # do something with the page source 
        soup = bs(page_source, 'html.parser')
        h1 = soup.find('h1', class_='m4l').text 
        print(h1)
        
  
urls = [ 
    'https://www.ozon.ru/product/zoloto-diskont-koltso-s-brilliantami-iz-zolota-585-proby-866806290/?asb=BziiWD35qjgkQXlqXlMRU5HlXd%252FLZDKzVY5h2YerMVP2edOfif55M4aX8xap7eps&asb2=1I7TDP8IFcxkO7N2fD7Uuf35KrwAJDgolqnaU5CZxusDgHCVbLJmMsHFRHWp3n_vWxj3wXNvazUP9GwGOnggHJYlpmmJwOLH-aIeEpDuPTfQgKyjkIheVqxpVknaIcrp1N-AjojIxBITNP5ZUF9U7xhJsl8GqshKoyDxr8xp8Hw&avtc=1&avte=2&avts=1696237898&keywords=%D0%BA%D0%BE%D0%BB%D1%8C%D1%86%D0%BE+%D0%BF%D0%B5%D1%87%D0%B0%D1%82%D0%BA%D0%B0+%D1%81+%D0%B1%D1%80%D0%B8%D0%BB%D0%BB%D0%B8%D0%B0%D0%BD%D1%82%D0%B0%D0%BC%D0%B8', 
    'https://en.wikipedia.org/wiki/1', 
    'https://en.wikipedia.org/wiki/2', 
    'https://en.wikipedia.org/wiki/3', 
] 

heads = []
threads = [] 
for url in urls: 
    t = ScrapeThread(url) 
    t.start() 
    threads.append(t) 

for t in threads: 
    t.join()
    

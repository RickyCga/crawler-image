# crawler-image
Download image from google-image with your own keyword. There are two methods here, one is ***crawlerImage.py*** and the other is ***crawlerBetter.py***

---
  
  
### 1. crawlerImage.py
  
This program use urllib and BeautifulSoup4 to send request and analysis HTML, then use wget to downlowd image from google-image-search. So you need to install urllib and bs4 before you exec it.
  
##### 1. Enter any User-Agent in line 35
##### 2. Use command line to exec this program
    $ python3 crawlerImage.py -k (keyword-with-dash)
  
  
  
### 2. crawlerBetter.py
  
This program use selenium to control Google Chrome webdriver and update HTML, then use wget to download image from google-image-search. Before you exec this program, you need to install selenium and [browser's webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads). This program is better than ***crawlerImage.py***, because it add new feature like **keyboard interrupt** and **it show simple details**.
  
##### 1. Use command line to exec this program
    $ python3 crawlerBetter.py -k (keyword-with-dash)

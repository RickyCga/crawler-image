from selenium import webdriver
import time
import argparse
import urllib.parse
import os
import sys
from subprocess import call

# Argument Parser
ap = argparse.ArgumentParser()
ap.add_argument("-k", "--keyword", required=True,
                help='keyword like: walking-people')
args = vars(ap.parse_args())

# Search KeyWord from argument KEYWORD
keyWord = args["keyword"].replace('-', ' ')
# Setup Dir for storage image
path = './TrainData/' + keyWord
# getsite's path need to add escape to space
escapePath = path.replace(' ', '\ ')
if not os.path.exists(path):
    os.mkdir(path, 0o777)
keyWord = urllib.parse.quote(keyWord)

if __name__ == "__main__":
    try:
        # open web-driver
        print("WebDriver Opening...")
        driver = webdriver.Chrome('./Chromedriver')
        # setup keyword search url
        url = 'https://www.google.com/search?tbm=isch&q=' + keyWord
        driver.get(url)
        # show up webdriver at right url
        time.sleep(1)
        flag = 0
        do = True
        print("website updating...")
        while do:
            testLen = len(driver.find_elements_by_class_name("rg_meta"))
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            setLen = len(driver.find_elements_by_class_name("rg_meta"))
            # check webdriver scroll down to the buttom
            if setLen == testLen:
                endLen = len(driver.find_elements_by_class_name("rg_meta"))
                time.sleep(1)
                try:
                    driver.find_element_by_xpath(
                        '//input[@type="button"]').click()
                    time.sleep(1)
                except:
                    testLen = len(
                        driver.find_elements_by_class_name("rg_meta"))
                    # check whether update after click "show more"
                    if endLen == testLen:  # no more image update after click
                        do = False

        # start download
        divInnerHTML = driver.find_elements_by_xpath("//div[@class='rg_meta']")
        numImg = 0  # for counting downloaded image number
        devnull = open(os.devnull, 'w')
        for obj in divInnerHTML:
            # get image website
            imgHttp = obj.get_attribute('innerHTML').split('":"')[
                4].split('"')[0]
            if imgHttp[-3:] != 'jpg':
                endLen -= 1
                continue
            # download with wget
            getSite = 'wget ' + imgHttp + ' -O ' + \
                escapePath + '/' + str(numImg) + '.jpg' + ' &'
            if call(getSite, shell=True, stdout=devnull, stderr=devnull):
                endLen -= 1
            else:
                numImg += 1
                print('Downloading...  ', round(
                    numImg / endLen * 100, 1), '%   ', numImg, '/', endLen, end='\r')

        # close opende file, stop webdriver and maintion user
        devnull.close()
        driver.close()
        driver.quit()
        print("\nDownload Finished!")
    except KeyboardInterrupt:
        print("\nDownload Interrupted...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

from selenium import webdriver
import time
from bs4 import BeautifulSoup

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome('chromedriver')
browser.get(start_url)
time.sleep(10)

def scrape():
    headers = ["V Mag","Proper name","Bayer designation","Distance (ly)","Spectral class","Mass","Radius", "Luminosity"]
    planet_data=[]

    soup = BeautifulSoup(browser.page_source, "html.parser")

    for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
        li_tags=ul_tag.find_all("li")
        temp_list = []
        for index, li_tag in enumerate(li_tags):
            if index == 0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")
            planet_data.append(temp_list)
from selenium import webdriver
import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/questions/42478591/python-selenium-chrome-webdriver"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(soup)
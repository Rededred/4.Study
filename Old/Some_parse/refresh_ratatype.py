from selenium import webdriver
import urllib
import urllib2
driver = webdriver.Firefox()
driver.get("Your desired URL goes here...")
#now you can refresh the page!
driver.refresh()
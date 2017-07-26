from selenium import webdriver
import time 
import os
import traceback


username = os.environ["BROWSERSTACK_USERNAME"]
access_key = os.environ["BROWSERSTACK_ACCESS_KEY"]

hub = 'hub.browserstack.com'
hub_port = 80
huburl = "http://%s:%s@%s:%d/wd/hub" %(username, access_key, hub, hub_port)

chrome_dc = {
		"os" : "WINDOWS",
		"os_version" : "10",
		"browser" : "Chrome",
		"browser_version" : "59",
		"name" : "chrome_",
		"project" : "SanketP",
		"build" : "Test",
		"name" : "Test",
		"browserstack.debug" : True,
		"browserstack.video" : True,
	}
firefox_dc = {
		"os" : "WINDOWS",
		"os_version" : "10",
		"browser" : "Firefox",
		"browser_version" : "53",
		"name" : "firefox_",
		"project" : "SanketP",
		"build" : "Test",
		"name" : "Test",
		"browserstack.debug" : True,
		"browserstack.video" : True,
	}

def start_session(huburl, browser_dc):
	try:
		browser = webdriver.Remote(huburl, browser_dc)
		test_case(browser)
	except Exception as e:
		print "[Exception] :: Error in session \n %s" %(e)
		traceback.print_exc()
	finally:
		try:
			if browser is not None:
				browser.quit()
		except Exception as ee:
			print "[Exception] :: \n %s" %(ee)

def test_case(browser):
	browser.maximize_window()
	browser.implicitly_wait(30)
	browser.get('https://www.flipkart.com/')
	browser.find_element_by_xpath('//*[@id="container"]/div/header/div[1]/div[2]/div/div/div[2]/form/div/div[1]/div/input').send_keys('iPhone 6')
	browser.find_element_by_xpath('//*[@id="container"]/div/header/div[1]/div[2]/div/div/div[2]/form/div/div[2]/button').click() #click on search
	browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/section/div[2]/div/div[2]/a[1]').click() #click on mobile
	browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/section/div[1]/label/div[1]').click() #click on assured
	browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[2]/div/div[1]/div/div/div[4]/section/div[2]/div[1]/div[1]/div/div/label/div[1]').click() #click on apple
	browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/section/div[4]/div[1]/select').click() #click on min
	browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/section/div[4]/div[1]/select/option[3]').click() #click on 30000INR

	count = 0
	mobiles={}
	for x in range(18):
		try:
			count +=1
			print count
			name = browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[1]/div/div[%d]/a/div[2]/div[1]/div[1]' %count).get_attribute('innerHTML')
			price = browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[1]/div/div[%d]/a/div[2]/div[2]/div[1]/div/div' %count).text#.get_attribute('innerHTML')
			link = browser.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[1]/div/div[%d]/a' %count).get_attribute('href')
			mobiles[name]=[price, link]
		except Exception as e:
			print "[Exception] :: \n %s" %(e)
	
	for mobile in mobiles:
		print " Mobile : %s,\t\t Price : %s,\n Link : %s \n\n" %(str(mobile), mobiles[mobile][0].encode('utf-8'), str(mobiles[mobile][1]))


if __name__ == '__main__':
	start_session(huburl, chrome_dc)

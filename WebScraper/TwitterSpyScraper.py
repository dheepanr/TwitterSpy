# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:41:05 2016

@author: dheepan.ramanan
"""

from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import re

class TwitterSpy(object):

	def bootup(self):
		
		driver = webdriver.PhantomJS('/Users/dheepan.ramanan/Documents/Resources/phantomjs-2.1.1-macosx/bin/phantomjs')
		driver.get("https://app.engagor.com/admin/")
		username = driver.find_element_by_xpath('//*[@id="emailInput"]')
		username.send_keys("dheepan.ramanan@clarabridge.com")
		password = driver.find_element_by_xpath('//*[@id="passwordInput"]')
		password.send_keys("q88SYHa1$&YJ")
		
		loginbutton = driver.find_element_by_xpath('//*[@id="loginButton"]')
		loginbutton.click()
		time.sleep(1)
		twitterspy = driver.find_element_by_xpath('//*[@id="menu"]/ul/li[4]/a')
		twitterspy.click()
		return driver
		
def scrape_data(driver, twitterId):
		searchbox = driver.find_element_by_xpath('//*[@id="app-contents"]/div/div[2]/form/input[1]')
		searchbox.send_keys(twitterId)
		submitbox = driver.find_element_by_xpath('//*[@id="app-contents"]/div/div[2]/form/input[2]')
		submitbox.click()
		try:
			driver.find_element_by_xpath('//*[@id="app-contents"]/div/table/tbody/tr/td[3]/a').click()
		except Exception:
			time.sleep(2)
			driver.find_element_by_xpath('//*[@id="app-contents"]/div/table/tbody/tr/td[3]/a').click()
		time.sleep(2)
		b = bs(driver.page_source, "html.parser")
		statsDict = {'name' :twitterId}
		
		try:
			twitterIDStats = b.find("tbody").find("small").text
		
		except AttributeError:
			time.sleep(5)
			twitterIDStats = b.find("tbody").find("small").text
			
		twitterIDStats = b.find("tbody").find("small").text
		followersRE = re.search(r'\d*\sfollowers', twitterIDStats)
		followers = int(followersRE.group(0).split('followers')[0])
		statsDict['followers'] = followers
		
		followingRE = re.search(r'\d*\sfollowing', twitterIDStats)
		following = int(followingRE.group(0).split('following')[0])
		statsDict['following'] = following
		try:
			statsbox = b.find('ul', attrs={"class":"twitter-profile-stats clearfix"}).findAll('li')
		except Exception:
			time.sleep(2)
			statsbox = b.find('ul', attrs={"class":"twitter-profile-stats clearfix"}).findAll('li')
			
		tweetsday = float(statsbox[0].strong.text)
		mentionsday = float(statsbox[1].strong.text)
		mentionsreplied = int(statsbox[2].strong.text.replace('%',''))
		repliesVposts = int(statsbox[3].strong.text.replace('%',''))
		responseTime = statsbox[4].strong.text
		withinHour = int(statsbox[5].strong.text.replace('%',''))
		
		statsDict['tweetsaday'] = tweetsday
		statsDict['mentionsday'] = mentionsday
		statsDict['mentionsreplied'] = mentionsreplied
		statsDict['repliesVposts'] = repliesVposts
		statsDict['responseTime'] = timeConverter(responseTime)
		statsDict['withinHour'] = withinHour
		
		twitterApp = b.findAll('tbody')[1].td.text
		statsDict['twitterApp'] = twitterApp
		driver.back()
		return statsDict


def timeConverter(responseTime):
	units = {'h':60, 'm':1, 's':.0167}	
	case1 = r'(\d.*[a-z]{3,4})'
	if re.search(case1, responseTime) is None:
		responseSplit = responseTime.split(' ')
		times = []
		for responseUnit in responseSplit:
			unit = responseUnit[-1]
			intUnit = units[unit]
			response = int(responseUnit.replace(unit,''))
			time = response * intUnit
			times.append(time)
		totalTime = sum(times)
		return totalTime
	else:
		numDays = re.search(case1, responseTime).group(0)
		intDays = int(re.sub(r'(\D.*)','',numDays))
		minuteDay = intDays * 1440
		#remove days
		stdResponseTime = responseTime.replace(numDays,'')
		responseSplit = stdResponseTime.split(' ')
		times = [minuteDay]
		for responseUnit in responseSplit[1:]:
			unit = responseUnit[-1]
			intUnit = units[unit]
			response = int(responseUnit.replace(unit,''))
			time = response * intUnit
			times.append(time)
		totalTime = sum(times)
		return totalTime
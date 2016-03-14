# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:41:05 2016

@author: dheepan.ramanan
"""

from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import re
import numpy as np

class TwitterSpy(object):
	def __init(self, twitterID):
		self.twitterID = twitterID
	
	def scrape(self, key,twitterID):
		
		driver = webdriver.PhantomJS('/Users/dheepan.ramanan/Documents/Resources/phantomjs-2.1.1-macosx/bin/phantomjs')
		driver.get("https://app.engagor.com/admin/")
		username = driver.find_element_by_xpath('//*[@id="emailInput"]')
		username.send_keys("dheepan.ramanan@clarabridge.com")
		password = driver.find_element_by_xpath('//*[@id="passwordInput"]')
		password.send_keys("q88SYHa1$&YJ")
		
		loginbutton = driver.find_element_by_xpath('//*[@id="loginButton"]')
		loginbutton.click()
		twitterspy = driver.find_element_by_xpath('//*[@id="menu"]/ul/li[4]/a')
		twitterspy.click()
		time.sleep(2)
		searchbox = driver.find_element_by_xpath('//*[@id="app-contents"]/div/div[2]/form/input[1]')
		searchbox.send_keys(twitterID)
		submitbox = driver.find_element_by_xpath('//*[@id="app-contents"]/div/div[2]/form/input[2]')
		submitbox.click()
		
		try:
			
			driver.find_element_by_xpath('//*[@id="app-contents"]/div/table/tbody/tr/td[3]/a').click()
			time.sleep(2)
			b = bs(driver.page_source, "html.parser")
			statsDict = {'name' :twitterID}
			
		except Exception:
			
			time.sleep(2)
			driver.find_element_by_xpath('//*[@id="app-contents"]/div/table/tbody/tr/td[3]/a').click()
			time.sleep(1)
			b = bs(driver.page_source, "html.parser")
			statsDict = {'name' :twitterID}
		
		try:
			
			twitterIDStats = b.find("tbody").find("small").text
			twitterIDStats = b.find("tbody").find("small").text
			followersRE = re.search(r'\d*\sfollowers', twitterIDStats)
			followers = int(followersRE.group(0).split('followers')[0])
			statsDict['followers'] = followers
			
			followingRE = re.search(r'\d*\sfollowing', twitterIDStats)
			following = int(followingRE.group(0).split('following')[0])
			statsDict['following'] = following
		
		except AttributeError:
			
			time.sleep(5)
			b = bs(driver.page_source, "html.parser")
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
			tweetsday = float(statsbox[0].strong.text)
			mentionsday = float(statsbox[1].strong.text)
			mentionsreplied = int(statsbox[2].strong.text.replace('%',''))
			repliesVposts = int(statsbox[3].strong.text.replace('%',''))
			responseTime = statsbox[4].strong.text
			withinHour = int(statsbox[5].strong.text.replace('%',''))
			
			statsDict['key'] = key			
			statsDict['twitterId'] = twitterID			
			statsDict['tweetsaday'] = tweetsday
			statsDict['mentionsday'] = mentionsday
			statsDict['mentionsreplied'] = mentionsreplied
			statsDict['repliesVposts'] = repliesVposts
			statsDict['responseTime'] = timeConverter(responseTime)
			statsDict['withinHour'] = withinHour
			
			twitterApp = b.findAll('tbody')
			statsDict['twitterApp'] = twitterApp
			driver.close()
			return statsDict
			
		except AttributeError:
			time.sleep(5)
			b = bs(driver.page_source, "html.parser")
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
			
			twitterApp = b.findAll('tbody')
			statsDict['twitterApp'] = twitterApp
			driver.close()
			
			return statsDict
			
	def startup(self):
			
			driver = webdriver.PhantomJS('/Users/dheepan.ramanan/Documents/Resources/phantomjs-2.1.1-macosx/bin/phantomjs')
			driver.get("https://app.engagor.com/admin/")
			username = driver.find_element_by_xpath('//*[@id="emailInput"]')
			username.send_keys("dheepan.ramanan@clarabridge.com")
			password = driver.find_element_by_xpath('//*[@id="passwordInput"]')
			password.send_keys("q88SYHa1$&YJ")
			
			loginbutton = driver.find_element_by_xpath('//*[@id="loginButton"]')
			loginbutton.click()
			time.sleep(2)
			twitterspy = driver.find_element_by_xpath('//*[@id="menu"]/ul/li[4]/a')
			twitterspy.click()
			time.sleep(2)
			return driver
		
def loopScrape(driver, key, twitterID):
	driver.get('https://app.engagor.com/admin/twitter/search?submit=Search&username='+twitterID)
		
	try:
			
		driver.find_element_by_xpath('//*[@id="app-contents"]/div/table/tbody/tr/td[3]/a').click()
		time.sleep(2)
		b = bs(driver.page_source, "html.parser")
		statsDict = {'name' :twitterID}
		
	except Exception:
		
		time.sleep(3)
		driver.find_element_by_xpath('//*[@id="app-contents"]/div/table/tbody/tr/td[3]/a').click()
		time.sleep(2)
		b = bs(driver.page_source, "html.parser")
		statsDict = {'name' :twitterID}
	try:
		
		twitterIDStats = b.find("tbody").find("small").text
		twitterIDStats = b.find("tbody").find("small").text
		followersRE = re.search(r'\d*\sfollowers', twitterIDStats)
		followers = int(followersRE.group(0).split('followers')[0])
		statsDict['followers'] = followers
		
		followingRE = re.search(r'\d*\sfollowing', twitterIDStats)
		following = int(followingRE.group(0).split('following')[0])
		statsDict['following'] = following
	
	except AttributeError:
		
		time.sleep(5)
		b = bs(driver.page_source, "html.parser")
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
		tweetsday = float(statsbox[0].strong.text)
		mentionsday = float(statsbox[1].strong.text)
		mentionsreplied = int(statsbox[2].strong.text.replace('%',''))
		repliesVposts = int(statsbox[3].strong.text.replace('%',''))
		responseTime = statsbox[4].strong.text
		withinHour = int(statsbox[5].strong.text.replace('%',''))
		
		statsDict['key'] = key			
		statsDict['twitterId'] = twitterID			
		statsDict['tweetsaday'] = tweetsday
		statsDict['mentionsday'] = mentionsday
		statsDict['mentionsreplied'] = mentionsreplied
		statsDict['repliesVposts'] = repliesVposts
		statsDict['responseTime'] = timeConverter(responseTime)
		statsDict['withinHour'] = withinHour
		
		twitterApp = b.findAll('tbody')
		statsDict['twitterApp'] = appTable(twitterApp)
		return statsDict
		
	except AttributeError:
		time.sleep(5)
		b = bs(driver.page_source, "html.parser")
		statsbox = b.find('ul', attrs={"class":"twitter-profile-stats clearfix"}).findAll('li')
		
		tweetsday = float(statsbox[0].strong.text)
		mentionsday = float(statsbox[1].strong.text)
		mentionsreplied = int(statsbox[2].strong.text.replace('%',''))
		repliesVposts = int(statsbox[3].strong.text.replace('%',''))
		responseTime = statsbox[4].strong.text
		withinHour = int(statsbox[5].strong.text.replace('%',''))
		
		statsDict['key'] = key			
		statsDict['twitterId'] = twitterID				
		statsDict['tweetsaday'] = tweetsday
		statsDict['mentionsday'] = mentionsday
		statsDict['mentionsreplied'] = mentionsreplied
		statsDict['repliesVposts'] = repliesVposts
		statsDict['responseTime'] = timeConverter(responseTime)
		statsDict['withinHour'] = withinHour
		
		twitterApp = b.findAll('tbody')
		statsDict['twitterApp'] = appTable(twitterApp)
		names = ['id','data']
		formats = ['object','f8']
		dtype = dict(names = names, formats=formats)
		topApps = np.array(appTable(twitterApp).items(), dtype=dtype)
		topAppsSorted = np.sort(topApps, order=['data'])[::-1].tolist()
		
		statsDict['NumberOneApp'] = topAppsSorted[0][0]
		statsDict['NumerOneAppUsage'] = topAppsSorted[0][1]
		
		if len(topAppsSorted) > 1:
			statsDict['NumberTwoApp'] = topAppsSorted[1][0]
			statsDict['NumerTwoAppUsage'] = topAppsSorted[1][1]
		else:
			statsDict['NumberTwoApp'] = ''
			statsDict['NumerTwoAppUsage'] = ''
			
		if len(topAppsSorted) > 2:
			statsDict['NumberThreeApp'] = topAppsSorted[2][0]
			statsDict['NumerTwoThreeUsage'] = topAppsSorted[2][1]
		else:
			statsDict['NumberThreeApp'] = ''
			statsDict['NumerTwoThreeUsage'] = ''
		
		 
		time.sleep(2)
		
		return statsDict
	
	
		


def timeConverter(responseTime):
	units = {'h':60, 'm':1, 's':.0167}	
	case1 = r'(\d.*[a-z]{3,4})'
	try:
		if re.search(case1, responseTime) is None:
			responseSplit = responseTime.split(' ')
			times = []
			for responseUnit in responseSplit[1:]:
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
	except KeyError:
		totalTime = ''
		return totalTime

def appTable(bs4list):
	links = bs4list[1].findAll('a')
	twitterApps = []
	for link in links:
		if link.has_attr('rel'):
			twitterApps.append(link.text)

	nums = []
	tds = bs4list[1].findAll('td')
	for td in tds:
			if re.search(r'\W\d',td.text):
				num = int(re.search(r'(.*)(\(\d.*\))',td.text).group(1).replace('\n','').replace(' ',''))
				nums.append(num)
	appVal = dict(zip(twitterApps,nums))
	return appVal
			
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:17:31 2016

@author: dheepan.ramanan
"""

from TwitterSpyScraper import TwitterSpy, loopScrape
import pandas as pd
import sqlite3
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException


conn = sqlite3.connect('TwitterSpy.db')
sfEngagor = pd.read_excel('/Users/dheepan.ramanan/Documents/TwitterSpy/Spreadsheets/engagorsalesforce.xlsx')
#retail test
c = conn.cursor()

targetHandles = sfEngagor["Main Twitter Handle"][1668:].to_dict()



twitterApps = open('apps.txt','r+')
scrapelog = open('scrapelog.txt','r+')
driver = TwitterSpy().startup()
'''
for key, handle in targetHandles.items():
	try:
		data = TwitterSpy().scrape(key, handle)
		c.execute("INSERT INTO TwitterHandles (key, twitterHandle, tweetsaday, mentionsday, mentionsreplied, repliesVposts,responseTime,withinHour) VALUES (?,?,?,?,?,?,?,?)",
			(data['key'],	
			data['twitterId'], 
			data['tweetsaday'],
			data['mentionsday'],
			data['mentionsreplied'],
			data['repliesVposts'],
			data['responseTime'], 
			data['withinHour']))
		conn.commit()
		twitterAppData = data['twitterApp']
		twitterApps.write(str(key)+'~'+str(twitterAppData)+'\n')
		scrapelog.write(str(key)+':'+str(handle)+'\n')
		print handle
		print key, " out of ", len(targetHandles), "Complete"
		
	except Exception:
		scrapelog.write(str(key)+':'+str(handle)+'\n')
		print key, handle		
		time.sleep(100)
		data = TwitterSpy().scrape(key, handle)
		c.execute("INSERT INTO TwitterHandles (key, twitterHandle, tweetsaday, mentionsday, mentionsreplied, repliesVposts,responseTime,withinHour) VALUES (?,?,?,?,?,?,?,?)",
			(data['key'],	
			data['twitterId'], 
			data['tweetsaday'],
			data['mentionsday'],
			data['mentionsreplied'],
			data['repliesVposts'],
			data['responseTime'], 
			data['withinHour']))
		twitterAppData = data['twitterApp']
		twitterApps.write(str(key)+'~'+str(twitterAppData)+'\n')
		conn.commit()
		print key, " out of ", len(targetHandles), "Complete"
		
'''
for key, handle in targetHandles.items():
	try:
		data = loopScrape(driver, key, handle)
		c.execute("INSERT INTO TwitterHandles (key, twitterHandle, tweetsaday, mentionsday, mentionsreplied, repliesVposts,responseTime,withinHour) VALUES (?,?,?,?,?,?,?,?)",
			(data['key'],	
			data['twitterId'], 
			data['tweetsaday'],
			data['mentionsday'],
			data['mentionsreplied'],
			data['repliesVposts'],
			data['responseTime'], 
			data['withinHour']))
		conn.commit()
		twitterAppData = data['twitterApp']
		twitterApps.write(str(key)+'~'+str(twitterAppData)+'\n')
		scrapelog.write(str(key)+':'+str(handle)+'\n')
		print handle
		print key, " out of ", 3244, "Complete"
	
	except ElementNotVisibleException:
		pass
		scrapelog.write(str(key)+':'+str(handle)+'\n')
		print 'FAILED'
		print key, handle
		
	except NoSuchElementException:
		pass
		scrapelog.write(str(key)+':'+str(handle)+'\n')
		print 'FAILED'
		print key, handle
		
	except AttributeError:
		pass
		scrapelog.write(str(key)+':'+str(handle)+'\n')
		print 'FAILED'
		print key, handle
	
						






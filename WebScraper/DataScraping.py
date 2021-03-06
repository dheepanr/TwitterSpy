# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:17:31 2016

@author: dheepan.ramanan
"""

from TwitterSpyScraper import TwitterSpy, loopScrape, appTable
import pandas as pd
import sqlite3
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
import numpy as np


conn = sqlite3.connect('TwitterSpy.db')
sfEngagor = pd.read_excel('/Users/dheepan.ramanan/Documents/TwitterSpy/AEaccounts.xlsx')
#retail test
c = conn.cursor()

targetHandles = sfEngagor["Twitter Handle"].to_dict()



apps = {}
scrapelog = open('scrapelog4.txt','wb')
driver = TwitterSpy().startup()
failedKey= []
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
		twitterAppData = appTable(data['twitterApp'])
		apps[handle] = [twitterAppData]
		scrapelog.write(u''.join((str(key),':',handle,'\n')).encode('utf-8').strip())
		print handle
		print key, " out of ", len(sfEngagor["Twitter Handle"]), "Complete"
	
	except ElementNotVisibleException:
		pass
		scrapelog.write(u''.join((str(key),':',handle,'\n')).encode('utf-8').strip())
		print 'FAILED'
		print key, handle
		failedKey.append(handle)
		
	except NoSuchElementException:
		pass
		scrapelog.write(str(key).encode('utf-8')+':'+str(handle).encode('utf-8')+'\n')
		print 'FAILED'
		print key, handle
		failedKey.append(handle)
		
	except AttributeError:
		pass
		scrapelog.write(u''.join((str(key),':',handle,'\n')).encode('utf-8').strip())
		print 'FAILED'
		print key, handle
		failedKey.append(handle)
		
	except TypeError:
		pass
		scrapelog.write(u''.join((str(key),':',handle,'\n')).encode('utf-8').strip())
		print 'FAILED'
		print key, handle
		failedKey.append(handle)
	
						
apps = []
for df in dfs:
		for key, val in df['twitterApp'].items():
			apps.append(key)
npList = np.unique(apps).tolist()

				
			





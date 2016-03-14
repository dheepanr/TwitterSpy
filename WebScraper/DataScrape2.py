# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 11:25:44 2016

@author: dheepan.ramanan
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:17:31 2016

@author: dheepan.ramanan
"""

from TwitterSpyScraper import TwitterSpy, loopScrape
import pandas as pd
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException



sfEngagor = pd.read_excel('/Users/dheepan.ramanan/Documents/TwitterSpy/AEaccounts.xlsx')
#retail test

targetHandles = sfEngagor["Twitter Handle"].to_dict()



apps = {}
dfs= []
scrapelog = open('scrapelog4.txt','wb')
driver = TwitterSpy().startup()
failedKey= []

for key, handle in targetHandles.items():
	try:
		data = loopScrape(driver, key, handle)
		scrapelog.write(u''.join((str(key),':',handle,'\n')).encode('utf-8').strip())
		print handle
		print key, " out of ", len(sfEngagor["Twitter Handle"]), "Complete"
		dfs.append(data)
	
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
		
		

	
						






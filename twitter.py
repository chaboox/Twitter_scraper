# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 10:51:49 2019

@author: deboosere_am
"""

import time
import operator
import unicodecsv as cs
import json
import msvcrt
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
base_url = u'https://twitter.com/search?q='
newlist = []
newlist2 = []
maleName = [u'Alain', u'François', u'Julien', u'Stéphane', u'Olivier', u'Leo', u'Mathieu', u'Maxime', u'Thomas', u'Nico']
femalName = [u'Jeanne', u'Nathalie', u'Isabelle', u'Lucie', u'Manon', u'Lea', u'Alice', u'Emeline', u'Charlotte', u'Morgane']
#femalName = [ u'Emeline']
for male in femalName:
    query = male
    print(male)
    url = base_url + query

    browser.get(url)
    time.sleep(1)

    body = browser.find_element_by_tag_name('body')

    for ls in range(1000):
        print(ls)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
    
    tweets = browser.find_elements_by_class_name("tweet-text")
    names = browser.find_elements_by_class_name("show-popup-with-id")
    aas = browser.find_elements_by_class_name("tweet")
#usernames = browser.find_elements_by_class_name("username u-dir u-textTruncate")
#usernames = browser.find_element_by_css_selector(".username")
    i = 0
    print(newlist)
    
  # for tweet in tweets:
    #    i = i +1
    #    
      #  print(str(i) + ' - ' + tweet.text )
     #   if tweet.text != None:
     #       if not(operator.contains(tweet.text.lower(), male.lower())):
     #           newlist.append([tweet.text, 1])
    
    i = 0
    for a in aas:
        replyB = 'nop'
        image = a.find_element_by_tag_name("img")
        tweeta = a.find_elements_by_class_name("tweet-text")
        name = a.find_elements_by_class_name("fullname")
        username = a.find_elements_by_class_name("username")
        reply = a.find_elements_by_class_name("ReplyingToContextBelowAuthor")
        #urllib.request.urlretrieve(image.get_attribute("src"), "male2/" +username[0].text +".jpg")
        if len(reply) > 0:
            replyB = 'WOUHOU'
        i = i +1
        print(str(i) + ' ----- ' + image.get_attribute("src") + '   KKKKKK  ' + tweeta[0].text + '  OOOO   ' + replyB + 'USER ' + username[0].text +' NAME ' + name[0].text )
        if tweeta[0].text != None:
            if not(operator.contains(tweeta[0].text.lower(), male.lower())):
                if replyB != 'WOUHOU':
                    newlist.append([tweeta[0].text, username[0].text, name[0].text, 1])
                    urllib.request.urlretrieve(image.get_attribute("src"), "femaleFinal/" +username[0].text +".jpg")
       
    
    '''
    i=0
    for name in names:
        i = i +1
        print(str(i) + ' - ' + name.text )
        newlist2.append([name.text, 1])
        finalList = [newlist, newlist2]    '''
    
#csv.register_dialect('myDialect',
#delimiter = ';',
#quoting=csv.QUOTE_ALL,
#skipinitialspace=True)

#with open('tweets.xls', 'w', newline='', encoding='utf-8') as myfile:
   # wr = csv.writer(myfile, dialect='myDialect')
   # wr.writerow(newlist)
   # for row in newlist2:
   #     wr.writerow(row)
        
with open('my_data_femaleFjson.json', 'w') as out_f:
        json.dump(newlist, out_f)

out_f.close()
    





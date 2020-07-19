#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing packages
from bs4 import BeautifulSoup
import csv
import requests
import re


# In[2]:


#defining URL
url= "https://www.census.gov/programs-surveys/popest.html"


# In[3]:


#sending/retrieving requests for response
r= requests.get(url)


# In[4]:


html= r.text
#parsing html using BeautifulSoup
census= BeautifulSoup(html, 'html.parser')


# In[5]:


find= census.find_all("a")


# In[6]:


len(find)


# In[7]:


links= set()


# In[8]:


for link in find:
    hrefs= str(link.get("href"))
    if hrefs.startswith('#http'):
        links.add((hrefs[1:]))
    elif hrefs.startswith('None'):
        ''
    elif hrefs.startswith('#'):
        ''
    elif hrefs.startswith('/'):
        links.add('https://www.census.gov' +hrefs)
    elif hrefs.endswith('.gov'):
        links.add(hrefs + '/')
    else:
        links.add(hrefs)


# In[9]:


len(links)


# In[10]:


file= open('my_export.csv', 'w')


# In[11]:


write= csv.writer(file, delimiter=' ', lineterminator='\r')


# In[12]:


links_list= []


# In[13]:


for x in links:
    links_list.append(x)
    if not links_list:
        write.writerow(links_list)
    else:
        del(x)
        


# In[ ]:





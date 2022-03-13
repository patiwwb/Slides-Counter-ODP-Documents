#!/usr/bin/env python
# coding: utf-8

# In[1]:


import glob


# In[18]:


txtfiles = []
all_files = glob.glob("./INCOMING FR/*.odp")
print(glob.glob("./INCOMING FR/*.odp"))


# In[3]:


FILES_COUNT = len(all_files)


# In[4]:


print(FILES_COUNT, ' Different .odp files')


# In[5]:


files_names = []
files_slides = []


# In[6]:


with open('files_list.txt', 'w') as the_file:
    for i in range(FILES_COUNT):
        files_names.append(all_files[i].split("\\")[-1])
        the_file.write(all_files[i].split("\\")[-1] + '\n')


# In[13]:


import zipfile
import re

counter = 0
FILEPATH = "./INCOMING FR/"
files_slides = []
for i in range(FILES_COUNT):
    archive = zipfile.ZipFile(FILEPATH + files_names[i], 'r')
    content_xml = archive.read('content.xml')
    x = re.findall(rb"<draw:page([\s\S]*?)<\/draw:page>", content_xml)
    r = len(x)
    files_slides.append(r)
    counter += int(r)
    archive.close()

print(counter, "slides in total")

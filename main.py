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


# In[14]:


with open('list.txt', 'w') as the_file:
    for i in range(FILES_COUNT):
        the_file.write(files_names[i] + " " + str(files_slides[i]) + '\n')


# In[15]:


import os.path
text = open("list.txt").read()

list_files = text.splitlines( )
for l in list_files:
    filename = l.split(" ")[0]
    extension = os.path.splitext(filename)[1]
    if(extension != ".odp"):
        print(filename, extension)
        list_files.remove(l)
#print(list_files)
files_dict = {}
for i in list_files:
    files_dict[i.split(" ")[0]] = i.split(" ")[1]

total_slides_count = 0
for value in files_dict.values():
    total_slides_count += int(value)
print(len(files_dict), "different files")
print(total_slides_count, "slides in total")

for k, v in files_dict.items():
    files_dict[k] = int(v)

"""
def by_value(item):
    return item[1]

for k, v in sorted(files_dict.items(), key=by_value):
    print(k, '->', v)

x1= 0
list1 = []
x2 = 0
list2 = []
i = 0
for k, v in sorted(files_dict.items(), key=by_value):
    if(i%2 == 0):
        x1 += v
        list1.append(k)
        i += 1
    else:
        x2+= v
        list2.append(k)
        i += 1
        
print(x1)
print(list1)
print(x2)
print(list2)

"""
liste = (list(files_dict.values()))

def sumSplit(left,right=[],difference=0):
    sumLeft,sumRight = sum(left),sum(right)

    # stop recursion if left is smaller than right
    if sumLeft<sumRight or len(left)<len(right): return

    # return a solution if sums match the tolerance target
    if sumLeft-sumRight == difference:
        return left, right, difference

    # recurse, brutally attempting to move each item to the right
    for i,value in enumerate(left):
        solution = sumSplit(left[:i]+left[i+1:],right+[value], difference)
        if solution: return solution

    if right or difference > 0: return 
    # allow for imperfect split (i.e. larger difference) ...
    for targetDiff in range(1, sumLeft-min(left)+1):
        solution = sumSplit(left, right, targetDiff)
        if solution: return solution 
     
def SelectFiles(l1,l2):
    tempdict = files_dict
    dic1 = {}
    dic2 = {}
    length_l1 = len(l1)
    length_l2 = len(l2)
    for i in range(length_l1):
        for key in list(tempdict.keys()):
            if(l1[i] == tempdict.get(key)):
                dic1[key] = int(tempdict.get(key))
                del tempdict[key]
                break;
        i +=1
    for i in range(length_l2):
        for key in list(tempdict.keys()):
            if(l2[i] == tempdict.get(key)):
                dic2[key] = int(tempdict.get(key))
                del tempdict[key]
                break;
        i +=1
    return dic1,dic2
    
print("Personne 1 a ",len(sumSplit(liste)[0])," fichiers avec ",sum(sumSplit(liste)[0]), "slides")
print("Personne 2 a ",len(sumSplit(liste)[1])," fichiers avec ",sum(sumSplit(liste)[1]), "slides")
#print(sumSplit(liste))
dic1,dic2 = SelectFiles(sumSplit(liste)[0],sumSplit(liste)[1])
print("----------------------------------------------------------------------------------")
print("Détail Personne 1")
sum1 = 0
for k, v in dic1.items():
    sum1 += v
print(len(dic1)," fichiers")
print(sum1, " slides")
for k, v in dic1.items():
    print(k,"-->",v)


print("----------------------------------------------------------------------------------")
print("Détail Personne 2")
sum2 = 0
for k, v in dic2.items():
    sum2 += v
print(len(dic2)," fichiers")
print(sum2, " slides")
for k, v in dic2.items():
    print(k,"-->",v)


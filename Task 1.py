#!/usr/bin/env python
# coding: utf-8

# # Task 1:
# a. A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
# 
# b. The text file, keylog.txt (attached), contains fifty successful login attempts.
# 
# c. Given that the three characters are always asked for in order, analyze the file so as to determine the shortest possible secret passcode of unknown length.
# ___

# # Solution

# Read file and import defaultdict function

# In[1]:


from collections import defaultdict

df = open('keylog.txt').readlines() # read file but need \n remove
keylog = [line.strip() for line in df] # list with separate values


# A defaultdict works exactly like a normal dict, but it is initialized with a function (“default factory”) that takes no arguments and provides the default value for a nonexistent key.

# In[2]:


df_dict = defaultdict(list)
for i in keylog:
    for j, n in enumerate(i):# separate index and value
        df_dict[n].append(j)


# Result in defaultdict where every unique value and index in a row from keylog
# 
# result can see next block

# In[3]:


dict_it = list(df_dict.items())
#show result
for k,v in dict_it:
    print(k,v)


# So next will be the last step calculate average value for every unique element and all that remains is sort average value descending

# In[4]:


avr_positions = {}
for k,v in dict_it:
    avr_positions[k] = float(sum(v))/float(len(v))


# So there can see that 7 will be first (wich 0.0 average value), next 3 (0.14) and last will be 0 because have maximal value

# In[5]:


avr_positions


# Let's sort

# In[6]:


sort_it = sorted(list(avr_positions.items()), key=lambda x: x[1])
a = [i for i,j in sort_it]
print(a)


# Answer: 73162890

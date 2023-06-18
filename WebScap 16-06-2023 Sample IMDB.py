#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
response=requests.get('https://www.imdb.com/chart/top/')
print(response)


# In[4]:


html_content = response.text


# In[ ]:


html_content


# In[5]:


soup = BeautifulSoup(html_content,"html.parser")


# In[ ]:


soup


# In[6]:


movie_titles=[]
movie_years=[]
movie_ratings=[]


# In[7]:


#select all table row in the list
rows=soup.select("tbody.lister-list tr")


# In[8]:


#select movie title, year and rating column
for row in rows:
    title_column=row.select(".titleColumn a")
    year_column=row.select(".secondaryInfo")
    rating_column=row.select(".imdbRating strong")
    
    #Extraxt title, year and rating text and add it to the list
    movie_titles.append(title_column[0].text)
    movie_years.append(year_column[0].text.strip("()")) #.strip() removes the year parantheses
    movie_ratings.append(rating_column[0].text)


# In[9]:


df=pd.DataFrame(columns=["Movie_Title", "Year", "Rating"])


# In[ ]:


for i in range(len(movie_titles)):
    df=df.append({
        "Movie Title": movie_titles[i],
        "Year": movie_years[i],
        "Rating": movie_ratings[i]
    }, ignore_index=True)


# In[11]:


print(df)


# In[12]:


df


# In[13]:


df.to_csv("IMDB Top 250 Charts Details.csv")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





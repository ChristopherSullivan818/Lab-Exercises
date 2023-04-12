#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
import csv
import seaborn as sns


# In[2]:


df= pd.read_csv("AB_NYC_2019 - AB_NYC_2019.csv")
df


# In[3]:


#This dataset can be used for a number of things such as comparing
#the neighborhood to the listings_count or number_of_reviews as seeing where
#or which neighborhoods that customers stay in the most


# In[4]:


cols=df.columns
sns.heatmap(df[cols].isnull()) #Finding NaN values


# In[5]:


df["last_review"] = df["last_review"].fillna("No Reviews")
df["reviews_per_month"] = df["reviews_per_month"].fillna("No Reviews")
df #Fills NaN with No Reviews


# In[10]:


df.last_review = df.last_review.str[0:4]
df.last_review #Only displays years for values that have years


# In[14]:


df.tail() #Returns last few rows


# In[13]:


df.iloc[3000:3003]#Returns rows 3000 - 3002


# In[46]:


import requests
import json
from googleapiclient.discovery import build


# In[30]:


def get_data(API_Key): #Function 1
    raw_response=requests.get(f"https://www.googleapis.com/youtube/v3/videos?id=7lCDEYXw3mM&key={API_Key}&part=snippet,contentDetails,statistics,status")
    response=raw_response.json()
    return response

get_data("AIzaSyDicEVjVA8YtjG-jA7v9Tw4_uVOLwWwR00")


# In[58]:


API_Key = "AIzaSyDicEVjVA8YtjG-jA7v9Tw4_uVOLwWwR00"
youtube = build('youtube', 'v3', developerKey= API_Key)

def channel_info(channel_id): #Function 2
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=channel_id)
    response=request.execute()
    
    return response
    
    
channel_info("UC-lHJZR3Gqxm24_Vd_AJ5Yw") #The channel ID for PewDiePie


# In[56]:


def subscriber_count(channel_id): #Function 3
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=channel_id)
    response=request.execute()
    sub_count=response['items'][0]['statistics']['subscriberCount']
    print(sub_count)
    
subscriber_count("UC-lHJZR3Gqxm24_Vd_AJ5Yw")


# In[57]:


def Channel_name(channel_id): #Function 4
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=channel_id)
    response=request.execute()
    name=response['items'][0]['snippet']['title']
    print(name)
    
Channel_name("UC-lHJZR3Gqxm24_Vd_AJ5Yw")


# In[59]:


def view_count(channel_id): #Function 5
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=channel_id)
    response=request.execute()
    views=response['items'][0]['statistics']['viewCount']
    print(views)
    
view_count("UC-lHJZR3Gqxm24_Vd_AJ5Yw")


# In[60]:


def get_video_ids(playlist_id): #Function 6
    request = youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId= playlist_id)
    response=request.execute()
    
    return response

get_video_ids("UU-lHJZR3Gqxm24_Vd_AJ5Yw")


# In[65]:


def number_of_uploads(playlist_id): #Function 7
    request = youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId= playlist_id)
    response=request.execute()

    number=response['pageInfo']['totalResults']
    
    print(number)

number_of_uploads("UU-lHJZR3Gqxm24_Vd_AJ5Yw")


# In[ ]:





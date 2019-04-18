
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import csv
import json

import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import sqlite3

DEVELOPER_KEY = "AIzaSyCjGtYNYaE8-CI0nYbNrrMDfBTFbtaeaIY"
#"AIzaSyAKlh8L9MNnZg-O75TkBxKSpQk0IorI1Vs"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

def call_mostpopular_video():

    # Call the videos.list method to retrieve video info
    list_videos_by_id = youtube.videos().list(
        part = "id, snippet, contentDetails, statistics",
                  chart ='mostPopular', regionCode ='DE',
           maxResults = 10, videoCategoryId ='').execute()

    # extracting the results from search response
    popular_videos = list_videos_by_id.get("items", [])
    # print(popular_videos)

    total_rows = []
    for video in popular_videos:

        row = []

        videoId = video['id']
        row.append(videoId)
        title = video['snippet']['title']
        row.append(title)

        response = youtube.videos().list(part='statistics, snippet',id=videoId).execute()

        channelId = response['items'][0]['snippet']['channelId']
        row.append(channelId)
        channelTitle = response['items'][0]['snippet']['channelTitle']
        row.append(channelTitle)
        # print(channelTitle)
        favoriteCount = response['items'][0]['statistics']['favoriteCount']
        row.append(favoriteCount)
        viewCount = response['items'][0]['statistics']['viewCount']
        row.append(viewCount)
        likeCount = response['items'][0]['statistics']['likeCount']
        row.append(likeCount)
        dislikeCount = response['items'][0]['statistics']['dislikeCount']
        row.append(dislikeCount)
        # if 'commentCount' in response['items'][0]['statistics']:
        #     commentCount = response['items'][0]['statistics']['commentCount']
        #     row.append(commentCount)
        # else:
        #     row.append('NULL')
        favoriteCount = response['items'][0]['statistics']['favoriteCount']
        row.append(favoriteCount)

        total_rows.append(row)

    return total_rows

#     call_mostpopular_video()
#
popular_video_list = call_mostpopular_video()

# print(popular_video_list)


Base = declarative_base()
session = scoped_session(sessionmaker())
engine = create_engine('sqlite:///youtube_popular_videos.sqlite', echo=True)

Base.metadata.bind = engine
session.configure(bind=engine)

def DB_setup():
    Base.metadata.create_all(engine)
    return engine

#
# class Video_class(Base):
#     __tablename__ = 'Video'
#     index = Column(Integer, primary_key = True, autoincrement = True)
#     videoId = Column(String(250), nullable = False)
#     title = Column(String(250), nullable = False)
#     channelId = Column(String(250), ForeignKey('Channel.channelId'))
#
#     channel = relationship("Channel_class")

class Video_class(Base):
    __tablename__ = 'Video'
    videoId = Column(String(250), primary_key = True, nullable = False)
    title = Column(String(250), nullable = False)
    channelId = Column(String(250), ForeignKey('Channel.channelId'))

    channel = relationship("Channel_class")

# video_test = Video_class()

class Channel_class(Base):
    __tablename__ = 'Channel'
    channelId = Column(String(250), primary_key = True)
    channelTitle = Column(Integer(), nullable = False)

    video = relationship('Video_class', backref = "Channel_class")

# channel_test = Channel_class()

class Reaction_class(Base):
    __tablename__ = 'Reaction'
    videoId = Column(String(250), primary_key = True, nullable = False)
    viewCount = Column(Integer(), nullable = False)
    likeCount = Column(Integer(), nullable = False)
    dislikeCount = Column(Integer(), nullable = False)
    favoriteCount = Column(Integer(), nullable = False)
#    commentCount = Column(Integer())

reaction_test = Reaction_class()

if __name__ == "__main__":
    DB_setup()
    print("Database created")


def DB_stowing():

    for video in popular_video_list:
        videoId = video[0]
        title = video[1]
        channelId = video[2]

        video_inst = Video_class(videoId = videoId, title=title, channelId = channelId)
        session.add(video_inst)

    session.commit()

    for video in popular_video_list:
        channelId = video[2]
        channelTitle = video[3]

        channel_inst = Channel_class(channelId = channelId, channelTitle=channelTitle)

        session.add(channel_inst)

    session.commit()

    for video in popular_video_list:
        videoId = video[0]
        viewCount = video[5]
        likeCount = video[6]
        dislikeCount = video[7]
        favoriteCount = video[8]

        reaction_inst = Reaction_class(videoId=videoId, viewCount=viewCount, likeCount=likeCount, dislikeCount=dislikeCount, favoriteCount=favoriteCount) #commentCount=commentCount)

        session.add(reaction_inst)

    session.commit()

if __name__ == "__main__":
    DB_stowing()
    print("Database filled with video info")
    # print(type(DB_setup())) : <class 'sqlalchemy.engine.base.Engine'>


import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import csv
import json
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import sqlite3
import os
from flask import (Flask, request, render_template, session, redirect, url_for, Response) # It should be inside a paranthesis?
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.debug = True
app.use_reloader = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///youtube_popular_videos.db'
# Q1. Should it be sqlite or .db?
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
session = db.session

DEVELOPER_KEY = "AIzaSyCjGtYNYaE8-CI0nYbNrrMDfBTFbtaeaIY"
#"AIzaSyAKlh8L9MNnZg-O75TkBxKSpQk0IorI1Vs"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)


# Q1. It doesn't create the cached file

@app.route('/')
def welcome():
    return render_template("welcome.html")

# RECIEVE INPUT FROM A USER
@app.route('/country')
def choose_country():
    country_codes = ["US", "GB", "IN", "DE", "CA", "FR", "KR", "RU", "JP", "BR", "MX"]
    #
    # if request.method == 'GET':
    #     code = request.args.get(country)
    return render_template("country.html", country_codes = country_codes)



# DEFINE CACHING PATTERN
CACHE_FNAME = "SI507finalproject_cached_data.json"

try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
except:
    CACHE_DICTION ={}

def params_unique():
    date = datetime.now().strftime("%m/%d/%Y")
    return date

# GET DATA FROM API IF IT WAS NOT CACHED
total_rows = []

def make_cache():
    unique_identifier = params_unique()
    if unique_identifier in CACHE_DICTION:
        print("Getting data from a cached file")
        return CACHE_DICTION[unique_identifier]

    # extracting the results from search response
    else:
        list_videos_by_id = youtube.videos().list(
            part = "id, snippet, contentDetails, statistics",
                      chart ='mostPopular', regionCode = "US",
               maxResults = 10, videoCategoryId ='').execute()

        popular_videos = list_videos_by_id.get("items")[0]
        print(popular_videos)
        popular_videos_obj = json.dumps(popular_videos)
        cache_file_obj = open(CACHE_FNAME, 'w')
        CACHE_DICTION[unique_identifier] = popular_videos_obj
        cache_file_obj.write(json.dumps(CACHE_DICTION))
        cache_file_obj.close()
        return popular_videos_obj

        # print(popular_videos)

def make_call():
    list_videos_by_id = youtube.videos().list(part = "id, snippet, contentDetails, statistics",
                      chart ='mostPopular', regionCode = "US",
               maxResults = 6, videoCategoryId ='').execute()
    popular_videos = list_videos_by_id.get("items", [])

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

popular_video_list = make_call()
# print('***This is where I need to check*** ',popular_video_list)


# SET UP DATABASE

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
    videoId = Column(String(250),ForeignKey('Reaction.videoId'), primary_key = True, nullable = False)
    title = Column(String(250), nullable = False)
    channelId = Column(String(250), ForeignKey('Channel.channelId'))

    channel = relationship("Channel_class")
    reaction = relationship("Reaction_class")

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
    videoTitle = Column(String(250), nullable = False)
    viewCount = Column(Integer(), nullable = False)
    likeCount = Column(Integer(), nullable = False)
    dislikeCount = Column(Integer(), nullable = False)

    video = relationship('Video_class', backref = "Reaction_class")


#    favoriteCount = Column(Integer())
#    commentCount = Column(Integer())

# reaction_test = Reaction_class()

if __name__ == "__main__":
    DB_setup()
    print("Database created")

print(popular_video_list)
# for video in popular_video_list:
#     print(popular_video_list[1])

def DB_stowing():

    for video in popular_video_list:
        videoId = video[0]
        title = video[1]
        channelId = video[2]
        if session.query(Video_class).filter_by(videoId = videoId).first():
            continue
        video_inst = Video_class(videoId = videoId, title=title, channelId = channelId)
        session.add(video_inst)

    session.commit()

    for video in popular_video_list:
        channelId = video[2]
        channelTitle = video[3]
        if session.query(Channel_class).filter_by(channelId = channelId ).first():
            continue
        channel_inst = Channel_class(channelId = channelId, channelTitle=channelTitle)
        session.add(channel_inst)

    session.commit()

    for video in popular_video_list:
        videoId = video[0]
        videoTitle = video[1]
        viewCount = video[5]
        likeCount = video[6]
        dislikeCount = video[7]
        favoriteCount = video[8]
        if session.query(Reaction_class).filter_by(videoId = videoId).first():
            continue

        reaction_inst = Reaction_class(videoId=videoId,videoTitle=videoTitle, viewCount=viewCount, likeCount=likeCount, dislikeCount=dislikeCount) #favoriteCount=favoriteCount) #commentCount=commentCount)

        session.add(reaction_inst)

    session.commit()

if __name__ == "__main__":
    DB_stowing()
    print("Database filled with video info")
    # print(type(DB_setup())) : <class 'sqlalchemy.engine.base.Engine'>


@app.route('/result')
def show_video():
    videos_bycountry = []
    videos = session.query(Video_class).all()
    for v in videos:
        videos_bycountry.append(v.title)
    return render_template("result.html", videos_bycountry = videos_bycountry)

@app.route('/reaction')
def show_reaction():
    reaction_tovideo = []
    videos = session.query(Reaction_class).all()
    for v in videos:
        reaction_tovideo.append((v.videoTitle, v.viewCount, v.likeCount, v.dislikeCount))
    return render_template("reaction.html", reaction_tovideo = reaction_tovideo)

@app.route('/channel')
def show_channel():
    channel_ofvideo = []
    channels = session.query(Channel_class).all()
    for c in channels:
        channel_ofvideo.append(c.channelTitle)

    return render_template("channel.html", channel_ofvideo = channel_ofvideo)



if __name__ == '__main__':
    app.run()

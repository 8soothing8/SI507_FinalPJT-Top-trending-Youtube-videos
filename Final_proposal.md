
# SI507 - Final Project by Youngsoo Choy

-------------------------------

## Overall

### My project will...

scrape data from youtube API and allow a user to search for the most viewed in a given country on a given date (or month). A route linked with the application will show the title of video, the name of channel, the number of likes and dislikes that the video got. Another route will visualize information about certain number of videos that user input in a specific country. The other route will show the top 5 most popular tags on a given day.   


### I want to focus on...
making an easy interface window to get a correct input from a user by specifying search terms. I'd like to make a dropdown menu on a route to avoid mistype or wrong input from a user.  


## Interface description

- Route 1: /mostview  →   
  This page will show the most viewed video on a given day.
  A user will be able to select a certain date to see the most viewed video and its producer(channel) name.

- Route 2: /topvideos  →   
  This page shows details of a certain number of the most viewed videos in a certain country. A user can choose a country they want to check and the number of the most viewed videos.

- Route 3: /populartags  →   
  This page will show the 5 most popular tags on a certain period of time (day or month). The application behind this will collect all tags in a video and show the top 5 tags


## Specifics

# I will be relying on data from
scraping , making requests to Youtube API, caching the data. The user input can specify the search term in the cached data.

An example of my data OR link to documentation of the API I’ll use OR the website I will be scraping is here: https://www.googleapis.com/youtube/v3nput)

I expect my database schema to include number tables. The entities each table will represent are: list entities, such as video titles, video makers, the number of likes and dislikes, etc.

I haven't decided yet if I will be saving data to a database when it’s accessed via API or directly accessing to specific information in a cached json file.

I am planning to use the following modules in writing my code, aside from Flask and SQLAlchemy or some equivalent:

 - requests_cache - for caching data I scrape
 - plotly - for charting/graphing data
 - matplotlib - I don't know about how to use it, but will check and see

I will be defining the following classes outside of Flask routes/models:

A class that search the most viewed video. The below is brief idea of what can construct the class.

class most_viewed(user_input):
    def __init__(self, cached_file):
        # I don't know what I need to put here to filter videos on a specific day
        self.title = cached_file["path1"]["path2"]
        self.date = cached_file["path1"]["path2"]
    def __str__(self):
        return "'The most popular video on {} is {}".format(self.title, self.date)

The assignment(s) in 507 we’ve done that are most like what I want to do are: project 4, project 1, lab3

Other useful resources for this project for me will be:
how to make dropdown menus on a page https://www.w3schools.com/howto/howto_js_dropdown.asp


## Other

### My biggest concerns about my work on this project are
 - whether I can scrape data from Youtube successfully. I haven't tried scraping yet, but I knew that Youtube data were open to public a few months ago. I should check if it's still available, and if I can use codes from my previous assignments for it.
 - whether I can broaden the period of search with some text data manipulation or not. I would try to make this application allow a user to search for a certain month. I might need to revisit advanced_expiry_caching.py to transform time data.
 DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
 - whether I can make dropdown menus for date selection. There should be three separate dropdown menus for Year, Month, Day information and the routes should be able to aggregate those three numbers to search for a specific date.   
 - which data visualization tools or methods that I need to use to make the information easily understandable.


### I feel confident that I can complete these parts of the project I am planning
...is not much. I'll figure out what I can do and can't do after I start building it.

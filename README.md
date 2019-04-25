# SI507_FinalPJT (https://github.com/8soothing8/SI507_FinalPJT)

## Project Description

This app finds the top 10 most popular videos on youtube in a certain country and build a database containing detailed information about them. 
A user can see the video that was most viewed, or most liked through an website (localhost route that will be created for next week)    

## How to run  
(GET YOUR OWN Youtube Data API key and replace a blank in 'DEVELOPER_KEY' = " " in SI507project_tools.py file with your own key)

1. Download or clone project files
2. Install all requirements with `pip install -r requirements.txt`
3. Run `python SI507project_tools.py

## How to use  

1. Access to  http://localhost:5000 on your browser
2. Navigate functions that you want to use on main page.

## Routes in this application   

- '/' : Main index page - It provides with welcome message and functions that links to search for several functions
- '/result' - shows the top 12 most popular video. 
- '/reaction' - displays view counts, like counts, and dislike count information of top trending videos.
- 'channel' - gives channels that created today's top trending videos.


## How to run tests
1. Run `python SI507project_tests.py in your command prompt. 
2. Check testing results on the prompt.

## In this repository:
- requirement.txt
- README.md
- SI507project_tests.py	
- SI507project_tools.py	
- templates
  -- welcome.html
  -- result.html
  -- channel.html
  -- reaction.html
  -- country.html
- youtube_popular_videos.db
- SI507finalproject_cached_data
- youtube_diagram.pdf
- screenshots
- Final_proposal.md

---

## Code Requirements for GradingPlease check the requirements you have accomplished in your code as demonstrated.
-  [x] This is a completed requirement.
-  [ ] This is an incomplete requirement.

### General
-  [x] Project is submitted as a Github repository
-  [x] Project includes a working Flask application that runs locally on a computer
-  [x] Project includes at least 1 test suite file with reasonable tests in it.
-  [x] Includes a `requirements.txt` file containing all required modules to run program
-  [x] Includes a clear and readable README.md that follows this template
-  [x] Includes a sample .sqlite/.db file
-  [x] Includes a diagram of your database schema
-  [x] Includes EVERY file needed in order to run the project
-  [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
-  [x] Includes at least 3 different routes
-  [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
-  [x] Interactions with a database that has at least 2 tables
-  [x] At least 1 relationship between 2 tables in database
-  [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
-  [x] Use of a new module
-  [x] Use of a second new module
-  [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
-  [ ] A many-to-many relationship in your database structure
-  [x] At least one form in your Flask application
-  [x] Templating in your Flask application
-  [x] Inclusion of JavaScript files in the application
-  [x] Links in the views of Flask application page/s
-  [ ] Relevant use of `itertools` and/or `collections`
-  [ ] Sourcing of data using web scraping
-  [x] Sourcing of data using web REST API requests
-  [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
-  [x] Caching of data you continually retrieve from the internet in some way

### Submission
-  [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
-  [x] I included a summary of my project and how I thought it went **in my Canvas submission**!


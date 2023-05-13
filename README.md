# Chinese Art Collections 
Final Project for EAS 143B

## Demo
To view a demo of the running app on the local host, please visit https://harvard.zoom.us/rec/share/wQPMCheYGh1Ea4v1bM21Ot6rruHk1w9rb9xcQPm3_39u2z5ZO9-DGHEBfkIYk6I.sH1BtdSemCurJ92v

## To run this application:

```
flask --debug run
```

# Architecture

|___README.md\
|___app.py\
|___requirements.txt\
|___collections\
|___collections.db\
|___static\
|___templates\
|   |___about.html\
|   |___art.html\
|   |___collections.html\
|   |___data.html\
|   |___error.html\
|   |___index.html\
|   |___layout.html\
\

## App.py
This file contains the Flask code for generating the app
## requirements.txt
Requirements needed to run the app.
## Collections folder
The collections folder is originally from the repo https://github.com/huiwenxchen/EAS-project. Using open access API and web scraping methods, I created a dataset of 8000+ open access Chinese art from three museums--The MET, Smithsonian National Museum of Asian Art/Freer Gallery of Art, and Cleveland Art Museum. These datasets are stored in csv files. I also ran Python data processing on the collected data for the purpose of this app.
## collections.db
This Sqlite3 database stores all csv results from the open access API and scraping.
## static
Contains the static images used on the web app and the css file.
## templates
layout.html is the base html file. All other html files in this folder are extensions of layout used to generated different pages of the app.




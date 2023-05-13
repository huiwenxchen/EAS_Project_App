# Chinese Art Collections 

Final Project for EAS 143B

To run this application:

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




# Chinese Art Collections 

Final Project for EAS 143B

To run this application:

```
flask --debug run
```

# Architecture

|___README.md\
|___app.py\
|___collections.db\
|___requirements.txt\
|___templates\
|   |___about.html\
|   |___art.html\
|   |___collections.html\
|   |___data.html\
|   |___error.html\
|   |___index.html\
|   |___layout.html\
|\
|\
|___static\
|\
|___collections\

## App.py
This file contains the Flask code for generating the app
## Collections folder
The collections folder is originally from the repo https://github.com/huiwenxchen/EAS-project. Using open access API and web scraping methods, I created a dataset of 8000+ open access Chinese art from three museums--The MET, Smithsonian National Museum of Asian Art/Freer Gallery of Art, and Cleveland Art Museum. These datasets are stored in csv files. I also ran Python data processing on the collected data for the purpose of this app.
## collections.db
This Sqlite3 database stores all csv results from the open access API and scraping.
## collections.db




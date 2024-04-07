# Patchuolink
<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="hub/apps/static/assets/img/brand/patchoulink.png" alt="Logo" width="437" height="322">
  </a>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project
<br />
<div align="center">
    <img src="hub/hub visualizer/website_dashboard_1.png" alt="Logo" width="756" height="473">
  </a>
</div>

To sustainably enhance patchouli oil production and farmer revenue in Indonesia, we introduce Patchoulink—an advanced IoT system for real-time cultivation monitoring. Our prototype focuses on data flow through wireless communication, data management, storage, and analysis, with a user-friendly website interface.

Utilizing wireless communication, nodes in the field transmit data in real time. The data journey begins with capturing analog signals from the sensor, packaging the data with communication protocols, and converting it into digital signals for transmission. Once received, the data is decoded and stored in a structured backend database, which records node configurations,  

The heart of Patchoulink lies in its ability to analyze and present this data in a website interface. Here, farmers gain actionable insights, visualized with clarity and precision. Defined thresholds alert users to optimal growing conditions, ensuring informed decision-making. Further enhancing usability, Patchoulink features an OpenAI chatbot for immediate support, simplifying the translation of complex data into actionable farming strategies.

Patchoulink is more than a technological advancement for Indonesian patchouli farming—it's a sustainable, intelligent revolution, empowering farmers with instant insights for informed decision-making.

## Getting Started
Node - Arduino Hardware
1. Install the right version of Arduino.io
2. Set up hardware
3. Upload the right code

Hub - Django Software
1. set up virtual environment (in terminal)
```
$ cd hub                              # go to the right directory
$ virtualenv env                      # create virtual environment
$ source env/bin/activate             # activate the virtual environment
```

2. set up MySQL server

3. set up database in MySQL workbench

4. set up the connections with the database in core/settings.py

5. create tables (in terminal)
```
$ python manage.py makemigrations     # create table 
$ python manage.py migrate            # migrate table
```

6. run the server
```
$ python manage.py runserver          # default port 8000
$ # Access the web app in browser: http://127.0.0.1:8000/
```


## Built With
** Node **
* Arduino
* RF module
* GPS module
* capacitor
* C++
* Arduino Library - timer
* Arduino Library - interrput.h

** Hub **
* Python Django
* MySQL
* html
* css
* Javascript
* python


## Code-base structure
```bash
< PROJECT ROOT >
  |-- node/
  |   |-- integrated_TX.ino                     # final TX code
  |   |-- integrated_RX.ino                     # final RX code 
  |   |-- <other files>                         # past versions
  |
  |
  |-- hub/
  |    |-- hub visualizer/                      # website interface final screenshots
  |    |-- mysql_database/                      # integration and database file
  |    |    |-- hubdemo.sql                     # creating the database
  |    |    |    |-- home_chatgptbot            # record the conversation with openai api chatbot
  |    |    |    |-- history_update             # record the update history for each round for all the nodes
  |    |    |    |-- node_info                  # record the node related information, like geographical 
  |    |    |-- loading_ver3.py                 # convert the serial monitor data in arduino to SQL database, with simple cleaning and query within
  |    |
  |    |-- core/                                # control the website in a whole serve as the high level controller
  |    |    |-- settings.py                     # contain all settings to connect with local database and basic settings for django webframe
  |    |    |-- urls.py                         # Define URLs served by all apps/nodes
  |    |
  |    |-- apps/                                # control all the functions embedded in the website
  |    |    |-- authentication/                 # control the function of for authentication, template default
  |    |    |
  |    |    |-- home/
  |    |    |   |-- models.py                   # contain all the data format converting from SQL database directly
  |    |    |   |-- urls.py                     # directly links for loading into different html template
  |    |    |   |-- views.py                    # the controller of all core pages, sending request, data query information, connecting with external api, and pagkage all information to each html template
  |    |    | 
  |    |    |-- static/
  |    |    |   |-- assets/
  |    |    |   |   |-- css/                    # contains all configurations for each page (shape, color, size...)
  |    |    |   |   |-- fonts/                  # special fonts information
  |    |    |   |   |-- js/                     # javascript static files
  |    |    |   |   |-- img/                    # image static files
  |    |    |   |   |
  |    |    |-- templates/
  |    |    |   |-- accounts/                   # the login and register page, default setting by the template
  |    |    |   |-- data_query/
  |    |    |   |   |-- each_update_full.html   # update_history raw data page
  |    |    |   |   |-- node_1.html             # information table specifically with node one
  |    |    |   |   |-- node_2.html             # information table specifically with node two
  |    |    |   |   |-- node_3.html             # information table specifically with node three
  |    |    |   |   |-- node_information.html   # node_information raw data page
  |    |    |   |   |-- node1analysis-li.html   # node one data analysis light intensity graph
  |    |    |   |   |-- node1analysis-m.html    # node one data analysis moisture graph
  |    |    |   |   |-- node1analysis-ph.html   # node one data analysis ph graph
  |    |    |   |   |-- node1analysis-temp.html # node one data analysis temperature graph
  |    |    |   |
  |    |    |   |-- home/
  |    |    |   |   |-- chatbot.html            # the chatbot page that supports instant communication
  |    |    |   |   |-- dashboard.html          # dashboard page contain all general performance
  |    |    |   |   |-- dashboardli.html        # dashboard page with light intensity graph
  |    |    |   |   |-- dashboardmoisture.html  # dashboard page with moisture graph
  |    |    |   |   |-- dashboardph.html        # dashboard page with ph graph
  |    |    |   |   |-- map.html                # map page showing the geographical position of each node
  |    |    |   |   |-- rawdata.html            # raw datapage that can link to different raw data
  |    |    |   |   |-- page-403.html           # if connection issue for 403 error page, default template setting
  |    |    |   |   |-- page-404.html           # if template loading issue for 404 error page, default template setting
  |    |    |   |   |-- page-500.html           # if other issue for 500 error page, default template setting
  |    |    |   |
  |    |    |   |-- includes/
  |    |    |   |   |-- sidenav.html            # sidebar structure and configuration there
  |    |    |   |
  |    |    |   |-- layout/
  |    |    |   |   |-- base.html               # base structure of each page, default template
  |
```

## Original Design Document
**Design Dossier 1.0**: [https://thunder-croissant-5df.notion.site/Praxis-III-04c66cfbf70f4f8fb3bc3ce591197d76](https://thunder-croissant-5df.notion.site/Praxis-III-04c66cfbf70f4f8fb3bc3ce591197d76)\\

**Design Dossier 2.0**: [https://drive.google.com/drive/folders/18xV06bwRk_xcrWZuJ-arpAHzBY_tWKWn?usp=sharing](https://drive.google.com/drive/folders/18xV06bwRk_xcrWZuJ-arpAHzBY_tWKWn?usp=sharing)

## Contacts
**Contact with the team**: [https://thunder-croissant-5df.notion.site/Team-Identity-66c85381681543b98f773d2f37996de5](https://thunder-croissant-5df.notion.site/Team-Identity-66c85381681543b98f773d2f37996de5)

## Acknowledgments
* using creative-tim Argon Django Template: [https://www.creative-tim.com/product/argon-dashboard-django](https://www.creative-tim.com/product/argon-dashboard-django)




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

There are many great README templates available on GitHub; however, I didn't find one that really suited my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!

Use the `BLANK_README.md` to get started.


## Node

## Hub


## Built With

## Code-base structure
```bash
< PROJECT ROOT >
  |-- hub/
  |    |-- hub visualizer/                      # website interface final screenshots
  |    |-- mysql_database/                      # integration and database file
  |    |    |-- hubdemo.sql                     # creating the database
  |    |    |    |-- home_chatgptbot            # record the conversation with openai api chatbot
  |    |    |    |-- history_update             # record the update history for each round for all the nodes
  |    |    |    |-- node_info                  # record the node related information, like geographical location and last update time...
  |    |    |
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
  |    |    |   |-- home/
  |    |    |   |   |-- node1analysis-temp.html # node one data analysis temperature graph
  |    |    |   |-- includes/
  |    |    |   |-- layout/
  |
  |
  |
  |
  |
```

## Original Design Document




## Contact


## Acknowledgments
Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!



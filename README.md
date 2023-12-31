﻿# BostonHacks_Project_2023
## By Yonish, Bogdan and Connor

### BostonHacks Project
### Digital Dreamers Track
### Uses Open AI API, Streamlit, Mongo DB, and Python


```
  ____                    _   ____    _             _            _     
 / ___|    ___    _   _  | | / ___|  | | __   ___  | |_    ___  | |__  
 \___ \   / _ \  | | | | | | \___ \  | |/ /  / _ \ | __|  / __| | '_ \ 
  ___) | | (_) | | |_| | | |  ___) | |   <  |  __/ | |_  | (__  | | | |
 |____/   \___/   \__,_| |_| |____/  |_|\_\  \___|  \__|  \___| |_| |_|

```
### Idea and Concept
SoulSketch is a webapp designed to show you an illustration of your soul. It uses a DALL-E API to generate an image.
The color palette of the image is based on specific percentages obtained from your emotional history. It allows the 
user to select from a series of different colors, which then reveals the emotion associated and any advice associated
with it. The user is also able to see a graph of their entire emotional history, seeing how they were feeling on those 
days. 

## Implementation
There were three main parts, which one group member respectively completed.
### Open AI API
First was the Open AI API, which Yonish worked
on, as they have a DALL-E API key. They also created prompt generator logic which is fed the user's color history.
Example Prompt:
<User-input> + With an exact color palette of 65% blue, 9% red, 11% purple, 5% green, 5% orange, and 5% grey.
### Streamlit Webapp
The second part of the project was the front-end web app, which Connor developed using Python and Streamlit. It features
a graph generator based on the color history and a persisting color list using session states. The code is quite ugly.
### MongoDB Databse
The final part of the project was the MongoDB database, as even with Streamlit's persisting data cache, if the user exits
or refreshes the page, all is lost. Bodgan was the primary developer of the MongoDB database, which uses the username as a
key, and pulls out the user's emotional history. 

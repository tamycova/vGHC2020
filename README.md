# vGHC2020

Grace Hopper Celebration is the world's largest gathering of women technologists. It is produced by AnitaB.org and presented in partnership with ACM. GHC 20 will be held at the end of September 2020.

This repo contains the scraped data of the agenda of GHC, the original agenda can be found [here](https://web.cvent.com/event/84f26b13-25ef-458c-9d38-38432d71be09/websitePage:645d57e4-75eb-4769-b2c0-f201a0bfc6ce). The agenda can be visualized in [this](https://bit.ly/2EtBTrZ) spreadsheet. 

**raw_data** contains two json with speaker and event data. Speakers and event keys are sequentially assigned and do not represent anything other than an unique identifier for the speaker/event.

**speakers.json**
- firstName
- lastName 
- company 
- biography
- title

**events.json**
- date (start_date, end_date, start_PT, end_PT, start_ET, end_ET) -> dictionary with the start and end days, and start and end times in PT and in ET
- categories
- speakerIds -> list of keys for speakers.json 
- description
- name 
- type

Addionally **generate_csv.py** is an example script to show how the raw data can be used, it turns the data into csv files that are later ingested in google spreadsheet for an easier [visualization](https://bit.ly/2EtBTrZ) to facilitate personal planning before and during the conference.

**PLEASE LET ME KNOW IF YOU FIND ANY ERRORS IN THE DATA - FEEL FREE TO OPEN AN ISSUE**



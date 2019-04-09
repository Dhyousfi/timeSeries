# IDF challenges 2019
Material for the SNCF challenge

Clone this repo and make changes as desired. Keep the structure of the starting kit. 
The directory FILES contains additional useful files that will be needed when uploading the challenge to Codalab.

Information to create/modify a starting kit: How_to_create_a_Starting_Kit.docx

Usage to create a Codalab competition bundle:

	`cd starting_kit/utilities`
	
	`python make_bundle.py`

There are 2 ways of running the script: 
+ with sample data found in the starting kit or 
+ with the real "big" dataset. In this case run:

	`python make_bundle.py starting_kit_dir big_data_dir`
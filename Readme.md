# NRS_DV360
NRS DV360
1. This Module fetches the Dv360 reports from gmail and push the parsed data to S3 for further processing.
2. We recieve below level of report
    1. Standard (daily)
2. Here we have imported get_email_attachment module for gmail login and to pull the report from the mail attachment.
3. The downloaded report will be parsed to get required fields data.
4. We then writes the data to .csv file and push the gzipped file to S3


Prerequisite:
Python - 3.10.8+

you need to create venv

`python3 -m venv {ENVIRONMENT NAME}`

Activate environment

`source {ENVIRONMENT NAME}/bin/activate`


# Create "requirements.txt" for each project before committing to code.

`pip install pipreqs`


`pipreqs {PROJECTPATH}` - which you need to execute everytime when you add any new packages.

`pipreqs --force {PROJECTPATH}`

Install dependencies
`pip install -r requirements.txt`



# CSV loader - practical tasks
`Helps to load CSV file from some URL and provide ability to parse data in some format`

##Original task description:

Create a program that fetches data from a csv file hosted on google drive and returns it to the user.
The URL for the file is: test_task_data.csv
https://drive.google.com/file/d/1zLdEcpzCp357s3Rse112Lch9EMUWzMLE/view

Requirements:

- It should be possible to run the program like ./run.py --fields data,campaign,clicks
- It should return the specified fields.
- It should return the data in JSON format in a "data" envelope.
- If the data in the file is updated it should always get the new data
- The code should be linted and have at least one test.
- Think about a few error cases.

## Environment:
Python 3.9.0

## How to start
- create venv: python -m venv venv 
- activate virtual env: ./venv/Scripts/activate
- install all dependencies: python -m pip install -r ./requirements.txt

## How to Run the tool
`python parser.py --csv-fields date,campaign,fields`

`python parser.py --csv-fields date,campaign,fields --csv-path your_csv_file.csv`

`python parser.py --csv-fields date,campaign,fields --csv-url https://google_drive_file_url`


## How to run tests
`python -m pytest`


`Author: Aliaksandr Bahdanovich  (bogdanovich.alex@gmail.com)`

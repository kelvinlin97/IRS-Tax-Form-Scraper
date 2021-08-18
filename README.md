# Pinwheel

Two Python utility tools built as a part of Pinwheel's coding challenge. The first utility tool takes in input from the command line on the specified tax form name e.g. Form W-2, Form 1095-C and returns json data on the form number, form title, minimum year, and maximum year. The second utility tool takes in a tax form name and a range of years and downloads all of the PDF files in a subdirectory.

# Usage

Our tool allows you to easily search for information regarding past IRS forms.

Follow along with the command line prompts to specify the form names you're searching for (space delimited)!

![Enter form names](https://i.imgur.com/73gb3RL.png)

Once you've entered the form names you're searching for, check the JSON data to see if it's correct. If it looks right, enter "y" and the JSON data will be downloaded in your main directory as "data.json".

![Show form data](https://i.imgur.com/gQtARbg.png)

# Setup

1. Fork and clone this repo.
2. Install dependencies: pip install -r requirements.txt
3. Run "python app.py" in your terminal
4. Follow our command line guiding :)!

# Technologies

Python Version: 3.9.5

Note: Refer to requirements.txt for a full list of dependencies used for this project.

[MIT License](https://github.com/kelvinlin97)

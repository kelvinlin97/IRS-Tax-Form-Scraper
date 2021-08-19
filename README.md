# IRS Tax Forms Scraper

Two Python utility tools built to make it easier to find and download tax forms. The first utility tool takes in input from the command line on the specified tax form name(s) e.g. Form W-2, Form 1095-C and returns json data on the form number, form title, minimum year, and maximum year. The second utility tool takes in a tax form name and a range of years and downloads all of the PDF files in a subdirectory.

# Usage

Our utility tools allows you to easily search for information regarding past IRS forms.

Follow along with the command line prompts!

## Utility 1 Instructions

Enter the form names you're requesting (e.g. "W-2 W-3 1095-C"), space delimited!

![Enter form names](https://i.imgur.com/73gb3RL.png)

Once you've entered the form names you're searching for, check the JSON data to see if the output is what is expected. If it looks right, enter "y" and the JSON data will be downloaded in your main directory as "data.json".

![Show form data](https://i.imgur.com/gQtARbg.png)

## Utility 2 Instructions

Enter the form name you want to download. Specify a range (note: ending year is the most recent year).

![Enter form name](https://i.imgur.com/QMUeqPH.png)

Your files will be downloaded in a subdirectory!

![Subdirectory files](https://i.imgur.com/YigHHrv.png)

# Setup

1. Fork and clone this repo.
2. Install dependencies: pip install -r requirements.txt
3. Choose from one of two scripts that contain our two different utilities.
4. Use "python app.py" to run utility 1 which generates JSON form data or use "python get_pdf.py" to run utility 2 which downloads pdf files into a subdirectory on a specified year range.
4. Follow our command line guiding :)!

# Technologies

Python Version: 3.9.5

Note: Refer to requirements.txt for a full list of dependencies used for this project.

[MIT License](https://github.com/kelvinlin97)

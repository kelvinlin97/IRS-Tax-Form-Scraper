import requests
from bs4 import BeautifulSoup
import json
import logging
import argparse

user_input = input("Enter tax form number (e.g. 1095-C, W-2). If entering multiple forms, please separate each form number by space: ").split(' ')

def get_JSON(data, name):
  max_year = 0
  min_year = 2021
  for column in data:
    if len(column) > 0:
      form_name = column[0]
      form_title = column[1]
      form_year = int(column[2])
      if form_name == name:
        max_year = max(max_year, form_year)
        min_year = min(min_year, form_year)
  if max_year == 0:
    logging.error('{name} not found did you enter the correct form name?'.format(name=name))
  json_data = {"form_number": name, "form_title": form_title, "min_year": min_year, "max_year": max_year}
  return json_data

def parse_text(text):
  parsedText = text.replace('\n', '')
  parsedText = text.replace('\t', '')
  parsedText = text.strip()
  return parsedText

def getFormInfo(user_input):
  url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value=form+{name}&isDescending=false'.format(name=user_input)
  html = requests.get(url)
  soup = BeautifulSoup(html.content, "html.parser")
  form_number = "Form {name}".format(name=user_input)
  form_table = soup.find('table', {"class": "picklist-dataTable"})
  rows = form_table.findChildren(['tr'])
  form_data = []
  json_data = []
  for row in rows:
    cells = row.findChildren('td')
    row_data = []
    for cell in cells:
      value = parse_text(cell.get_text())
      row_data.append(value)
    form_data.append(row_data)
  return get_JSON(form_data, form_number)

def compileUserJSON(input):
  if input[0] == '' or input is None:
    logging.error('Error, input is empty')
  user_requested_json = []
  for name in input:
    user_requested_json.append(getFormInfo(name))
  return user_requested_json

data = compileUserJSON(user_input)

print(data)

download_input = input("Download data? (y/n) ")

def downloadData(download_input, data):
  if download_input == 'y':
    # Saves json data into data.json file in main directory
    with open('data.json', 'w', encoding='utf-8') as f:
      json.dump(data, f, ensure_ascii=False, indent=4)
  elif download_input == 'n':
    return
  else:
    logging.error('Please select either y or n')

downloadData(download_input, data)


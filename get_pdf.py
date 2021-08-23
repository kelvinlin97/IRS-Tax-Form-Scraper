import requests
from bs4 import BeautifulSoup
import urllib.request
import os

form_numbers = input("Enter tax form number (e.g. 1095-C, W-2): ")
form_start_years = int(input("Enter starting year for requested forms: "))
form_end_years = int(input("Enter ending year for requested forms (enter same year as starting year if only single year requested): "))

def download_forms(name, forms, start, end):
  dir_name = name
  form_dict_by_year = {}
  for form in forms:
    if len(form) > 0:
      form_name = form[0]
      form_link = form[1]
      form_year = form[3]
      if form_name == name:
        if start == end and int(form_year) == start:
          form_dict_by_year[form_year] = form_link
        else:
          if int(form_year) <= end and int(form_year) >= start:
            form_dict_by_year[form_year] = form_link
  os.mkdir(dir_name)
  for year in form_dict_by_year:
    response = urllib.request.urlopen(form_dict_by_year[year])
    file = open("{name}/{name} - {year}.pdf".format(name=dir_name, year=year), 'wb')
    file.write(response.read())
    file.close()
    print("Downloaded {name} {year}!".format(name=dir_name, year=year))

def get_forms(number, start, end):
  url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value=form+{name}&isDescending=false'.format(name=number)
  html = requests.get(url)
  soup = BeautifulSoup(html.content, "html.parser")
  form_number = "Form {name}".format(name=number)
  form_table = soup.find('table', {"class": "picklist-dataTable"})
  rows = form_table.findChildren(['tr'])
  form_data = []
  for row in rows:
    cells = row.findChildren('td')
    row_data = []
    for cell in cells:
      value = cell.get_text()
      value = value.replace('\n', '')
      value = value.replace('\t', '')
      value = value.strip()
      a_ref = cell.find_all('a', href=True)
      row_data.append(value)
      if(len(a_ref) > 0):
        row_data.append(a_ref[0]['href'])
    form_data.append(row_data)
  download_forms(form_number, form_data, start, end)

get_forms(form_numbers, form_start_years, form_end_years)

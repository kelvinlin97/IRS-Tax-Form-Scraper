userInput = input("Enter tax form number (e.g. 1095-C, W-2). If entering multiple forms, please separate each form number by space: ").split(' ')

def getFormInfo(userInput):
  url = 'https://apps.irs.gov/app/picklist/list/priorFormPublication.html?resultsPerPage=200&sortColumn=sortOrder&indexOfFirstRow=0&criteria=formNumber&value=form+{name}&isDescending=false'.format(name=userInput)
  print(url)

for name in userInput:
  getFormInfo(name)

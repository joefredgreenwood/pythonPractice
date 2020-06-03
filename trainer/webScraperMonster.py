import requests
from bs4 import BeautifulSoup
import xlsxwriter

workbook = xlsxwriter.Workbook('softwareJobs.xlsx')
worksheet = workbook.add_worksheet('jobs1')
bold = workbook.add_format({'bold': True})
worksheet.set_column('B:B',30)
worksheet.set_column('A:A',30)
worksheet.set_column('C:C',30)


row = 1
column = 0



URL = 'https://www.monster.co.uk/jobs/search/?q=Software-Developer&where=Leeds__2C-Yorkshire'
page = requests.get(URL)

#beautifulsoup gets all the html content from a page
soup = BeautifulSoup(page.content, 'html.parser')
#searchresults is the div that everything else is stored in
results = soup.find(id='SearchResults')
# print(results.prettify())

worksheet.write(0,0,'Job Title', bold)
worksheet.write(0,1,'Company', bold)
worksheet.write(0,2,'Location', bold)

#card-content basically shows each listing
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title') #This will fetch the title
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
#     linka = job_elem.find('a')['href']
    if None in (title_elem, company_elem, location_elem): #In case one of the listing doesn't have a value or is an advert
        continue
    print(title_elem.text.strip()) #The .text gets just the text not the html and the .strip gets rid of whitespace
    print(company_elem.text.strip())
    print(location_elem.text.strip())
#     print(linka)
    print() #Adds a line inbetween
    worksheet.write(row, column, title_elem.text) 
    worksheet.write(row, column + 1, company_elem.text) 
    worksheet.write(row, column + 2, location_elem.text) 
#     worksheet.write(row, column + 3, linka)
    row += 1
#Finds any h2 which contains the string    
workbook.close()
python_jobs = results.find_all('h2',
                               string=lambda text: 'java' in text.lower())
print(len(python_jobs))
for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")
    



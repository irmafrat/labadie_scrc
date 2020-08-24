import requests
from bs4 import BeautifulSoup

#TODO
#FOR LOOPS EXTRACTING ALL WEBSITE DATA (SUBJECT HEADINGS AND QUANTITY OF FOLDERS)
#STRIP FOLDER QUANTITY FROM SUBJECT HEADING
#METADATA CROSSWALK TO EAD/MODS
#DIVIDE COLLECTIONS FROM EPHEMERA MATERIALS
#XML OUTPUT
#TEST EAD/MODS IMPORT TO ARCHIVESSPACE


#TEST
url = "https://apps.lib.umich.edu/labadie-collection/subject-vertical-files/complete-listing"
response= requests.get(url)
html_soup= BeautifulSoup(response.text, 'html.parser')
data = html_soup.find('td',class_= "views-field views-field-title")



print(type(html_soup))
print(response)
# print(html_soup)
print(f"subject headings: {data.text.strip()}")

# html class "views-field views-field-title"

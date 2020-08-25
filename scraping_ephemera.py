import requests
from bs4 import BeautifulSoup
from cache.irmacache import Cache

cache_filename = "subject_headings.json"
cache = Cache(cache_filename)

#TODO
# DONE: FOR LOOPS EXTRACTING ALL WEBSITE DATA (SUBJECT HEADINGS AND QUANTITY OF FOLDERS)
#STRIP FOLDER QUANTITY FROM SUBJECT HEADING
#METADATA CROSSWALK TO EAD/MODS
#DIVIDE COLLECTIONS FROM EPHEMERA MATERIALS
#XML OUTPUT
#TEST EAD/MODS IMPORT TO ARCHIVESSPACE

data_storage= []
url = "https://apps.lib.umich.edu/labadie-collection/subject-vertical-files/complete-listing"
idx = 0
param = {"page":idx}
response= cache.get(url,param)


# Extracting the subject headings from the Labadie Subject Vertical File from the website and the quantity 
# of folders for each subject heading 
while not "<strong>Sorry</strong>" in response:
    html_soup = BeautifulSoup(response,'html.parser')
    data = html_soup.find_all('td',class_= "views-field views-field-title")
    for subject_heading in data:
        data_storage.append(subject_heading.text.strip())
    idx += 1
    print(f"Finished: {idx}")
    param.update({'page': idx})
    response = cache.get(url,param)

# print(f"subject headings: {data_storage}")
# print(f"{len(data_storage)} subject headings founded")

for folder_quantity in data_storage:
    if "folder(s)" in folder_quantity:
        split_subject_heading = folder_quantity.split(' - ')
        quantity = split_subject_heading[-1]
        clean_subject_heading = " - ".join(split_subject_heading[:-1])
        print(f"{clean_subject_heading} has {quantity}")


# EXTRACTING COLLECTIONS MATERIALS FROM EPHEMERA

collection_headings = ["Anarchism",
"Civil Liberties",
"Colonialism and Imperialism",
"Communism",
"Co-operatives",
"Ecology",
"Labor",
"Pacifism",
"Prisons and Prisoners",
"Radical Right",
"Religion",
"Sexual Freedom",
"Socialism",
"Underground Press",
"Women",
"Youth and Student Protest",
"Animal Liberation",
"Conservatism",
"Education",
"Housing",
"Internationalism",
"Libertarianism",
"Media"]

for subject_heading in data_storage:
    strip_sh= subject_heading.split(" - ")
    if collection_headings in strip_sh:
        print(strip_sh)

    

import requests
from bs4 import BeautifulSoup
from cache.irmacache import Cache

cache_filename = "subject_headings.json"
cache = Cache(cache_filename)

#TODO
# DONE: FOR LOOPS EXTRACTING ALL WEBSITE DATA (SUBJECT HEADINGS AND QUANTITY OF FOLDERS)
# DONE: STRIP FOLDER QUANTITY FROM SUBJECT HEADING
# DONE: DIVIDE COLLECTIONS FROM EPHEMERA MATERIALS
#METADATA CROSSWALK TO EAD/MODS
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

#TEST
# print(f"subject headings: {data_storage}")
# print(f"{len(data_storage)} subject headings founded")

# STRIP FOLDER QUANTITY FROM SUBJECT HEADING

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
"Media",
"Spain",
"Argentina",
"Art",
"Birth Control",
"Boycotts",
"Capitalism",
"Counterculture",
"Euthanasia",
"Farmers",
"Fascism",   
"Films",
"G.I. Protest",
"Globalism",
"Health",
"Immigration",
"Iran",
"Marijuana",
"Michigan",
"Militarism",
"Monetary Reform",
"Narcotics",
"New Left",
"Peace Corps",
"Racism",
"Refugees",
"Technology",
"Theater",
"Vietnam war",
"Single Tax"]

potential_collections_items= []
potential_ephemera_collection= []
for subject_heading in data_storage:
    missing=True
    for heading in collection_headings:
        if heading in subject_heading:
            potential_collections_items.append(subject_heading)
            missing=False
            break
    if missing:
        potential_ephemera_collection.append(subject_heading)
    

#TEST
print(f"Potential Collections Items Quantity: {len(potential_collections_items)}")
print(f"Potential Ephemera Items Quantity: {len(potential_ephemera_collection)}")
print(f"Collection Quantity: {len(data_storage)}")

# WRITTING FILES WITH LIST OF POTENTIAL COLLECTIONS ITEMS AND POTENTIAL EPHEMERA COLLECTION ITEMS

f = open("potential_collections.txt", "w")
for item in potential_collections_items:
    f.write(f"{item}\n")
f.close()

f = open("potential_ephemera.txt", "w")
for item in potential_ephemera_collection:
    f.write(f"{item}\n")
f.close()
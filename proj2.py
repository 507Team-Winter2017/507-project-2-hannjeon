#proj2.py
import requests
from bs4 import BeautifulSoup

base_url='http://www.nytimes.com'
r=requests.get(base_url)
soup=BeautifulSoup(r.text, 'html.parser')

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here
headline=[]
for story_heading in soup.find_all(class_="story-heading"):
	if story_heading.a:
		headline.append(story_heading.a.text.replace("\n", " ").strip())
	else:
		headline.append(story_heading.contents[0].replace("\n", " ").strip())

for i in headline[:10]:
	print (i)

# else: 
#         print(story_heading.contents[0].replace("\n", " ").strip())

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
base_url_two='http://www.michigandaily.com'
r_two=requests.get(base_url_two)
soup_two=BeautifulSoup(r_two.text, 'html.parser')

section_div = soup_two.find(class_='pane-mostread')

for item in section_div.find_all('a'):
	print(item.get_text())

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
base_url_three='http://newmantaylor.com/gallery.html'
r_three=requests.get(base_url_three)
soup_three=BeautifulSoup(r_three.text, 'html.parser')

for img in soup_three.find_all('img'):
	alt= 'No alternative text provided!'
	if (img.has_attr('alt')):
		alt=img['alt']
	print(alt)

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")
### Your Problem 4 solution goes here
urls=[]
num=0

for i in range(6):
	base_url_four='https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4&page='+str(i)
	r_four=requests.get(base_url_four, headers={'User-Agent': 'SI_CLASS'})
	soup_four=BeautifulSoup(r_four.text, 'html.parser')

	section_div_four = soup_four.find_all(class_='field-name-contact-details')
	for item in section_div_four:
		if item.a:
			urls.append(item.a['href'])


def print_email(add):
	base_url_five='https://www.si.umich.edu'+add
	r_five=requests.get(base_url_five, headers={'User-Agent': 'SI_CLASS'})
	soup_five=BeautifulSoup(r_five.text, 'html.parser')

	section_div_five = soup_five.find(class_='field-type-email')
	for item in section_div_five:
		if item.a:
			return (item.a.text)


for url in urls:
	num+=1
	print (num, print_email(url))
	



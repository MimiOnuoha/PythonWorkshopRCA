from bs4 import BeautifulSoup
import requests, csv

result = requests.get("http://www.gawker.com/")

c = result.content

soup = BeautifulSoup(c)
links = []
for link in soup.find_all("a"):
	links.append(link.get('href'))


print len(links)
print links


with open ("all_links.csv", "wb") as file:
	writer = csv.writer(file)
	for link in links:
		writer.writerow([link])
import csv
import requests
from BeautifulSoup import BeautifulSoup

with open('ddr3.csv', 'rb') as f:
    reader = csv.reader(f)
    master = list(reader)

holder = []
for row in master:
	url = 'http://ddr.com/properties/' + str(row[0])
	response = requests.get(url)
	html = response.content

	soup = BeautifulSoup(html)
	table = soup.findAll('div', attrs={'class': 'contact-item internal col-xs-12 col-sm-6'})
	info = []


	for i in table:
		if "Property Manager" in i.h4:
			n = i.find('p', attrs={'class': 'visible-xs'})
			info.append(n.text)


	row.append(info)
	holder.append(row)

outfile = open("./ddrPMs.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(holder)

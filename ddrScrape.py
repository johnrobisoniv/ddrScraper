import csv
import requests
from BeautifulSoup import BeautifulSoup

pg = 1
data = []

while pg < 16:

	url = 'http://ddr.com/properties/search?page=' + str(pg) +'&q%5Bstate%5D=&q%5Bzip%5D=&q%5Bname%5D=&q%5Bmsa%5D=&q%5Bavailable_units%5D=&q%5Bproperty_size%5D=&q%5Bleasing_contact%5D=&q%5Bmajor_tenant%5D=&q%5Btypeahead%5D=0'
	response = requests.get(url)
	html = response.content

	soup = BeautifulSoup(html)
	table = soup.find('div', attrs={'id': 'map-list'})

	for row in table.findAll('div', attrs={'class': 'list-item clearfix'}):
		datalist = []
		datalist.append(row.get('data-property-id'))

		for d in row.findAll('a', attrs={'class': 'directions-marker visible-xs'}):
			datalist.append(d.get('data-lat'))
			datalist.append(d.get('data-lng'))
		for e in row.findAll('div', attrs={'class': 'list-location col-xs-6 col-sm-4'}):
			for f in e.findAll('a'):
				datalist.append(f.text)
			for g in e.findAll('p'):
				datalist.append(g.text)
		for h in row.findAll('div', attrs={'class': 'list-details col-xs-6 col-sm-4'}):
			for i in h.findAll('p'):
				datalist.append(i.text.replace('Project Size:', ''))
		for j in row.findAll('div', attrs={'class': 'list-details col-sm-4 tenants-list hidden-mobile'}):
			for k in j.findAll('p'):

				datalist.append(k.text.replace('Major Tenants:', '').split(', '))


		data.append(datalist)
	pg += 1
outfile = open("./ddr3.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(data)

	#for cell in row.findAll('div', attrs={'class': 'directions-marker visible-xs'}):
	#	print cell.tag.get('data-lat')


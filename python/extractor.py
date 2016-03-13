from lxml import html
import requests
import json

def remove_whitespaces(string):
    string = string.replace('\n', ' ').strip()
    while len(string) != len(string.replace('  ', ' ')):
        string = string.replace('  ', ' ')
    return string

data = {}

for year in range(1996, 2016):

    year_data = []
    data[year] = year_data

    page = requests.get('http://old.chem.uni.wroc.pl/wiadchem/wiadch{}.htm'.format(str(year)[2:]))

    # page = requests.get('http://old.chem.uni.wroc.pl/wiadchem/wiadch96.htm')
    tree = html.fromstring(page.content)

    elems = tree.xpath('/html/body/div/div[1]/ol/li/a')

    for i, elem in enumerate(elems):
        publication = {
            'title': '',
            'authors': '',
            'institute': '',
            'abstract': '',
            'ref': ''
        }
        year_data.append(publication)

        title = elem.text_content()
        title = remove_whitespaces(title)

        # print u'{year}: {number}. {title}'.format(year=year, number=i+1, title=title)
        publication['title'] = title

        if year == 1999 and i == 11:
            year_data.append({
                title: 'Notatki chaotyczne. XXII. PARADYGMAT PANGLOSA'
            })

    # print '-------------------------------------------------'

    # author
    elems = tree.xpath('//div/div/h4')

    if len(elems) != len(year_data):
        print "rok " + str(year) + ' jest zepsuty o: ' + str(len(elems) - len(year_data))
    else:
        for i, elem in enumerate(elems):
            authors = elem.text_content()
            authors = remove_whitespaces(authors)
            year_data[i]['authors'] = authors
            print authors

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

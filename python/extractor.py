from __future__ import unicode_literals
from lxml import html
import requests
import json
import re

def remove_whitespaces(string):
    string = string.replace('\n', ' ').strip()
    while len(string) != len(string.replace('  ', ' ')):
        string = string.replace('  ', ' ')
    return string

data = {}

for year in [1996]: #range(1996, 2016):

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
            'institutes': {},
            'abstract': '',
            'ref': '',
            'emails': []
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

        elif year == 2010 and i == 22:
            year_data.append({
                title: 'Cosmetic Applications of whey'
            })
        elif year == 2014 and i == 45:
            year_data.append({
                title: 'MAX RUDOLF LEMBERG (1896-1975) - AN AUSTRALIAN BIOCHEMIST OF WROCLAW ORIGIN'
            })

    if year == 2004:
        year_data.remove(year_data[31])

    # print '-------------------------------------------------'

    # institute
    # elems = tree.xpath("//div/div/p[@class='adres']")
    elems = tree.xpath("//div/div/p[contains(@class,'adres') or contains(@class,'ADRES')]")
    # elems = [remove_whitespaces(elem.text_content()) for elem in elems]

    authors_2007 = None

    if year == 1996:
        elems.insert(16, None)
        elems.insert(22, None)
    elif year == 1998:
        elems.insert(22, '')
    elif year == 2000:
        # elems[33] += ', ' + elems[34]
        elems.remove(elems[34])
    elif year == 2001:
        elems.insert(8, '')
    elif year == 2002:
        elems.insert(7, '')
    elif year == 2007:
        authors_2007 = elems[14]
        elems.remove(elems[14])
        elems.remove(elems[34])
    elif year == 2011:
        elems.insert(25, 'wpisz z autora')
    elif year == 2012:
        elems.insert(16, 'wpisz z autora')
    elif year == 2013:
        elems.insert(18, 'wpisz z autora')
    elif year == 2014:
        elems.insert(20, 'wpisz z autora')
        elems.insert(42, 'wpisz z autora')
        elems.insert(43, 'wpisz z autora')
    elif year == 2015:
        elems.insert(11, 'wpisz z autora')



    if len(elems) != len(year_data):
        print "INSTITUTE: rok " + str(year) + ' jest zepsuty o: ' + str(len(elems) - len(year_data))
    else:
        for i, elem in enumerate(elems):
            # year_data[i]['institute'] = institute

            if elem != None:
                children = [elem for elem in elem.getchildren() if elem.tag != 'br']

                if children:
                    for child in children:
                        assert child.tag == 'sup'
                        year_data[i]['institutes'][child.text] = child.tail
                else:
                    year_data[i]['institutes']['1'] = remove_whitespaces(elem.text_content())



            # match = re.findall(r'[\w\.-]+@[\w\.-]+', institute)
            # if match:
            #     year_data[i]['emails'] = match

            # print institute

    # author
    elems = tree.xpath('//div/div/h4')
    elems = [remove_whitespaces(elem.text_content()) for elem in elems]

    if year == 2000:
        elems[33] += ', ' + elems[34]
        elems.remove(elems[34])
    elif year == 2007:
        elems.insert(14, authors_2007)
    elif year == 2015:
        elems[11] = elems[11][:78]

    if len(elems) != len(year_data):
        print "AUTHORS: rok " + str(year) + ' jest zepsuty o: ' + str(len(elems) - len(year_data))
    else:
        for i, authors in enumerate(elems):
            year_data[i]['authors'] = authors
            # print authors


    # ref
    elems = tree.xpath("//div/p[@class='stopka']/text()")
    if len(elems) == 0:
        elems = tree.xpath("//div/p[@class='Stopka']/text()")
    elems = [remove_whitespaces(elem) for elem in elems if remove_whitespaces(elem) != '' and remove_whitespaces(elem) != '|']

    if year == 2001:
        elems.insert(18, '')
    elif year == 2011:
        elems.insert(27, '')
    elif year == 2014:
        elems.insert(2, '')


    if len(elems) != len(year_data):
        print "REF: rok " + str(year) + ' jest zepsuty o: ' + str(len(elems) - len(year_data))
    else:
        for i, elem in enumerate(elems):
            ref = elem
            year_data[i]['ref'] = ref
            # print ref

    # abstract
    # if year in [2002, 2003]:
    #     elems = tree.xpath("/html/body/div/div/*")
    # else:
    elems = tree.xpath("/html/body//div/*")

    abstract = None
    abstracts = []
    for elem in elems:
        if elem.tag == 'div' and elem.attrib['class'].lower() == 'abstract':
            if abstract != None:
                abstracts.append('\n'.join(abstract))

            abstract = []
        if elem.tag == 'p' and 'class' in elem.attrib and elem.attrib['class'].lower() == 'paragraf10':
            abstract.append(remove_whitespaces(elem.text_content()))

    if abstract != None:
        abstracts.append('\n'.join(abstract))

    if len(abstracts) != len(year_data):
        print "ABSTRACTS: rok " + str(year) + ' jest zepsuty o: ' + str(len(abstracts) - len(year_data))
    else:
        for i, abstract in enumerate(abstracts):
            year_data[i]['abstract'] = abstract
            # print ref


with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

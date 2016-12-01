from ListCleanTag import get_filepaths_cleantag
import csv
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global number_of_starttags
        number_of_starttags += 1

    def handle_endtag(self, tag):
        global number_of_endtags
        number_of_endtags += 1

filenames = get_filepaths_cleantag(r"C:\Users\firlyarmanda\PycharmProjects\EkstraksiBerita\PreProcesing")
index = 0
for f in filenames:
    file_html = open(str(f), "r")
    html = file_html.read()
    soup = BeautifulSoup(html.strip(), 'html.parser')
    ress = []
    for line in html.decode('utf-8').strip().split('\n'):
        link_words = 0

        line_soup = BeautifulSoup(line.strip(), 'html.parser')
        tagging = [tag.name.encode('utf-8') for tag in line_soup.find_all()]
        for link in line_soup.findAll('a'):
            link_words += len(link.text.split())
        words_count = len(line_soup.text.split()) - link_words
        number_tag_p = len(line_soup.find_all('p'))
        number_tag_br = len(line_soup.find_all('br'))
        number_tag_break = number_tag_br + number_tag_p

        number_of_starttags = 0
        number_of_endtags = 0

        parser = MyHTMLParser()
        parser.feed(line.lstrip())
        number_tag = number_of_starttags + number_of_endtags
        CTTD = 0
        if words_count + link_words == 0:
            CTTD
        else:
            CTTD = words_count + (0.5 * link_words) + number_tag - number_tag_break
        res = [line_soup,tagging, words_count, link_words, number_tag, number_tag_break, CTTD]
        ress.append(res)

    index += 1
    stored_file = "textdetection/textdetection" + '{0:03}'.format(index) + ".csv"
    firstline = ["HTML", "TAG", "TC", "LTC", "TG", "P", "CTTD"]

    filewrite = open(stored_file, "wb")
    writer = csv.writer(filewrite, lineterminator='\n')
    writer.writerow(firstline)
    for val in ress:
        writer.writerow(val)
    filewrite.close



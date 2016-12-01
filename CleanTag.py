from List import get_filepaths
from bs4 import BeautifulSoup
from bs4 import Comment

filenames = get_filepaths(r"C:\Traning")
index = 0
for f in filenames:
    file_html=open(str(f),"r")
    soup = BeautifulSoup(file_html,"html.parser")
    [x.extract() for x in soup.find_all('script')]
    [x.extract() for x in soup.find_all('style')]
    [x.extract() for x in soup.find_all('meta')]
    [x.extract() for x in soup.find_all('noscript')]
    [x.extract() for x in soup.find_all(text=lambda text:isinstance(text, Comment))]

    #print f
    index += 1
    stored_file = "PreProcesing\extracts" + '{0:03}'.format(index) + ".html"
    filewrite = open(stored_file, "w")
    filewrite.write(str(soup) + '\n')
    filewrite.close

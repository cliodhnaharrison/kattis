from bs4 import BeautifulSoup

infile = open("50W, 0.7Pa, Ar, TA, Single Probe.ldf","r")
contents = infile.read()
soup = BeautifulSoup(contents,'xml')
date = soup.find("date")


#Unicode string of the date of the scan [u'07.07.2017']
uni_date =  date.contents

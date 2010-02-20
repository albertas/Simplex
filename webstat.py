#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ši programa nurodytam puslapiui pateikia tokią statistiką:
1. Kokiu greičių parsiųstas puslapis (bps)
2. Puslapio turinio SHA1 kontrolinę sumą
3. Puslapio turinio baitų skaičių
4. Puslapio eilučių skaičių (<br> arba <p> žymių skaičius) 

Programoje realizuotas metodas getWebStat() bei clasė MyHTMLParser
"""
import sys
import time
import urllib
import hashlib
import HTMLParser

class MyHTMLParser(HTMLParser.HTMLParser):
    """ Parsinimo klasė skirta suskaičiuoti dokumento naujų eilučių žymes """
    newlines = 0
    def handle_starttag(self, tag, attrs):
        if tag in ['p', 'br']:
            self.newlines += 1

def getWebStat():
    """ Raportuok puslapio statistikas """
    if len(sys.argv) < 2:
        url = raw_input("Įveskite puslapio adresą: ")
    else:
        url = sys.argv[1]
    time_before = time.time()
    f = urllib.urlopen(url)
    time_after = time.time()
    page_content = f.read()
    f.close()
    load_speed = len(page_content) * 8 / (time_after - time_before)
    print "Puslapio parsiuntimo greitis:", load_speed, "bps"
    print "Puslapio SHA1 kontrolinė suma:"
    print hashlib.sha1(page_content).hexdigest()
    print "Puslapio baitų skaičius:", len(page_content)
    myparser = MyHTMLParser()
    myparser.feed(page_content)
    print "Puslapyje yra", myparser.newlines, "naujų eilučių"
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    getWebStat()
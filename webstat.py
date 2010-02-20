#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ši programa nurodytam puslapiui pateikia tokią statistiką:
1. Kokiu greičių parsiųstas puslapis (bps)
2. Puslapio turinio SHA1 kontrolinę sumą
3. Puslapio turinio baitų skaičių
4. Puslapio eilučių skaičių (<br> žymių skaičius) 

Realizuotos dvi funkcijos: testFunciton() bei getWebStat(url), pavyzdžiui:

>>> testFunction()
4
"""
import sys
import time
import urllib

def testFunction():
    return 4

def main():
    if len(sys.argv) < 2:
        url = raw_input("Įveskite puslapio adresą: ")
    else:
        url = sys.argv[1]
    time_before = time.time()
    f = urllib.urlopen(url)
    time_after = time.time()
    byte_count = len(f.read())
    load_speed = byte_count * 8 / (time_after - time_before)
    print "Puslapio parsiuntimo greitis:", load_speed, "bps."
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
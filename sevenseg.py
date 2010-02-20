#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ši programa pavaizduoja grafiškai įvestą skaičių. Skaičius turi būti ne 
ilgesnis kaip 10 skaitmenų.
"""

import sys

big_numbers = \
"""  ###           ###    ###           ###    ###    ###    ###    ###  
 #   #      #      #      #  #   #  #      #          #  #   #  #   # 
 #   #      #      #      #  #   #  #      #          #  #   #  #   # 
 #   #      #      #      #  #   #  #      #          #  #   #  #   # 
                ###    ###    ###    ###    ###           ###    ###  
 #   #      #  #          #      #      #  #   #      #  #   #      # 
 #   #      #  #          #      #      #  #   #      #  #   #      # 
 #   #      #  #          #      #      #  #   #      #  #   #      # 
  ###           ###    ###           ###    ###           ###    ###  """

def sevenSeg():
    """ Išspausdink pateiktą dešimtainį skaičių dideliais skaitmenim """
    if len(sys.argv) < 2:
        number = int(raw_input("Įveskite teigiamą sveikąjį skaičių: "))
    else:
        number = int(sys.argv[1])
    for i in range(9):
        line = ''
        tmp = number
        while tmp != 0:
            range_from = (tmp % 10) * 7 + i * 71
            range_to = (tmp % 10 + 1) * 7 + i * 71
            line = big_numbers[range_from:range_to] + line
            tmp /= 10
        print line

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    sevenSeg()
        
    
        
        
        
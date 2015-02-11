from __future__ import division

import re

names = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

for code in names: 
    if re.search(r"5", code): 
        print("\n" + code) 

for code in names: 
    if re.search(r"(d|e)", code): 
        print("\n" + code) 

for code in names: 
    if re.search(r"d.*e", code): 
        print("\n" + code)

for code in names: 
    if re.search(r"(d.e)", code): 
        print("\n" + code) 

for code in names: 
    if re.search(r"d.*e", code) or re.search(r"e.*d", code): 
        print("\n" + code) 

for code in names: 
    if re.search(r"^(x|y)", code): 
        print("\n" + code) 

for code in names: 
    if re.search(r"^(x|y).*e$", code): 
        print("\n" + code) 

for code in names: 
    if re.search(r"\d{3,}", code): 
        print("\n" + code) 

for code in names: 
    if re.search(r"d[arp]$", code): 
        print("\n" + code) 

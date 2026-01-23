#!/usr/bin/env python3
import ROOT
import optparse
import numpy
import os, sys
import math
from array import array
import json

tag = sys.argv[1]
scale = float(sys.argv[2])

if "V1" not in tag:
    
    inputFile = tag + "/" + tag + "_Uncertainty_AK4PFchs.txt"

    output_file = open(tag + "_Uncertainty_AK4PFchs.txt", "x")

    input_file = open(inputFile)
    for line in input_file:
        if "Uncertainty" in line:
            print(line.split("\n")[0])
            output_file.write(line)
        else: 
            items = line.split("\n")[0].split(" ")
            if items[2]!="150":
                print("Waning: no 150")
            elif len(items)%3!=1:
                print("Items in line not divisible by 3")
            else:
                new_line_list = [ ] 
                for it, item in enumerate(items):
                    if it<=2 or it%3==0:
                        new_line_list.append(item)
                    else:
                        new_unc = round(scale*float(item),4)
                        add_zero = ""
                        if round(10000*new_unc,0)%1000==0:
                            add_zero = "000"
                        elif round(10000*new_unc,0)%100==0:
                            add_zero = "00"
                        elif round(10000*new_unc,0)%10==0:
                            add_zero = "0"
                        new_line_list.append(str(new_unc)+add_zero)
                print(line.split("\n")[0])
                print(" ".join(new_line_list))
                print("\n")
                output_file.write(" ".join(new_line_list)+"\n")




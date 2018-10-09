#!/usr/bin/env python2
from prettytable import PrettyTable
from pprint import pprint as pp

_2fu_file = "/home/mulo/Desktop/cytosine_crys/espresso/2fu/Analysis.txt"
_3fu_file = "/home/mulo/Desktop/cytosine_crys/espresso/3fu/Analysis.txt"
_4fu_file = "/home/mulo/Desktop/cytosine_crys/espresso/4fu/Analysis.txt"

addvsen = {}
addvssym = {}
addvsfu = {}

_2fu_data_raw = open(_2fu_file,"r").readlines()
_2fu_base = _2fu_file.split("Analysis.txt")[0]
for i in range(len(_2fu_data_raw)):
  _2fu_data_raw[i] = _2fu_data_raw[i].rstrip("\n")
  if(len(_2fu_data_raw[i].split("|"))!=1):
    if(_2fu_data_raw[i].split("|")[11].rstrip(" ").lstrip(" ")!="Strange Error"):
      if(_2fu_data_raw[i].split("|")[1].rstrip(" ").lstrip(" ")!="Address"):
        add = _2fu_base + _2fu_data_raw[i].split("|")[1].rstrip(" ").lstrip(" ")
        name = add.split("/")[-1]
        add = add.split(name)[0]+"Analysis/"+name.split(".out")[0]+"_final.cif"
        addvsen[add] = \
        float(_2fu_data_raw[i].split("|")[11].rstrip(" ").lstrip(" ").split()[0])/2.
        addvssym[add] = \
        _2fu_data_raw[i].split("|")[13].rstrip(" ").lstrip(" ")
        addvsfu[add] = "2fu"

_3fu_data_raw = open(_3fu_file,"r").readlines()
_3fu_base = _3fu_file.split("Analysis.txt")[0]
for i in range(len(_3fu_data_raw)):
  _3fu_data_raw[i] = _3fu_data_raw[i].rstrip("\n")
  if(len(_3fu_data_raw[i].split("|"))!=1):
    if(_3fu_data_raw[i].split("|")[11].rstrip(" ").lstrip(" ")!="Strange Error"):
      if(_3fu_data_raw[i].split("|")[1].rstrip(" ").lstrip(" ")!="Address"):
        add = _3fu_base + _3fu_data_raw[i].split("|")[1].rstrip(" ").lstrip(" ")
        name = add.split("/")[-1]
        add = add.split(name)[0]+"Analysis/"+name.split(".out")[0]+"_final.cif"
        addvsen[add] = \
        float(_3fu_data_raw[i].split("|")[11].rstrip(" ").lstrip(" ").split()[0])/3.
        addvssym[add] = \
        _3fu_data_raw[i].split("|")[13].rstrip(" ").lstrip(" ")
        addvsfu[add] = "3fu"

_4fu_data_raw = open(_4fu_file,"r").readlines()
_4fu_base = _4fu_file.split("Analysis.txt")[0]
for i in range(len(_4fu_data_raw)):
  _4fu_data_raw[i] = _4fu_data_raw[i].rstrip("\n")
  if(len(_4fu_data_raw[i].split("|"))!=1):
    if(_4fu_data_raw[i].split("|")[11].rstrip(" ").lstrip(" ")!="Strange Error"):
      if(_4fu_data_raw[i].split("|")[1].rstrip(" ").lstrip(" ")!="Address"):
        add = _4fu_base + _4fu_data_raw[i].split("|")[1].rstrip(" ").lstrip(" ")
        name = add.split("/")[-1]
        add = add.split(name)[0]+"Analysis/"+name.split(".out")[0]+"_final.cif"
        addvsen[add] = \
        float(_4fu_data_raw[i].split("|")[11].rstrip(" ").lstrip(" ").split()[0])/4.
        addvssym[add] = \
        _4fu_data_raw[i].split("|")[13].rstrip(" ").lstrip(" ")
        addvsfu[add] = "4fu"

energy_sorted = sorted(addvsen.items(), key=lambda t: t[1], reverse=False)

table = PrettyTable([
"Cif Address",
"Energy(Ry)",
"Formula Unit",
"Symmetry"
])

for i in range(len(energy_sorted)):
  table.add_row([energy_sorted[i][0],addvsen[energy_sorted[i][0]],addvsfu[energy_sorted[i][0]],addvssym[energy_sorted[i][0]]])

print table

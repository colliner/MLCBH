import numpy as np
import sys
import cbh
import json

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]

smi_file="../data/MLCBH_Supporting_Information.txt"
inp_file="../data/MLCBH_inputs.txt"
out_file="../data/MLCBH_outputs.txt"
lab_file="../data/MLCBH_labels.txt"

smiles_arr=[x.split(' ') for x in list(filter(None,open(smi_file, "r").read().split("\n")))]

cbh_rung=[1,2]

def calc_cbh_inputs(cbh_rung):
  global inp_file, out_file, lab_file, smiles_arr
  for rung in cbh_rung:
    print("Calculating CBH{} Rung".format(rung))
    prod, reac, good_smiles = list(), list(), list()

    for smiles in smiles_arr:
      try:
        left, right = cbh.cbh_n([smiles[1]], [], rung)
        for x in left:
          if x not in prod:
            prod.append(x)
        for x in remove_values_from_list(right, '[H+]'):
          if x not in reac:
            reac.append(x)
        good_smiles.append(smiles)
      except:
        print('Failed : {}'.format(smiles))
    x_inputs=open(inp_file.replace('CBH','CBH{}'.format(rung)),"w")
    y_output=open(out_file.replace('CBH','CBH{}'.format(rung)), "w")

    for smiles in good_smiles:
      stng=[]
      left, right = cbh.cbh_n([smiles[1]], [], rung)
      for x in prod:
        stng.append(left.count(x))
      for x in reac:
        stng.append(-1*right.count(x))
      #print("{} :\n {}".format(smiles[1]," ".join([str(x) for x in stng])))
      x_inputs.write(" ".join([str(x) for x in stng])+"\n")
      y_output.write(" ".join([str(x) for x in smiles])+"\n")
    x_inputs.close()
    y_output.close()

    print('Length of good smiles : {}'.format(len(good_smiles)))

    with open(lab_file.replace('CBH','CBH{}'.format(rung)),"w") as fn:
      fn.write(" ".join([str(x) for x in prod+reac])+"\n")

    print('Reactants :\n{}'.format(reac))
    print('Products :\n{}'.format(prod))
    print('Length of input vec : {}'.format(len(reac)+len(prod)))
  return

calc_cbh_inputs(cbh_rung)


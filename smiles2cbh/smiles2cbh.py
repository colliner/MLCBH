import sys
from pycbh import smi2mh, smifromfn

if __name__=='__main__':
  '''
  USAGE: python3 smiles2cbh.py
  '''
  smi_file="../data/MLCBH_Supporting_Information.txt"
  inp_file="../data/MLCBH_inputs.txt"
  out_file="../data/MLCBH_outputs.txt"
  lab_file="../data/MLCBH_labels.txt"
  rungs = [1,2]
  smiles_arr=smifromfn(smi_file)
  print_str=['Loaded {} smiles from {}'.format(len(smiles_arr),smi_file)]
  for rung in rungs:
    print('Calculating CBH-{} Rung'.format(rung))
    cbh_mh, good_x, labels = smi2mh(smiles_arr[1::], rung)
    x_inputs=open(inp_file.replace('CBH','CBH{}'.format(rung)),"w")
    y_output=open(out_file.replace('CBH','CBH{}'.format(rung)), "w")
    y_output.write(" ".join([str(x) for x in smiles_arr[0]])+"\n")
    for idx, v in enumerate(cbh_mh):
      x_inputs.write(" ".join([str(x) for x in v])+"\n")
      y_output.write(" ".join([str(x) for x in good_x[idx]])+"\n")
    x_inputs.close()
    y_output.close()

    print_str.append('\nCBH-{} vectors generated:\n  Written to:\n    {}\n    {}\n    {}\n  Length of good smiles : {}'.format(rung,inp_file.replace('CBH','CBH{}'.format(rung)),out_file.replace('CBH','CBH{}'.format(rung)),lab_file.replace('CBH','CBH{}'.format(rung)),len(good_x)))

    with open(lab_file.replace('CBH','CBH{}'.format(rung)),"w") as fn:
      fn.write(" ".join([str(x) for x in labels])+"\n")

    print_str.append('  Length of input vec : {}'.format(len(labels)))
  
  print('\n'.join(print_str))


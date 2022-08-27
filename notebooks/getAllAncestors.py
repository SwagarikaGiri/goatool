import os
import pandas as pd
from goatools.gosubdag.gosubdag import GoSubDag
import csv

from goatools.obo_parser import GODag

# Load a small test GO DAG and all the optional relationships,
# like 'regulates' and 'part_of'
godag = GODag('../tests/data/i126/viral_gene_silence.obo',
              optional_attrs={'relationship'})



filename='GotermList.tab'
df = pd.read_csv(filename,sep='\t')
goterms=df['Goterm'].tolist()
with open("Goterm-Ancestors-list.tab",'w' ,newline='', encoding='utf-8') as output_csvfile:
        spamwriter = csv.writer(output_csvfile, delimiter='\t')
        index_list = ['Goterm','Parents']
        spamwriter.writerow(index_list)
        for ele in goterms:
            col1=[]
            try:
                col1.append(ele)
                gosubdag_r0 = GoSubDag([ele], godag, prt=None)
                P=gosubdag_r0.rcntobj.go2ancestors[ele]
                list_=list(P)
                ancestors=';'.join(list_)
                col1.append(ancestors)
                spamwriter.writerow(col1)
                print(col1)
            except:
                print(ele)
    
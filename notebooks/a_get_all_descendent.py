import os
import pandas as pd
from goatools.gosubdag.gosubdag import GoSubDag
import csv

from goatools.obo_parser import GODag

# Load a small test GO DAG and all the optional relationships,
# like 'regulates' and 'part_of'
godag = GODag('../tests/data/i126/go_2021.obo',
              optional_attrs={'relationship'})



filename='GotermList.tab'
df = pd.read_csv(filename,sep='\t')
goterm_list=df['Goterm'].tolist()
with open("Goterm-Descendent-list.tab",'w' ,newline='', encoding='utf-8') as output_csvfile:
        spamwriter = csv.writer(output_csvfile, delimiter='\t')
        index_list = ['Goterm','Descendent']
        spamwriter.writerow(index_list)
        for ele in goterm_list:
            col1=[]
            goterm=godag[ele]
            if(goterm.is_obsolete):
                try:
                    gosubdag_r0 = GoSubDag([ele], godag, prt=None)
                    P=gosubdag_r0.rcntobj.go2descendants[ele]
                    list_=list(P)
                    descendent=';'.join(list_)
                    col1.append(ele)
                    col1.append(descendent)
                    spamwriter.writerow(col1)
                    print(col1)
                except:
                    col1.append(ele)
                    descendent=ele
                    col1.append(descendent)
                    pamwriter.writerow(col1)
                    
    
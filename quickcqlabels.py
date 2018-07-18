#this script will take a set of Cq values and a properly formatted PCR plan for a 384 well plate and output Cq values next to their appropiate well label
#assumes two input files: raw cq excel file, and your properly formatted PCR plan, [OPTIONAL] 'name of output file'.csv
#...in that order! It's important for arcane programming reasons.

#imports we need
import pandas as pd
import sys

def main_code():
    #reads in raw Cq values and takes only the Cq column
    cq = pd.read_excel(sys.argv[1])
    cq = cq.set_index(['Well'])
    cq = cq['Cq']

    #reads in formatted qPCR plan
    plan = pd.read_excel(sys.argv[2])

    #formats the plan dataframe so each label includes the target gene
    for i in range(0,15):
        gene = plan.iloc[i,24]
        name = plan.iloc[i]
        plan.iloc[i] = gene + ': ' + name
    #discard the gene col as this just gets in the way now
    plan = plan.drop(['Gene'], axis=1)

    #this loop will combine the plan and cq dataframes by appending to a list named 'res' and then converting that into a dataframe named 'combined'
    res = []
    col_counter = 0
    for j in range(0,16):
        letter = plan.index[j]
        for i in range(0,24):
            res.append([plan.at[letter,i+1], cq.iloc[i+col_counter]])
        col_counter = col_counter+24
    combined = pd.DataFrame(res)
    combined = combined.rename(index=str, columns={0:'gene',1:'Cq'})
    combined = combined.set_index(cq.index)
    #save the results!
    if len(sys.argv) > 3:
        combined.to_csv(sys.argv[3])
    else:
        combined.to_csv('combined.csv')

#quick and dirty check to make sure script has between 2 and 3 arguments presented to it (3 and 4 because list[0] returns script name)
if len(sys.argv) > 2:
    if len(sys.argv) < 5:
        main_code()
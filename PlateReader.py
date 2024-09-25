#Try to do the data manipulations from the 96 well plates
#Depends
#xlrd

#only works with one control lane in column 11
#maybe specify where it is in ata entry?

import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
import seaborn as sns
import sys


in_file = sys.argv[1]
option = sys.argv[2]
norm_opt = sys.argv[3]
assay = sys.argv[4]
ID = sys.argv[5]
initial_concentration = int(sys.argv[6])
dilution_factor = int(sys.argv[7])

#Section for debugging
#test = norm_opt
#print("\ntest\n",test,type(test),"\ntest\n")




#Only use excel sorry
df = pd.read_excel(in_file, sheet_name = 'RawData',skiprows = 2,nrows = 8,usecols = 'C:N')



#Get average of column 12 and subtract this from the rest of the table
def blank_clear(a):
    neg_average = round(a[a.columns[-1]].mean(),6)
    #print("Blank average:", neg_average)
    df = a.subtract(neg_average, axis = 1)
    return df

def normalize(a):
    pos_average = round(a[a.columns[-2]].mean(),6)
    #print("Control average after substracting blank:", pos_average)
    df = a.div(pos_average, axis = 1) * 100
    return df

def drug_conc(drug, initial_concentration, dilutions, factor):
    dilution_list = []
    if drug != "":
        for i in range(1, dilutions + 1):
            dilution_factor = round(initial_concentration / (factor ** (i - 1)),6)
            dilution_list.append(dilution_factor)
        
        dilution_list.append("Control")
        dilution_list.append("Blank")
    else:
        dilution_list =list(range(1,13))
    return dilution_list
 
def assay_type(a):
    if (a == "CV"):
        wl = "(595nm)"
        col = "violet"
    elif (a == "XTT"):
        wl = "(495nm)"
        col = "orange"
    elif (a == "OD600"):
        wl = "(600nm)"
        col = "skyblue"
    else:
        wl = ""
        col = "lightgreen"
    return wl, col   
    
def bar_plot(a,labs, drug, col, wl):
    plot.figure(figsize=(10,6))
    plot.subplots_adjust(bottom=0.15)
    vals = (a.describe())
    entries = 12 + 1
    x =list(range(1,entries))
    
    y = vals.loc['mean'].tolist()
    e = vals.loc['std'].tolist()
    
    plot.bar(x, y, yerr = e,capsize = 3,width = 0.4, align='center', color = col)
    plot.ylim([0,(max(y) + max(e)+10)]) 
    plot.ylabel("Absorbance " + wl)
    if drug != "":
        plot.xticks(x, labs, rotation = 30)
        plot.xlabel(drug + " concentration " + (u"\u03bcg/mL"))
    else:
        plot.xticks(x, labs)  
        plot.xlabel("Column")
    
    plot.savefig('Plot.tiff')
    plot.show()   
    


#Averages blank value and subtracts from data array
df = blank_clear(df)


#Averages positive control and divides each value in array by this
if norm_opt == "norm":
    df = normalize(df)

#Gets color that corresponds with each assay
try:
    wl, color = assay_type(assay)
except NameError:
    assay = ""
    wl, color = assay_type(assay) 

#Does the calculation for drug concentration and dilution for columns 1-10
try:
    x = drug_conc(ID, initial_concentration, 10, dilution_factor)
except NameError:
    ID = ""
    x = drug_conc(ID, initial_concentration, 10, dilution_factor)

#Creates an output file is selected
if option == "calc" or option == "calcandplot":
    with pd.ExcelWriter('Processed_Data.xlsx') as writer:
        df.to_excel(writer)

#Makes the actual plot and saves it
if option == "plot" or option == "calcandplot":
    bar_plot(df,x, ID, color, wl)
    





#print("Done!")
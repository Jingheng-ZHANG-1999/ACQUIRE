# -*- coding: utf-8 -*-
###############batch mode
"""
input filepath and the program will write assay results into a txt file.
"""  
print("||","P.acnes Genotyping System v1.0","||",sep=10*"*")
filepath = input("Please input file path:")
ermx_cut = 6.10
ct58t_cut,ct58g_cut,ct59g_cut = 10.50,8.00,9.50
tg_cut,gg_cut = 6.50,5.00
import xlrd 
wb = xlrd.open_workbook(filepath)
sheet1 = wb.sheet_by_index(0)
row_num = sheet1.nrows #number of subjects
res = []

for i in range(0, row_num):
  ct16s = float(sheet1.row_values(i)[0])
  ctermx = float(sheet1.row_values(i)[1])
  ct58a = float(sheet1.row_values(i)[2])
  ct58t = float(sheet1.row_values(i)[3])
  ct58g = float(sheet1.row_values(i)[4])
  ct59a = float(sheet1.row_values(i)[5])
  ct59g = float(sheet1.row_values(i)[6])
  ct58t_a = ct58t - ct58a
  ct58g_a = ct58g - ct58a
  ct59g_a = ct59g - ct59a
              
  if(ct58t<min(ct58a,ct58g))and(ct59g_a>tg_cut)and(ctermx-ct16s>ermx_cut):
        res.append("C")#TA,NEG
  elif(ct58t<min(ct58a,ct58g))and(ct59g_a>tg_cut)and(ctermx-ct16s<=ermx_cut):  
        res.append("D")#TA,POS    
  elif(ct58t<min(ct58a,ct58g))and(ct59g_a<=tg_cut)and(ctermx-ct16s>ermx_cut):
        res.append("I")#TG,NEG       
  elif(ct58t<min(ct58a,ct58g))and(ct59g_a<=tg_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("J")#TG,POS 
  elif(ct58g<min(ct58a,ct58t))and(ct59g_a>ct59g_cut)and(ctermx-ct16s>ermx_cut):
        res.append("E")#GA,NEG            
  elif(ct58g<min(ct58a,ct58t))and(ct59g_a>ct59g_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("F")#GA,POS
  elif(ct58g<min(ct58a,ct58t))and(ct59g_a<=ct59g_cut)and(ctermx-ct16s>ermx_cut):
        res.append("K") # GG,NEG    
  elif(ct58g<min(ct58a,ct58t))and(ct59g_a<=ct59g_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("L") #GG,POS  
  elif(ct58t_a>ct58t_cut)and(ct58g_a>ct58g_cut)and(ct59g_a>ct59g_cut)and(ctermx-ct16s>ermx_cut):
        res.append("A") #AA,NEG
  elif(ct58t_a>ct58t_cut)and(ct58g_a>ct58g_cut)and(ct59g_a>ct59g_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("B")#AA,POS
  elif(ct58t_a<=ct58t_cut)and(ct59g_a>tg_cut)and(ctermx-ct16s>ermx_cut):
        res.append("C")  #  TA,NEG
  elif(ct58t_a<=ct58t_cut)and(ct59g_a>tg_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("D")#TA,POS
  elif(ct58t_a>ct58t_cut)and(ct58g_a<=ct58g_cut)and(ct59g_a>ct59g_cut)and(ctermx-ct16s>ermx_cut):
        res.append("E")   # GA,NEG
  elif(ct58t_a>ct58t_cut)and(ct58g_a<=ct58g_cut)and(ct59g_a>ct59g_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("F") #GA,POS
  elif(ct58t_a>ct58t_cut)and(ct58g_a>gg_cut)and(ct59g_a<=ct59g_cut)and(ctermx-ct16s>ermx_cut):
        res.append("G")    #AG,NEG
  elif(ct58t_a>ct58t_cut)and(ct58g_a>gg_cut)and(ct59g_a<=ct59g_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("H")#AG,POS
  elif(ct58t_a<=ct58t_cut)and(ct59g_a<=tg_cut)and(ctermx-ct16s>ermx_cut):
        res.append("I")  # TG,NEG
  elif(ct58t_a<=ct58t_cut)and(ct59g_a<=tg_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("J")#TG,POS
  elif(ct58t_a>ct58t_cut)and(ct59g_a<=ct59g_cut)and(ct58g_a<=gg_cut)and(ctermx-ct16s>ermx_cut):
        res.append("K")#GG,NEG
  elif(ct58t_a>ct58t_cut)and(ct59g_a<=ct59g_cut)and(ct58g_a<=gg_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("L")  # GG,POS
  else:res.append("unk")
print(
       " ACQUIRE Result code: "
       "A for AA, ermX NEG ; B for AA, ermX POS; "
       "C for TA, ermX NEG ; D for TA, ermX POS; "
       "E for GA, ermX NEG ; F for GA, ermX POS; "
       "G for AG, ermX NEG ; H for AG, ermX NEG; "
       "I for TG, ermX NEG ; J for TG, ermX NEG; "
       "K for GG, ermX NEG ; L for GG, ermX NEG. "
         
      )
print(res)    
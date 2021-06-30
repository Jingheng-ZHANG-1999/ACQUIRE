# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:05:13 2020
@author: Zhang Jingheng #########single specimen mode
"""
print("|||","P.acnes Genotyping System v1.0","|||",sep=15*"#")
print("|||","Single Specimen Mode","|||",sep=15*"#")
print("please input qPCR results:")
ermx_cut = 6.10
ct58t_cut,ct58g_cut,ct59g_cut = 10.50,8.00,9.50
tg_cut,gg_cut = 6.50,5.00
ct16s = float(input("Please input Ct(16S) and press enter:"))
ctermx = float(input("Please input Ct(ermX):"))
ct58a = float(input("Please input Ct(58A):"))
ct58t = float(input("Please input Ct(58T):"))
ct58g = float(input("Please input Ct(58G):"))
ct59a = float(input("Please input Ct(59A):"))
ct59g = float(input("Please input Ct(59G):"))
ct58t_a = ct58t - ct58a
ct58g_a = ct58g - ct58a
ct59g_a = ct59g - ct59a
res = []

if(ct58t<min(ct58a,ct58g))and(ct59g_a>tg_cut)and(ctermx-ct16s>ermx_cut):
        res.append("Genotype:TA(mutation),ermX gene (-)")#TA,NEG
elif(ct58t<min(ct58a,ct58g))and(ct59g_a>tg_cut)and(ctermx-ct16s<=ermx_cut):  
        res.append("Genotype:TA(mutation),ermX gene (+)")#TA,POS    
elif(ct58t<min(ct58a,ct58g))and(ct59g_a<=tg_cut)and(ctermx-ct16s>ermx_cut):
        res.append("Genotype:TG(mutation),ermX gene (-)")#TG,NEG       
elif(ct58t<min(ct58a,ct58g))and(ct59g_a<=tg_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("Genotype:TG(mutation),ermX gene (+)")#TG,POS 
elif(ct58g<min(ct58a,ct58t))and(ct59g_a>ct59g_cut)and(ctermx-ct16s>ermx_cut):
        res.append("Genotype:GA(mutation),ermX gene (-)")#GA,NEG            
elif(ct58g<min(ct58a,ct58t))and(ct59g_a>ct59g_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("Genotype:GA(mutation),ermX gene (+)")#GA,POS
elif(ct58g<min(ct58a,ct58t))and(ct59g_a<=ct59g_cut)and(ctermx-ct16s>ermx_cut):
        res.append("Genotype:GG(mutation),ermX gene (-)") # GG,NEG    
elif(ct58g<min(ct58a,ct58t))and(ct59g_a<=ct59g_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("Genotype:GG(mutation),ermX gene (+)") #GG,POS  
elif(ct58t_a>ct58t_cut)and(ct58g_a>ct58g_cut)and(ct59g_a>ct59g_cut)and(ctermx-ct16s>ermx_cut):
        res.append("Genotype:AA(wildtype),ermX gene (-)") #AA,NEG
elif(ct58t_a>ct58t_cut)and(ct58g_a>ct58g_cut)and(ct59g_a>ct59g_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("Genotype:AA(wildtype),ermX gene (+)")#AA,POS
elif(ct58t_a<=ct58t_cut)and(ct59g_a>tg_cut)and(ctermx-ct16s>ermx_cut):
        res.append("Genotype:TA(mutation),ermX gene (-)")  #  TA,NEG
elif(ct58t_a<=ct58t_cut)and(ct59g_a>tg_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("Genotype:TA(mutation),ermX gene (+)")#TA,POS
elif(ct58t_a>ct58t_cut)and(ct58g_a<=ct58g_cut)and(ct59g_a>ct59g_cut)and(ctermx-ct16s>ermx_cut):
        res.append("Genotype:GA(mutation),ermX gene (-)")   # GA,NEG
elif(ct58t_a>ct58t_cut)and(ct58g_a<=ct58g_cut)and(ct59g_a>ct59g_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("Genotype:GA(mutation),ermX gene (+)") #GA,POS
elif(ct58t_a>ct58t_cut)and(ct58g_a>gg_cut)and(ct59g_a<=ct59g_cut)and(ctermx-ct16s>ermx_cut):
        res.append("Genotype:AG(mutation),ermX gene (-)")    #AG,NEG
elif(ct58t_a>ct58t_cut)and(ct58g_a>gg_cut)and(ct59g_a<=ct59g_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("Genotype:AG(mutation),ermX gene (+)")#AG,POS
elif(ct58t_a<=ct58t_cut)and(ct59g_a<=tg_cut)and(ctermx-ct16s>ermx_cut):
        res.append("Genotype:TG(mutation),ermX gene (-)")  # TG,NEG
elif(ct58t_a<=ct58t_cut)and(ct59g_a<=tg_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("Genotype:TG(mutation),ermX gene (+)")#TG,POS
elif(ct58t_a>ct58t_cut)and(ct59g_a<=ct59g_cut)and(ct58g_a<=gg_cut)and(ctermx-ct16s>ermx_cut):
        res.append("Genotype:GG(mutation),ermX gene (-)")#GG,NEG
elif(ct58t_a>ct58t_cut)and(ct59g_a<=ct59g_cut)and(ct58g_a<=gg_cut)and(ctermx-ct16s<=ermx_cut):
        res.append("Genotype:GG(mutation),ermX gene (+)")  # GG,POS
print("|||","P.acnes Genotyping Results:","|||",sep=15*"#")
print(res)


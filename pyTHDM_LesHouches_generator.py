#!/usr/bin/env python

#Created by Andres Rivera. File for red LSHAFiles
# 17-07-2021

import pyslha

def buildSLHAinFile():

    ########################### CREATED THE LHAFILE #######################
    #Read the blocks, but do not read all its entries.
    LHA = pyslha.readSLHAFile('LesHouches.in.THDMII_low', ignorenomass=True)

    #Add entries with coments (some of them were vacum)
    #Block MODSEL      #  
    LHA.blocks['MODSEL'].entries[1]='0               #  1/0: High/low scale input' 
    LHA.blocks['MODSEL'].entries[2]='1              # Boundary Condition'
    LHA.blocks['MODSEL'].entries[6]='1               # Generation Mixing'
    LHA.blocks['MODSEL'].entries[12]='173.5          # Renormalization scale'    

    #Block SMINPUTS    # Standard Model inputs 
    LHA.blocks['SMINPUTS'].entries[2]='1.166370E-05    # G_F,Fermi constantt'
    LHA.blocks['SMINPUTS'].entries[3]='1.187000E-01    # alpha_s(MZ) SM MSbar'
    LHA.blocks['SMINPUTS'].entries[4]='9.118870E+01    # Z-boson pole mass'
    LHA.blocks['SMINPUTS'].entries[5]='4.180000E+00    # m_b(mb) SM MSbar'
    LHA.blocks['SMINPUTS'].entries[6]='1.735000E+02    # m_top(pole)'
    LHA.blocks['SMINPUTS'].entries[7]='1.776690E+00    # m_tau(pole)'

    #Block MINPAR      # Input parameters 
    LHA.blocks['MINPAR'].entries[1]='1.0000000E-01    # Lambda1Input'
    LHA.blocks['MINPAR'].entries[2]='2.7000000E-01    # Lambda2Input'
    LHA.blocks['MINPAR'].entries[3]='1.1000000E+00    # Lambda3Input'
    LHA.blocks['MINPAR'].entries[4]='-5.0000000E-01    # Lambda4Input'
    LHA.blocks['MINPAR'].entries[5]='5.0000000E-01    # Lambda5Input'
    LHA.blocks['MINPAR'].entries[9]='-5.0000000E+03    # M12input'
    LHA.blocks['MINPAR'].entries[10]='5.1000000E+01    # TanBeta'
    
    #Block SPhenoInput   # SPheno specific input 
    LHA.blocks['SPHENOINPUT'].entries[1]='-1              # error level'  
    LHA.blocks['SPHENOINPUT'].entries[2]='0              # SPA conventions' 
    LHA.blocks['SPHENOINPUT'].entries[7]='1              # Skip 2-loop Higgs corrections' 
    LHA.blocks['SPHENOINPUT'].entries[8]='3              # Method used for two-loop calculation' 
    LHA.blocks['SPHENOINPUT'].entries[9]='1              # Gaugeless limit used at two-loop' 
    LHA.blocks['SPHENOINPUT'].entries[10]='0              # safe-mode used at two-loop' 
    LHA.blocks['SPHENOINPUT'].entries[11]='1               # calculate branching ratios' 
    LHA.blocks['SPHENOINPUT'].entries[13]='1               # 3-Body decays: none (0), fermion (1), scalar (2), both (3)' 
    LHA.blocks['SPHENOINPUT'].entries[14]='0               # Run couplings to scale of decaying particle' 
    LHA.blocks['SPHENOINPUT'].entries[12]='1.000E-04       # write only branching ratios larger than this value' 
    LHA.blocks['SPHENOINPUT'].entries[15]='1.000E-30       # write only decay if width larger than this value' 
    LHA.blocks['SPHENOINPUT'].entries[16]='1              # One-loop decays' 
    LHA.blocks['SPHENOINPUT'].entries[19]='-2              # Matching order (-2:automatic, -1:pole, 0-2: tree, one- & two-loop)' 
    LHA.blocks['SPHENOINPUT'].entries[31]='-1              # fixed GUT scale (-1: dynamical GUT scale)' 
    LHA.blocks['SPHENOINPUT'].entries[32]='0               # Strict unification' 
    LHA.blocks['SPHENOINPUT'].entries[34]='1.000E-04       # Precision of mass calculation' 
    LHA.blocks['SPHENOINPUT'].entries[35]='40              # Maximal number of iterations'
    LHA.blocks['SPHENOINPUT'].entries[36]='5               # Minimal number of iterations before discarding points'
    LHA.blocks['SPHENOINPUT'].entries[37]='1               # Set Yukawa scheme' 
    LHA.blocks['SPHENOINPUT'].entries[38]='1               # 1- or 2-Loop RGEs' 
    LHA.blocks['SPHENOINPUT'].entries[50]='1               # Majorana phases: use only positive masses (put 0 to use file with CalcHep/Micromegas!)' 
    LHA.blocks['SPHENOINPUT'].entries[51]='0               # Write Output in CKM basis' 
    LHA.blocks['SPHENOINPUT'].entries[52]='0               # Write spectrum in case of tachyonic states' 
    LHA.blocks['SPHENOINPUT'].entries[55]='0               # Calculate loop corrected masses' 
    LHA.blocks['SPHENOINPUT'].entries[57]='1               # Calculate low energy constraints' 
    LHA.blocks['SPHENOINPUT'].entries[65]='1               # Solution tadpole equation' 
    LHA.blocks['SPHENOINPUT'].entries[66]='1               # Two-Scale Matching' 
    LHA.blocks['SPHENOINPUT'].entries[67]='1               # effective Higgs mass calculation' 
    LHA.blocks['SPHENOINPUT'].entries[75]='0               # Write WHIZARD files' 
    LHA.blocks['SPHENOINPUT'].entries[76]='2               # Write HiggsBounds file: 2 for HiggsBounds5, 1 for HiggsBounds4 and below'   
    LHA.blocks['SPHENOINPUT'].entries[77]='0               # Output for MicrOmegas (running masses for light quarks; real mixing matrices)'   
    LHA.blocks['SPHENOINPUT'].entries[78]='0               # Output for MadGraph (writes also vanishing blocks)'   
    LHA.blocks['SPHENOINPUT'].entries[79]='0               # Write WCXF files (exchange format for Wilson coefficients)' 
    LHA.blocks['SPHENOINPUT'].entries[86]='0.              # Maximal width to be counted as invisible in Higgs decays; -1: only LSP' 
    LHA.blocks['SPHENOINPUT'].entries[440]='1               # Tree-level unitarity constraints (limit s->infinity)' 
    LHA.blocks['SPHENOINPUT'].entries[441]='1               # Full tree-level unitarity constraints' 
    LHA.blocks['SPHENOINPUT'].entries[442]='1000.           # sqrt(s_min)'   
    LHA.blocks['SPHENOINPUT'].entries[443]='2000.           # sqrt(s_max)'   
    LHA.blocks['SPHENOINPUT'].entries[444]='5               # steps'   
    LHA.blocks['SPHENOINPUT'].entries[445]='0               # running'   
    LHA.blocks['SPHENOINPUT'].entries[510]='0.              # Write tree level values for tadpole solutions' 
    LHA.blocks['SPHENOINPUT'].entries[515]='0               # Write parameter values at GUT scale' 
    LHA.blocks['SPHENOINPUT'].entries[520]='1.              # Write effective Higgs couplings (HiggsBounds blocks): put 0 to use file with MadGraph!' 
    LHA.blocks['SPHENOINPUT'].entries[521]='1.              # Diphoton/Digluon widths including higher order' 
    LHA.blocks['SPHENOINPUT'].entries[525]='0.              # Write loop contributions to diphoton decay of Higgs' 
    LHA.blocks['SPHENOINPUT'].entries[530]='0.              # Write Blocks for Vevacious' 

    #Block DECAYOPTIONS   # Options to turn on/off specific decays 
    LHA.blocks['DECAYOPTIONS'].entries[1]='1     # Calc 3-Body decays of Fu' 
    LHA.blocks['DECAYOPTIONS'].entries[2]='1     # Calc 3-Body decays of Fe' 
    LHA.blocks['DECAYOPTIONS'].entries[3]='1     # Calc 3-Body decays of Fd' 
    LHA.blocks['DECAYOPTIONS'].entries[1001]='1     # Loop Decay of Fu' 
    LHA.blocks['DECAYOPTIONS'].entries[1002]='1     # Loop Decay of Fe' 
    LHA.blocks['DECAYOPTIONS'].entries[1003]='1     # Loop Decay of Fd' 
    LHA.blocks['DECAYOPTIONS'].entries[1004]='1     # Loop Decay of hh' 
    LHA.blocks['DECAYOPTIONS'].entries[1005]='1     # Loop Decay of Ah' 
    LHA.blocks['DECAYOPTIONS'].entries[1006]='1     # Loop Decay of Hm' 
    LHA.blocks['DECAYOPTIONS'].entries[1114]='1.     # U-factors (0: off, 1:p2_i=m2_i, 2:p2=0, p3:p2_i=m2_1)' 
    LHA.blocks['DECAYOPTIONS'].entries[1115]='1.     # Use loop-corrected masses for external states' 
    LHA.blocks['DECAYOPTIONS'].entries[1116]='0.     # OS values for W,Z and fermions (0: off, 1:g1,g2,v 2:g1,g2,v,Y_i)' 
    LHA.blocks['DECAYOPTIONS'].entries[1117]='0.     # Use defined counter-terms' 
    LHA.blocks['DECAYOPTIONS'].entries[1118]='1.     # Use everywhere loop-corrected masses for loop-induced decays' 

    #############################################################

    return LHA

# Example: Modific the LesHouches_low   
#LHA.blocks['MINPAR'].entries[2]='%.7E    # MDFInput' %222
#xdict['MINPAR'].entries[3]='%.6E    # MS12Input' %MS12      

#Write the file
#pyslha.writeSLHAFile('InputFile',LHA)
 

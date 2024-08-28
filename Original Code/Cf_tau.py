#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:39:28 2018

@author: Paola
"""

import numpy as np

import matplotlib.pyplot as plt 
#import os
from matplotlib.backends.backend_pdf import PdfPages


#pp2= PdfPages('Cf_tau_sametau.pdf')
f = plt.figure(figsize=(12,5))
ax = f.add_subplot(121)
ax2 = f.add_subplot(122)

save_format = '.pdf'
#==========================================
# Input parameters: values from the spectra

case_num = 1
case_name = ''

if case_num == 1  :  
    case_name = 'Case spSpec-51959-051-305'
    I1=3
    I2=I1
    Io1=10
    Io2=7

elif case_num == 2:
        case_name = 'Case LBQS'
        I1=8
        I2=I1
        Io1=23
        Io2=18

elif case_num == 3:
        case_name = 'Case 304'
        I1=1.5
        I2=I1
        Io1=10
        Io2=7.5

elif case_num ==4: 
        case_name = 'Case 901'
        I1=10.5
        I2=I1
        Io1=22
        Io2=16.5
        
elif case_num == 5:
        case_name = 'Case spSpec-51959-051-305'
        I1=3
        I2=I1
        Io1=10
        Io2=7

elif case_num == 6:
        case_name = 'Case LBQS, Absorption complex D'
        I1=8
        I2=I1
        Io1=23
        Io2=18

else:
        case_name = 'No inputs'
        I1 = 0
        I2 = I1
        Io1 = 0
        Io2 = 0
# ------------------------------------------
#-- First set of plots. 

alpha=round(Io1/Io2,1) # Io1=alpha * Io2

pp2= PdfPages('Cf_tau_sametau_case'+ str(case_num) + save_format)

Spectral_value_Cf2Cf1=round((1.-(I2/Io2))/(1.-(I1/Io1)),2) #Cf2/Cf1 from writing eqn for each intensity and dividing
Spectral_value_1=round(1.-(I1/Io1),2) #  = Cf1(1-exp(-tau))
Spectral_value_2=round(1.-(I2/Io2),4)


tau= np.arange(0.1,5,0.1)
ttau=tau*(-1)  #= -tau
yy=(alpha-1.)/(np.exp(ttau)-1.)  # right side of eqn
Cf1=0.1
plt.title(case_name)
for lala in range(1,11):

    Cf2 = yy+alpha*Cf1 #Correct -Taylor
    
    plt.subplot(1, 2, 1)
    
    
    plt.plot(tau, Cf2 , label = r'$Cf_1$='+str(Cf1),color=[0.05,0.6,lala/10.])

    plt.xlabel(r"$\tau$")
    #plt.ylabel(r"$C_{f2}- \alpha C_{f1}$")
    plt.ylabel(r"$C_{f2}$")
    plt.ylim(0,1)
    plt.xlim(-0.95,5)
          
    Cf1=round(Cf1+0.1,1)


print('Spectral_value_2=' +str(Spectral_value_2))

#Spectral_Cf2=Spectral_value_2/(1.-np.exp(-tau)) #Not sure about how this is gotten. 
Spectral_Cf2 = Cf2*(1-np.exp(ttau)) #From the equation shown in the graph and below in line 117

print('Spectral_Cf2 ('+str(len(Spectral_Cf2))+')= '+str(Spectral_Cf2))
plt.plot(tau,Spectral_Cf2,color='r')

#This is just the spectral value. IDK what the importance is for it to be on the graph and how it corresponds to the Spectral_Cf2 plotted
plt.text(2.8,0.5,r"$C_{f2}(1-e^{- \tau})=$"+str(Spectral_value_2),color='r',fontsize=10) 

############################################################################################################################################################
#mintau=(-1)*np.log(1.-(Spectral_value_1/1.))  # From Cf1(1-exp(-tau))=1-I1/I01; since that is the value of tau for Cf=1 and the observational data
#mintau = 2.3
mintau = (-1)*np.log(Spectral_value_1)
print('mintau = '+ str(mintau))
plt.plot([mintau,mintau],[0,1],'r--',) #RED Line of line (^). Biggest step is understanding  
plt.text(mintau-1,-0.1,r"-ln(1-I1/I0 ) = "+str(round(mintau,2)),color = 'r',fontsize=10)
    
#ee=np.exp(-tau)*Cf2
#sv=min(abs(ee-Spectral_value_2))
#sv_index=np.where(ee == sv+Spectral_value_2)
#sv_index=np.where(ee == -(sv+Spectral_value_2))


plt.legend(loc='upper left')
plt.text(3,0.19,r"$C_{f2}- \alpha C_{f1} = \frac{\alpha - 1}{e^{- \tau}-1}$",bbox=dict(facecolor='white', alpha=0.7))
plt.text(3,0.12,r"assume $\tau_1 = \tau_2$")
plt.text(3,0.05,r"$\alpha =$"+str(alpha)+r"; $I_{o1} = \alpha I_{o2}$",bbox=dict(facecolor='white', alpha=0.7))

##########################################################################################################################################################

Cf1=0.1



for lala in range(1,11):
    
    Cf2Cf1=(yy+alpha*Cf1)/Cf1  # Cf2/Cf1
    
    plt.title(case_name)
    
    plt.subplot(1, 2, 2)
    plt.plot(tau,Cf2Cf1,label=r'$Cf_1$='+str(Cf1),color=[0.05,0.6,lala/10.])
    plt.xlabel(r"$\tau$")
    plt.ylabel(r"$C_{f2}/C_{f1}$")
    plt.ylim(0,1)
    plt.xlim(-0.95,5)

    Cf1=round(Cf1+0.1,1)
    
plt.legend(loc='upper left')
plt.text(3,0.19,r"$C_{f2}- \alpha C_{f1} = \frac{\alpha - 1}{e^{- \tau}-1}$",bbox=dict(facecolor='white', alpha=0.7))
plt.text(3,0.12,r"assume $\tau_1 = \tau_2$")
plt.text(3,0.05,r"$\alpha =$"+str(alpha)+r"; $I_{o1} = \alpha I_{o2}$",bbox=dict(facecolor='white', alpha=0.7))


plt.plot([0,6],[Spectral_value_Cf2Cf1,Spectral_value_Cf2Cf1],color='r')
rr=round(Spectral_value_2/Spectral_value_1,2)
plt.text(3.2,0.8,r"$C_{f2}/C_{f1}=$"+str(rr),color='r',fontsize=10)

plt.plot([mintau,mintau],[0,1],'r--',)

#pp1.savefig()
#pp1.close()
pp2.savefig()
pp2.close()

##########################################################################################################################################################

# -------------------------- Second set of plots 

# This case seems unreasonable to me:
# If I don't have absorption, e(-tau)=1 --> I1=I01; I2=Io2; I1=I2, but Io1=alpha*Io2
# but if it skips the tau =o region, it mihgt be feasable? (and the red part avoids it...)

pp1= PdfPages('Cf_tau_sameCf_case' + str(case_num) + save_format)

ff = plt.figure(figsize=(12,5))
ax = f.add_subplot(121)
ax2 = f.add_subplot(122)

Cf=np.arange(0.1,1.1,0.02)

yyy=(1.-alpha)*(1.-Cf)/Cf

tau1=0.1

for lala in range(1,52): #The number of lines produced on the first graph
    plt.title(case_name)
    tau2=(-1)*(np.log(alpha*np.exp(-tau1)-yyy)) #Equation is correct, but coming up with an error when ran
    
    plt.subplot(1, 2, 1)
    
#    print(tau1-0.1)
    
    if round((tau1-0.1),1) % 1 == 0:
        plt.plot(Cf,tau2,label=r'$\tau_1$='+str(tau1),color=[0.05,0.6,lala/51.])
    else: 
        plt.plot(Cf,tau2,color=[0.05,0.6,lala/51.])
    plt.ylabel(r"$\tau_2$")
    plt.xlabel(r"$C_{f}$")
    plt.xlim(0,1)
    plt.ylim(0,5)
    
    tau1=round(tau1+0.1,2)
    
    
tau1=round(tau1-0.1,2)
    
plt.legend(loc='upper left')
plt.text(0.6,4.6,r"$\frac{1-C_{f}}{C_{f}} = \frac{\alpha e^{- \tau_1} - e^{- \tau_2}}{1 - \alpha}$",fontsize=10,bbox=dict(facecolor='white', alpha=0.7))
plt.text(0.6,4.15,r"assume $C_{f1} = C_{f2}$")
plt.text(0.6,3.8,r"$\alpha =$"+str(alpha)+r"; $I_{o1} = \alpha I_{o2}$",bbox=dict(facecolor='white', alpha=0.7))


#plt.plot([mintau,mintau],[0,1],'r--',)


Spectral_tau2=(-1)*np.log(1.-(Spectral_value_2/Cf))  # From Spectral_value/Cf = 1-exp(-tau)
plt.plot(Cf,Spectral_tau2,'r:')
plt.plot(Cf[5:],Spectral_tau2[5:],'ro')
plt.text(0.23,2.5,r"$C_{f} (1-e^{- \tau_2})=$"+str(Spectral_value_2),color='r',fontsize=12) #RED LINE

#maxtau2=-(1)*np.log(1.-((Spectral_value_2/Spectral_value_1)*(1.-np.exp(-tau1))))  # Bring Cf=Sp1/(1-exp(-tau1)) into Cf*(1-exp(-tau2))=Sp2
maxtau2=-(1)*np.log(1.-((Spectral_value_2/Spectral_value_1)))  # Bring Cf=Sp1/(1-exp(-tau1)) into Cf*(1-exp(-tau2))=Sp2
mintau2=(-1)*np.log(1.-(Spectral_value_2/1.))  # Point where Cf=1 in Cf*(1-exp(-tau2))=Sp2
plt.plot([0,1],[mintau2,mintau2],'r--',)
plt.plot([0,1],[maxtau2,maxtau2],'r--',)
plt.plot([Spectral_value_1,Spectral_value_1],[0,5],'r--')

tau1=0.1
plt.subplot(1, 2, 2)
for lala in range(1,52):
    
    plt.title(case_name)
    
    tau2=(-1)*np.log(alpha*np.exp(-tau1)-yyy)
    
    tau2tau1=tau2/tau1
    
    
    
    if round((tau1-0.1),1) % 1 == 0:
        plt.plot(Cf,tau2tau1,label=r'$\tau_1$='+str(tau1),color=[0.05,0.6,lala/51.])
    else: 
        plt.plot(Cf,tau2tau1,color=[0.05,0.6,lala/51.])
    plt.ylabel(r"$\tau_2/\tau_1$")
    plt.xlabel(r"$C_{f}$")
    plt.xlim(0,1)
    plt.ylim(0,1)
    
    tau1=round(tau1+0.1,2)
    
plt.legend(loc='upper left')
plt.text(0.55,0.92,r"$\frac{1-C_{f}}{C_{f}} = \frac{\alpha e^{- \tau_1} - e^{- \tau_2}}{1 - \alpha}$",fontsize=12,bbox=dict(facecolor='white', alpha=0.7))
plt.text(0.55,0.83,r"assume $C_{f1} = C_{f2}$")
plt.text(0.55,0.76,r"$\alpha =$"+str(alpha)+r"; $I_{o1} = \alpha I_{o2}$",bbox=dict(facecolor='white', alpha=0.7))


pp1.savefig()
pp1.close()
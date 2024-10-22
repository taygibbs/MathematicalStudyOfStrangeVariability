# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:54:39 2024

@author: Taylor Gibbons
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import StrangeVariabilityCalculationFunctions as svc

def visualize(data,xaxis,yaxis, graph_num = 0): #In Progress, and more of a test than an actual function to be used
    """
    
    """
    
    number = 0
    if graph_num == 1 or graph_num == 0:
        plt.figure(number)
        plt.scatter(data[xaxis],data[yaxis])
        plt.title('Minimum Optical Depth by Number of Days Between Observations')
        plt.xlabel('Number of Days between Observations')
        plt.ylabel('Minimum Optical Depth')
        number += 1
    if graph_num == 2 or graph_num == 0:
        plt.figure(number)
        plt.scatter(data['days'],data['new_alpha'])
        plt.title('New Alpha vs Number of Days Between Obervations')
        plt.ylabel('New alpha')
        plt.xlabel('Number of Days Between Observations')
        number += 1
    if graph_num == 3 or graph_num == 0:
        plt.figure(number)
        plt.scatter(data[''])
    if graph_num == 4 or graph_num == 0:
        table = pd.pivot_table(data, values = ['new_alpha','minOpt','minCov1','minCov2'],index = ['objectName'], aggfunc= 'mean')
        xdata = table['new_alpha']
        xbins = np.array([0.25,0.5,0.75,1])

        style = {'facecolor': 'none', 'edgecolor': 'C0','linewidth':3}

        fig,ax = plt.subplots()

        ax.hist(xdata,bins = xbins, **style)
        ax.set_ylabel('Number of Objects with new alpha values')
        ax.set_xlabel('New Alpha')
        
        
        
        
def Cf_grapher(data, graph_num= 0):
    """
    

    Parameters
    ----------
    data : DataFrame
        A dataframe that contains all of the calculated values and initial values
        from the detection code. This requires:
            I01, I02, I1, I2, alpha, minOpt, minCov1 (spectral values 1, sv1), 
            minCov2 (Spectral_value_2, sv2), Spec_Cf1, Spec_Cf2, Spec_Cf2Cf1 
    graph_num : int, optional
        DESCRIPTION. The default is 0. This input changes based on the graph you are
        looking to get

    Returns
    -------
    None.

    """

    
    
    prev_num = 0
    
    
    #alpha, mintau, Sv1, Sv2, Spectral_value_Cf2Cf1, Spectral_Cf1, Spectral_Cf2 =svc.min_value_finder(I01, I02, I1, I2, prev_num)
    tau = np.arange(0.1,5,0.1)
    
    alpha_eqn = 'I01 = aI02'
    if graph_num == 0:
        plt.figure(figsize= (18,5))
    else:
        plt.figure(figsize= (6,5))
    
    for index, row in data.iterrows():
        alpha = row['alpha']
        Spectral_Cf1 = row['Spec_Cf1']
        Spectral_Cf2 = row['Spec_Cf2']
        Spectral_value_Cf2Cf1 = row['Spec_Cf2Cf1']
        Sv1 = row['minCov1']
        Sv2 = row['minCov2']
        mintau = row['minOpt']
        
        print('Plotting: ' + row['objectName'])
        
        
        if graph_num == 1 or graph_num == 0:
            
            if graph_num == 0:
                plt.subplot(1, 3, 1)
                plt.suptitle(row['objectName'] + '(' + str(prev_num) + ')')
                     
            
            
            plt.title(r'$C_{f1}$ vs. $\tau$')
            Cf2=0.1
            ttau=tau*(-1)  #= -tau
            for lala in range(1,11):
        
                Cf1 = (Cf2 - ((alpha-1)/(np.exp(ttau)-1)))/ alpha
                
                plt.plot(tau, Cf1 ,label = r'$Cf_2$='+str(Cf2),color=[0.05,0.6,lala/10.])
        
                plt.xlabel(r"$\tau$")
                
                plt.ylabel(r"$C_{f1}$")
                plt.ylim(0,1)
                plt.xlim(-0.95,5)
                      
                Cf2=round(Cf2+0.1,1)
                
                
            
            plt.plot(tau,Spectral_Cf1,color = 'r')
            plt.text(2.8,Sv1-0.05,r'$C_{f1}(1-e^{- \tau})=$' + str(Sv1),color='r',fontsize=10)
        
            #plt.legend(loc='upper left')
            #plt.text(3,0.19,r"$C_{f2}- \alpha C_{f1} = \frac{\alpha - 1}{e^{- \tau}-1}$",bbox=dict(facecolor='white', alpha=0.7))
            #plt.text(3,0.12,r"assume $\tau_1 = \tau_2$")
            #plt.text(3,0.05,r"$\alpha =$"+str(alpha)+r"; $I_{o1} = \alpha I_{o2}$",bbox=dict(facecolor='white', alpha=0.7))
        
            plt.plot([mintau,mintau],[0,1],'r--',) #RED verticle dotted Line of line (^). Biggest step is understanding  
            plt.text(mintau-1,-0.1,r"mintau= "+str(round(mintau,2)),color = 'r',fontsize=12)
        
        if graph_num == 1 or graph_num == 1221:
            plt.figure(figsize= (12,5))
            plt.suptitle(row['objectName'] + '(' + str(prev_num) + ')')
            plt.subplot(1, 2, 1)
            plt.title(r'$C_{f1}$ vs. $\tau$')
            Cf2=0.1
            ttau=tau*(-1)  #= -tau
            for lala in range(1,11):
        
                Cf1 = (Cf2 - ((alpha-1)/(np.exp(ttau)-1)))/ alpha
                
                plt.plot(tau, Cf1 ,label = r'$Cf_2$='+str(Cf2),color=[0.05,0.6,lala/10.])
        
                plt.xlabel(r"$\tau$")
                
                plt.ylabel(r"$C_{f1}$")
                plt.ylim(0,1)
                plt.xlim(-0.95,5)
                      
                Cf2=round(Cf2+0.1,1)
                
                
            plt.subplot(1,2,1)
            plt.plot(tau,Spectral_Cf1,color = 'r')
            plt.text(2.8,Sv1-0.05,r'$C_{f1}(1-e^{- \tau})=$' + str(Sv1),color='r',fontsize=10)
        
            #plt.legend(loc='upper left')
            #plt.text(3,0.19,r"$C_{f2}- \alpha C_{f1} = \frac{\alpha - 1}{e^{- \tau}-1}$",bbox=dict(facecolor='white', alpha=0.7))
            #plt.text(3,0.12,r"assume $\tau_1 = \tau_2$")
            #plt.text(3,0.05,r"$\alpha =$"+str(alpha)+r"; $I_{o1} = \alpha I_{o2}$",bbox=dict(facecolor='white', alpha=0.7))
        
            plt.plot([mintau,mintau],[0,1],'r--',) #RED verticle dotted Line of line (^). Biggest step is understanding  
            plt.text(mintau-1,-0.1,r"mintau= "+str(round(mintau,2)),color = 'r',fontsize=12)
            
            
            plt.subplot(1, 2, 2)
            plt.title(r'$C_{f2}$ vs. $\tau$')
            Cf1=0.1
            ttau=tau*(-1)  #= -tau
            for lala in range(1,11):
                 
                Cf2 = (Cf1 - ((alpha-1)/(np.exp(ttau)-1)))/ alpha
                
                plt.plot(tau, Cf2 ,label = r'$Cf_2$='+str(Cf2),color=[0.05,0.6,lala/10.])
        
                plt.xlabel(r"$\tau$")
                
                plt.ylabel(r"$C_{f1}$")
                plt.ylim(0,1)
                plt.xlim(-0.95,5)
                      
                Cf1=round(Cf1+0.1,1)
                
                
            
            plt.plot(tau,Spectral_Cf1,color = 'r')
            plt.text(2.8,Sv1-0.05,r'$C_{f1}(1-e^{- \tau})=$' + str(Sv1),color='r',fontsize=10)
        
            #plt.legend(loc='upper left')
            #plt.text(3,0.19,r"$C_{f2}- \alpha C_{f1} = \frac{\alpha - 1}{e^{- \tau}-1}$",bbox=dict(facecolor='white', alpha=0.7))
            #plt.text(3,0.12,r"assume $\tau_1 = \tau_2$")
            #plt.text(3,0.05,r"$\alpha =$"+str(alpha)+r"; $I_{o1} = \alpha I_{o2}$",bbox=dict(facecolor='white', alpha=0.7))
        
            plt.plot([mintau,mintau],[0,1],'r--',) #RED verticle dotted Line of line (^). Biggest step is understanding  
            plt.text(mintau-1,-0.1,r"mintau= "+str(round(mintau,2)),color = 'r',fontsize=12)
    
    ##########################################################################################################################################################
        if graph_num == 2 or graph_num == 0:
            tau= np.arange(0.1,5,0.1)
            ttau=tau*(-1)  #= -tau
        
            
            Cf1=0.1
            plt.subplot(1, 3, 2)
            
            plt.title(r'$C_{f2}$ vs. $\tau$')        
            plt.xlabel(r"$\tau$")
                
            plt.ylabel(r"$C_{f2}$")
            for lala in range(1,11):
        
                Cf2 =(alpha-1.)/(np.exp(ttau)-1.)+alpha*Cf1 
                
                
                plt.plot(tau, Cf2 , label = r'$Cf_1$='+str(Cf1),color=[0.05,0.6,lala/10.])
        
        
                plt.ylim(0,1)
                plt.xlim(-0.95,5)
        
                
                Cf1=round(Cf1+0.1,1)
        
            
        
            Spectral_Cf1 = Sv1/(1-np.exp(-tau)) #this will go specifically into the graph tau vs. Cf1.
            plt.plot(tau,Spectral_Cf2,color='r')
            plt.text(2.8,Sv2-0.05,r"$C_{f2}(1-e^{- \tau})=$"+str(Sv2),color='r',fontsize=10) 
        
            mintau=(-1)*np.log(1.-(Sv2/1.))  # From Cf1(1-exp(-tau))=1-I1/I01; since that is the value of tau for Cf=1 and the observational data
        
            plt.plot([mintau,mintau],[0,1],'r--',) #RED verticle dotted Line of line (^). Biggest step is understanding  
            plt.text(mintau-1,-0.1,r"mintau= "+str(round(mintau,2)),color = 'r',fontsize=12)
        
        
            plt.legend(loc='upper left')
            plt.text(3,0.19,r"$C_{f2}- \alpha C_{f1} = \frac{\alpha - 1}{e^{- \tau}-1}$",bbox=dict(facecolor='white', alpha=0.7))
            plt.text(3,0.12,r"assume $\tau_1 = \tau_2$")
            plt.text(3,0.05,r"$\alpha =$"+str(alpha) + alpha_eqn ,bbox=dict(facecolor='white', alpha=0.7))
    
    #plotting mintau on the first plot.
    
    ##########################################################################################################################################################
        if graph_num == 3 or graph_num == 0:
            Cf1=0.1
            
            plt.subplot(1, 3, 3)  
            plt.title(r'$C_{f2}/C_{f1}$ vs. $\tau$')
                  
            plt.xlabel(r"$\tau$")
            plt.ylabel(r"$C_{f2}/C_{f1}$")
            for lala in range(1,11):
                
                Cf2Cf1=((alpha-1.)/(np.exp(ttau)-1.)+alpha*Cf1)/Cf1  # Cf2/Cf1
                
                
                
                
                plt.plot(tau,Cf2Cf1,label=r'$Cf_1$='+str(Cf1),color=[0.05,0.6,lala/10.])
        
                plt.ylim(0.75 * Spectral_value_Cf2Cf1,1.2 * Spectral_value_Cf2Cf1)
                plt.xlim(-0.95,5)
                
                
                Cf1=round(Cf1+0.1,1)
                
            plt.legend(loc='lower left')
            plt.text(3, 0.84 * Spectral_value_Cf2Cf1,r"$C_{f2}- \alpha C_{f1} = \frac{\alpha - 1}{e^{- \tau}-1}$",bbox=dict(facecolor = 'white', alpha=0.7))
            plt.text(3,0.80 * Spectral_value_Cf2Cf1,r"assume $\tau_1 = \tau_2$")
            plt.text(3,0.76 * Spectral_value_Cf2Cf1,r"$\alpha =$"+str(alpha)+r"; $I_{o1} = \alpha I_{o2}$",bbox=dict(facecolor='white', alpha=0.7))
        
        
            plt.plot([0,6],[Spectral_value_Cf2Cf1,Spectral_value_Cf2Cf1],color='r') #The horizontal red line showing the ratio between spectral_v_2 to spec_v_1
            rr=round(Sv2/Sv1,2)
            plt.text(3.2,Spectral_value_Cf2Cf1 - 0.05,r"$C_{f2}/C_{f1}=$"+str(rr),color='r',fontsize=12)
        
            #plt.plot([mintau,mintau],[0,1.2 * Spectral_value_Cf2Cf1],'r--',)
            #plt.text(mintau-1,0.7 * Spectral_value_Cf2Cf1,r"mintau= "+str(round(mintau,2)),color = 'r',fontsize=12)
            
            
        plt.savefig(os.getcwd() + '/CovOpt_Plots/' + row['objectName'] + ' (' + str(prev_num) + ').png',dpi= 500)
        #plt.show()
        plt.clf()
        
        
def alpha_Testing(I01, I02, I1, I2, Sv1, Sv2, Spectral_Cf1, Spectral_Cf2, graph):
    """

     I01 : float
         The average value of the flux around the trough of the first observation.
     I02 : float
         The average value of the flux around the trouhg of the second observation.
     I12 : float
         The average value of the flux at the bottom of the trough. At the point of 
         using this code, the values should be found and the quasars that have strange 
         variablity should be found.

    Returns
    -------
    None.

    
    OUTLINE:
       1. Take in values from observations
       2. Makes the two alpha values (at least one of both cases, maybe 2)
       3. graphs the two 

    """
    
    
    a12 = round(I01/I02,2)
    a21 = round(I02/I01,2)
    print('a12 = I01/I02 = ' + str(a12) + '\n'
          + 'a21 = I02/I01 = ' + str(a21))
    
    
    if a12 < 1: #1st Case where the second epoch is larger than the first 
        print('Proceeding with Case #1:')
    elif a21 < 1: #2nd Case where second epoch is less than the first
        print('Proceeding with Case #2')    
    
    if graph == 'yes':
        """
        Plan for this part of the function is to make is so that it ends up being
        a lot more consolidated. Ie, instead of the two graphs being made 
        separately, it will be made in one for loop with the graphs being made
        at generally the same time
        """
        #CASE 1: a12 < 1
        title = 'Alpha12 = ' + str(a12)+ ' Alpha21 = '+str(a21)
        tau_label = r'$\tau$'
        cf1_label = r'$C_{f1}$'
        cf2_label = r'$C_{f2}$'
        
        tau = np.arange(0.1,5.1,0.1)
        ttau=tau*(-1)  #= -tau
        
        plt.figure(figsize= (12,5))
        plt.suptitle(title)

        plt.subplot(1,2,1)
        plt.title(cf1_label + ' using ' + r'$\alpha_{12}$' + '=' + str(a12))
        plt.xlabel(r"$\tau$")
        plt.ylabel(r"$C_{f1}$")
        plt.ylim(0,1)
        plt.xlim(-0.95,5) 
        
        
        plt.subplot(1,2,2)
        plt.title(cf2_label + ' using ' + r'$\alpha_{12}$' + '=' + str(a12))
        plt.xlabel(tau_label)
        plt.ylabel(cf2_label)
        plt.ylim(0,1)
        plt.xlim(-0.95,5)        
        
        Cf=0.1
        
        for lala in range(1,11):
    
            plt.subplot(1,2,1)
            Cf1 = a21*Cf + (a21-1)/(np.exp(ttau)-1)
            plt.plot(tau, Cf1 ,label = r'$Cf_2$='+str(Cf),color=[0.05,0.6,lala/10.])

            plt.subplot(1,2,2)
            Cf2 = a12*Cf + (a12-1)/(np.exp(ttau)-1)
            plt.plot(tau, Cf2 ,label = cf2_label +'='+str(Cf),color=[0.05,0.6,lala/10.])

    
            Cf=round(Cf+0.1,1)
            
        
        
        Cf1=0.1
        ttau=tau*(-1)  #= -tau
        
        #Save figure and clear to start new one
        plt.show()
        plt.savefig(os.getcwd() + '/AlphaChangePlots/' + title + ').png',dpi= 500)
        
        
        
        plt.figure(figsize = (12,5))
        plt.suptitle(title)
        
        plt.subplot(1,2,1)
        plt.title(cf1_label + ' using ' + r'$\alpha_{12}$' + '=' + str(a21))
        plt.xlabel(tau_label)
        plt.ylabel(cf1_label)
        plt.ylim(0,1)
        plt.xlim(-0.95,5)
        
        
        plt.subplot(1,2,2)
        plt.title(cf2_label + ' using ' + r'$\alpha_{12}$' + '=' + str(a21))
        plt.xlabel(tau_label)
        plt.ylabel(cf2_label)
        plt.ylim(0,1)
        plt.xlim(-0.95,5)
        
        
        Cf = 0.1 
        for index in range(1,11):
            
            #Cf1 vs tau
            plt.subplot(1,2,1)
            
            Cf1 = a12*Cf + (a12-1)/(np.exp(ttau)-1)
            plt.plot(tau, Cf1, label = r'$C_f2$=' + str(Cf1), color = [0.05,0.6,index/10.])
            
            
           
            #Cf2 vs tau
            plt.subplot(1,2,2)
            Cf2 = a21*Cf + (a21-1)/(np.exp(ttau)-1)
            
            plt.plot(tau, Cf2, label= cf2_label + '= ' + str(Cf), color= [0.05, 0.6, index/10.])

            
            Cf = round(Cf + 0.1,1)
            
        #plt.text(2.8,Sv1-0.05,r'$C_{f1}(1-e^{- \tau})=$' + str(Sv1),color='r',fontsize=10)    
        plt.show()
        plt.savefig(os.getcwd() + '/AlphaChangePlots/' + title + '(1).png',dpi=500)
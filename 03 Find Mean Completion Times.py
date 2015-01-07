import networkx as nx
import matplotlib.pyplot as plt
import operator
import os
import numpy as np
import random
import math
#os.chdir('C:\Users\moqri\Google Drive\UF\RanGen')
pos = {};pos['0']=(0,0);pos['1']=(1,1);pos['2']=(2,-1);pos['3']=(3,0);pos['4']=(4,-1);pos['5']=(5,1);pos['6']=(6,0)

def removeSeris():    
    for ed1 in G.edges():
        for ed2 in G.edges():      
            if ed1[0]=='0' or ed1[1]=='6' or (ed1!=ed2 and (ed1[0] == ed2[0] or ed1[1] == ed2[1])):
                break
        else:
            for ed3 in G.edges():
                if ed1[1]==ed3[0]:
                    G.add_edge(ed1[0],ed3[1])
            G.remove_node(ed1[1])

def removeParallel():    
    for nd1 in G.nodes():
        for nd2 in G.nodes():      
            for nd3 in G.nodes():    
                for nd4 in G.nodes():    
                    if nd3!=nd4 and (nd1,nd3) in G.edges() and (nd3,nd2) in G.edges() and (nd1,nd4) in G.edges() and (nd4,nd2) in G.edges():
                        for ed in G.edges():
                            if (ed[0] != nd1 and ed[1]==nd3) or (ed[0] != nd1 and ed[1]==nd4) or (ed[1] != nd2 and ed[0]==nd3) or (ed[1] != nd2 and ed[0]==nd4):
                                break
                        else:
                            G.remove_node(nd4)                                                
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
f = open('02 Random Networks.txt')
OUT= open('04 Completion Times.txt','w') 

countline=0
for line in f:
    print countline; countline=countline+1
    OUT.write(line.strip()+';')
    rand2nodes=random.sample(range(5), 2)
    OUT.write(str(rand2nodes[0]+1)+','+str(rand2nodes[1]+1)+'; ')

    mean = [1,1,1,1,1]
    cov = [[10,0,0,0,0],[0,10,0,0,0],[0,0,10,0,0],[0,0,0,10,0],[0,0,0,0,10]]
    for rep in range(0,3):
        if (rep==1):
            cov[rand2nodes[0]][rand2nodes[1]]=(5)
            cov[rand2nodes[1]][rand2nodes[0]]=(5)
        if (rep==2):
            cov[rand2nodes[0]][rand2nodes[1]]=(10)
            cov[rand2nodes[1]][rand2nodes[0]]=(10)            
        times=[]
        for repeat in range(1000):
            time=[0,0,0,0,0,0,0]
            time[1:6]= np.random.multivariate_normal(mean,cov)

            for i in range (1,7):            
                time[i]=max(time[i],0)
            PosWeight=map(float,time); NegWeight=[]
            for i in range(0,len(PosWeight)): NegWeight.append(operator.neg(PosWeight[i]))
            line=line.split(";")[0];            
            line=line.rstrip()
            G=nx.DiGraph()
            G.add_node('0');G.add_node('1');G.add_node('2');G.add_node('3');G.add_node('4');G.add_node('5');G.add_node('6')
            edges = line.split(' ')
            for edge in edges:  
                edge=edge.split('-')
                G.add_edge(edge[0],edge[1],w=NegWeight[int(edge[0])])
            pred, dist=nx.bellman_ford(G,'0',weight='w')               
            times.append(-dist['6'])  


        OUT.write(str(numpy.mean(times))+','+str(numpy.std(times))+';')
   
        if (rep==2):
            try:
                n=nx.shortest_path_length(G,str(min(rand2nodes[0],rand2nodes[1])+1),str(max(rand2nodes[0],rand2nodes[1])+1))
                OUT.write('series activities;')
        
            except nx.NetworkXNoPath:
                OUT.write('non-series activities;')        
        
        removed=1
        while removed==1:
            #nx.draw(G,pos)
            #plt.show()
            #raw_input("Press Enter to continue...")
            nodes=len(G.nodes())
            removeSeris()
            removeParallel()
            if nodes==len(G.nodes()): 
                removed=0
            else:
                removed=1
        if (rep==2):
            if len(G.nodes())>3:
                OUT.write('non-series-parallel Graph\n')       
            else:
                OUT.write('series-parallel Graph\n')     
OUT.close()

        


    






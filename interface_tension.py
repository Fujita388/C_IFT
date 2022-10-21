# ". venv/bin/activate"を実行すること

from scipy import integrate
import sys
import numpy as np

with open("stress_tensor.dat", "r") as f:
    lines = f.readlines()
ITF = []
for i in range(100):
    x_lis=[]
    y_lis=[]
    y = []
    for j in range(1000):
        k = i*1001+j+4
#        print(k)
        data = lines[k].split()
        x_lis.append(float(data[1])*102)  # *102で座標へ変換
        y.append((float(data[5])+float(data[6])-2*float(data[7]))/1061.208)  # /1061.208はave/chunkで出力されたものが応力テンソル*体積なので規格化している
    simps = integrate.simps(y,x_lis)
    print(simps)
    if i > 19:
        ITF.append(float(simps))
#print(y,x_lis)
#print(np.average(ITF), np.std(ITF)/np.sqrt(len(ITF)))

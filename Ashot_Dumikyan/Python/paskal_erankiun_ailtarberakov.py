#!/usr/bin/python
# -*- coding: utf-8 -*-

minchev = 1+ input("ներուծեք ձեր թիվը  ")
sp=[]
for i in range(0,minchev):
        sp.append([])
i=1
sp[0].append(1)
for i in range(1,minchev):
    sp[i].append(1)
    for j in range(1,i-1):
            k=sp[i-1][j-1]+sp[i-1][j]
            sp[i].append(k)
    sp[i].append(1)
sp.__delitem__(1)
for i in sp:
        print(i)
input()

exit ()
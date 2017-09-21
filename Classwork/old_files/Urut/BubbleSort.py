import random
import os
mass=[]

for i in range(10):
	mass.append(random.randint(0,100))
x=random.randint(0,1000)
count = 0

z=0
while (z<1000):
	print "LOADING[#                 ]" + str(z) +"%"
	os.system('sleep 0.001')                                                                         
	os.system('clear')
	z+=1
	print "LOADING[##                ]" + str(z) +"%"
	os.system('sleep 0.001')                                                                         
	os.system('clear')
	z+=1
	print "LOADING[###               ]"  + str(z) +"%"
	os.system('sleep 0.001')                                                                         
	os.system('clear')
	z+=1
	print "LOADING[####              ]"  + str(z) +"%"
	os.system('sleep 0.001')                                                                         
	os.system('clear')
	z+=1
	print "LOADING[#####             ]"  + str(z) +"%"
	os.system('sleep 0.001')                                                                         
	os.system('clear')
	z+=1
	print "LOADING[######            ]"  + str(z) +"%"
	os.system('sleep 0.001')                                                                         
	os.system('clear')
	z+=1
	print "LOADING[#######           ]" + str(z) +"%"
	os.system('sleep 0.001')                                                                         
	os.system('clear')
	z+=1
	print "LOADING[########          ]" + str(z) +"%"
	os.system('sleep 0.001')                                                                         
	os.system('clear')
	z+=1
	print "LOADING[#########         ]"  + str(z) +"%"
	os.system('sleep 0.001')                                                                         
	os.system('clear')
	z+=1
	print "LOADING[##########        ]"  + str(z) +"%"
	os.system('sleep 0.001')                                                                         
	os.system('clear')
	z+=1
	print "LOADING[###########       ]"  + str(z) +"%"
	os.system('sleep 0.001')                                                                         
	os.system('clear')
	z+=1
	print "LOADING[############      ]"  + str(z) +"%"
	os.system('sleep 0.001')                                                                         
	os.system('clear')
	z+=1
	print "LOADING[##############    ]"  + str(z) +"%"
	os.system('sleep 0.001')                                                                         
	os.system('clear')
	z+=1
	print "LOADING[################  ]"  + str(z) +"%"
	os.system('sleep 0.001')                                                                         
	os.system('clear')
	z+=1
	print "LOADING[##################]"  + str(z) +"%"
	os.system('sleep 0.1') 
	os.system('clear')	
	
	z+=50


print "Old Massive " + str(mass)	




for j in range(len(mass)):
	for i in range(len(mass)-1-j):
		if (mass[i]>mass[i+1]):
			mass[i],mass[i+1] = mass[i+1],mass[i]
			count+=1

print "In "+str(count)+" Steps"
 

print "Sorted massive" + str(mass)

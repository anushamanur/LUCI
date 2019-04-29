import cv2
import numpy as np
import csv
import glob
import pickle

#img = cv2.imread('1.tif',0)
#rows,cols = img.shape
arr = []
lab=[]
o=1
z=0
Files1=sorted(glob.glob("a/*.tif"))
Files2=sorted(glob.glob("b/*.tif"))
Files3=sorted(glob.glob("c/*.tif"))
Files4=sorted(glob.glob("d/*.tif"))

for file1,file2,file3,file4 in zip(Files1, Files2, Files3, Files4):
	img1=cv2.imread(file1,0)
	img2=cv2.imread(file2,0)
	img3=cv2.imread(file3,0)
	img4=cv2.imread(file4,0)
	#print (file1)
	
	#print (img.shape)
	rows,cols= img1.shape
	#t=row*cols
	for i in range(rows):
		for j in range(cols):
			a=img1[i,j]
			b=img2[i,j]
			c=img3[i,j]
			d=img4[i,j]	
			t=[]
			t.extend((a,b,c,d))
			l=[]
			# order - water forest desert snow N/A
			if((a>=0 and a<=74) and (b>=0 and b<=51) and (c>=0 and c<=25 ) and (d>=0 and d<=25)):
				#print ("water") 
				l.extend((o,z,z,z,z)) 
			elif ((a>=0 and a<=39) and (b>=0 and b<=25) and (c>=26 and c<=134) and (d>=11 and d<=117)):
				#print ("forest")
				l.extend((z,o,z,z,z)) 
			elif ((a>=111 and a<=240) and (b>=135 and b<=250) and (c>=130 and c<=255) and (d>=13 and d<=90)):
				#print ("snow")
				l.extend((z,z,z,o,z))
			elif ((a>=95 and a<=200) and (b>=80 and b<=210) and (c>=55 and c<=222) and (d>=91 and d<=235)):
				#print ("desert")
				l.extend((z,z,o,z,z)) #desert
			else :
				#print ("none")
				l.extend((z,z,z,z,o)) #none
			arr.append(t)
			lab.append(l)


#PIK1 = "pix.dat"
PIK2 = "label.dat"
#print("pix-dump")
#with open(PIK1, "wb") as f:
#    pickle.dump(arr, f)   
print("label-dump")
with open(PIK2, "wb") as f:
    pickle.dump(lab, f)
	

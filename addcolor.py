import pickle
from PIL import Image
import cv2
import numpy as np

arr=[]
label=[]

PIK = "label.dat"
#res = Image.new('RGB', (450,450))

res = np.zeros((450,450,3), np.uint8)
#res[:,0:0.5*450] = (255,0,0)      # (B, G, R)
#res[:,0.5*450:450] = (0,255,0)

with open(PIK, "rb") as f:
    label= pickle.load(f)
    
for i in range(0,449):
	for j in range(0,449):
		if label[i]==[1,0,0,0,0]: #water
			res[i][j]= [255,0,0]
			print ("water") 
		elif label[i]==[0,1,0,0,0] : #forest
			res[i][j]= [0,255,0]
		elif label[i]==[0,0,1,0,0] : #desert
			res[i][j]= [0,51,102]
			print("d")
		elif label[i]==[0,0,0,1,0] : #snow
			res[i][j]= [255,255,153]
		elif label[i]==[0,0,0,0,1] : 
			res[i][j]= [102,178,255] #NA
	
			
cv2.imshow("res",res)
cv2.waitKey(0)	
#print res.shape
#print label.size
#print res[0][0]	
#print res[0][1]	
#print res[0][2]	
#print res[0][3]	
#print res[0][4]	
'''print res[0][5]	
print res[0][6]	
print res[0][7]	
print res[0][8]	'''
#rgb = cv2.cvtColor(res,cv2.COLOR_GRAY2BGR)
rgb = cv2.applyColorMap(res, cv2.COLORMAP_JET)	
cv2.imwrite("res.jpg",rgb)

	 	
	

	
	

    		



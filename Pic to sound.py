from PIL import Image #i want to preface, this file was very quickly done and thrown together, im dont know anything about algorithms to make the code quicker, maybe when I get into compsci I can learn it ;)
import winsound
from random import randint

def myMap(n, start1, stop1, start2, stop2):

  return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

types= ['png','jpg']
img = input("Please write the name of the image file (jpg,png), JPG and PNG are the only supported formats\nWrite it here: ") #stores user input
imgSPLIT = img.split('.') #This is used to seperate the file name and extension for error checking later

if len(imgSPLIT) != 2:  #If the file doesnt have an extension or has more than 1 extension, its a file we dont want to process
  print("ERROR, unexpected file extension")
  exit()

elif imgSPLIT[1] not in types:
  print("ERROR, unexpected file extension")
  exit()


try:
  picture = Image.open(img)
  pic = picture.load()        #This try catch checks to see if the file exists. If an error is returned, the program stops
except Exception as e:
  print(f"ERROR {e}")
  exit()
picture.show()
for i in range(picture.size[0]): #rows
  for y in range(picture.size[1]):


    cols = [pic[i,y][0],pic[i,y][1],pic[i,y][2]]
    cols = sorted(cols)
    x = abs(int(myMap(cols[2]-(cols[1]+cols[0]),0,255,37,32767/4)))

   
    winsound.Beep(x,randint(0,750))

# This microservice monitors imgSrv.txt for a digit representing the image set that was last shown to the user
# If the digit changes, the paths to all 9 images from a different image set are written to imgPath.txt

import random
import time

def main():
    print('image microservice running...')
    prevImgSetNum = None #used to detect changes in imgSrv.txt

    while True:
        #read current image set number from file
        with open('imgSrv.txt','r') as readfile:
            currImgSetNum = readfile.read().strip()

        #only update paths if imgSrv.txt has been updated
        if currImgSetNum != prevImgSetNum:
            print('New image set requested')

            #ensure that new set is different than previous
            newImgSetNum = currImgSetNum
            while newImgSetNum == currImgSetNum:
                #generate random number for image set
                newImgSetNum = str(random.randint(1,10))

            #write all 9 file paths from the set to imgPath.txt
            with open('imgPath.txt','w') as writefile:
                print('Writing paths to image set ' + newImgSetNum + ' to file')
                for i in range(1,10):
                    imgPath = './images/' + newImgSetNum + '/' + str(i) + '.png\n'
                    writefile.write(imgPath)

            #Update tracker
            prevImgSetNum = currImgSetNum
            
        else:
            time.sleep(0.1)



if __name__ == "__main__":
    main()


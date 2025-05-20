import time

def main():
    while True:
        num = input('Enter a digit: ')
        with open('imgSrv.txt','w') as writefile:
            writefile.write(num)

        time.sleep(1)

        with open('imgPath.txt','r') as readfile:
            paths = readfile.read()
        
        print('File paths:')
        print(paths)


if __name__ == "__main__":
    main()
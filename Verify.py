import os

def main():

    #Handbrake generates logs every time you encode. Paste in where it's located on your PC
    HandbrakeLogDirectory="C:\\Users\\Anton\\AppData\\Roaming\\HandBrake\\logs"
    
    #os.chdir(HandbrakeLogDirectory)
    cwd=os.getcwd()
    print(cwd)

    #for filename in os.listdir(HandbrakeLogDirectory):
    #    print(filename)









if __name__ == '__main__':
    main()

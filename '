import os

def main():

    #Handbrake generates logs every time you encode. Paste in where it's located on your PC
    HandbrakeLogDirectory="C:\\Users\\Anton\\AppData\\Roaming\\HandBrake\\logs"
    
    #This is the string that will pop up numerous times in each log where subtitles are borked
    Error="time went backwards"

    #change your working directory to where the logs are stored
    os.chdir(HandbrakeLogDirectory)

    for filename in os.listdir(HandbrakeLogDirectory):
        with open(filename, 'r') as fp:

            #dumps all lines into the content variable
            content=fp.read()
            
            if Error in content:
                print(filename)





if __name__ == '__main__':
    main()

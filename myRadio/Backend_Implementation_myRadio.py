# length of audio file, length of genre, size of audio array, which array to choose from

import backend_arrays_data
from pydub import AudioSegment 

import random
import math
#database periodic files
period = backend_arrays_data.period
# period={"Pop": ["bro","sis","dad"], "RnB" : ["tired","suicidal","death","cry"], "Country": ["weed","spiritual","zen"], "news": ["sports","president","elections"]}
#user inputted periodic variables' dict
front_Inp_Per=[["Pop",5],["RnB",20],["News",30],["Country",15],["Pop",17]]
#database frequency files
frequent = backend_arrays_data.frequent
#user inputted frequency variables' dict
front_Inp_Fre={"Jokes":1,"Riddles":15,"Voice":20}
hasJokes=False
hasRiddles=False
hasVoiceNotes=False
divisions=len(front_Inp_Per)
#func for total time
def totalTime():
    time=0
    for i in range(len(front_Inp_Per)):
        
        time+=front_Inp_Per[i][1]
    return time*60000
time=totalTime()      

def genreLength(track):
    genreTime = 0
    for song in track:
        genreTime += backend_arrays_data.get_time(song)
    return genreTime

if front_Inp_Fre["Voice"]!=0:
    hasVoiceNotes=True

#method to make a group of new random periodic audio files
def newAudioRand(genre,time):
    out=[]
    totalTime=0
    genreTrack = period[genre]
    random.shuffle(genreTrack)
    i=0
    while(True):
        out.append(genreTrack[i%len(genreTrack)])
        totalTime+=backend_arrays_data.get_time(genreTrack[i%len(genreTrack)]) #change to time
        i+=1
        if (totalTime >= time):
            return out

news=[] #keep track of where news are as they are not overwritten by frequency variables
# #returns array with periodic audio files
def makePeriodicAudioFiles():
    output=[]
    for i in range(len(front_Inp_Per)):
        temp=[]
        temp=newAudioRand(front_Inp_Per[i][0],60000*front_Inp_Per[i][1])
        if front_Inp_Per[i][0]=="news":
            news.append(i)
        output.append(temp)
    return output
    

# returns riddle and voicenote freq files array and freq
def freqFiles():
    riddleFreq=front_Inp_Fre["Riddles"]
    riddleNum=0
    if riddleFreq!=0:
        hasRiddles=True
        riddleNum= math.ceil(time/(60000*riddleFreq))
        usedRiddles=frequent["Riddles"]
        random.shuffle(usedRiddles)
        finalRid=[]
        for i in range(riddleNum):
            finalRid.append(usedRiddles[i%len(usedRiddles)])
    voiceNoteFreq=front_Inp_Fre["Voice"]
    if voiceNoteFreq!=0:
        hasVoiceNotes=True
        voiceNoteNum= math.ceil(time/(60000*voiceNoteFreq))
        usedVoiceNotes=frequent["Voice"]
        random.shuffle(usedVoiceNotes)
        finalVoiceNote=[]
        for i in range(voiceNoteNum):
            finalVoiceNote.append(usedVoiceNotes[i%len(usedVoiceNotes)])
    global dictAfterJoke
    dictAfterJoke={"riddleNum" : riddleNum, "voiceNoteNum" : voiceNoteNum, "riddlesAre": finalRid, "voiceNotesAre":finalVoiceNote}



# #returns joke freq files and each's period
def randJokes():
    arrayOut=[]
    overTime=0
    usedJokes=backend_arrays_data.frequent["Jokes"]
    random.shuffle(usedJokes)
    x=0
    while(True):
        
        i=random.randint(5,20)
        overTime+=i*60000
        
        x+=1
        arrayOut.append([usedJokes[x%len(usedJokes)],i])
        if overTime>time:
            break
    return arrayOut

# #implements jokes if toggled
if front_Inp_Fre["Jokes"]==1:
    hasJokes=True
    global jokes
    jokes= randJokes()

# #print(time)
# #print(makePeriodicAudioFiles())
# #print(freqFiles())
def overWriteJ():
    global x 
    x = makePeriodicAudioFiles()
    arrayIn=x
    if hasJokes:
        arrayJokes=jokes
        print(arrayJokes)
        timeSoFarJ=0
        arrayOut=[]
        y=0
        global temp2
        temp2=[]

        for i in range(divisions):
            temp=[]
            
            for j in range(len(arrayIn[i])):
                timeNowJ=backend_arrays_data.get_time(arrayIn[i][j])
                timeSoFarJ+=timeNowJ
                lengthIn=60000*arrayJokes[y][1]-timeSoFarJ
                if lengthIn>=0:
                    temp.append(arrayIn[i][j])
                    j+=1
                else:
                    
                    if i in news:
                        timeSoFarJ=0
                        i+=1
                        j=0
                        break
                    var1 = arrayIn[i][j][:lengthIn].fade_out(2000)
                    var2 = arrayIn[i][j][lengthIn:].fade_in(2000)
                    temp2.append(str(i)+","+str(j))

                        
                    temp.append(var1+arrayJokes[y][0]+var2)
                    timeSoFarJ=0
                    timeNowJ=0
                    y+=1
                    j+=1
            arrayOut.append(temp)
    else: arrayOut=arrayIn
    return arrayOut
# print(overWriteJ())
# print(temp2)





def overWriteVN():
    beforeVN=afterJokes
    global temp3
    temp3=[]
    if hasVoiceNotes:
        arrayVN=dictAfterJoke["voiceNotesAre"]
        timeSoFarJ=0
        arrayOut=[]
        y=0
        

        for i in range(divisions):
            temp=[]
            
            for j in range(len(beforeVN[i])):
                timeNowJ=backend_arrays_data.get_time(beforeVN[i][j])
                timeSoFarJ+=timeNowJ
                lengthIn=60000*front_Inp_Fre["Voice"]-timeSoFarJ
                if lengthIn>=0:
                    temp.append(beforeVN[i][j])
                    j+=1
                else:
                    print(news)
                    print(temp2)
                    if i in news:
                        timeSoFarJ=0
                        i+=1
                        j=0
                        break
                    if i in temp2 and j in temp2[i]:
                        timeSoFarJ=0
                        j+=1
                        break
                    var1 = beforeVN[i][j][:lengthIn].fade_out(2000)
                    var2 = beforeVN[i][j][lengthIn:].fade_in(2000)
                    temp3.append(str(i)+","+str(j))

                        
                    temp.append(var1+arrayVN[y]+var2)
                    timeSoFarJ=0
                    timeNowJ=0
                    y+=1
                    j+=1
            arrayOut.append(temp)
    else: arrayOut=beforeVN
    return arrayOut

def makeAudioFile():
    output_File = AudioSegment.empty()
    global afterJokes
    afterJokes=overWriteJ()
    freqFiles()
    currOut= overWriteVN()
    # other methods then next thing
    for track in currOut:
        for song in track:
            output_File = output_File + song
    output_File.export("Final12.mp3", format = "mp3")

makeAudioFile()
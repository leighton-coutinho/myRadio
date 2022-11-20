from django.shortcuts import render
from django.http import HttpResponseRedirect, FileResponse, HttpResponse
from .forms import RecordingForm

# Create your views here.
def index(request):
    submitted=False
    if request.method == "POST":
        form = RecordingForm(request.POST)
        mydict = request.POST.dict()
        mycount = 0
        mymusarray = [[]]
        mynewdict = {}
        #convert first 20 key and value pairs into 2D array for music/news function
        for key in mydict:
            if (key == 'csrfmiddlewaretoken' or mydict[key] == ""):
                mycount += 1
                continue
            if (mycount <= 20):
                if (mycount % 2 == 1):
                    mymusarray.append([mydict[key],''])
                else:
                    #change second element of last index
                    mymusarray[-1][1] = mydict[key]
            else:
                #means we are doing jokes, riddles and files
                mynewdict[key] = mydict[key]
            mycount += 1
        mymusarray.pop(0)
        print(mydict)
        print(mymusarray)
        #id box is unchecked, mynewdict will not have a key value pair for jokes i.e j
        print(mynewdict)
        img = open('MyFM/static/media/myaudio.mp3', 'rb')
       # response = HttpResponse()
       # response.write(img.read())
        #response['Content-Type'] ='audio/mp3'
       # return response
       # response = FileResponse(img)
        #return response
        return HttpResponseRedirect('submitted')
    #do what we want with the submitted form here using request.POST or request.body
    form = RecordingForm
    #this means we are done so we redirect to a submitted page after we parse the data and call our functions
    return render(request,'index.html',{'form':form})

def submittedview(request):
    return render(request,'submitted.html')


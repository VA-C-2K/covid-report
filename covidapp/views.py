from django.shortcuts import render
import requests
import json


url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "e7e6c4d562mshc834ed1be88c9bfp1e6d82jsn2b5def4d143d",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()
# Create your views here.
def helloworldview(request):
    mylist=[]
    noofresult=int(response['results'])
    for x in range(0,noofresult):
        mylist.append(response['response'][x]['country'])
    
    if request.method=="POST":
        selectedcountry=request.POST['selectedcountry']
        for x in range(0,noofresult):
            if selectedcountry==response['response'][x]['country']:
                new=response['response'][x]['cases']['new']
                active=response['response'][x]['cases']['active']
                critical=response['response'][x]['cases']['critical']
                recovered=response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                deaths=int(total)-int(active)-int(recovered)
        context={'selectedcountry':selectedcountry,'mylist':mylist,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':total,'deaths':deaths}
        return render(request,'helloworld.html',context)
    
    """[summary]mylist=[]
    for x in range(0,noofresult):
        mylist.append(response['response'][x]['country']) """ 
    context={'mylist':mylist}
    return render(request,'helloworld.html',context)
    
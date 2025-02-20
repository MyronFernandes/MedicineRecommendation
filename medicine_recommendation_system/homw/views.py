import os
import pickle
from django.shortcuts import render
from medicine_recommendation_system.settings import STATICFILES_DIRS
file_path = os.path.join(STATICFILES_DIRS[0], 'Medicine.pkl')
data = pickle.load(open(file_path,"rb"))
def index(request):
    li=[]
    for d in data['Medicine Name']:
        li.append(d)
    lig=[]
    for d in data['Uses']:
        lig.append(d)
    return render(request, 'first.html',{'Mn':li,'Mu':lig})
def display(request):
    if request.method == 'POST':
        name = request.POST.get('selectedMedicineName')
        li=name.split("%")
        dict={}
        index=[]
        for i in li:
            ind=data.index[data['Medicine Name'] == i].tolist()
            for inde in ind:
                index.append(inde)
        for ind in index:
            dict[ind]=[data.loc[ind,'Medicine Name'],data.loc[ind,'Uses'],data.loc[ind,'Side_effects'],data.loc[ind,'Image URL'],data.loc[ind,'Manufacturer']]
    return render(request,"index.html",{'dict':dict})
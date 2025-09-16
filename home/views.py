from django.shortcuts import render,HttpResponse
import joblib



model=joblib.load('static/random_forest_regressor')

# Create your views here.
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def prediction(request):
    if request.method=="POST":
        age=int(request.POST.get('age'))
        sex=int(request.POST.get('sex'))
        bmi=int(request.POST.get('bmi'))
        children=int(request.POST.get('children'))
        smoker=int(request.POST.get('smoker'))
        region=int(request.POST.get('region'))
        
        # print(age,bmi,children,smoker,region)
        
        pred=model.predict([[age,sex,bmi,children,smoker,region]])
        
        # print(pred)
        
        output={
            "output": pred[0]
        }
        return render(request,'prediction.html',output)
    else:
        return render(request,'prediction.html')
    
def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')
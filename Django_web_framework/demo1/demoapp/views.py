from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponsePermanentRedirect,Http404,HttpResponseNotFound
from django.urls import reverse
from django.views import View #for class based
from . import forms



def index(request, id):  # http://127.0.0.1:8000/index/5

    print(request.method)
    print(request.FILES)
    print(request.COOKIES)
    print(request.user)

    meta=request.META

    # for k,v in meta.items():
    #    print(f"{k}:::::{v}")
    path=request.path
    scheme=request.scheme
    address=request.META['REMOTE_ADDR']
    user_agent=request.META['HTTP_USER_AGENT']
    path_info=request.path_info
    response=HttpResponse()
    response.headers['age']=25
    content = """<h1> Hello, {}. This is the index view of Demo app. </h1 ><p>Path is {}<p>
    <p>scheme is {}<p>
    <p>address is {}<p>
    <p>user_agent is {}<p>
    <p>path_info is {}<p>
    <p>header is {}<p>
    """.format(id,path, scheme, address, user_agent, path_info, response.headers)
    return HttpResponse(content)


def home(request):  # http://127.0.0.1:8000/index/?name=sandy
    print(request)
    try:
        if request.GET['name']:
            return HttpResponse(request.GET['name'])
    except :

        #raise Http404("hi")
        return HttpResponseNotFound('hi page not found')

def showform(request):  # http://127.0.0.1:8000/register/
    form=forms.ApplicationForm()
    return render(request,'forms.html',{'form':form})

# def getform(request):
#     print(request)
#     print(request.COOKIES)
#     if request.method=='POST':
#         name=request.POST['name']
#         pas = request.POST['password']

#         content=f"<h1> Name is {name} and password is {pas}<h1>" #post  http://127.0.0.1:8000/register/ to http://127.0.0.1:8000/user/
#         return HttpResponse(content)
#     #return redirect('../register/')  # http://127.0.0.1:8000/register/  with get method
#     return HttpResponsePermanentRedirect(reverse('demoapp:register'))  #Django’s reverse() function returns the URL path to which it is mapped.

class Getform(View):
    def get(self,req):
        return HttpResponsePermanentRedirect(reverse('demoapp:register'))
    def post(self,req):
        print(req.POST)
        # name= req.POST.get('name')
        # pas=req.POST.get('password')
        # # post  http://127.0.0.1:8000/register/ to http://127.0.0.1:8000/user/
        form_data = forms.ApplicationForm(req.POST,req.FILES)
        if not form_data.is_valid():
             print(form_data.errors)  # Logs a dictionary of field errors

        if form_data.is_valid():
            form_data.save()
            name=form_data.cleaned_data["name"] 
            apply=form_data.cleaned_data["applying_to"] 

            content = f"<h1> Name is {name} and applying to {apply}<h1>"
            return HttpResponse(content)
        else:
            return HttpResponsePermanentRedirect(reverse('demoapp:register'))

def reg(request,num):
    return HttpResponse("HI")
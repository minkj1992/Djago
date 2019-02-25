from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')
    # if request.method=='POST':
    #     form = ProductForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         post.save()
    #         # session을 통해서 show랑 변수 공유
    #         # request.session['image']=request.POST.get("name")
    #         return redirect('/search/' + str(post.id))
    # else: form=ProfileForm()
    # # return render(request,'upload.html',{'form':form})  

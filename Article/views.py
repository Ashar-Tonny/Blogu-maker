from django.shortcuts import render,redirect
from .models import Article
from .form import create
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
# Create your views here.
def Display_view(request):
    data = Article.objects.all().order_by('Creation_date')
    return render(request,"Article.html",{"Data":data})

def Detail_view(request,content):
    details = Article.objects.get(slug = content)
    return render(request,'content.html',{"Details":details})

                            #CRUD operations

# Create view

@login_required(login_url='Accounts:logger')
def create_view(request):
    if request.method == "POST":
        form = create(request.POST, request.FILES)
        if form.is_valid():
            saving = form.save(commit=False)
            saving.Author = request.user
            saving.save()
            return redirect('Article:home')
    else:
        form = create()
    return render(request,"create_blog.html",{"Form":form})
def update_view(request,index):
    Index = get_object_or_404(Article,id = index)
    if request.method == 'POST':
        
        form = create(request.POST, request.FILES, instance=Index)
        if form.is_valid():
            form.save()
            return redirect('Article:details', content=Index.slug)
    else:
        form = create(instance=Index)
    return render(request,"update.html",{"Form":form, "Details":Index, "index":index})

@login_required(login_url='Accounts:logger')
def delete_view(request,index):
    article = get_object_or_404(Article, id=index)
    if request.method == 'POST':
        article.delete()
        return redirect('Article:home')
    return render(request, 'delete_confirm.html', {'article': article})
            
            
        






from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog
# Create your views here.

def welcome(request):
    return render(request, 'viewcrud/index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'viewcrud/funccrud.html', {'blogs':blogs})

def create(request):
    # 새로운 데이터 블로그 글 저장하는 역할 == POST
    if request.method == 'POST':
        # 입력된 블로그 글들을 저장해라
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False) #아직 저장하지않고
            post.pub_date = timezone.now() #현재 날짜 저장후
            post.save()                    #저장
            return redirect('home')

    # 글쓰기 페이지를 띄워주는 역할 == GET (!=POST)
    else:
        #단순히 입력받을 수 있는 form을 띄워줘라
        form = NewBlog()
        return render(request, 'viewcrud/new.html',{'form':form})
 

def update(request, pk):
    # 수정할 블로그 객체를 가져오기
    blog = get_object_or_404(Blog, pk = pk)

    # 해당하는 블로그 객체 pk에 맞는 입력공간
    form = NewBlog(request.POST, instance=blog) 

    if form.is_valid():
        form.save()                   
        return redirect('home')
    return render(request, 'viewcrud/new.html', {'form':form})
   

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk) # 삭제하고 싶은 특정 블로그 가져옴
    blog.delete()
    return redirect('home')

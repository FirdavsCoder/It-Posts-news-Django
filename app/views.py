from tabnanny import process_tokens
from django.shortcuts import render

from .models import Post

def main(request):
    
    post = Post.objects.all()
    return render(request,'blog/basic.html',{"posts":post})



def post_detail(request,id):    
    posts=Post.objects.get(id=id)
    return render(request,'blog/post_detail.html',{"posts":posts})





from django.shortcuts import render,redirect 

def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login-user")
        # return render(request,"loginpage.html")
    context={}
    return render(request,"chatpage.html",context)
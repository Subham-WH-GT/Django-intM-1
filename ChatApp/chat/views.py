from django.shortcuts import render,redirect 
from .models import Chat,Group
def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        # print("not authenticated")
        return redirect("login-user")
        # return render(request,"loginpage.html")
    context={
        'viewname':'chatPage',
    }
    # print("authenticated")
    # print(request.META)
    return render(request,"chatpage.html",context)

def groupchat(request,group_name):
    # group=Group.objects.get(name=group_name)
    # chats=[]
    # if (group):
    #     chats=Chat.objects.filter(group=group_name)    
    # else:
    #     group=Group(name=group_name)
    #     group.save()
    group, created = Group.objects.get_or_create(name=group_name)
    chats = Chat.objects.filter(group=group) if not created else []

    context={
        'viewname':'groupchat',
        'groupname':group_name,
        'chats':chats,
    }
    return render(request,"chatpage.html",context)

from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt


url = "https://api.github.com/users/"

@csrf_exempt
def index(request):
    if request.method == "POST":
        githubname = request.POST.get("githubname")
        response_user = requests.get(url+githubname)
        user_info = response_user.json()

        response_repos = requests.get(url+githubname+"/repos")
        repos_info = response_repos.json()

        if "message" in user_info:
            error = "Kullanıcı adı bulunamadı."
            return render(request,"index.html",{"error":error})
        else:
            return render(request,"index.html",{"info":user_info,"repos":repos_info})
    else:
        return render(request,"index.html")

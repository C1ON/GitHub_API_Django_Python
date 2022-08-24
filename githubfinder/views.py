from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_exempt


url = "https://api.github.com/users/"

@csrf_exempt
def index(request):
    if request.method == "POST":
        githubname = request.POST.get("githubname")
        response_user = requests.get(url+githubname)
        user = response_user.json()

        response_repos = requests.get(url+githubname+"/repos")
        repos = response_repos.json()

        if "message" in user:
            error = "Kullanıcı adı bulunamadı."
            return render(request,"index.html",{"error":error})
        else:
            return render(request,"index.html",{"info":user,"repos":repos})
    else:
        return render(request,"index.html")

from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login ,logout 
# Create your views here.
User = get_user_model()



#registration logic
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name", "")
        last_name  = request.POST.get("last_name", "")
        username   = request.POST.get("username")
        email      = request.POST.get("email")
        password1  = request.POST.get("password1")
        password2  = request.POST.get("password2")
        check=User.objects.filter(username=username).exists()
        if check:
            return render(request, "accounts/register.html", {"error": "Username already taken"})
        if User.objects.filter(email=email).exists():
            return render(request, "accounts/register.html", {"error": "Email already registered"})
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, "accounts/register.html", {"error": "Username already taken"})
            
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name, 
                last_name=last_name,
                
            )
            
            
            return redirect("accounts:login")
        else:
            return render(request, "accounts/register.html", {"error": "Passwords do not match"})

    return render(request, "accounts/register.html")

#login logic
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Step 1: Check credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # ✅ Step 2: Log the user into session
            login(request, user)

            # Optional: handle next redirect
            next_url = request.POST.get("next")
            if next_url:
                return redirect(next_url)

            return redirect("BlogUpload:display_blogs")

        else:
            return render(request, "accounts/login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "accounts/login.html")

#logout logic
def logoutt(request):
    logout(request)
    return redirect("accounts:login")



    

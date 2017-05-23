from django.shortcuts import render, redirect;
from django.contrib import auth;

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
	if request.method == "GET":
		return render(request, "auth/login.html");
	elif request.method == "POST":
		username = request.POST['username'];
		password = request.POST['password'];
		# make sure the username and password is good
		user = auth.authenticate(username=username, password=password);
		if user is not None:
			if user.is_active:
				#associate the user with the session
				auth.login(request, user);

				#read the destination
				next = "";
				if "next" in request.GET:
					next = request.GET["next"];
				if next == None or next == "":
					next = "/";
				return redirect(next);
			else:
				#account is disabled
				return render(request, 'auth/login.html', { "warning" : "Yout account is disabled, please contact your administrator" });
			
		else:
			# non existant user
			return render(request, 'auth/login.html', { "warning" : "invalid username and or password" });

def register(request):

     if request.method == "GET":
         return render(request, "auth/register.html");
     elif request.method == "POST":
         username = request.POST["username"];
         password = request.POST["password"];
         email = request.POST["email"];
         # call create_user from the ORM. Make sure you call save!
         auth.models.User.objects.create_user(username, email, password).save();
         #log users in
         user = auth.authenticate(username = username, password = password);
         return render(request, "auth/registered.html");

				

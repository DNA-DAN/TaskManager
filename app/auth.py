from django.shortcuts import render, redirect;
from django.contrib import auth;

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
				
				
				

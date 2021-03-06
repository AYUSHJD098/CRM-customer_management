from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kargs):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kargs)
	return wrapper_func



def allowed_users(allowed_roles=[]):
	def decorators(view_func):
		def wrapper_func(request, *args, **kargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name 
			if group in allowed_roles:
				return view_func(request, *args, **kargs)
			else:
				return HttpResponse(' You are not authorized to visit this page (403)')
		return wrapper_func
	return decorators

                        
import requests
from django.shortcuts import render
from django.views import View
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponse, JsonResponse

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            url = "http://127.0.0.2:8002/auth/register/"

            data = {
                'username': username,
                'password': password,
                'email': email
            }
            response = requests.post(url, json=data)
            if response.status_code == 201:
                return HttpResponse('You have successfully registered')
            else:
                return HttpResponse(f"Error: {response.json()['detail']}")
        return HttpResponse("Form is not valid")

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            api_url = 'http://127.0.0.2:8002/auth/login/'

            data = {
                "username_or_email": username_or_email,
                "password": password
            }
            response = requests.post(api_url, json=data)

            if response.status_code == 200:
                return JsonResponse({'message': 'Successfully logged in!', 'data': response.json()})
            else:
                return JsonResponse({'error': 'Failed to login', 'details': response.json()},
                                    status=response.status_code)

class PostGetView(View):
    def get(self, request):
        page = requests.get("http://127.0.0.2:8002/posts/?size=2").json()['page']
        pages = requests.get("http://127.0.0.2:8002/posts/?size=2").json()["pages"]

        if page is not None:
            data = requests.get(f"http://127.0.0.2:8002/posts/?page={page}&size=2").json()["items"]
            return render(request, "post.html",
                          context={"posts": data, "pages": pages, "page": page, "next": int(page) + 1,
                                   "previous": int(page) - 1})

        return render(request, "post.html", context={"message": "Not found"})

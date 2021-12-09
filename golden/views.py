from django.shortcuts import render

# Create your views here.
from golden.serializer import ProfileSerializer, ProjectSerializer
from django.http.response import HttpResponseRedirect
from golden.models import Profile, Project, Reviews
from golden.forms import ProjectForm, ReviewForm, SignupForm, UserProfileForm
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


def index(request):
    projects = Project.objects.all()
    profile = Profile.objects.all()
    review = Reviews.objects.all()
    return render(request,'index.html', {'projects':projects,'profile':profile,'review':review})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})

@login_required(login_url='/accounts/login/')    
def profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if  profile_form.is_valid():
            profile_form.save()
            return redirect('home')
    else:
        profile_form = UserProfileForm(instance=request.user)
        # user_form = UserUpdateForm(instance=request.user)
    return render(request, 'profile.html',{ "profile_form": profile_form})

@login_required(login_url='/accounts/login')
def project(request):
	current_user = request.user
	if request.method == 'POST':
		form = ProjectForm(request.POST,request.FILES)
		if form.is_valid():
			new_project = form.save(commit=False)
			new_project.user = current_user
			new_project.save()
			return redirect('index')
	else:
			form = ProjectForm()
	return render(request, 'project.html',{"form":form})

@login_required(login_url='/accounts/login')
def project_view(request,id):
    project = Project.objects.get(id = id)
    reviews = Reviews.objects.all()
    return render(request, 'project_view.html',{"reviews":reviews,"project":project})

@login_required(login_url='/accounts/login/')
def review_project(request,project_id):
    proj = Project.project_by_id(id=project_id)
    project = get_object_or_404(Project, pk=project_id)
    current_user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():

            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            review = Reviews()
            review.project = project
            review.user = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.average = (review.design + review.usability + review.content)/3
            review.save()
            return HttpResponseRedirect(reverse('projectdetails', args=(project.id,)))
    else:
        form = ReviewForm()
    return render(request, 'reviews.html', {"user":current_user,"project":proj,"form":form})

def search_project(request): 
    if 'project' in request.GET and request.GET['project']:
        name = request.GET.get("project")
        searchResults = Project.search_by_project_title(name)
        message = f'name'
        params = {
            'results': searchResults,
            'message': message
        }
        return render(request, 'search.html', params)
    else:
        message = "You haven't searched for any project"
    return render(request, 'search.html', {'message': message})

class ProfileList(APIView):
   
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
   
    
class ProjectList(APIView):
   
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    
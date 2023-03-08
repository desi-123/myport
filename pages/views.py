from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About, Skill, Project, Contact, Resume

def index(request):
 about = About.objects.all()
 skills = Skill.objects.all()
 projects = Project.objects.all()
 resumes = Resume.objects.all()
 context = {
  'about': about,
  'skills': skills,
  'projects': projects,
  'resumes': resumes,
 }

 # Contact
 if request.method == 'POST':
  name = request.POST['name']
  email = request.POST['email']
  phone = request.POST['phone']
  message = request.POST['message']
  user_id = request.POST['user_id']
  contact = Contact(name=name, email=email, phone=phone, message=message, user_id=user_id)

    # Check if user has made inquiry already
  if request.user.is_authenticated:
   user_id = request.user.id
   has_contacted = Contact.objects.all().filter(user_id=user_id)
   if has_contacted:
    messages.error(request, 'You have already messaged to Desalegn Wagaw!')
    return redirect('index')

  contact.save()
  messages.success(request, 'Your message has been submitted to Desalegn Wagaw!')


 return render(request, 'pages/index.html', context)



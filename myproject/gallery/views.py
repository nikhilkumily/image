# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View,TemplateView
# from django.views.generic.list import ListView
from django.shortcuts import render,redirect
from .models import Gallery,Photos,UserContinuation,User
from .forms import GalleryForm,ImageForm,AddUserForm,UserForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Create your views here.


# class GalleryListView(ListView):
#     model = Gallery
#     queryset= Gallery.objects.all()
#     template_name = 'gallerylist.html'


class GalleryListView(View):
    template_name='gallerylist.html'
    def get(self,request):
        obj=Gallery.objects.all()
        context={
        'gallery_list':obj
        }
        return render(request,self.template_name,context)



# class ImageListView(ListView):
#     model = Photos
#     queryset= Photos.objects.all()
#     template_name = 'imagelist.html'

class ImageListView(View):
    template_name='imagelist.html'
    def get(self,request):
        obj=Photos.objects.all()
        context={
        'image_list':obj
        }
        return render(request,self.template_name,context)


class ImageListView2(View):
    template_name='imagelist2.html'
    def get(self,request):
        obj=Photos.objects.all()
        context={
        'image_list2':obj
        }
        return render(request,self.template_name,context)



class HomeView(TemplateView):
    template_name = 'home.html'

class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(View):
    template_name = 'login.html'
    # template_name1 = 'about.html'

    def get(self,request):

            form = UserForm
            return render(request,self.template_name,{'form':form})

    def post(self,request):

        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            # if user.is_active:
                login(request, user)
                return redirect("home")
            # if request.user.is_staff:
            #     return redirect('home')
            # else:
            #     return redirect('index')
          
        else:
            return redirect('index')
       

class Gallery_views(View):
    template_name = 'addgallery.html'
    form_class = GalleryForm

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            obj = Gallery.objects.create(
                userdata = request.user,
                description = request.POST.get('description'),
                g_name = request.POST.get('g_name'),
                )
                                
            obj.save()

            return redirect('gallerylist')
        else:
            form = self.form_class()
            return render(request,self.template_name,{'form':form})



class Image_views(View):
    template_name = 'addimage.html'
    form_class = ImageForm

    def get(self,request):
        form = self.form_class()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        
        print(request.POST.get('i_name'))
        print(request.POST.get('i_description'))
        print(request.POST.get('gallery_name'))
        print(request.FILES.get('image'))

        form = self.form_class(request.POST or None, request.FILES or None)
        if form.is_valid():
            g_name = Gallery.objects.get(id = request.POST.get('gallery_name'))
            print("inside")
            obj = Photos.objects.create(
                i_name = request.POST.get('i_name'),
                i_description = request.POST.get('i_description'),
                gallery_name = g_name,
                image = request.FILES.get('image'),
                )                          
            obj.save()

            return redirect('imagelist')

        else:
            print("else")
            form = self.form_class()
            return render(request,self.template_name,{'form':form})




class AddUser(View):

    template_name = 'signup.html'
    form_class = UserForm
    cnt_class = AddUserForm

    def get(self,request):
        # if request.user.is_superuser:
        form1 = self.form_class()
        form2 = AddUserForm()
        return render(request,self.template_name,{'form1':form1, 'form2':form2})
        # else:
        #     return HttpResponse('invalid user')

    def post(self,request):
        print(request.POST.get('gender'))
        print(request.POST.get('dob'))
        print(request.POST.get('phoneno'))
        print(request.POST.get('first_name'))
        print(request.POST.get('username'))
        # print(request.POST)
        form1 = self.form_class(request.POST)
        form2 = AddUserForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("inside fn")
            usr = User.objects.create_user(
                username = request.POST.get('username'),
                first_name = request.POST.get('first_name'),
                last_name = request.POST.get('last_name'),
                email = request.POST.get('email'),
                password = request.POST.get('password1'))
            usr.is_staff=True
            usr.save()
            # usr_cnt = Department.objects.get(id = request.POST.get('doc_dept'))
            usr_cnt = UserContinuation.objects.create(
                userdata = usr,
                # doc_address = request.POST.get('doc_address'),
                gender = request.POST.get('gender'),
                dob = request.POST.get('dob'),
                phoneno = request.POST.get('phoneno'),
                # date_join = request.POST.get('date_join'),
                # doc_status = request.POST.get('doc_status'),
                # doc_fee = request.POST.get('doc_fee'),
                )

            usr_cnt.save()

            return redirect('index')
            return HttpResponse("successfully saved")

        else:
            form1 = self.form_class()
            form2 = AddUserForm()
            return render(request,self.template_name,{'form1':form1,'form2':form2})
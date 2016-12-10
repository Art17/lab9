from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import DirectorSearchForm, DirectorCreationForm
from .models import Director
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math
from django.views import View
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from .serializers import DirectorSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer


@api_view(['GET'])
def get_directors(request):
    if request.method == 'GET':
        word = request.GET.get('name')
        if word is not None:
            directors = Director.objects.filter(name__startswith=word)
        else:
            directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        res = {
            'dirs': serializer.data,
            'can_delete': request.user.has_perm('directors.can_delete')
        }
        return Response(res)



@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CreateView(View):
    def get(self, request):
        dir_form = DirectorCreationForm()
        args = dict()
        args['form'] = dir_form
        return render(request, 'create_director.html', args)


    def post(self, request):
        dir_form = DirectorCreationForm(request.POST, request.FILES)
        if dir_form.is_valid():
            dir_form.save()
            return HttpResponse('Director added successfully')
        else:
            return render(request, 'create_director.html', {'form': dir_form})


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DirectorsView(View):
    def get(self, request):
        args = dict()

        args['form'] = DirectorSearchForm()
        return render(request, 'directors.html', args)


    def post(self, request):
        if 'settings' in request.POST:
            settings = request.POST['settings']
            request.session['settings'] = settings
            return HttpResponseRedirect('/directors/')


@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required(login_url='/login/'), name='dispatch')
class DirectorView(View):
    def get(self, request, id):
        args = dict()
        try:
            dir = Director.objects.get(id=id)
            args['dir'] = dir
            return render(request, 'director.html', args)
        except:
            return HttpResponse('director doesnt exist')


    def post(self, request, id):
        if request.user.has_perm('directors.can_delete'):
            try:
                dir = Director.objects.get(id=id)
                name = dir.name
                dir.delete()
                return HttpResponse('Director %s has been deleted' % name)
            except:
                return HttpResponse('director doesnt exist')
        else:
            raise PermissionDenied


def user_check(user):
    return user.is_superuser


@user_passes_test(user_check)
def my_admin(request):
    args = dict()
    args['users'] = User.objects.all()
    return render(request, 'my_admin.html', args)
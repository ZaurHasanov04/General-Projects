from urllib.request import Request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic.edit import DeleteView, UpdateView
from .models import *
# Create your views here.


class MyTaskView(View):
    # template='index.html'
    def get(self, request):
        task = Task.objects.filter(status=True)
        
        context={
            'task':task
        }

        return render(request, 'index.html', context)

    def post(self, request):
        
        text=request.POST.get('text')
        if text:
            task=Task(text=request.POST.get('text'))
            task.save()
            return HttpResponseRedirect(request.path_info)
        else:
            context={
                'error' : 'Input must be filled'
            }

            return redirect(reverse('task'))


class DeleteTask(View):
    def get(self, request, pk):
        task=Task.objects.get(id=pk)
        task.delete()
        return redirect('task')


class TaskUpdateView(View):

    def post(self, request, pk):
        task = Task.objects.get(id = pk)
        task.text = request.POST.get('text')
        status = request.POST.get('status')

        if status == 'False':
            task.status = False

        task.save()
        
        return redirect('task')

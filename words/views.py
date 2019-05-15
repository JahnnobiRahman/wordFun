from django.shortcuts import render , redirect, get_object_or_404
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Word

def home(request):
    words=Word.objects
    return render(request, 'words/home.html',{'words':words})


@login_required(login_url="/accounts/signup")
def add(request):
    if request.method=='POST':
        try:
            word = Word.objects.get(word_num = request.POST['word_num'])
            return render (request,'words/add.html',{'error':'Word has already been taken'})
        except Word.DoesNotExist:
            if request.POST['word_num'] and request.POST['defi'] and request.POST['use_in'] :
                word=Word()
                word.word_num= request.POST['word_num']
                word.defi=request.POST['defi']
                word.use_in= request.POST['use_in']
                word.imp= 1
                word.adder=request.user
                word.save()
                return redirect('/words/' + str(word.id))
        
        
        else:
            return render(request, 'words/add.html',{'error':'All fields are required'})


    else:
        return render(request, 'words/add.html')




def detail(request, word_id):
    word = get_object_or_404(Word, pk=word_id)
    return render(request, 'words/detail.html',{'word':word})



@login_required(login_url="/accounts/signup")
def important(request,word_id):
   if request.method=='POST':
      word = get_object_or_404(Word ,pk =word_id)
      word.imp +=1
      word.save()
      return redirect('/words/' + str(word.id))


def result(request):

        return render(request, 'words/add.html', {'error': 'Your valid word is not found '})
    
    
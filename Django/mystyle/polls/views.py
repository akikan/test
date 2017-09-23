from django.shortcuts import render


def index(request):
    quest=[]
    quest.append([1,1])
    quest.append([2,12])
    quest.append([3,13])
    quest.append([4,14])
    quest.append([5,15])

    return render(request, 'polls/index.html', {
        'questions': quest,
    })
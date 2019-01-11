from django.shortcuts import render


# Create your views here.
def table(request):
    color = list(range(0, 250, 4))
    black = list(range(0, 250, 4))
    lines = [(color[i], black[i]) for i in list(range(50))]
    context = {'lines': list(range(0, 255, 5))}
    print(lines)
    return render(request, 'ex03/index.html', context)

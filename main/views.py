from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245491',
        'name': 'Rizki Hidayatul Laeli',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
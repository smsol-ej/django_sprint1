from django.shortcuts import render


def about(request):
    template = 'pages/about.html'
    return render(request, template)


def rules(requtes):
    template = 'pages/rules.html'
    return render(requtes, template)

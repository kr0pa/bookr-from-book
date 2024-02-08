from django.shortcuts import render


# Create your views here.
def index(request):
    hello = "Witaj w witrynie Bookr"

    return render(request, 'base.html', {'hello': hello})


def book_search(request):
    search = request.GET.get("search")

    return render(request, 'book-search.html', {'search': search})

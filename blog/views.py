from django.shortcuts import render

# test data

posts = [
    {
        'author': 'Abhijeet',
        'title': 'First Post',
        'content': 'Content of first post',
        'date_posted': 'September 2, 2002'
    },
    {
        'author': 'Vandana',
        'title': 'Second Post',
        'content': 'Content of second post',
        'date_posted': 'January 26, 2000'

    }
]


# Create your views here.

def home(request):
    # First View Blog Home

    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def about(request):
    # second view About Page
    return render(request, 'blog/about.html')

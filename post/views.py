from django.shortcuts import render, redirect
from post_comments.models import PostComments, Contact, TrendComments, CultureComments, BusinessComments, LifestyleComments, HeadlineComments
from .models import Trending, Post, Headline, Culture, Business, LifeStyle, Post1


def index(request):
    trends = Trending.objects.order_by('-created_on')[0:6]
    posts = Post.objects.order_by('-created_on')[0:3]
    post1 = Post1.objects.order_by('-created_on')[0:3]
    headlines = Headline.objects.order_by('-created_on')[0:6]
    cultures = Culture.objects.order_by('-created_on')[0:6]
    businesses = Business.objects.order_by('-created_on')[0:6]
    lifestyles = LifeStyle.objects.order_by('-created_on')[0:6]
    name = {'posts': posts,
            'trends': trends,
            'headlines': headlines,
            'cultures': cultures,
            'businesses': businesses,
            'lifestyles': lifestyles,
            'post1': post1
            }

    return render(request, 'index.html', name)


def single_post(request, pk):
    posts = Post.objects.get(id=pk)
    trendings = Trending.objects.order_by('-created_on')[0:6]
    recent = Post.objects.order_by('-created_on')[0:3]
    comment = PostComments.objects.order_by('-created_on')[0:3]
    name = {
        'trendings': trendings,
        'posts': posts,
        'comment': comment,
        'recent': recent
    }
    if request.method == 'POST':
        comment_name = request.POST.get('comment_name')
        email = request.POST.get('comment_email')
        message = request.POST.get('comment_message')
        new_comment = PostComments(name=comment_name, email=email, comment=message)
        new_comment.save()
        return redirect('.')

    return render(request, 'single-post.html', name)


def single_trend(request, pk):
    trendings = Trending.objects.order_by('-created_on')[0:6]
    trends = Trending.objects.get(id=pk)
    recent = Post.objects.order_by('-created_on')[0:3]
    comment = TrendComments.objects.order_by('-created_on')[0:3]
    name = {
        'trendings': trendings,
        'trends': trends,
        'comment': comment,
        'recent': recent

    }
    if request.method == 'POST':
        comment_name = request.POST.get('comment_name')
        email = request.POST.get('comment_email')
        message = request.POST.get('comment_message')
        new_comment = TrendComments(name=comment_name, email=email, comment=message)
        new_comment.save()
        return redirect('.')

    return render(request, 'single-trend.html', name)


def single_culture(request, pk):
    cultures = Culture.objects.get(id=pk)
    trendings = Trending.objects.order_by('-created_on')[0:6]
    recent = Post.objects.order_by('-created_on')[0:3]
    comment = CultureComments.objects.order_by('-created_on')[0:3]
    name = {
        'cultures': cultures,
        'trendings': trendings,
        'comment': comment,
        'recent': recent

    }

    if request.method == 'POST':
        comment_name = request.POST.get('comment_name')
        email = request.POST.get('comment_email')
        message = request.POST.get('comment_message')
        new_comment = CultureComments(name=comment_name, email=email, comment=message)
        new_comment.save()
        return redirect('.')

    return render(request, 'single-culture.html', name)


def single_headline(request, pk):
    headlines = Headline.objects.get(id=pk)
    trendings = Trending.objects.order_by('-created_on')[0:6]
    recent = Post.objects.order_by('-created_on')[0:3]
    comment = HeadlineComments.objects.order_by('-created_on')[0:5]

    name = {'headlines': headlines,
            'trendings': trendings,
            'comment': comment,
            'recent': recent
            }
    if request.method == 'POST':
        comment_name = request.POST.get('comment_name')
        email = request.POST.get('comment_email')
        message = request.POST.get('comment_message')
        new_comment = HeadlineComments(name=comment_name, email=email, comment=message)
        new_comment.save()
        return redirect('.')

    return render(request, 'single-headline.html', name)


def single_business(request, pk):
    businesses = Business.objects.get(id=pk)
    recent = Post.objects.order_by('-created_on')[0:3]
    trendings = Trending.objects.order_by('-created_on')[0:6]
    comment = BusinessComments.objects.order_by('-created_on')[0:3]
    name = {
        'businesses': businesses,
        'trendings': trendings,
        'comment': comment,
        'recent': recent

    }
    if request.method == 'POST':
        comment_name = request.POST.get('comment_name')
        email = request.POST.get('comment_email')
        message = request.POST.get('comment_message')
        new_comment = BusinessComments(name=comment_name, email=email, comment=message)
        new_comment.save()
        return redirect('.')

    return render(request, 'single-business.html', name)


def single_lifestyle(request, pk):
    lifestyles = LifeStyle.objects.get(id=pk)
    recent = Post.objects.order_by('-created_on')[0:3]
    trendings = Trending.objects.order_by('-created_on')[0:6]
    comment = LifestyleComments.objects.order_by('-created_on')[0:3]
    name = {
        'lifestyles': lifestyles,
        'trendings': trendings,
        'comment': comment,
        'recent': recent
    }
    if request.method == 'POST':
        comment_name = request.POST.get('comment_name')
        email = request.POST.get('comment_email')
        message = request.POST.get('comment_message')
        new_comment = LifestyleComments(name=comment_name, email=email, comment=message)
        new_comment.save()
        return redirect('.')

    return render(request, 'single-lifestyle.html', name)


def about(request):
    posts = Post.objects.order_by('-created_on')[0:3]
    return render(request, 'about.html', {'posts': posts})


def contact(request):
    posts = Post.objects.order_by('-created_on')[0:3]
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contacts = Contact(name=name, email=email, subject=subject, message=message)
        contacts.save()
        return redirect('.')
    return render(request, 'contact.html', {'posts': posts})


def category(request):
    return render(request, 'category.html')


def search_result(request):
    return render(request, 'search-result.html')


from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from django.db.models import Q
# Create your views here.
def index(request):
    reviews = Review.objects.order_by('pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)

def new(request):
    return render(request, 'reviews/new.html')

def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:index')
    
    else:
        review_form = ReviewForm()
    
    context = {
        'review_form': review_form,
    }
    return render(request, 'reviews/new.html', context=context)

def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review': review,
    }
    return render(request, 'reviews/detail.html', context)

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:detail', review.pk)
    
    else:
        review_form = ReviewForm(instance=review)
    
    context = {
        'review_form': review_form,
    }

    return render(request, 'reviews/update.html', context)

def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect('reviews:index')

def search(request):
    if request.method == "GET":
        content_list = Review.objects.all()
        search = request.GET.get("search", "")

        if search:
            search_list = content_list.filter(
                Q(title__icontains=search)
                | Q(content__icontains=search)
                | Q(movie_name__icontains=search)
            )
            context = {
                "search": search_list
            }
            return render(request, 'reviews.search.html', context)
        
        else:
            k=1
            context = {
                "search": k
            }
            return render(request, 'reviews/search.html', context)
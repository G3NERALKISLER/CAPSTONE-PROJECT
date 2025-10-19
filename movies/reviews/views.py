from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics, permissions
from .models import Review
from .forms import ReviewForm
from .serializers import ReviewSerializer
# Create your views here.
#views for displaying reviews templates
@login_required
def add_review(request, imdb_id, movie_title):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie_title = movie_title
            review.imdb_id = imdb_id
            review.save()
            return redirect('movies:movie_detail', imdb_id=imdb_id)
    else:
        form = ReviewForm() 


        return render(request, 'reviews/create_review.html', {'form': form, 'movie_title': movie_title})
@login_required
def edit_review(request,pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('movies:movie_detail', imdb_id=review.imdb_id)
        
    else:
            form = ReviewForm(instance=review)
            return render(request, 'reviews/edit_review.html ', {'form':form, 'review':review})

@login_required
def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        imdb_id = review.imdb_id
        review.delete()
        return redirect('movies:movie_detail', imdb_id=imdb_id)
    else:
        return render(request, 'reviews/delete_review.html', {'review': review})

#views for APIs
class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.request.user == self.get_object().user:
            serializer.save()
        else:
            raise PermissionDenied("You can only edit your own review.")


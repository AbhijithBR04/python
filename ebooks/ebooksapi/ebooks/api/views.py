from rest_framework import generics
from rest_framework.generics import get_object_or_404
from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer , ReviewSerializer
from rest_framework import permissions
from ebooks.api.permissions import IsAdminUserOrReadOnly,IsReviewAuthotOrReadOnly
from rest_framework.exceptions import ValidationError
from ebooks.api.pagination import smallSetPagination

class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by('-id')
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = smallSetPagination

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ReviewListCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook =  get_object_or_404(Ebook, pk= ebook_pk)

        review_author = self.request.user
        review_queryset = Review.objects.filter(ebook=ebook,review_author=review_author)

        if review_queryset.exists():
            raise ValidationError('You have already reviewed this ebook.')

        serializer.save(ebook=ebook, review_author= review_author)

class ReviewDetailCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthotOrReadOnly]

# class EbookListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer

#     def get(self , request, *args , **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs) 

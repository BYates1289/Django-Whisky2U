from django.urls import path
from product.views import SingleProductView, BuyNow, MonthlySubscription, FaqPageView, AddComment, EditComment

app_name = "product"

urlpatterns = [
    path('single_product/<int:id>',
         SingleProductView.as_view(), name='single_product'),
    path('add-comment/', AddComment.as_view(), name='add_comment'),
    path('edit-comment/', EditComment.as_view(), name='edit_comment'),

    path('Buy-Now/<int:p>/<int:q>/', BuyNow.as_view(), name='buy-now'),
    path('Monthly/<int:p>/<int:q>/', MonthlySubscription.as_view(), name='monthly'),
    path('faq/', FaqPageView.as_view(), name='faq'),

]

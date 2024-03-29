from xml.etree.ElementTree import Comment
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .models import Product, Category, Rating
from order.models import Address, Delivery
from registration.models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
import stripe
from django.db.models import Avg
import os

DOMAIN_NAME = os.getenv("DOMAIN_NAME")


stripe.api_key = os.getenv("STRIPE_API_KEY")


# Create your views here.
class ProductPageView(TemplateView):
    template_name = "new_template/product-page.html"


class SingleProductView(View):
    def get(self, request, id, *args, **kwargs):
        get_product = Product.objects.filter(id=id).first()
        buy = False
        reviewed = False

        if request.user.is_authenticated:
            if Address.objects.filter(user=request.user).exists():
                address = Address.objects.filter(user=request.user).first()
                if Delivery.objects.filter(
                    address=address, product=get_product
                ).exists():
                    buy = True
            if Rating.objects.filter(user=request.user, product=get_product).exists():
                reviewed = True
        # print(buy)

        get_related = None
        get_comment = None

        if get_product.category.name == "5cl":
            get_category = Category.objects.filter(name="5cl").first()
            get_related = Product.objects.filter(category=get_category)
            get_comment = Rating.objects.filter(product=get_product)

        if get_product.category.name == "70cl":
            get_category = Category.objects.filter(name="70cl").first()
            get_related = Product.objects.filter(category=get_category)
            get_comment = Rating.objects.filter(product=get_product)

        context = {
            "product": get_product,
            "related": get_related,
            "comments": get_comment,
            "total_comment": Rating.objects.filter(product=get_product).count(),
            "buy": buy,
            "reviewed": reviewed,
        }

        return render(request, "new_template/product-page.html", context=context)


class AddComment(LoginRequiredMixin, View):
    login_url = "/login/"

    def post(self, request):
        id = request.POST.get("id")
        rate = request.POST.get("rate")
        if not rate:
            rate = 0
        comment = request.POST.get("comment")
        product = Product.objects.get(pk=id)

        rating = Rating.objects.create(
            product=product,
            user=request.user,
            comment=comment,
            stars=rate,
        )
        rating.save()

        product.total_ratings = Rating.objects.filter(product=product).count()
        ratings = Rating.objects.filter(product=product)
        num = int(ratings.aggregate(Avg("stars"))["stars__avg"])
        product.rating_number = num
        product.save()
        data = {}
        data["comment"] = comment
        return JsonResponse(data, status=200)

        # return HttpResponseRedirect(f'/single_product/{id}')


class EditComment(LoginRequiredMixin, View):
    login_url = "/login/"

    def post(self, request):
        cid = request.POST.get("cid")
        if Rating.objects.filter(user=request.user, id=cid).exists():
            pid = request.POST.get("pid")
            rate = request.POST.get("rate")
            if not rate:
                rate = 0
            comment = request.POST.get("comment")
            print(rate, pid, cid, comment)
            product = Product.objects.get(pk=pid)

            Rating.objects.filter(id=cid).update(
                comment=comment,
                stars=rate,
            )

            product.total_ratings = Rating.objects.filter(product=product).count()
            ratings = Rating.objects.filter(product=product)
            num = int(ratings.aggregate(Avg("stars"))["stars__avg"])
            product.rating_number = num
            product.save()
            data = {}
            data["comment"] = comment
            return HttpResponseRedirect(f"/single_product/{pid}")

            # return JsonResponse(data, status=200)
        else:
            return HttpResponseRedirect("/")


class BuyNow(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, p, q, *args, **kwargs):
        product = p
        quantity = q

        get_product = Product.objects.filter(pk=product).first()
        stripe_not_subscribe_price_id = get_product.product_price_not_subscribe_id

        user = CustomUser.objects.filter(email=request.user).first()
        stripe_user_id = user.stripe_id

        DOMAIN = DOMAIN_NAME

        checkout_session = stripe.checkout.Session.create(
            customer=stripe_user_id,
            line_items=[
                {
                    "price": stripe_not_subscribe_price_id,
                    "quantity": quantity,
                },
            ],
            payment_method_types=[
                "card",
            ],
            mode="payment",  # for one time payment
            payment_intent_data={
                "metadata": {
                    "product_id": get_product.product_stripe_id,
                    "product_price": get_product.price,
                    "quantity": quantity,
                    "total": int(get_product.price) * int(quantity),
                },
            },
            success_url=DOMAIN
            + f"orders/create/delivery/{{CHECKOUT_SESSION_ID}}/{product}/{quantity}/single/",
            cancel_url=DOMAIN + f"single_product/{product}",
        )

        return redirect(checkout_session.url, code=303)


class MonthlySubscription(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request, p, q, *args, **kwargs):
        product = p
        quantity = q

        get_product = Product.objects.filter(pk=product).first()
        stripe_is_subscribe_price_id = get_product.product_price_is_subscribe_id

        user = CustomUser.objects.filter(email=request.user).first()
        stripe_user_id = user.stripe_id

        # 4242 4242 4242 4242 -- Fake card to test the checkout session
        DOMAIN = DOMAIN_NAME

        checkout_session = stripe.checkout.Session.create(
            customer=stripe_user_id,
            line_items=[
                {
                    "price": stripe_is_subscribe_price_id,
                    "quantity": quantity,
                },
            ],
            payment_method_types=[
                "card",
            ],
            mode="subscription",
            success_url=DOMAIN
            + f"orders/create/delivery/{{CHECKOUT_SESSION_ID}}/{product}/{quantity}/subscription/",
            cancel_url=DOMAIN + f"single_product/{product}",
        )

        return redirect(checkout_session.url, code=303)


class FaqPageView(TemplateView):
    template_name = "new_template/faq-contact.html"

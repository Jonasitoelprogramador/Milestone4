import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, redirect
from .models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
#The below is created following a tutorial that can be found here: https://www.youtube.com/watch?v=722A27IoQnk&t=716s


def Success(request):
    return render(request, "products/success.html")


def Cancel(request):
    return render(request, "products/cancel.html")


def ProductLanding(request):
    product = Product.objects.get(name="subscription")
    print(f"This is the output I'm after {type(product)}")
    context = {
        "product": product
    }
    return render(request, "products/product-landing.html", context)


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Product.objects.get(id=product_id)
        YOUR_DOMAIN = "https://8000-jonasitoelprogr-mileston-7nkbtlfiplb.ws-eu31.gitpod.io/"
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': product.price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return redirect(checkout_session.url, code=303)
import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from accounts.models import Payment
from users.models import Host, Worker

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
        YOUR_DOMAIN = "https://8000-jonasitoelprogr-mileston-7nkbtlfiplb.ws-eu33.gitpod.io/"
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': product.price_id,
                    'quantity': 1,
                },
            ],
            metadata={
                "user_id": request.user.id,
                "user_type": request.user.type 
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return redirect(checkout_session.url, code=303)


'''@csrf_exempt
def StripeWebhook(request):
    payload = request.body
    print("just printing this thing out there you go all good")
    return HttpResponse(status=200)'''

@csrf_exempt
def StripeWebhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        customer_id = session["metadata"]["user_id"]
        customer_type = session["metadata"]["user_type"]
        if customer_type == "host":
            obj = Host.objects.get(user=customer_id)
            obj.payment_status = 'paid'
            obj.save()
        elif customer_type == "worker":
            obj = Worker.objects.get(user=customer_id)
            obj.payment_status = 'paid'
            obj.save()
            
    # Passed signature verification
    return HttpResponse(status=200)

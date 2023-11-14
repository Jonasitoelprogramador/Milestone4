import stripe
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from users.models import Host, Worker
from .forms import ProductForm
from django.contrib.auth.decorators import user_passes_test
from users.views import host_worker_exist




stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
#The below is created following a tutorial that can be found here: https://www.youtube.com/watch?v=722A27IoQnk&t=716s


def user_paid(user):
    print(f'payment status: {user.host.payment_status}')
    try:
        return user.host.payment_status == "nonpaid"
    except AttributeError:
        print('getting to here')
        return False


@user_passes_test(user_paid, login_url="/")
@user_passes_test(host_worker_exist, login_url="/users/profile")
def Success(request):
    return render(request, "products/success.html")


@user_passes_test(user_paid, login_url="/")
@user_passes_test(host_worker_exist, login_url="/users/profile")
def Cancel(request):
    return render(request, "products/cancel.html")


# inspired by https://www.youtube.com/watch?v=722A27IoQnk&t=2539s
# This creates the page in which users fill in their details
@user_passes_test(user_paid, login_url="/")
@user_passes_test(host_worker_exist, login_url="/users/profile")
def CreateCheckoutSessionView(request):
    # get the product stored in the db
    product_id = Product.objects.get(name=request.POST.get('products')).id
    product = Product.objects.get(id=product_id)
    # define where you would like Stripe to redirect to post payment
    YOUR_DOMAIN = "https://language-stay-2.herokuapp.com/success"
    checkout_session = stripe.checkout.Session.create(
        # create a dictionary to pass through to Stripe checkout
        line_items=[
            {
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price': product.price_id,
                'quantity': 1,
            },
        ],
        # This is used to identify the user in the webhook view post payment
        metadata={
            "user_id": request.user.id,
            "user_role": request.user.role 
        },
        mode='payment',
        # The exact URL to redirect to depending on success or failure
        success_url=YOUR_DOMAIN + '/success',
        cancel_url=YOUR_DOMAIN + '/cancel',
    )
    return redirect(checkout_session.url, code=303)

# This recieves the request that is send back from Stripe on successful payment
#@user_passes_test(user_paid, login_url="/")
#@user_passes_test(host_worker_exist, login_url="/users/profile")
@csrf_exempt
def StripeWebhook(request):
    print('webhook hit')
    '''payload = request.body
    # required to verify request is coming from Stripe
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    # checking request does have correct header
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
    '''
    # If the request is correct
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # update the payment_status attribute in the Host/Worker model to paid
        customer_id = session["metadata"]["user_id"]
        customer_role = session["metadata"]["user_role"]
        if customer_role == "host":
            obj = Host.objects.get(user=customer_id)
            obj.payment_status = 'paid'
            obj.save()
        elif customer_role == "worker":
            obj = Worker.objects.get(user=customer_id)
            obj.payment_status = 'paid'
            obj.save()
            
    # Passed signature verification'''
    return HttpResponse(status=200)

@csrf_exempt
def Testing(request):
    print('hello my friend')
    print(request)

@user_passes_test(host_worker_exist, login_url="/users/profile")
@user_passes_test(lambda u: u.is_superuser)
def ProductView(request, pk=None):
    forms_list = []
    if request.method == 'POST':
        product_instance = Product.objects.get(id=pk)
        product_filled_form = ProductForm(request.POST, instance=product_instance)
        if product_filled_form.is_valid():
            product_filled_form.save()
    instances = list(Product.objects.all())
    # loop through all the instances
    for i in range(len(instances)):
        # get each instance
        instancey = Product.objects.get(pk=instances[i].pk)
        # bind each instance to a form
        forms_list.append([ProductForm(instance=instancey), instancey.pk])
    return render(request, "products/product-admin.html", {'forms_list': forms_list, 'product_form': ProductForm, 'upgradeHidden': 'hidden', 'admin': 'Admin Access'})


@user_passes_test(host_worker_exist, login_url="/users/profile")
@user_passes_test(lambda u: u.is_superuser)
def ProductDelete(request, pk):
    product_instance = Product.objects.get(id=pk)
    product_instance.delete()
    return redirect(ProductView)


@user_passes_test(host_worker_exist, login_url="/users/profile")
@user_passes_test(lambda u: u.is_superuser)
def ProductAdd(request):
    product_filled_form = ProductForm(request.POST)
    if product_filled_form.is_valid():
            product_filled_form.save()
    return redirect(ProductView)



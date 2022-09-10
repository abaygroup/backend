from django.shortcuts import render, redirect, get_object_or_404
import hashlib
import requests
from random import randint
import xmltodict
from .models import Membership, User
from .serializers import MembershipSerializer
from rest_framework.generics import views
from rest_framework import status, permissions
from rest_framework.response import Response


class PricingView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        premium = get_object_or_404(Membership, slug="premium")
        pricing_list = Membership.objects.exclude(slug='free').order_by('membership_type')
        pricing_serializer = MembershipSerializer(pricing_list, many=True)
        premium_serializer = MembershipSerializer(premium, partial=True)
        context = {
            'pricing_list': pricing_serializer.data,
            'premium': premium_serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)


# Pricing plan page
def pricing_detail(request, slug):
    if request.user.is_authenticated:
        pricing = get_object_or_404(Membership, slug=slug)

        url = 'init_payment.php'
        secret_key = 'qzsMJuE7enblhJXC'
        pg_merchant_id = 545547

        def sort_list(var):
            data_value = ''
            sorted_tuple = sorted(var.items(), key=lambda x: x[0])
            for k in sorted_tuple:
                print(str(k[1]))
                data_value = data_value + str(k[1]) + ';'
            data_value = url + ';' + data_value + '' + secret_key
            hash_object = hashlib.md5(data_value.encode('utf-8')).hexdigest()
            return hash_object

        if request.POST:
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            full_name = request.POST.get('full_name')

            var = {
                'pg_amount': pricing.price,
                'pg_description': 'Premium подписка',
                'pg_merchant_id': pg_merchant_id,
                'pg_order_id': randint(0, 10000),
                'pg_salt': 'Premium подписка: {}'.format(full_name),
                'pg_currency': 'USD',
                'pg_success_url': 'http://127.0.0.1:8000/pricing/success-payment/',
                'pg_failure_url': 'http://127.0.0.1:8000/pricing/failure-payment/',
                'pg_user_contact_email': email,
                'pg_user_phone': phone,
                'pg_payment_method': 'bankcard',
                'pg_testing_mode': '1',
            }

            pg_sig = sort_list(var)
            var['pg_sig'] = pg_sig

            r = requests.post('https://api.paybox.money/init_payment.php', data=var)
            print(xmltodict.parse(r.text))

            return redirect(xmltodict.parse(r.text)['response']['pg_redirect_url'])
        else:
            print('Dont POST request')

        context = {
            'slug': slug,
            'pricing': pricing
        }
        return render(request, 'accounts/pricing_detail.html', context)
    else:
        return redirect('/admin/')


def user_profile(request, username):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=username)
        print(user.user_membership.membership)
        return render(request, 'accounts/user.html', {'user': user})

    else:
        return redirect('/admin/')


def success_payment(request):
    return render(request, 'accounts/success_payment.html', {})


def failure_payment(request):
    return render(request, 'accounts/failure_payment.html', {})
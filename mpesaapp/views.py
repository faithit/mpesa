from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient


# Create your views here.
def index(request):
    return render(request, 'pay.html')
def payment_info(request):
    return render(request, 'paymentinfo.html')
def lipa_na_mpesa_online(request):
    if request.method == "POST":
        phone_number=request.POST[("abcd")]
        amount=int(request.POST[("amount")])
        account_reference="TechWise"
        transaction_desc="school fees payment"
        callback_url="https://3f395e3dd5be.ngrok-free.app/callback"
        cl=MpesaClient()
        response =cl.stk_push(phone_number,amount,account_reference,transaction_desc,callback_url)
        return redirect('paymentinfo')
    return HttpResponse("invalid request")
@csrf_exempt
def callback(request):
    if request.method == "POST":
        data=request.POST
        print("mpesa callback response",data)
        return JsonResponse({"status":"success"})
    return JsonResponse({'status':"invalid request"})


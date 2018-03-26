from django.shortcuts import render, redirect, HttpResponse
from .models import Email_Address, Cafe
from functions.email_sender import Email_Sender


def add_accounts_view(request):
    if request.method == 'POST':
        url = request.POST['url']
        print(url)
        Email_Address.objects.crawl(url)
    return redirect('cafe-list')



def cafe_search_view(request):
    context = {}
    return render(request, 'naver_cafe_crawler.html',context)


def cafe_list_view(request):
    cafes = Cafe.objects.all()
    context = {
        'cafes': cafes
    }

    return render(request, 'cafe_list.html', context)


def account_list_view(request, pk):
    accounts = Cafe.objects.get(pk = pk).email_address_set.all()
    context = {
        'accounts': accounts
    }

    return render(request, 'account_list.html', context)

def email_send_view(request):
    if request.method == 'POST':
        pk = request.POST.get('submit')
        email_id = request.POST['email_address']
        password = request.POST['password']
        empty_list =[]
        recipients_list = Cafe.objects.get(pk=pk).email_address_set.all()
        for recipient in recipients_list:
            empty_list.append(str(recipient)+'@naver.com')
        subject = request.POST['subject']
        message = request.POST['message']
        email_sender = Email_Sender()
        email_sender.send(
            email_id=email_id,
            password=password,
            recipients=empty_list,
            subject=subject,
            message=message
        )
    return HttpResponse('email sent!!')
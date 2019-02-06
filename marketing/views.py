from django.shortcuts import render


def index(request):
    return render(request, 'marketing/index.html')


def contact_lists(request):
    return render(request, 'marketing/lists/index.html')


def contact_list_new(request):
    return render(request, {}, 'marketing/lists/new.html')


def contact_list_detail(request):
    return render(request, {}, 'marketing/lists/detail.html')


def email_template_list(request):
    return render(request, {}, 'marketing/email_template/index.html')


def email_template_new(request):
    return render(request, {}, 'marketing/email_template/new.html')


def email_template_edit(request):
    return render(request, {}, 'marketing/email_template/edit.html')


def email_template_detail(request):
    return render(request, {}, 'marketing/email_template/detail.html')


def campaign_list(request):
    return render(request, {}, 'marketing/campaign/index.html')


def campaign_new(request):
    return render(request, {}, 'marketing/campaign/new.html')


def campaign_edit(request):
    return render(request, {}, 'marketing/campaign/edit.html')


def campaign_details(request):
    return render(request, {}, 'marketing/campaign/details.html')

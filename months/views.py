from django.http import HttpResponse
from django.shortcuts import render

month_dic = {
    'january': 'this is the first month',
    'february': 'this is the second month',
    'march': 'this is the third month',
    'april': 'this is the fourth month',
    'may': 'this is the fifth month',
    'june': 'this is the sixth month',
    'july': 'this is the seventh month',
    'august': 'this is the eighth month',
    'september': 'this is the ninth month',
    'october': 'this is the tenth month',
    'november': 'this is the eleventh month',
    'december': 'this is the twelveth month',
}


def ViewMonths(request):
    month_key = list(month_dic.keys())
    # item = ''
    # for i in month_key:
    #     item += f'<h1>{i}</h1>'
    # return HttpResponse(item)
    return render(request, 'months/viewmonth.html', context={'month_name': month_key})

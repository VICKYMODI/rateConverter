from django.shortcuts import render
import requests


# Create your views here.

def currencyConverter(request):
	response = requests.get('http://data.fixer.io/api/latest?access_key=40eac7a32ba84e0369830d99248246b7&%20base%20=%20USD')
	apidata = response.json()
	country = apidata['rates']
	countryCode = []

	countryCode = country.keys()

	if request.method == 'POST':
		value = request.POST['value']
		HomeCur = request.POST['homrcur']
		targetcur = request.POST['targetcur']

		#eurovalue = country.get('"HomeCur"')
		HomeEurovalue = country[HomeCur]
		TargetEuroValue = country[targetcur]

		#print(HomeEurovalue)

		givenValueIntoEuro = float(value)/float(HomeEurovalue)
		targetCurrency = givenValueIntoEuro * TargetEuroValue
		print(targetCurrency)
		return render(request, 'home.html',{'targetCurrency' : targetCurrency,'value':value,'HomeCur':HomeCur,'targetcur':targetcur})
	else:
		return render(request, 'home.html',{'countryCode' : countryCode})

	

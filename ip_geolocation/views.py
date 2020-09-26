from django.shortcuts import render
import requests as Requests   #Renamed to prevent usage confusions between request and requests

def home(request):
	is_cached = ('geodata' in request.session)

	if not is_cached:
		#print("is not cached")   #for debugging only
		ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')

		# Get the json answer from the service:
		response = Requests.get('http://freegeoip.app/json/%s' % ip_address)
		
		# Save data on the session (cache). Simplest way.
		request.session['geodata'] = response.json()
	
	geodata = request.session['geodata']
	
	#print(geodata) #for debugging only

	return render(request, 'ip_geolocation/home.html', {   
		'ip': geodata['ip'],
		'country': geodata['country_name'],
		'latitude': geodata['latitude'],
		'longitude': geodata['longitude']
    })



def computepay(hours,rate_per_hour):
	if(hours<=40):
		grosspay= hours*rate_per_hour
	else:
		grosspay = (40 * rate_per_hour) + (1.5 * (hours -40) *rate_per_hour)
	return grosspay

hours = raw_input('Enter the no. of hours')
rate_per_hour = raw_input('Enter the rate per hour')
try:
    print(computepay(int(hours),float(rate_per_hour)))
except:
    print('Error')
    quit()
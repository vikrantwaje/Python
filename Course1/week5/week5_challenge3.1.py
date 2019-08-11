
hours = raw_input('Enter the no. of hours:')
rate_per_hours = raw_input('Enter the rate per hour:')
if(int(hours)<=40):
    gross_pay = int(hours) * float(rate_per_hours)
else:
    gross_pay = (40 * float(rate_per_hours)) + (1.5 *float(rate_per_hours)*(int(hours) - 40))
print(gross_pay)    
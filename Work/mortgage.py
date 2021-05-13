# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
nbMonths = 0
extra_payment = 1000.0
extra_payment_start_month = 61 # 5 years
extra_payment_end_month = 108 # 9 years

while principal > 0 and principal >= payment:
    nbMonths += 1
    if nbMonths < extra_payment_start_month or nbMonths > extra_payment_end_month:
        extra_payment = 0
    else:
        extra_payment = 1000
    principal = principal * (1+rate/12) - (payment + extra_payment)
    total_paid = total_paid + payment + extra_payment
    print(f'{nbMonths} {total_paid:0.2f} {principal:0.2f}')
if principal > 0:
    nbMonths += 1
    remain = principal
    total_paid = total_paid + remain
    principal = 0
    print(f'{nbMonths} {total_paid:0.2f} {principal:0.2f}')

print('Total paid', round(total_paid,2), "\nMonths" , nbMonths)
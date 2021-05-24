# mortgage.py

height = 100
bounce = 1
while bounce <= 10:
    height = height * (3/5)
    print(bounce, height)
    bounce += 1

# Exercise 1.5
root@DESKTOP-GPGGT7K:~/practical-python/Work# cat mortgage.py
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000


while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

#    if principal < payment:
#        payment = principal

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print('Month', month, 'Total Paid', round(total_paid,2), 'Remaining', round(principal,2))
    
# Exercise 1.7

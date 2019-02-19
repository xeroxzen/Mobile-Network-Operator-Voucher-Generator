'''
This is a Python module for generating recharge vouchers.
'''


import string
import re
from random import*
import __init__

rechPin = string.digits	
rechargeCard = "".join(choice(rechPin) for x in range(randint(16, 16)))
voucher = re.sub('[a-z, A-Z]', '0-9', rechargeCard)

def generator():
	global rechargeCard
	global voucher
	return voucher

print('************Recharge Pin***************\n')
print("AIRTIME GENERATED: ",generator())
print('---------------------------------------')
if(len(generator()) == 16):
	print('All good. Trying Recharging.')	
print('----------------------------------------')
print('\n**************************************\n')
print('***Thank you for trying Airtime Generator***')
print('\n****************************************\n')

# UNITTEST 
from numtowords import LaoNum

num = LaoNum()
test = num.numbertolaotext(1234567890123.05)
print(''.join(test))

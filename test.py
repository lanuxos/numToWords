# UNITTEST 
import unittest
from numtowords import NumToWords1

# tc = {123:'NEUNG HOY SAO SAM', 1234:'NEUNG PHUN SONG HOY SAM SIP SEE', 12345:'NEUNG MEUN SONG PHUN SAM HOY SEE SIP HA'}
tc = {0: "SOUN", 1: "NEUNG", 2: "SONG", 3: "SAM", 4: "SEE", 5: "HA", 6: "HOK", 7: "JED", 8: "PAED", 9: "GAO", 10: "SIP", 11: "SIP ED", 12: "SIP SONG", 15: "SIP HA", 20: "SAO", 21: "SAO ED", 22: "SAO SONG", 26: "SAO HOK", 30: "SAM SIP", 31: "SAM SIP ED", 32: "SAM SIP SONG", 37: "SAM SIP JED", 40: "SEE SIP", 41: "SEE SIP ED", 42: "SEE SIP SONG", 48: "SEE SIP PAED", 50: "HA SIP", 51: "HA SIP ED", 53: "HA SIP SAM", 59: "HA SIP GAO", 100: "NEUNG HOY", 101: "NEUNG HOY ED", 102: "NEUNG HOY SONG", 110: "NEUNG HOY SIP", 111: "NEUNG HOY SIP ED", 112: "NEUNG HOY SIP SONG", 120: "NEUNG HOY SAO", 121: "NEUNG HOY SAO ED", 122: "NEUNG HOY SAO SONG", 1000: "NEUNG PHUN", 1001: "NEUNG PHUN NEUNG", 1002: "NEUNG PHUN SONG", 1010: "NEUNG PHUN SIP", 1011: "NEUNG PHUN SIP ED", 1020: "NEUNG PHUN SAO", 1021: "NEUNG PHUN SAO ED", 10000: "NEUNG MEUN", 10001: "NEUNG MEUN NEUNG", 10010: "NEUNG MEUN SIP", 10011: "NEUNG MEUN SIP ED", 10020: "NEUNG MEUN SAO", 10021: "NEUNG MEUN SAO ED", 30310: "SAM MEUN SAM HOY SIP", 403652: "SEE SEAN SAM PHUN HOK HOY HA SIP SONG", 4001325: "SEE LARN NEUNG PHUN SAM HOY SAO HA", 4500315: "SEE LARN HA SEAN SAM HOY SIP HA", 405123640: "SEE HOY HA LARN NEUNG SEAN SONG MEUN SAM PHUN HOK HOY SEE SIP", 60013456: "HOK SIP LARN NEUNG MEUN SAM PHUN SEE HOY HA SIP HOK", 9010430590: "GAO TEU SIP LARN SEE SEAN SAM MEUN HA HOY GAO SIP", 1010101010: "NEUNG TEU SIP LARN NEUNG SEAN NEUNG PHUN SIP",
}

result = []
compare = []

for i, j in tc.items():
    # assert NumToWords1(i) == j, 'Incorrect result!!!'
    # print(i,j,NumToWords1(int(i)))
    result.append(NumToWords1(i))
    compare.append(j)

if result == compare:
    print('\n======\nPassed\n======')
else:
    print('\n======\nError!\n======')
# class NumTest(unittest.TestCase):
#     def NumTest(self):
#         for i, j in tc.items():
#             self.assertEqual(NumToWords1(i), j, 'Something else')
#             print(NumToWords1(i))

# if __name__ == '__main__':
#     unittest.main()

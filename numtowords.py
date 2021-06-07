# NUMBER TO LAO WORDS CONVERTION SCRIPT
# FOLKED FROM https://github.com/pinyoothotaboot/num-thai
import re
from decimal import Decimal

# FOLKED FROM OTHER REPO

class LaoNum:

    def __init__(self):

        self.number = None
        self.num_text = {
            '-': "ລົບ", '.': "ຈຸດ", 0: "ສູນ", 1: "ໜຶ່ງ",
            2: "ສອງ", 3: "ສາມ", 4: "ສີ່", 5: "ຫ້າ",
            6: "ຫົກ", 7: "ເຈັດ", 8: "ແປດ", 9: "ເກົ້າ",
            "0": "", "1": "ສິບ", "2": "ຮ້ອຍ", "3": "ພັນ",
            "4": "ໝື່ນ", "5": "ແສນ", "6": "ລ້ານ"
        }

    def process_int(self):
        result = []
        le = len(str(self.number))
        val = self.num_text['6']
        i = 0

        for x in range(0, le):
            n = int(self.number % 10)
            self.number /= 10

            if le > 1:
                if x >= 1 and x % 6 == 0:
                    if n == 1 and le < 8:
                        result.append(self.num_text[n]+val)
                    elif n == 1 and le > 7:
                        result.append("ເອັດ"+val)
                    else:
                        if n != 0:
                            result.append(self.num_text[n]+val)
                        else:
                            result.append(val)

                elif x == 0 and n == 1:
                    result.append("ເອັດ")
                else:
                    if i == 1 and n == 1:
                        result.append(self.num_text[str(i)])
                    elif i == 1 and n == 2:
                        result.append("ຊາວ")
                        # result.append("ຊາວ"+self.num_text[str(i)])
                    elif n == 0:
                        pass
                    else:
                        result.append(self.num_text[n]+self.num_text[str(i)])
            else:
                result.append(self.num_text[n])

            if i > 5:
                val += val
                i = 0
            i += 1

        return list(reversed(result))

    """
        Function    : NumberToTextThai
        Description : This function to convert number to thai text.
        Input       : Number
        Return      : Thai text
        Example     : NumberToTextThai(110)
                    >> ["ໜຶ່ງຮ້ອຍ","ສິບ"]
    """

    def numbertolaotext(self, number):

        result = []
        fnumber = 0

        if type(number) not in [int, float]:

            raise TypeError("ກະລຸນາປ້ອນຕົວເລກ...")

        if len(str(abs(number))) > 16 or len(str(abs(number))) < 1:

            raise ValueError("ຂອບເຂດຕົວເລກທີ່ປ້ອນຕ້ອງຢູ່ລະຫວ່າງ 1-16 ຫຼັກ")

        if number < 0:
            result.append(self.num_text['-'])
            number = abs(number)

        if type(number) in [int]:
            self.number = number
        elif type(number) in [float]:
            self.number = int(number)
            fnumber = Decimal(str(number)) % 1

        result.extend(self.process_int())

        if fnumber > 0:
            str1 = str(fnumber)
            for i in range(1, len(str1)):
                if str1[i] == '.':
                    result.append(self.num_text[str1[i]])
                else:
                    result.append(self.num_text[int(str1[i])])

        return result

    """
        Function    : TextThaiToNumber
        Description : This function to convert thai text to number.
        Input       : Thai text
        Return      : Number
        Example     : TextThaiToNumber("ໜຶ່ງຮ້ອຍສິບຈຸດສາມສອງໜຶ່ງ")
                    >> 110.321
    """

    def laotexttonumber(self, txt):
        unit_text = {
            'ໜຶ່ງ': 1, 'ເອັດ': 1, 'ສອງ': 2,
            'ສາມ': 3, 'ສີ່': 4, 'ຫ້າ': 5, 'ຫົກ': 6,
            'ເຈັດ': 7, 'ແປດ': 8, 'ເກົ້າ': 9
        }

        deci = {
            "ຊາວ": 20, "ສາມສິບ": 30, "ສີ່ສິບ": 40, "ຫ້າສິບ": 50,
            "ຫົກສິບ": 60, "ເຈັດສິບ": 70, "ແປດສິບ": 80, "ເກົ້າສິບ": 90
        }

        cross_text = {
            'ຮ້ອຍ': 100, 'ພັນ': 1000, 'ໝື່ນ': 10000, 'ແສນ': 100000, 'ລ້ານ': 1000000,
        }

        ten = {
            "ສິບ": 10
        }

        lao_float = {
            "ຈຸດ": '.', "ສູນ": "0", "ໜຶ່ງ": '1', "ສອງ": '2',
            "ສາມ": '3', "ສີ່": '4', "ຫ້າ": '5', "ຫົກ": '6',
            "ເຈັດ": '7', "ແປດ": '8', "ເກົ່າ": '9'
        }

        lao_num = [
            "໑", "໒", "໓", "໔", "໕", "໖", "໗", "໘", "໙"
        ]

        float_text = ''

        if type(txt) in [int, float]:
            raise TypeError("ຂໍ້ຄວາມທີ່ປ້ອນຕ້ອນເປັນຕົວໜັງສືທີ່ຖືກຕ້ອງ ເຊັ່ນ: ໜຶ່ງຮ້ອຍຊາວສາມຈຸດໜຶ່ງສອງສາມ")

        t = re.search(r'[ก-໙]+', txt, re.M | re.I)

        # ກວດສອບວ່າຄ່າ Input ເຂົ້າມາເປັນພາສາລາວ ຫລື ບໍ່
        if t:
            # ຫາກມີຕົວເລກລາວປົນໃນຂໍ້ຄວາມ ໃຫ້ປ່ຽນເປັນຍະຫວ່າງ
            for i in lao_num:
                txt = re.sub(str(i), '', txt)

            # ຄົ້ນຫາຄຳວ່າ ຈຸດ
            searchObj = re.search(r'ຈຸດ.+', txt, re.M | re.I)

            # ຫາກມີຄຳວ່າ ຈຸດ
            if searchObj:
                # ເກັບຂໍ້ມູນຫລັງຈຸດໄປຈົນສຸດຂໍ້ຄວາມ
                float_text = searchObj.group()

                # ຕັດຫລັງຈຸດອອກ
                txt = re.sub(str(float_text), '', txt)
        else:
            raise ValueError("ຂໍ້ມຄວາມທີ່ປ້ອນມາຕ້ອງຢູ່ໃນ ก-໙")

        fl = list()

        # ກວດສອບຂໍ້ມູນໃນ float_text ວ່າບໍ່ມີຊ່ອງຫວ່າງ
        if float_text != '':
            # ປ່ຽນເລກລາຍເປັນຕົວເລກ
            for i in lao_float:
                float_text = re.sub(i, lao_float[i], float_text)

            # ກຳນົດຕົວປ່ຽນ list
            fl = list(float_text)

            # ກວດສອບຄວາມຖືກຕ້ອງຂອງຂໍ້ມູນ
            for i in range(len(fl)):
                if fl[i] not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    raise ValueError(
                        "ມີຂໍ້ມູນຫຼັງຈຸດທີ່ສະກົດຜິດ")
                    break

            float_text = ''.join(fl)

        # ກວດສອບຄ່າລົບ
        obj_minus = re.search(r"ລົບ", txt, re.M | re.I)

        minus = ''

        # ຫາກພົບຄຳວ່າ (ລົບ)
        if obj_minus:
            minus = '-'
            txt = re.sub(r"ລົບ", "", txt)
        # ຫາຄຳຫຼັກສິບທີ່ຫຼາຍກວ່າ 20 ຂຶ້ນໄປ
        for i in deci:
            txt = re.sub(str(i), '+%s' % str(deci[i]), txt)
        # ຫາຄຳທີ່ເປັນຫຼັກໜ່ວຍ 1-9 ລວມຄຳວ່າ ເອັດ
        for i in unit_text:
            txt = re.sub(str(i), '+%s' % str(unit_text[i]), txt)
        # ຫາຄຳທີ່ຢູ່ໃນຫຼັກສິບ 10 -19
        for i in ten:
            if i != 'ຊາວ':
                txt = re.sub(str(i), '+%s' % str(ten[i]), txt)
            else:
                txt = re.sub(str(i), txt)
        # ຫາຄຳທີ່ເປັນ ຕົວຄູນ ຮ້ອຍ ສິບ ...
        for i in cross_text:
            if i == "ລ້ານ":
                txt = re.sub(str(i), ')*%s' % str(cross_text[i]), txt)
            else:
                txt = re.sub(str(i), '*%s' % str(cross_text[i]), txt)

        ls = list(txt)

        count = 0
        # ຫາກເກີນລ້ານ ໃຫ້ນັບຈຳນວນ ໂດຍມີວົງເລັບປິດ
        for x in range(len(ls)):
            if ls[x] == ')':
                count += 1
            if ls[x] not in ['(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '*']:
                raise ValueError(
                    "ມີຂໍ້ຄວາມທີ່ສະກົດບໍ່ຖືກຕ້ອງ ໃນກຸ່ມຈຳນວນເຕັມ")
                break

        # ກວດສອບ Count >1 ກໍ່ໃຫ້ສ້າງວົງເພີ່ມວົງເລັບຕາມຈຳນວນ Count
        if count > 0:
            ls[0] = ls[0].replace(str(ls[0]), str('('*(count)+ls[0]))

        # ປ່ຽນຮູບແບບ String ໃຫ້ເປັນຜົນຮັບຕົວເລກ
        if ls:
            result = eval(str(''.join(ls)))
        else:
            raise ValueError("ຂໍໂທດ ບໍ່ພົບຂໍ້ມູນ")

        total_result = ''

        if minus != '':
            total_result = str(minus)+str(result)+str(float_text)
        else:
            total_result = str(result)+str(float_text)

        return total_result

# BUG #
# def NumToWords1(num):
#     # starttime = time.time()
#     # numbers = {0: 'ສູນ', 1: 'ໜຶ່ງ', 2: 'ສອງ', 3: 'ສາມ', 4: 'ສີ່', 5: 'ຫ້າ', 6: 'ຫົກ', 7: 'ເຈັດ', 8: 'ແປດ', 9: 'ເກົ້າ'}
#     numbers = {0: 'SOUN', 1: 'NEUNG', 2: 'SONG', 3: 'SAM', 4: 'SEE', 5: 'HA', 6: 'HOK', 7: 'JED', 8: 'PAED', 9: 'GAO'}
#     main, point = [], []
#     result = ''
#     # argument
#     num = str(num)
#     # split
#     sp = num.replace(',', '.').replace(';', '.').replace(' ','').split('.')
#         # validation
#     if len(sp) > 2:
#         # if incorrect return error message
#         return print('Error!')
#     # remove leading zero rstrip for tailing zero, lstrip for leading zero, strip for both leading-tailing zero
#     if sp[0] <= '0':
#         pass
#     else:
#         sp[0] = sp[0].lstrip('0')
#     # check length
#     cl = len(sp[0])
#     if cl == 1:
#         num = int(sp[0])
#         for a in numbers:
#             if num in set(numbers):
#                 print(numbers[num])
#                 result = numbers[num]
#                 return result
#                 # print(time.time()-starttime)
#                 break
#             else:
#                 print('Error')
#     elif cl == 2:
#         main.clear()
#         m1, m2 = int(sp[0][0]), int(sp[0][1])
#         for a in numbers:
#             if m1 in set(numbers):
#                 if m1 == 1:
#                     main.append('SIP')
#                     break
#                 elif m1 == 2:
#                     main.append('SAO')
#                     break
#                 else:
#                     main.append(numbers[m1]+' SIP')
#                     break
#         for a in numbers:
#             if m2 in set(numbers):
#                 if m2 == 1:
#                     main.append('ED')
#                     break
#                 elif m2 == 0:
#                     pass
#                 else:
#                     main.append(numbers[m2])
#                     break
#         print(' '.join(main))
#         result = ' '.join(main)
#         return result
#         # print(time.time()-starttime)
#     elif cl == 3:
#         main.clear()
#         m1, m2, m3 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2])
#         for a in numbers:
#             if m1 in set(numbers):
#                 main.append(numbers[m1] + ' HOY')
#                 break
#         for a in numbers:
#             if m2 in set(numbers):
#                 if m2 == 0:
#                     break
#                 elif m2 == 1:
#                         main.append('SIP')
#                         break
#                 elif m2 == 2:
#                     main.append('SAO')
#                     break
#                 else:
#                     main.append(numbers[m2]+' SIP')
#                     break
#         for a in numbers:
#             if m3 in set(numbers):
#                 if numbers[m3] == 'NEUNG':
#                     main.append('ED')
#                     break
#                 elif numbers[m3] == 'SOUN':
#                     pass
#                 else:
#                     main.append(numbers[m3])
#                     break
#         print(' '.join(main))
#         result = ' '.join(main)
#         return result
#         # print(time.time()-starttime)
#     elif cl == 4:
#         main.clear()
#         m1, m2, m3, m4 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3])
#         for a in numbers:
#             if m1 in set(numbers):
#                 main.append(numbers[m1] + ' PHUN')
#                 break
#         for a in numbers:
#             if m2 in set(numbers):
#                 if m2 == 0:
#                     break
#                 else:
#                     main.append(numbers[m2] + ' HOY')
#                     break
#         for a in numbers:
#             if m3 in set(numbers):
#                 if m3 == 0:
#                     break
#                 if m3 == 1:
#                     main.append('SIP')
#                     break
#                 elif m3 == 2:
#                     main.append('SAO')
#                     break
#                 else:
#                     main.append(numbers[m3]+' SIP')
#                     break
#         for a in numbers:
#             if m4 in set(numbers):
#                 if m4 == 1 and m3 == 0:
#                     main.append('NEUNG')
#                     break
#                 elif m4 == 1 and m3 != 0:
#                     main.append('ED')
#                     break
#                 elif m4 == 0:
#                     pass
#                 else:
#                     main.append(numbers[m4])
#                     break
#         print(' '.join(main))
#         result = ' '.join(main)
#         return result
#         # print(time.time()-starttime)
#     elif cl == 5:
#         main.clear()
#         m1, m2, m3, m4, m5 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4])
#         for a in numbers:
#             if m1 in set(numbers):
#                 main.append(numbers[m1] + ' MEUN')
#                 break
#         for a in numbers:
#             if m2 in set(numbers):
#                 if m2 == 0:
#                     break
#                 elif m2 == 1:
#                     main.append('ED')
#                     break
#                 else:
#                     main.append(numbers[m2] + ' PHUN')
#                     break
#         for a in numbers:
#             if m3 in set(numbers):
#                 if m3 == 0:
#                     break
#                 else:
#                     main.append(numbers[m3] + ' HOY')
#                     break
#         for a in numbers:
#             if m4 in set(numbers):
#                 if m4 == 0:
#                     break
#                 if m4 == 1:
#                     main.append('SIP')
#                     break
#                 elif m4 == 2:
#                     main.append('SAO')
#                     break
#                 else:
#                     main.append(numbers[m4]+' SIP')
#                     break
#         for a in numbers:
#             if m5 in set(numbers):
#                 if m5 == 1 and m4 == 0:
#                     main.append('NEUNG')
#                     break
#                 elif m5 == 1 and m4 != 0:
#                     main.append('ED')
#                     break
#                 elif m5 == 0:
#                     pass
#                 else:
#                     main.append(numbers[m5])
#                     break
#         print(' '.join(main))
#         result = ' '.join(main)
#         return result
#         # print(time.time()-starttime)
#     elif cl == 6:
#         main.clear()
#         m1, m2, m3, m4, m5, m6 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4]), int(sp[0][5])
#         for a in numbers:
#             if m1 in set(numbers) and m1 != 0:
#                 main.append(numbers[m1] + ' SEAN')
#                 break
#             else:
#                 break
#         for a in numbers:
#             if m2 in set(numbers) and m2 != 0:
#                 main.append(numbers[m2] + ' MEUN')
#                 break
#             else:
#                 break
#         for a in numbers:
#             if m3 in set(numbers) and m3 != 0:
#                 main.append(numbers[m3] + ' PHUN')
#                 break
#             else:
#                 break
#         for a in numbers:
#             if m4 in set(numbers) and m4 != 0:
#                 main.append(numbers[m4] + ' HOY')
#                 break
#             else:
#                 break
#         for a in numbers:
#             if m5 in set(numbers):
#                 if numbers[m5] == 'NEUNG':
#                     main.append('SIP')
#                     break
#                 elif numbers[m5] == 'SONG':
#                     main.append('SAO')
#                     break
#                 else:
#                     main.append(numbers[m5]+' SIP')
#                     break
#         for a in numbers:
#             if m6 in set(numbers):
#                 if numbers[m6] == 'NEUNG':
#                     main.append('ED')
#                     break
#                 elif numbers[m6] == 'SOUN':
#                     pass
#                 else:
#                     main.append(numbers[m6])
#                     break
#         print(' '.join(main))
#         result = ' '.join(main)
#         return result
#         # print(time.time()-starttime)
#     elif cl == 7:
#         main.clear()
#         m1, m2, m3, m4, m5, m6, m7 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4]), int(sp[0][5]), int(sp[0][6])
#         for a in numbers:
#             if m1 in set(numbers):
#                 main.append(numbers[m1] + ' LARN')
#                 break
#         for a in numbers:
#             if m2 in set(numbers) and m2 != 0:
#                 main.append(numbers[m2] + ' SEAN')
#                 break
#             else:
#                 break
#         for a in numbers:
#             if m3 in set(numbers) and m3 != 0:
#                 main.append(numbers[m3] + ' MEUN')
#                 break
#             else:
#                 break
#         for a in numbers:
#             if m4 in set(numbers) and m4 != 0:
#                 main.append(numbers[m4] + ' PHUN')
#                 break
#             else:
#                 break
#         for a in numbers:
#             if m5 in set(numbers) and m5 != 0:
#                 main.append(numbers[m5] + ' HOY')
#                 break
#             else:
#                 break
#         for a in numbers:
#             if m6 in set(numbers):
#                 if numbers[m6] == 'NEUNG':
#                     main.append('SIP')
#                     break
#                 elif numbers[m6] == 'SONG':
#                     main.append('SAO')
#                     break
#                 else:
#                     main.append(numbers[m6]+' SIP')
#                     break
#         for a in numbers:
#             if m7 in set(numbers):
#                 if numbers[m7] == 'NEUNG':
#                     main.append('ED')
#                     break
#                 elif numbers[m7] == 'SOUN':
#                     pass
#                 else:
#                     main.append(numbers[m7])
#                     break
#         print(' '.join(main))
#         result = ' '.join(main)
#         return result
#         # print(time.time()-starttime)
#     elif cl == 8:
#         main.clear()
#         m1, m2, m3, m4, m5, m6, m7, m8 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4]), int(sp[0][5]), int(sp[0][6]), int(sp[0][7])
#         for a in numbers:
#             if m1 in set(numbers) and m1 != 1:
#                 main.append(numbers[m1] + ' SIP LARN')
#                 break
#             else:
#                 main.append('SIP LARN')
#                 break
#         for a in numbers:
#             if m2 in set(numbers) and m2 != 0:
#                 main.append(numbers[m2] + ' LARN')
#                 break
#             else:
#                 break
#         for a in numbers:
#             if m3 in set(numbers) and m3 != 0:
#                 main.append(numbers[m3] + ' SEAN')
#                 break
#             else:
#                 break
#         for a in numbers:
#             if m4 in set(numbers) and m4 != 0:
#                 main.append(numbers[m4] + ' MEUN')
#                 break
#             else:
#                 break
#         for a in numbers:
#             if m5 in set(numbers) and m5 != 0:
#                 main.append(numbers[m5] + ' PHUN')
#                 break
#             else:
#                 break
#         for a in numbers:
#             if m6 in set(numbers) and m6 != 0:
#                 main.append(numbers[m6] + ' HOY')
#                 break
#             else:
#                 break
#         for a in numbers:
#             if m7 in set(numbers):
#                 if numbers[m7] == 'NEUNG':
#                     main.append('SIP')
#                     break
#                 elif numbers[m7] == 'SONG':
#                     main.append('SAO')
#                     break
#                 else:
#                     main.append(numbers[m7]+' SIP')
#                     break
#         for a in numbers:
#             if m8 in set(numbers):
#                 if numbers[m8] == 'NEUNG':
#                     main.append('ED')
#                     break
#                 elif numbers[m8] == 'SOUN':
#                     pass
#                 else:
#                     main.append(numbers[m8])
#                     break
#         print(' '.join(main))
#         result = ' '.join(main)
#         return result
#         # print(time.time()-starttime)
#     elif cl == 9:
#         main.clear()
#         m1, m2, m3, m4, m5, m6, m7, m8, m9 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4]), int(sp[0][5]), int(sp[0][6]), int(sp[0][7]), int(sp[0][8])
#         for a in numbers:
#             if m1 in set(numbers):
#                 if m1 == 0:
#                     break
#                 if m1 > 0: 
#                     if m2 == 0 and m3 == 0:
#                         main.append(numbers[m1] + ' HOY LARN')
#                         break
#                     elif m2 == 0 and m3 > 0:
#                         main.append(numbers[m1] + ' HOY ' + numbers[m3] + ' LARN')
#                         break
#                     elif m2 == 1:
#                         if m3 == 0:
#                             main.append(numbers[m1] + ' HOY SIP LARN')
#                             break
#                         elif m3 ==1:
#                             main.append(numbers[m1] + ' HOY SIP ED LARN')
#                             break
#                         else:
#                             main.append(numbers[m1] + ' HOY SIP ' + numbers[m3] + ' LARN' )
#                             break
#                     elif m2 == 2:
#                         if m3 == 0:
#                             main.append(numbers[m1] + ' HOY SAO LARN')
#                             break
#                         elif m3 ==1:
#                             main.append(numbers[m1] + ' HOY SAO ED LARN')
#                             break
#                         else:
#                             main.append(numbers[m1] + ' HOY SAO ' + numbers[m3] + ' LARN' )
#                             break
#                     else:
#                         if m3 == 0:
#                             main.append(numbers[m1] + ' HOY ' + numbers[m2] + ' SIP LARN')
#                             break
#                         else:
#                             main.append(numbers[m1] + ' HOY ' + numbers[m2] + ' SIP ' + numbers[m3] + ' LARN')
#                             break
#         for a in numbers:
#             if m4 in set(numbers) and m4 != 0:
#                 main.append(numbers[m4] + ' SEAN')
#                 break
#         for a in numbers:
#             if m5 in set(numbers) and m5 != 0:
#                 main.append(numbers[m5] + ' MEUN')
#                 break
#         for a in numbers:
#             if m6 in set(numbers) and m6 != 0:
#                 main.append(numbers[m6] + ' PHUN')
#                 break
#         for a in numbers:
#             if m7 in set(numbers) and m7 != 0:
#                 main.append(numbers[m7] + ' HOY')
#                 break
#         for a in numbers:
#             if m8 in set(numbers) and m8 != 0:
#                 if m8 == 1:
#                     main.append('SIP')
#                     break
#                 elif m8 == 2:
#                     main.append('SAO')
#                     break
#                 else:
#                     main.append(numbers[m8]+' SIP')
#                     break
#         for a in numbers:
#             if m9 in set(numbers) and m9 != 0:
#                 if m9 == 1 and m8 != 0:
#                     main.append('ED')
#                     break
#                 elif m9 == 1 and m8 ==0:
#                     main.append('NEUNG')
#                     break
#                 elif m9 == 0:
#                     break
#                 else:
#                     main.append(numbers[m9])
#                     break
#         print(' '.join(main))
#         result = ' '.join(main)
#         return result
#         # print(time.time()-starttime)
#     elif cl == 10:
#         main.clear()
#         m1, m2, m3, m4, m5, m6, m7, m8, m9, m10 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4]), int(sp[0][5]), int(sp[0][6]), int(sp[0][7]), int(sp[0][8]), int(sp[0][9])
#         for a in numbers:
#             if m1 in set(numbers):
#                 main.append(numbers[m1] + ' TEU')
#                 break
#         for a in numbers:
#             if m2 in set(numbers):
#                 if m2 == 0:
#                     if m3 == 0:
#                         if m4 == 0:
#                             break
#                         else:
#                             main.append(numbers[m4] + ' LARN')
#                             break
#                     elif m3 == 1:
#                         if m4 == 0:
#                             main.append('SIP LARN')
#                             break
#                         elif m4 == 1:
#                             main.append('SIP ED LARN')
#                             break
#                         else:
#                             main.append('SIP ' + numbers[m4] + ' LARN' )
#                             break
#                     elif m3 == 2:
#                         if m4 == 0:
#                             main.append('SAO LARN')
#                             break
#                         elif m4 ==1:
#                             main.append('SAO ED LARN')
#                             break
#                         else:
#                             main.append('SAO ' + numbers[m4] + ' LARN' )
#                             break
#                     else:
#                         if m4 == 0:
#                             main.append(numbers[m3] + ' SIP LARN')
#                             break
#                         if m4 == 1:
#                             main.append(numbers[m3] + ' SIP ED LARN')
#                             break
#                         else:
#                             main.append(numbers[m3] + ' SIP ' + numbers[m4] + ' LARN')
#                             break
#                 if m2 > 0: 
#                     if m3 == 0:
#                         main.append(numbers[m2] + ' HOY LARN')
#                         break
#                     elif m3 == 1:
#                         if m4 == 0:
#                             main.append(numbers[m2] + ' HOY SIP LARN')
#                             break
#                         elif m4 ==1:
#                             main.append(numbers[m2] + ' HOY SIP ED LARN')
#                             break
#                         else:
#                             main.append(numbers[m2] + ' HOY SIP ' + numbers[m4] + ' LARN' )
#                             break
#                     elif m3 == 2:
#                         if m4 == 0:
#                             main.append(numbers[m2] + ' HOY SAO LARN')
#                             break
#                         elif m4 ==1:
#                             main.append(numbers[m2] + ' HOY SAO ED LARN')
#                             break
#                         else:
#                             main.append(numbers[m2] + ' HOY SAO ' + numbers[m4] + ' LARN' )
#                             break
#                     else:
#                         if m4 == 0:
#                             main.append(numbers[m2] + ' HOY ' + numbers[m3] + ' SIP LARN')
#                             break
#                         else:
#                             main.append(numbers[m2] + ' HOY ' + numbers[m3] + ' SIP ' + numbers[m4] + ' LARN')
#                             break
#         for a in numbers:
#             if m5 in set(numbers) and m5 != 0:
#                 main.append(numbers[m5] + ' SEAN')
#                 break
#         for a in numbers:
#             if m6 in set(numbers) and m6 != 0:
#                 main.append(numbers[m6] + ' MEUN')
#                 break
#         for a in numbers:
#             if m7 in set(numbers) and m7 != 0:
#                 main.append(numbers[m7] + ' PHUN')
#                 break
#         for a in numbers:
#             if m8 in set(numbers) and m8 != 0:
#                 main.append(numbers[m8] + ' HOY')
#                 break
#         for a in numbers:
#             if m9 in set(numbers) and m9 != 0:
#                 if m9 == 1:
#                     main.append('SIP')
#                     break
#                 elif m9 == 2:
#                     main.append('SAO')
#                     break
#                 else:
#                     main.append(numbers[m9]+' SIP')
#                     break
#         for a in numbers:
#             if m10 in set(numbers) and m10 != 0:
#                 if m10 == 1 and m9 != 0:
#                     main.append('ED')
#                     break
#                 elif m10 == 1 and m9 ==0:
#                     main.append('NEUNG')
#                     break
#                 elif m10 == 0:
#                     break
#                 else:
#                     main.append(numbers[m10])
#                     break
#         print(' '.join(main))
#         result = ' '.join(main)
#         return result
#         # print(time.time()-starttime)
#     elif cl == 11:
#         main.clear()
#         m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4]), int(sp[0][5]), int(sp[0][6]), int(sp[0][7]), int(sp[0][8]), int(sp[0][9]), int(sp[0][10])
#         for a in numbers:
#             if m1 in set(numbers):
#                 if m1 == 1:
#                     if m2 == 0:
#                         main.append(' SIP TEU')
#                         break
#                     elif m2 == 1:
#                         main.append(' SIP ED TEU')
#                         break
#                     else:
#                         main.append(' SIP ' + numbers[m2] + ' TEU')
#                         break
#                 if m1 == 2:
#                     if m2 == 0:
#                         main.append(' SAO TEU')
#                         break
#                     elif m2 == 1:
#                         main.append(' SAO ED TEU')
#                         break
#                     else:
#                         main.append(' SAO ' + numbers[m2] + ' TEU')
#                         break
#                 else:
#                     if m2 == 1:
#                         main.append(numbers[m1] + ' SIP ED TEU')
#                         break
#                     else:
#                         if m3 == 0:
#                             main.append(numbers[m1] + ' SIP TEU')
#                             break
#                         else:
#                             main.append(numbers[m1] + ' SIP ' + numbers[m2] + ' TEU')
#                             break
#         for a in numbers:
#             if m3 in set(numbers):
#                 if m3 == 0:
#                     if m4 == 0 and m5 == 0:
#                         break
#                     elif m4 == 0 and m5 != 0:
#                         main.append(numbers[m5] + ' LARN')
#                         break
#                     elif m4 == 1:
#                         if m5 == 0:
#                             main.append('SIP LARN')
#                             break
#                         elif m5 == 1:
#                             main.append('SIP ED LARN')
#                             break
#                         else:
#                             main.append('SIP ' + numbers[m5] + ' LARN')
#                             break
#                     elif m4 == 2:
#                         if m5 == 0:
#                             main.append('SAO LARN')
#                             break
#                         elif m5 == 1:
#                             main.append('SAO ED LARN')
#                             break
#                         else:
#                             main.append('SAO ' + numbers[m5] + ' LARN')
#                             break
#                     else:
#                         if m5 == 0:
#                             main.append(numbers[m4] + ' SIP LARN')
#                             break
#                         else:
#                             main.append(numbers[m4] + ' SIP ' + numbers[m5] + ' LARN')
#                             break
#                 if m3 > 0: 
#                     if m4 == 0:
#                         main.append(numbers[m3] + ' HOY ' + numbers[m5] + ' LARN')
#                         break
#                     elif m4 == 1:
#                         if m5 == 0:
#                             main.append(numbers[m3] + ' HOY SIP LARN')
#                             break
#                         elif m5 ==1:
#                             main.append(numbers[m3] + ' HOY SIP ED LARN')
#                             break
#                         else:
#                             main.append(numbers[m3] + ' HOY SIP ' + numbers[m5] + ' LARN' )
#                             break
#                     elif m4 == 2:
#                         if m5 == 0:
#                             main.append(numbers[m3] + ' HOY SAO LARN')
#                             break
#                         elif m5 ==1:
#                             main.append(numbers[m3] + ' HOY SAO ED LARN')
#                             break
#                         else:
#                             main.append(numbers[m3] + ' HOY SAO ' + numbers[m5] + ' LARN' )
#                             break
#                     else:
#                         if m5 == 0:
#                             main.append(numbers[m3] + ' HOY ' + numbers[m4] + ' SIP LARN')
#                             break
#                         else:
#                             main.append(numbers[m3] + ' HOY ' + numbers[m4] + ' SIP ' + numbers[m5] + ' LARN')
#                             break
#         for a in numbers:
#             if m6 in set(numbers) and m6 != 0:
#                 main.append(numbers[m6] + ' SEAN')
#                 break
#         for a in numbers:
#             if m7 in set(numbers) and m7 != 0:
#                 main.append(numbers[m7] + ' MEUN')
#                 break
#         for a in numbers:
#             if m8 in set(numbers) and m8 != 0:
#                 main.append(numbers[m8] + ' PHUN')
#                 break
#         for a in numbers:
#             if m9 in set(numbers) and m9 != 0:
#                 main.append(numbers[m9] + ' HOY')
#                 break
#         for a in numbers:
#             if m10 in set(numbers) and m10 != 0:
#                 if m10 == 1:
#                     main.append('SIP')
#                     break
#                 elif m10 == 2:
#                     main.append('SAO')
#                     break
#                 else:
#                     main.append(numbers[m10]+' SIP')
#                     break
#         for a in numbers:
#             if m11 in set(numbers) and m11 != 0:
#                 if m11 == 1 and m10 != 0:
#                     main.append('ED')
#                     break
#                 elif m11 == 1 and m10 ==0:
#                     main.append('NEUNG')
#                     break
#                 elif m11 == 0:
#                     break
#                 else:
#                     main.append(numbers[m11])
#                     break
#         print(' '.join(main))
#         result = ' '.join(main)
#         return result
#         # print(time.time()-starttime)
#     elif cl == 12:
#         main.clear()
#         m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4]), int(sp[0][5]), int(sp[0][6]), int(sp[0][7]), int(sp[0][8]), int(sp[0][9]), int(sp[0][10]), int(sp[0][11])
#         for a in numbers:
#             if m1 in set(numbers):
#                 if m2 == 0:
#                     if m3 == 0:
#                         main.append(numbers[m1] + ' HOY TEU')
#                         break
#                     else:
#                         main.append(numbers[m1] + ' HOY ' + numbers[m3] + ' TEU')
#                         break
#                 elif m2 == 1:
#                     if m3 == 0:
#                         main.append(numbers[m1] + ' HOY SIP TEU')
#                         break
#                     elif m3 == 1:
#                         main.append(numbers[m1] + ' HOY SIP ED TEU')
#                         break
#                     else:
#                         main.append(numbers[m1] + ' HOY ' + numbers[m2] + ' SIP ' + numbers[m3] + ' TEU')
#                         break
#                 elif m2 == 2:
#                     if m3 == 0:
#                         main.append(numbers[m1] + ' HOY SAO TEU')
#                         break
#                     elif m3 == 1:
#                         main.append(numbers[m1] + ' HOY SAO ED TEU')
#                         break
#                     else:
#                         main.append(numbers[m1] + ' HOY SAO ' + numbers[m3] + ' TEU')
#                         break
#                 else:
#                     if m3 == 0:
#                         main.append(numbers[m1] + ' HOY ' + numbers[m2] + ' SIP TEU')
#                         break
#                     elif m3 == 1:
#                         main.append(numbers[m1] + ' HOY ' + numbers[m2] + ' SIP ED TEU')
#                         break
#                     else:
#                         main.append(numbers[m1] + ' HOY ' + numbers[m2] + ' SIP ' + numbers[m3] + ' TEU')
#                         break
#         for a in numbers:
#             if m4 in set(numbers):
#                 if m4 == 0:
#                     if m5 == 0:
#                         if m6 == 0:
#                             main.append(numbers[m5] + 'SIP LARN')
#                             break
#                         elif m6 == 1:
#                             main.append(numbers[m5] + 'SIP ED LARN')
#                             break
#                         else:
#                             main.append(
#                                 numbers[m5] + 'SIP ' + numbers[m6] + ' LARN')
#                             break
#                     elif m5 == 1:
#                         if m6 == 0:
#                             main.append('SIP LARN')
#                             break
#                         elif m6 == 1:
#                             main.append('SIP ED LARN')
#                             break
#                         else:
#                             main.append('SIP ' + numbers[m6] + ' LARN')
#                             break
#                     elif m5 == 2:
#                         if m6 == 0:
#                             main.append('SAO LARN')
#                             break
#                         elif m6 == 1:
#                             main.append('SAO ED LARN')
#                             break
#                         else:
#                             main.append('SAO ' + numbers[m6] + ' LARN')
#                             break
#                     else:
#                         if m6 == 0:
#                             main.append(numbers[m5] + ' SIP LARN')
#                             break
#                         else:
#                             main.append(numbers[m5] + ' SIP ' + numbers[m6] + ' LARN')
#                             break
#                 if m4 > 0: 
#                     if m5 == 0:
#                         if m6 == 0:
#                             main.append(numbers[m5] + 'SIP LARN')
#                             break
#                         elif m6 == 1:
#                             main.append(numbers[m5] + 'SIP ED LARN')
#                             break
#                         else:
#                             main.append(numbers[m5] + 'SIP ' + numbers[m6] + ' LARN')
#                             break
#                     elif m5 == 1:
#                         if m6 == 0:
#                             main.append(numbers[m4] + ' HOY SIP LARN')
#                             break
#                         elif m6 ==1:
#                             main.append(numbers[m4] + ' HOY SIP ED LARN')
#                             break
#                         else:
#                             main.append(numbers[m4] + ' HOY SIP ' + numbers[m6] + ' LARN' )
#                             break
#                     elif m5 == 2:
#                         if m6 == 0:
#                             main.append(numbers[m4] + ' HOY SAO LARN')
#                             break
#                         elif m6 ==1:
#                             main.append(numbers[m4] + ' HOY SAO ED LARN')
#                             break
#                         else:
#                             main.append(numbers[m4] + ' HOY SAO ' + numbers[m6] + ' LARN' )
#                             break
#                     else:
#                         if m6 == 0:
#                             main.append(numbers[m4] + ' HOY ' + numbers[m5] + ' SIP LARN')
#                             break
#                         else:
#                             main.append(numbers[m4] + ' HOY ' + numbers[m5] + ' SIP ' + numbers[m6] + ' LARN')
#                             break
#         for a in numbers:
#             if m7 in set(numbers) and m7 != 0:
#                 main.append(numbers[m7] + ' SEAN')
#                 break
#         for a in numbers:
#             if m8 in set(numbers) and m8 != 0:
#                 main.append(numbers[m8] + ' MEUN')
#                 break
#         for a in numbers:
#             if m9 in set(numbers) and m9 != 0:
#                 main.append(numbers[m9] + ' PHUN')
#                 break
#         for a in numbers:
#             if m10 in set(numbers) and m10 != 0:
#                 main.append(numbers[m10] + ' HOY')
#                 break
#         for a in numbers:
#             if m11 in set(numbers) and m11 != 0:
#                 if m11 == 1:
#                     main.append('SIP')
#                     break
#                 elif m11 == 2:
#                     main.append('SAO')
#                     break
#                 else:
#                     main.append(numbers[m11]+' SIP')
#                     break
#         for a in numbers:
#             if m12 in set(numbers) and m12 != 0:
#                 if m12 == 1 and m11 != 0:
#                     main.append('ED')
#                     break
#                 elif m12 == 1 and m11 ==0:
#                     main.append('NEUNG')
#                     break
#                 elif m12 == 0:
#                     break
#                 else:
#                     main.append(numbers[m12])
#                     break
#         print(' '.join(main))
#         result = ' '.join(main)
#         return result
#         # print(time.time()-starttime)
#     else:
#         print('ERROR !!! Out of range, the number is too large!!!')



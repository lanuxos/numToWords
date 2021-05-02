# NUMBER TO LAO WORDS CONVERTION SCRIPT 
# RANGE OF NUMBER IS 0-999999999999 [12 DIGITS]
# import time

def NumToWords1(num):
    # starttime = time.time()
    # numbers = {0: 'ສູນ', 1: 'ໜຶ່ງ', 2: 'ສອງ', 3: 'ສາມ', 4: 'ສີ່', 5: 'ຫ້າ', 6: 'ຫົກ', 7: 'ເຈັດ', 8: 'ແປດ', 9: 'ເກົ້າ'}
    numbers = {0: 'SOUN', 1: 'NEUNG', 2: 'SONG', 3: 'SAM', 4: 'SEE', 5: 'HA', 6: 'HOK', 7: 'JED', 8: 'PAED', 9: 'GAO'}
    main, point = [], []
    # argument
    num = str(num)
    # split
    sp = num.replace(',', '.').replace(';', '.').replace(' ','').split('.')
        # validation
    if len(sp) > 2:
        # if incorrect return error message
        return print('Error!')
    # remove leading zero rstrip for tailing zero, lstrip for leading zero, strip for both leading-tailing zero
    if sp[0] <= '0':
        pass
    else:
        sp[0] = sp[0].lstrip('0')
    # check length
    cl = len(sp[0])
    if cl == 1:
        num = int(sp[0])
        for a in numbers:
            if num in set(numbers):
                print(numbers[num])
                # print(time.time()-starttime)
                break
            else:
                print('Error')
    elif cl == 2:
        main.clear()
        m1, m2 = int(sp[0][0]), int(sp[0][1])
        for a in numbers:
            if m1 in set(numbers):
                if m1 == 1:
                    main.append('SIP')
                    break
                elif m1 == 2:
                    main.append('SAO')
                    break
                else:
                    main.append(numbers[m1]+' SIP')
                    break
        for a in numbers:
            if m2 in set(numbers):
                if m2 == 1:
                    main.append('ED')
                    break
                elif m2 == 0:
                    pass
                else:
                    main.append(numbers[m2])
                    break
        print(' '.join(main))
        # print(time.time()-starttime)
    elif cl == 3:
        main.clear()
        m1, m2, m3 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2])
        for a in numbers:
            if m1 in set(numbers):
                main.append(numbers[m1] + ' HOY')
                break
        for a in numbers:
            if m2 in set(numbers):
                if m2 == 0:
                    break
                elif m2 == 1:
                        main.append('SIP')
                        break
                elif m2 == 2:
                    main.append('SAO')
                    break
                else:
                    main.append(numbers[m2]+' SIP')
                    break
        for a in numbers:
            if m3 in set(numbers):
                if numbers[m3] == 'NEUNG':
                    main.append('ED')
                    break
                elif numbers[m3] == 'SOUN':
                    pass
                else:
                    main.append(numbers[m3])
                    break
        print(' '.join(main))
        # print(time.time()-starttime)
    elif cl == 4:
        main.clear()
        m1, m2, m3, m4 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3])
        for a in numbers:
            if m1 in set(numbers):
                main.append(numbers[m1] + ' PHUN')
                break
        for a in numbers:
            if m2 in set(numbers):
                if m2 == 0:
                    break
                else:
                    main.append(numbers[m2] + ' HOY')
                    break
        for a in numbers:
            if m3 in set(numbers):
                if m3 == 0:
                    break
                if m3 == 1:
                    main.append('SIP')
                    break
                elif m3 == 2:
                    main.append('SAO')
                    break
                else:
                    main.append(numbers[m3]+' SIP')
                    break
        for a in numbers:
            if m4 in set(numbers):
                if m4 == 1 and m3 == 0:
                    main.append('NEUNG')
                    break
                elif m4 == 1 and m3 != 0:
                    main.append('ED')
                    break
                elif m4 == 0:
                    pass
                else:
                    main.append(numbers[m4])
                    break
        print(' '.join(main))
        # print(time.time()-starttime)
    elif cl == 5:
        main.clear()
        m1, m2, m3, m4, m5 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4])
        for a in numbers:
            if m1 in set(numbers):
                main.append(numbers[m1] + ' MEUN')
                break
        for a in numbers:
            if m2 in set(numbers):
                if m2 == 0:
                    break
                elif m2 == 1:
                    main.append('ED')
                    break
                else:
                    main.append(numbers[m2] + ' PHUN')
                    break
        for a in numbers:
            if m3 in set(numbers):
                if m3 == 0:
                    break
                else:
                    main.append(numbers[m3] + ' HOY')
                    break
        for a in numbers:
            if m4 in set(numbers):
                if m4 == 0:
                    break
                if m4 == 1:
                    main.append('SIP')
                    break
                elif m4 == 2:
                    main.append('SAO')
                    break
                else:
                    main.append(numbers[m4]+' SIP')
                    break
        for a in numbers:
            if m5 in set(numbers):
                if m5 == 1 and m4 == 0:
                    main.append('NEUNG')
                    break
                elif m5 == 1 and m4 != 0:
                    main.append('ED')
                    break
                elif m5 == 0:
                    pass
                else:
                    main.append(numbers[m5])
                    break
        print(' '.join(main))
        # print(time.time()-starttime)
    elif cl == 6:
        main.clear()
        m1, m2, m3, m4, m5, m6 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4]), int(sp[0][5])
        for a in numbers:
            if m1 in set(numbers):
                main.append(numbers[m1] + ' SEAN')
                break
        for a in numbers:
            if m2 in set(numbers):
                main.append(numbers[m2] + ' MEUN')
                break
        for a in numbers:
            if m3 in set(numbers):
                main.append(numbers[m3] + ' PHUN')
                break
        for a in numbers:
            if m4 in set(numbers):
                main.append(numbers[m4] + ' HOY')
                break
        for a in numbers:
            if m5 in set(numbers):
                if numbers[m5] == 'NEUNG':
                    main.append('SIP')
                    break
                elif numbers[m5] == 'SONG':
                    main.append('SAO')
                    break
                else:
                    main.append(numbers[m5]+' SIP')
                    break
        for a in numbers:
            if m6 in set(numbers):
                if numbers[m6] == 'NEUNG':
                    main.append('ED')
                    break
                elif numbers[m6] == 'SOUN':
                    pass
                else:
                    main.append(numbers[m6])
                    break
        print(' '.join(main))
        # print(time.time()-starttime)
    elif cl == 7:
        main.clear()
        m1, m2, m3, m4, m5, m6, m7 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4]), int(sp[0][5]), int(sp[0][6])
        for a in numbers:
            if m1 in set(numbers):
                main.append(numbers[m1] + ' LARN')
                break
        for a in numbers:
            if m2 in set(numbers):
                main.append(numbers[m2] + ' SEAN')
                break
        for a in numbers:
            if m3 in set(numbers):
                main.append(numbers[m3] + ' MEUN')
                break
        for a in numbers:
            if m4 in set(numbers):
                main.append(numbers[m4] + ' PHUN')
                break
        for a in numbers:
            if m5 in set(numbers):
                main.append(numbers[m5] + ' HOY')
                break
        for a in numbers:
            if m6 in set(numbers):
                if numbers[m6] == 'NEUNG':
                    main.append('SIP')
                    break
                elif numbers[m6] == 'SONG':
                    main.append('SAO')
                    break
                else:
                    main.append(numbers[m6]+' SIP')
                    break
        for a in numbers:
            if m7 in set(numbers):
                if numbers[m7] == 'NEUNG':
                    main.append('ED')
                    break
                elif numbers[m7] == 'SOUN':
                    pass
                else:
                    main.append(numbers[m7])
                    break
        print(' '.join(main))
        # print(time.time()-starttime)
    elif cl == 8:
        main.clear()
        m1, m2, m3, m4, m5, m6, m7, m8 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4]), int(sp[0][5]), int(sp[0][6]), int(sp[0][7])
        for a in numbers:
            if m1 in set(numbers):
                main.append(numbers[m1] + ' SIP LARN')
                break
        for a in numbers:
            if m2 in set(numbers):
                main.append(numbers[m2] + ' LARN')
                break
        for a in numbers:
            if m3 in set(numbers):
                main.append(numbers[m3] + ' SEAN')
                break
        for a in numbers:
            if m4 in set(numbers):
                main.append(numbers[m4] + ' MEUN')
                break
        for a in numbers:
            if m5 in set(numbers):
                main.append(numbers[m5] + ' PHUN')
                break
        for a in numbers:
            if m6 in set(numbers):
                main.append(numbers[m6] + ' HOY')
                break
        for a in numbers:
            if m7 in set(numbers):
                if numbers[m7] == 'NEUNG':
                    main.append('SIP')
                    break
                elif numbers[m7] == 'SONG':
                    main.append('SAO')
                    break
                else:
                    main.append(numbers[m7]+' SIP')
                    break
        for a in numbers:
            if m8 in set(numbers):
                if numbers[m8] == 'NEUNG':
                    main.append('ED')
                    break
                elif numbers[m8] == 'SOUN':
                    pass
                else:
                    main.append(numbers[m8])
                    break
        print(' '.join(main))
        # print(time.time()-starttime)
    elif cl == 9:
        main.clear()
        m1, m2, m3, m4, m5, m6, m7, m8, m9 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4]), int(sp[0][5]), int(sp[0][6]), int(sp[0][7]), int(sp[0][8])
        for a in numbers:
            if m1 in set(numbers):
                if m1 == 0:
                    break
                if m1 > 0: 
                    if m2 == 0:
                        main.append(numbers[m1] + ' HOY LARN')
                        break
                    elif m2 == 1:
                        if m3 == 0:
                            main.append(numbers[m1] + ' HOY SIP LARN')
                            break
                        elif m3 ==1:
                            main.append(numbers[m1] + ' HOY SIP ED LARN')
                            break
                        else:
                            main.append(numbers[m1] + ' HOY SIP ' + numbers[m3] + ' LARN' )
                            break
                    elif m2 == 2:
                        if m3 == 0:
                            main.append(numbers[m1] + ' HOY SAO LARN')
                            break
                        elif m3 ==1:
                            main.append(numbers[m1] + ' HOY SAO ED LARN')
                            break
                        else:
                            main.append(numbers[m1] + ' HOY SAO ' + numbers[m3] + ' LARN' )
                            break
                    else:
                        if m3 == 0:
                            main.append(numbers[m1] + ' HOY ' + numbers[m2] + ' SIP LARN')
                            break
                        else:
                            main.append(numbers[m1] + ' HOY ' + numbers[m2] + ' SIP ' + numbers[m3] + ' LARN')
                            break
        for a in numbers:
            if m4 in set(numbers) and m4 != 0:
                main.append(numbers[m4] + ' SEAN')
                break
        for a in numbers:
            if m5 in set(numbers) and m5 != 0:
                main.append(numbers[m5] + ' MEUN')
                break
        for a in numbers:
            if m6 in set(numbers) and m6 != 0:
                main.append(numbers[m6] + ' PHUN')
                break
        for a in numbers:
            if m7 in set(numbers) and m7 != 0:
                main.append(numbers[m7] + ' HOY')
                break
        for a in numbers:
            if m8 in set(numbers) and m8 != 0:
                if m8 == 1:
                    main.append('SIP')
                    break
                elif m8 == 2:
                    main.append('SAO')
                    break
                else:
                    main.append(numbers[m8]+' SIP')
                    break
        for a in numbers:
            if m9 in set(numbers) and m9 != 0:
                if m9 == 1 and m8 != 0:
                    main.append('ED')
                    break
                elif m9 == 1 and m8 ==0:
                    main.append('NEUNG')
                    break
                elif m9 == 0:
                    break
                else:
                    main.append(numbers[m9])
                    break
        print(' '.join(main))
        # print(time.time()-starttime)
    elif cl == 10:
        main.clear()
        m1, m2, m3, m4, m5, m6, m7, m8, m9, m10 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4]), int(sp[0][5]), int(sp[0][6]), int(sp[0][7]), int(sp[0][8]), int(sp[0][9])
        for a in numbers:
            if m1 in set(numbers):
                main.append(numbers[m1] + ' TEU')
                break
        for a in numbers:
            if m2 in set(numbers):
                if m2 == 0:
                    if m3 == 0:
                        if m4 == 0:
                            break
                        else:
                            main.append(numbers[m4] + ' LARN')
                            break
                    elif m3 == 1:
                        if m4 == 0:
                            main.append('SIP LARN')
                            break
                        elif m4 == 1:
                            main.append('SIP ED LARN')
                            break
                        else:
                            main.append('SIP ' + numbers[m4] + ' LARN' )
                            break
                    elif m3 == 2:
                        if m4 == 0:
                            main.append('SAO LARN')
                            break
                        elif m4 ==1:
                            main.append('SAO ED LARN')
                            break
                        else:
                            main.append('SAO ' + numbers[m4] + ' LARN' )
                            break
                    else:
                        if m4 == 0:
                            main.append(numbers[m3] + ' SIP LARN')
                            break
                        if m4 == 1:
                            main.append(numbers[m3] + ' SIP ED LARN')
                            break
                        else:
                            main.append(numbers[m3] + ' SIP ' + numbers[m4] + ' LARN')
                            break
                if m2 > 0: 
                    if m3 == 0:
                        main.append(numbers[m2] + ' HOY LARN')
                        break
                    elif m3 == 1:
                        if m4 == 0:
                            main.append(numbers[m2] + ' HOY SIP LARN')
                            break
                        elif m4 ==1:
                            main.append(numbers[m2] + ' HOY SIP ED LARN')
                            break
                        else:
                            main.append(numbers[m2] + ' HOY SIP ' + numbers[m4] + ' LARN' )
                            break
                    elif m3 == 2:
                        if m4 == 0:
                            main.append(numbers[m2] + ' HOY SAO LARN')
                            break
                        elif m4 ==1:
                            main.append(numbers[m2] + ' HOY SAO ED LARN')
                            break
                        else:
                            main.append(numbers[m2] + ' HOY SAO ' + numbers[m4] + ' LARN' )
                            break
                    else:
                        if m4 == 0:
                            main.append(numbers[m2] + ' HOY ' + numbers[m3] + ' SIP LARN')
                            break
                        else:
                            main.append(numbers[m2] + ' HOY ' + numbers[m3] + ' SIP ' + numbers[m4] + ' LARN')
                            break
        for a in numbers:
            if m5 in set(numbers) and m5 != 0:
                main.append(numbers[m5] + ' SEAN')
                break
        for a in numbers:
            if m6 in set(numbers) and m6 != 0:
                main.append(numbers[m6] + ' MEUN')
                break
        for a in numbers:
            if m7 in set(numbers) and m7 != 0:
                main.append(numbers[m7] + ' PHUN')
                break
        for a in numbers:
            if m8 in set(numbers) and m8 != 0:
                main.append(numbers[m8] + ' HOY')
                break
        for a in numbers:
            if m9 in set(numbers) and m9 != 0:
                if m9 == 1:
                    main.append('SIP')
                    break
                elif m9 == 2:
                    main.append('SAO')
                    break
                else:
                    main.append(numbers[m9]+' SIP')
                    break
        for a in numbers:
            if m10 in set(numbers) and m10 != 0:
                if m10 == 1 and m9 != 0:
                    main.append('ED')
                    break
                elif m10 == 1 and m9 ==0:
                    main.append('NEUNG')
                    break
                elif m10 == 0:
                    break
                else:
                    main.append(numbers[m10])
                    break
        print(' '.join(main))
        # print(time.time()-starttime)
    elif cl == 11:
        main.clear()
        m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4]), int(sp[0][5]), int(sp[0][6]), int(sp[0][7]), int(sp[0][8]), int(sp[0][9]), int(sp[0][10])
        for a in numbers:
            if m1 in set(numbers):
                if m1 == 1:
                    if m2 == 0:
                        main.append(' SIP TEU')
                        break
                    elif m2 == 1:
                        main.append(' SIP ED TEU')
                        break
                    else:
                        main.append(' SIP ' + numbers[m2] + ' TEU')
                        break
                if m1 == 2:
                    if m2 == 0:
                        main.append(' SAO TEU')
                        break
                    elif m2 == 1:
                        main.append(' SAO ED TEU')
                        break
                    else:
                        main.append(' SAO ' + numbers[m2] + ' TEU')
                        break
                else:
                    if m2 == 1:
                        main.append(numbers[m1] + ' SIP ED TEU')
                        break
                    else:
                        main.append(numbers[m1] + ' SIP ' + numbers[m2] + ' TEU')
                        break
        for a in numbers:
            if m3 in set(numbers):
                if m3 == 0:
                    if m4 == 0:
                        main.append(numbers[m5] + ' LARN')
                        break
                    elif m4 == 1:
                        if m5 == 0:
                            main.append('SIP LARN')
                            break
                        elif m5 == 1:
                            main.append('SIP ED LARN')
                            break
                        else:
                            main.append('SIP ' + numbers[m5] + ' LARN')
                            break
                    elif m4 == 2:
                        if m5 == 0:
                            main.append('SAO LARN')
                            break
                        elif m5 == 1:
                            main.append('SAO ED LARN')
                            break
                        else:
                            main.append('SAO ' + numbers[m5] + ' LARN')
                            break
                    else:
                        if m5 == 0:
                            main.append(numbers[m4] + ' SIP LARN')
                            break
                        else:
                            main.append(numbers[m4] + ' SIP ' + numbers[m5] + ' LARN')
                            break
                if m3 > 0: 
                    if m4 == 0:
                        main.append(numbers[m3] + ' HOY ' + numbers[m5] + ' LARN')
                        break
                    elif m4 == 1:
                        if m5 == 0:
                            main.append(numbers[m3] + ' HOY SIP LARN')
                            break
                        elif m5 ==1:
                            main.append(numbers[m3] + ' HOY SIP ED LARN')
                            break
                        else:
                            main.append(numbers[m3] + ' HOY SIP ' + numbers[m5] + ' LARN' )
                            break
                    elif m4 == 2:
                        if m5 == 0:
                            main.append(numbers[m3] + ' HOY SAO LARN')
                            break
                        elif m5 ==1:
                            main.append(numbers[m3] + ' HOY SAO ED LARN')
                            break
                        else:
                            main.append(numbers[m3] + ' HOY SAO ' + numbers[m5] + ' LARN' )
                            break
                    else:
                        if m5 == 0:
                            main.append(numbers[m3] + ' HOY ' + numbers[m4] + ' SIP LARN')
                            break
                        else:
                            main.append(numbers[m3] + ' HOY ' + numbers[m4] + ' SIP ' + numbers[m5] + ' LARN')
                            break
        for a in numbers:
            if m6 in set(numbers) and m6 != 0:
                main.append(numbers[m6] + ' SEAN')
                break
        for a in numbers:
            if m7 in set(numbers) and m7 != 0:
                main.append(numbers[m7] + ' MEUN')
                break
        for a in numbers:
            if m8 in set(numbers) and m8 != 0:
                main.append(numbers[m8] + ' PHUN')
                break
        for a in numbers:
            if m9 in set(numbers) and m9 != 0:
                main.append(numbers[m9] + ' HOY')
                break
        for a in numbers:
            if m10 in set(numbers) and m10 != 0:
                if m10 == 1:
                    main.append('SIP')
                    break
                elif m10 == 2:
                    main.append('SAO')
                    break
                else:
                    main.append(numbers[m10]+' SIP')
                    break
        for a in numbers:
            if m11 in set(numbers) and m11 != 0:
                if m11 == 1 and m10 != 0:
                    main.append('ED')
                    break
                elif m11 == 1 and m10 ==0:
                    main.append('NEUNG')
                    break
                elif m11 == 0:
                    break
                else:
                    main.append(numbers[m11])
                    break
        print(' '.join(main))
        # print(time.time()-starttime)
    elif cl == 12:
        main.clear()
        m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12 = int(sp[0][0]), int(sp[0][1]), int(sp[0][2]), int(sp[0][3]), int(sp[0][4]), int(sp[0][5]), int(sp[0][6]), int(sp[0][7]), int(sp[0][8]), int(sp[0][9]), int(sp[0][10]), int(sp[0][11])
        for a in numbers:
            if m1 in set(numbers):
                if m2 == 0:
                    if m3 == 0:
                        main.append(numbers[m1] + ' HOY TEU')
                        break
                    else:
                        main.append(numbers[m1] + ' HOY ' + numbers[m3] + ' TEU')
                        break
                elif m2 == 1:
                    if m3 == 0:
                        main.append(numbers[m1] + ' HOY SIP TEU')
                        break
                    elif m3 == 1:
                        main.append(numbers[m1] + ' HOY SIP ED TEU')
                        break
                    else:
                        main.append(numbers[m1] + ' HOY ' + numbers[m2] + ' SIP ' + numbers[m3] + ' TEU')
                        break
                elif m2 == 2:
                    if m3 == 0:
                        main.append(numbers[m1] + ' HOY SAO TEU')
                        break
                    elif m3 == 1:
                        main.append(numbers[m1] + ' HOY SAO ED TEU')
                        break
                    else:
                        main.append(numbers[m1] + ' HOY SAO ' + numbers[m3] + ' TEU')
                        break
                else:
                    if m3 == 0:
                        main.append(numbers[m1] + ' HOY ' + numbers[m2] + ' SIP TEU')
                        break
                    elif m3 == 1:
                        main.append(numbers[m1] + ' HOY ' + numbers[m2] + ' SIP ED TEU')
                        break
                    else:
                        main.append(numbers[m1] + ' HOY ' + numbers[m2] + ' SIP ' + numbers[m3] + ' TEU')
                        break
        for a in numbers:
            if m4 in set(numbers):
                if m4 == 0:
                    if m5 == 0:
                        if m6 == 0:
                            main.append(numbers[m5] + 'SIP LARN')
                            break
                        elif m6 == 1:
                            main.append(numbers[m5] + 'SIP ED LARN')
                            break
                        else:
                            main.append(
                                numbers[m5] + 'SIP ' + numbers[m6] + ' LARN')
                            break
                    elif m5 == 1:
                        if m6 == 0:
                            main.append('SIP LARN')
                            break
                        elif m6 == 1:
                            main.append('HOY SIP ED LARN')
                            break
                        else:
                            main.append('HOY SIP ' + numbers[m6] + ' LARN')
                            break
                    elif m5 == 2:
                        if m6 == 0:
                            main.append('SAO LARN')
                            break
                        elif m6 == 1:
                            main.append('SAO ED LARN')
                            break
                        else:
                            main.append('SAO ' + numbers[m6] + ' LARN')
                            break
                    else:
                        if m6 == 0:
                            main.append(numbers[m5] + ' SIP LARN')
                            break
                        else:
                            main.append(numbers[m5] + ' SIP ' + numbers[m6] + ' LARN')
                            break
                if m4 > 0: 
                    if m5 == 0:
                        if m6 == 0:
                            main.append(numbers[m5] + 'SIP LARN')
                            break
                        elif m6 == 1:
                            main.append(numbers[m5] + 'SIP ED LARN')
                            break
                        else:
                            main.append(numbers[m5] + 'SIP ' + numbers[m6] + ' LARN')
                            break
                    elif m5 == 1:
                        if m6 == 0:
                            main.append(numbers[m4] + ' HOY SIP LARN')
                            break
                        elif m6 ==1:
                            main.append(numbers[m4] + ' HOY SIP ED LARN')
                            break
                        else:
                            main.append(numbers[m4] + ' HOY SIP ' + numbers[m6] + ' LARN' )
                            break
                    elif m5 == 2:
                        if m6 == 0:
                            main.append(numbers[m4] + ' HOY SAO LARN')
                            break
                        elif m6 ==1:
                            main.append(numbers[m4] + ' HOY SAO ED LARN')
                            break
                        else:
                            main.append(numbers[m4] + ' HOY SAO ' + numbers[m6] + ' LARN' )
                            break
                    else:
                        if m6 == 0:
                            main.append(numbers[m4] + ' HOY ' + numbers[m5] + ' SIP LARN')
                            break
                        else:
                            main.append(numbers[m4] + ' HOY ' + numbers[m5] + ' SIP ' + numbers[m6] + ' LARN')
                            break
        for a in numbers:
            if m7 in set(numbers) and m7 != 0:
                main.append(numbers[m7] + ' SEAN')
                break
        for a in numbers:
            if m8 in set(numbers) and m8 != 0:
                main.append(numbers[m8] + ' MEUN')
                break
        for a in numbers:
            if m9 in set(numbers) and m9 != 0:
                main.append(numbers[m9] + ' PHUN')
                break
        for a in numbers:
            if m10 in set(numbers) and m10 != 0:
                main.append(numbers[m10] + ' HOY')
                break
        for a in numbers:
            if m11 in set(numbers) and m11 != 0:
                if m11 == 1:
                    main.append('SIP')
                    break
                elif m11 == 2:
                    main.append('SAO')
                    break
                else:
                    main.append(numbers[m11]+' SIP')
                    break
        for a in numbers:
            if m12 in set(numbers) and m12 != 0:
                if m12 == 1 and m11 != 0:
                    main.append('ED')
                    break
                elif m12 == 1 and m11 ==0:
                    main.append('NEUNG')
                    break
                elif m12 == 0:
                    break
                else:
                    main.append(numbers[m12])
                    break
        print(' '.join(main))
        # print(time.time()-starttime)
    else:
        print('ERROR !!! Out of range, the number is too large!!!')

while True:
    NumToWords1(input('Input Number Here [max length 15]:'))

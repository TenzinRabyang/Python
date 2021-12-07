# Performing Pearson_Correlation function
# The Pearson correlation coefficient measures the linear association between variables
# formula ∑(x-mx)(y-my) / sqrt(∑(x-mx)2∑(y-my)2)
def Pearson_Correlation(pref1,in1,in2):
    from math import sqrt
    import other_similarity as other
    othersi = other.others_similarity()
    
    global no, deno1, deno2, s1, s2, l1, l2, row1, row2, b1, b2, b3, Aavg, Bavg, input1, pref, input2, a, b
    no, deno1, deno2, Aavg, Bavg, a, b = 0, 0, 0, 0, 0, 0, 0
    row1, row2, b1, b2, b3 =[], [], [], [], []
    pref, input1, input2 = pref1, in1, in2
    s1, s2 = " " in input1, " " in input2
    l1, l2 = len(input1), len(input2)
    
    def find_total(x,y):
        global row1, row2, Aavg, Bavg, no, deno1, deno2
        for i in range(len(x)):
            row1.append(x[i])
            row2.append(y[i])
        try:
            Aavg = sum(row1)/len(row1)
            Bavg = sum(row2)/len(row2)
        except:
            pass
        
        for i in range(len(x)):
            a = x[i]
            b = y[i]
            no = no + (a-Aavg)*(b-Bavg)
            deno1 = deno1 + pow(a-Aavg,2)
            deno2 = deno2 + pow(b-Bavg,2)
        return no, deno1, deno2
    
    # USER TO USER----------------------------------------------------------------------------------------1
    if l1 <= 6 and l2 <= 6:
        for i in pref[input1]:
            if i in pref[input2]:
                a = int(pref[input1][i][3])
                b = int(pref[input2][i][3])
                row1.append(a)
                row2.append(b)
        othersi.list_len(row1,row2)
        try:
            Aavg = sum(row1)/len(row1)
            Bavg = sum(row2)/len(row2)
        except:
            pass
        for i in range(len(row1)):
            a = row1[i]
            b = row2[i]
            no = no + (a-Aavg)*(b-Bavg)
            deno1 = deno1 + pow(a-Aavg,2)
            deno2 = deno2 + pow(b-Bavg,2)
    # BOOK TO BOOK----------------------------------------------------------------------------------------2
    elif s1 == True and s2 == True:
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input1 in k1:
                    a = int(v1[3]) # converting to int
                elif input2 in k1:
                    b = int(v1[3]) # converting to int
                row1.append(a)
                row2.append(b)
        try:
            Aavg = sum(row1)/len(row1)
            Bavg = sum(row2)/len(row2)
        except:
            pass
        othersi.list_len(row1,row2)
        for i in range(len(row1)):
            a = row1[i]
            b = row2[i]
            no = no + (a-Aavg)*(b-Bavg)
            deno1 = deno1 + pow(a-Aavg,2)
            deno2 = deno2 + pow(b-Bavg,2)
    # ISBN TO ISBN-------------------------------------------------------------------------------3
    elif l1 == 10 and l2 ==10:
        for k,v in pref.items():
            for k1,v1 in v.items():
                for i in v1:
                    if input1 in v1[0]:
                        a = int(v1[3])
                    elif input2 in v1[0]:
                        b = int(v1[3])
                    row1.append(a)
                    row2.append(b)
                    break
        try:
            Aavg = sum(row1)/len(row1)
            Bavg = sum(row2)/len(row2)
        except:
            pass
        othersi.list_len(row1,row2)
        for i in range(len(row1)):
            a = row1[i]
            b = row2[i]
            no = no + (a-Aavg)*(b-Bavg)
            deno1 = deno1 + pow(a-Aavg,2)
            deno2 = deno2 + pow(b-Bavg,2)
    # ISBN TO USER---------------------------------------------------------------------------4
    elif l1 == 10 and l2 <= 6:
        for k,v in pref.items():
            for k1,v1 in v.items():
                for i in v1:
                    if input1 in v1[0]:
                        b2.append(int(v1[3]))
                    break
        for i in pref[input2]:
            a = int(pref[input2][i][3]) # converting to int
            b1.append(a)
        othersi.list_len(b2,b1)
        find_total(b2,b1)
    # ISBN TO BOOKNAME---------------------------------------------------------------------5
    elif l1 == 10 and s2 == True:
        for k,v in pref.items():
            for k1,v1 in v.items():
                for i in v1:
                    if input1 in v1[0]:
                        b2.append(int(v1[3]))
                    break
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input2 in k1:
                    b3.append(int(v1[3]))
        othersi.list_len(b2,b3)
        find_total(b2,b3)
    # USER TO ISBN --------------------------------------------------------6
    elif l1 <= 6 and l2 == 10:
        for i in pref[input1]:
            a = int(pref[input1][i][3]) # converting to int
            b1.append(a)
        for k,v in pref.items():
            for k1,v1 in v.items():
                for i in v1:
                    if input2 in v1[0]:
                        b2.append(int(v1[3]))
                    break
        othersi.list_len(b1,b2)
        find_total(b1,b2)
    # USER TO BOOKNAME-------------------------------------------------7
    elif l1 <= 6 and s2 == True:
        for i in pref[input1]:
            a = int(pref[input1][i][3]) # converting to int
            b1.append(a)
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input2 in k1:
                    b3.append(int(v1[3]))
        othersi.list_len(b1,b3)
        find_total(b1,b3)
    # BOOKNAME TO ISBN----------------------------------------------8
    elif s1 == True and l2 == 10:
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input1 in k1:
                    b3.append(int(v1[3]))
        for k,v in pref.items():
            for k1,v1 in v.items():
                for i in v1:
                    if input2 in v1[0]:
                        b2.append(int(v1[3]))
                    break
        othersi.list_len(b3,b2)
        find_total(b3,b2)
    # BOOKNAME TO USER----------------------------------------9
    elif s1 == True and l2 <= 6:
        for k,v in pref.items():
            for k1,v1 in v.items():
                if input1 in k1:
                    b3.append(int(v1[3]))
        for i in pref[input2]:
            a = int(pref[input2][i][3]) # converting to int
            b1.append(a)
        othersi.list_len(b3,b1)
        find_total(b3,b1)
    try:
        return no/sqrt(deno1*deno2)
    except:
        return "Undefine, Lack of observation"

"""
------------------------------------------------------------------------
Functions for A08
------------------------------------------------------------------------
Author: Anshul Khatri
ID:     193313680
Email:  khat3680@mylaurier.ca
__updated__ = "2019-11-14"
------------------------------------------------------------------------
""" 
def sum_digit_string(my_str):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in my_str.
    Use: total = sum_digit_string(my_str)
    -------------------------------------------------------
    Parameters:
        my_str - a string (str)
    Returns:
        total - total of all the digits in my_str (int)
    ------------------------------------------------------
    """
    total = 0
    n = len(my_str)
    for i in range(0, n, 1):
        if(my_str[i] == '0'):
            total += 0
        elif(my_str[i] == '1'):
            total += 1
        elif(my_str[i] == '2'):
            total += 2
        elif(my_str[i] == '3'):
            total += 3
        elif(my_str[i] == '4'):
            total += 4
        elif(my_str[i] == '5'):
            total += 5
        elif(my_str[i] == '6'):
            total += 6
        elif(my_str[i] == '7'):
            total += 7
        elif(my_str[i] == '8'):
            total += 8
        elif(my_str[i] == '9'):
            total += 9
        else:
            continue
    
    return total

def find_function(my_str):
    """
    -------------------------------------------------------
    finds most repeated character and returns them
    Use: char = find_functions(my_str)
    -------------------------------------------------------
    Parameters:
        my_str - a string (str)
    Returns:
        char - most repeated characterin the string (char)
    ------------------------------------------------------
    """
    my_str = my_str.lower()
    ac = 0
    bc = 0
    cc = 0
    dc = 0
    ec = 0
    fc = 0
    gc = 0
    hc = 0
    ic = 0
    jc = 0
    kc = 0
    lc = 0
    mc = 0
    nc = 0
    oc = 0
    pc = 0
    qc = 0
    rc = 0
    sc = 0
    tc = 0
    uc = 0
    vc = 0
    wc = 0
    xc = 0
    yc = 0
    zc = 0
    list = []
    n = len(my_str)
    for i in range(0, n, 1):
        if(my_str[i] == 'a'):
            ac += 1
        elif(my_str[i] == 'b'):
            bc += 1
        elif(my_str[i] == 'c'):
            cc += 1
        elif(my_str[i] == 'd'):
            dc += 1
        elif(my_str[i] == 'e'):
            ec += 1
        elif(my_str[i] == 'f'):
            fc += 1
        elif(my_str[i] == 'g'):
            gc += 1
        elif(my_str[i] == 'h'):
            hc += 1
        elif(my_str[i] == 'i'):
            ic += 1
        elif(my_str[i] == 'j'):
            jc += 1
        elif(my_str[i] == 'k'):
            kc += 1
        elif(my_str[i] == 'l'):
            lc += 1
        elif(my_str[i] == 'm'):
            mc += 1
        elif(my_str[i] == 'n'):
            nc += 1
        elif(my_str[i] == 'o'):
            oc += 1
        elif(my_str[i] == 'p'):
            pc += 1
        elif(my_str[i] == 'q'):
            qc += 1
        elif(my_str[i] == 'r'):
            rc += 1
        elif(my_str[i] == 's'):
            sc += 1
        elif(my_str[i] == 't'):
            tc += 1
        elif(my_str[i] == 'u'):
            uc += 1
        elif(my_str[i] == 'v'):
            vc += 1
        elif(my_str[i] == 'w'):
            wc += 1
        elif(my_str[i] == 'x'):
            xc += 1
        elif(my_str[i] == 'y'):
            yc += 1
        elif(my_str[i] == 'z'):
            zc += 1
        else:
            continue
        
    list.append(ac)
    list.append(bc)
    list.append(cc)
    list.append(dc)
    list.append(ec)
    list.append(fc)
    list.append(gc)
    list.append(hc)
    list.append(ic)
    list.append(jc)
    list.append(kc)
    list.append(lc)
    list.append(mc)
    list.append(nc)
    list.append(oc)
    list.append(pc)
    list.append(qc)
    list.append(rc)
    list.append(sc)
    list.append(tc)
    list.append(uc)
    list.append(vc)
    list.append(wc)
    list.append(xc)
    list.append(yc)
    list.append(zc)
    max = 0
    for j in range(0, 25, 1):
        if(list[j] > max):
            max = list[j]
            var = j
        else:
            continue

    place = var + 1

    if(place == 1):
        char = 'a'
    elif(place == 2):
        char = 'b'
    elif(place == 3):
        char = 'c'
    elif(place == 4):
        char = 'd'
    elif(place == 5):
        char = 'e'
    elif(place == 6):
        char = 'f'
    elif(place == 7):
        char = 'g'
    elif(place == 8):
        char = 'h'
    elif(place == 9):
        char = 'i'
    elif(place == 10):
        char = 'j'
    elif(place == 11):
        char = 'k'
    elif(place == 12):
        char = 'l'
    elif(place == 13):
        char = 'm'
    elif(place == 14):
        char = 'n'
    elif(place == 15):
        char = 'o'
    elif(place == 16):
        char = 'p'
    elif(place == 17):
        char = 'q'
    elif(place == 18):
        char = 'r'
    elif(place == 19):
        char = 's'
    elif(place == 20):
        char = 't'
    elif(place == 21):
        char = 'u'
    elif(place == 22):
        char = 'v'
    elif(place == 23):
        char = 'w'
    elif(place == 24):
        char = 'x'
    elif(place == 25):
        char = 'y'
    elif(place == 26):
        char = 'z'
        
    return  char




def string_capitalizer(my_str):
    """
    -------------------------------------------------------
    Asks a user for an string, and
    returns a new string that has first letter as capital.
    Use:  string_org = string_capitalizer(my_str)
    -------------------------------------------------------
    Parameters:
        my_str - (string) : The string with sentences in it.
    Returns:
        str_new- (string) : The string with the required operation.
    ------------------------------------------------------
    """
    str_new = None
    if len(my_str)==0 :
        str_new = None
        
    else:
        x=list(my_str)
        x[0]=x[0].upper() 
    
        for i in range(len(x)):
            if x[i]== '.' :
                    x[i+2]=x[i+2].upper()
    x=''.join(x)
    str_new=x
    return str_new
                

def is_word_chain(mylist):
    """
    -------------------------------------------------------
    Asks a user for an list of words, and
    returns wheather it forms a word chain or not .
    Use:  word_ch = is_word_chain(mylist)
    -------------------------------------------------------
    Parameters:
        mylist - (list) : The list with words in it.
    Returns:
        present- (boolean) : Returns true or false .
    ------------------------------------------------------
    """
    present=None   
    x=[]    
    if len(mylist)==0 or len(mylist)==1:
            present=False
        
    else:
        
        for i in range(4):
            x.append(mylist[i].split())
            print(x[0][0][-1])
            #print(mylist[i+1][0])
            if x[0][0][-1].upper()== x[1][1][1].upper() :
                present=True
            else:
                present=False 
 
    return present




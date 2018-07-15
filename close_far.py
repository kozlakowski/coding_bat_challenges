









def close_far(a,b,c):

    b_close = ""
    c_close = ""

    if (abs(b) == abs(a) + 1) or (abs(b) == abs(a) - 1):
        b_close = "close"

    elif (abs(c) == abs(a) + 1) or (abs(c) == abs(a) - 1):
        c_close = "close"



    b_far = ""
    c_far = ""

    if ((abs(b) >= abs(a) + 2) or (abs(b) <= abs(a) - 2)) and ((abs(b) >= abs(c) + 2) or (abs(b) <= abs(c) - 2)):
        b_far = "far"

    elif ((abs(c) >= abs(a) + 2) or (abs(c) <= abs(a) - 2)) and ((abs(c) >= abs(b) + 2) or (abs(c) <= abs(b) - 2)):
        c_far = "far"

    print(b_close, c_close, b_far, c_far)



    if ((b_close == "close") or (c_close == "close")) and ((b_far == "far") or (c_far == "far")):
        return True
    else:
        return False




print(close_far(1,2,3))











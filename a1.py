#############################PART-1#############################################



#half adder simply adds two bits and outputs a sum and carry

#inputs (a and b)	carry|   sum
#        0     0     0   |    0
#        0     1     0   |    1
#        1     0     0   |    1
#        1     1     1   |    0

#carry = and gate
#sum = if both a,b same then 0 otherwise 1 (xor)

def hadd(a,b):
    return ((a or b) and not (a and b), a and b)

# The full adder can add 3 bits that can handle an incoming carry

# input   a b c         ouput carry sum
        # 1 0 0                 0    1
        # 0 1 0                 0    1
        # 0 0 1                 0    1
        # 1 1 0                 1    0
        # 1 0 1                 1    0
        # 0 1 1                 1    0
        # 1 1 1                 1    1


#QUESTION1######################################################################

def add(a,b,c):
    (s1,c1) = hadd(a,b)
    (s2,c2) = hadd(s1,c)
    return (s2,c1 or c2)

#explanation for the code is due to the original logic circuit design
#a + b = sum1 + carry1
#sum 1 + carry input = sum 2 + carry 2
#final output = sum 2 + bool addition of carry 2 and carry 1

#QUESTION2######################################################################

def add4(a0,a1,a2,a3,b0,b1,b2,b3,c):
    (s1,c1) = add(a0,b0,c)
    (s2,c2) = add(a1,b1,c1)
    (s3,c3) = add(a2,b2,c2)
    (s4,c4) = add(a3,b3,c3)
    return (s1,s2,s3,s4,c4)

#QUESTION3######################################################################

def cmp(a0,a1,a2,a3, b0,b1,b2,b3):
    if a3==b3 and a2==b2 and a1==b1 and a0==b0:
        return True

    elif a3 <b3:
        return True

    else:
        if a2 <b2:
            return True
        else:
            if a1 <b1:
                return True
            else:
                if a0 <b0:
                    return True
                else:
                    return False

#QUESTION4######################################################################

#we will start by making half subtractor or 2 bit subtractor and then proceed to
#3 bit and 4 bit subtractor

#inputs (a and  b)   difference| borrow
#        0  -   0          0   |    0
#        0  -   1          1   |    1
#        1  -   0          1   |    0
#        1  -   1          0   |    0

#Xor operation on a and b gives the value of the Difference.
#AND operation on a complement and b gives the value of Borrow.

def hsub(a,b):
    difference = (a or b) and not (a and b)
    borrow = (not a) and b
    return (difference,borrow)

#now lets move onto 3 bit or full subtractor

# input   a b c        ouput differ borrow
        # 1 0 0                 1   0
        # 0 1 0                 1   1
        # 0 0 1                 1   1
        # 1 1 0                 0   0
        # 1 0 1                 0   0
        # 0 1 1                 0   1
        # 1 1 1                 1   1
        # 0 0 0                 0   0

#note here that a and b and c are bits written in which the diff (D) = a-b
#and borrow(B) = D-c
# concept:0 - 1 => B=1 and D=1 (first take borrow then subtract)

def fsub(a,b,c):
    (D1,B1) = hsub(a,b)
    (D2,B2) = hsub(D1,c)
    return (D2, B2 or B1)

#now making a 4 bit subtractor

# a0  a1  a2  a3
# 1   1   0   1
# --------------
# b0  b1  b2  b3  to be subtracted
# 1   0   0   1
# ______________
# c0  c1  c2  c3  these are borrows eg - c0 is borrow from row 2, c1 is borrow from row 3, c2 is borrow from row 4
# 0   0   0   0   B
# ______________
# 0   1   0   0   D

def sub4(a0,a1,a2,a3,b0,b1,b2,b3):
    if cmp(a0,a1,a2,a3,b0,b1,b2,b3) == False:
        (D1,B1) = fsub(a0,b0,False) #the question hasnt given an input third bit
        (D2,B2) = fsub(a1,b1,B1)
        (D3,B3) = fsub(a2,b2,B2)
        (D4,B4) = fsub(a3,b3,B3)
        return (True,D1,D2,D3,D4)
    else:
        (D1,B1) = fsub(b0,a0,False)
        (D2,B2) = fsub(b1,a1,B1)
        (D3,B3) = fsub(b2,a2,B2)
        (D4,B4) = fsub(b3,a3,B3)
        return (False,D1,D2,D3,D4)





############################PART-2##############################################





#QUESTION1######################################################################

# to make an 8 bit adder using two 4 bit adders

def add8(a,b,c):

    a = (a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7])
    b = (b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7])

    (s1,s2,s3,s4,c1)    = add4(a[0],a[1],a[2],a[3],b[0],b[1],b[2],b[3],False)
    (s5,s6,s7,s8,cout)  = add4(a[4],a[5],a[6],a[7],b[4],b[5],b[6],b[7],c1)

    s = (s1,s2,s3,s4,s5,s6,s7,s8)

    return s,cout

#QUESTION2######################################################################

#To make a multiplier

# def mul4(a,b):
#     a = (a[0],a[1],a[2],a[3])
#     b = (b[0],b[1],b[2],b[3])

#     if a == (False, False, False, False):
#         return (False,False,False,False,False,False,False,False) #base case for recursion
#     elif b == (False, False, False, False):
#         return (False,False,False,False,False,False,False,False) #base case for recursion


#     else:
#         (c_sign,c1,c2,c3,c4) = sub4(b[0],b[1],b[2],b[3], True, False, False, False) #subtracting 1 from b
#         c_prime = (c1,c2,c3,c4) #ignoring the sign as we only need the magnitude

#         a_prime = (a[0],a[1],a[2],a[3], False,False,False,False)
#         rec = mul4(c_prime,a)

#         (x,y) = add8(a_prime,rec,False)
#         return x

# print(mul4((True,True,False,True), (True,False,False,True)))

def mul4(a,b):
    a = (a[0],a[1],a[2],a[3])
    b = (b[0],b[1],b[2],b[3])

    (s1,c1) = a[0] and b[0], False

    (s2,c2) = add(a[0] and b[1], a[1] and b[0], c1)
    (s3,c3) = add(a[1] and b[1], a[2] and b[0], c2)
    (s4,c4) = add(a[2] and b[1], a[3] and b[0], c3)
    (s5,c5) = add(a[3] and b[1], False, c4)
    (s6,c6) = add(False, False, c5)

    (s7,c7) = add(a[0] and b[2], s3, False)
    (t1,c8) = add(a[1] and b[2], s4, c7)
    (t2,c9) = add(a[2] and b[2], s5, c8)
    (t3,c10) = add(a[3] and b[2], s6, c9)

    (u1,c11) = add(a[0] and b[3], t1, False)
    (u2,c12) = add(a[1] and b[3], t2, c11)
    (u3,c13) = add(a[2] and b[3], t3, c12)
    (u4,c14) = add(a[3] and b[3], False, c13)

    P1 = s1
    P2 = s2
    P3 = s7
    P4 = u1
    P5 = u2
    P6 = u3
    P7 = u4
    P8 = c14

    return (P1,P2,P3,P4,P5,P6,P7,P8)

#########################END OF ASSIGNMENT 1####################################
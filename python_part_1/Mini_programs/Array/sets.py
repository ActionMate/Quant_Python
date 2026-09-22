"""     Without manually calculating the answers, write Python statements that produce:
Q1 : All elements appearing in either set.
Q2 : Elements common to both.
Q3 : Elements in A but not B.
Q4 : Elements appearing in exactly one of the two sets.
Q5 : Check whether 12 belongs to A.     """

A = {2, 4, 6, 8, 10}
B = {4, 8, 12, 16}

'''     Question 1 :    '''
print(A|B)
'''     Question 2 :    '''
print(A&B)
'''     Question 3 :    '''
print(A-B)
'''     Question 4 :    '''
print((A|B)-(A&B))
'''     Question 5 :    '''
print(12 in A)
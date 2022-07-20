A = [ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ]
B = 48

# total sum - ( continuous ) minimum sum
# have to find sub array of length -> len(A) - B with minimum sum and minus from total sum
tSum = sum(A)
cSum = 0
mSum = 100000
for i in range(0, B):
    for j in range(i, i + len(A)-B):
        cSum = cSum + A[j]
    if cSum < mSum:
        mSum = cSum

    cSum = 0

print(tSum - mSum)


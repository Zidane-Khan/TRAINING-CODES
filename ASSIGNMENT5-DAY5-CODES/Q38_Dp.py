# 38. Given two strings s1 and s2, find the length of their longest common 
# subsequence (LCS). Solve the problem using dynamic programming. 

s1="zidane"
s2="khan"

s3=[]
for i in s1:
    # print(i)
    for j in s2:
        # print(j)
        if i==j:
            print(s3.append(i))

print(f"The LCS of given word is {''.join(s3)}")
# count=0
# for i in s3:
#     count+=1
# print(count)

LENGTH=len(s3)
print(f"the length of LCS is {LENGTH}")

 
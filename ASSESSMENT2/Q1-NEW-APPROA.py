# 1. Write a Python function that compresses a string such that repeated characters 
# are replaced by the character followed by the count of occurrences. For example, the string "aaabbbcc" should become "a3b3c2". If the compressed string is not shorter than the original string, return the original string.
# a. Example Input: "aabbbcccc"
#      Expected Output: "a2b3c4"
# b. Example Input: "abc"
#      Expected Output: "abc"
STRING="aabbbcccc"
for i in range(len(STRING)):
    count=0
    if STRING[i]!=STRING[i-1]:
        count+=1
        for j in range(1, len(STRING)):
            if (STRING[i]==STRING[j] and i!=j):
                count=count+1
        
        if count==1:
            print(STRING[i],end='')
        else:
            print(STRING[i]+str(count),end='')
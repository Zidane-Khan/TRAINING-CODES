

My_File = 'C:\\Users\\Zidane Khan\\Downloads\\EXAMPLE.txt'  

with open(My_File, 'r') as file:

    contents = file.read()

    print("This is content of Source File",contents)

    words=contents.split(" ")
    print(words)
    
    # count=0
    # for i in words:
    #     for j in words:
    #         if i==j:
    #             count=count+1
    #     print(i,count)

    word_count={}
    # word_count=[]
    # count=0
    for i in words:
        if i in word_count:
            word_count[i]+=1
        else:
            word_count[i]=1
 
        
    for i in word_count.items():

        print(i)




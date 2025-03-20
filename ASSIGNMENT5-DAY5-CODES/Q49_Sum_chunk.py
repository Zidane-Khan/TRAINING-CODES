# 49. Write a Python program that uses multiple threads to compute the sum 
# of elements in a large list. Divide the list into chunks and let each thread 
# compute the sum of its chunk. 


# import threading
# import time

# List=[2,4,6,1,2]
# def nsum_elements():

#     Sum=0
#     for i in List:
#         Sum=Sum+i
#     print(Sum)
#     time.sleep(2)



# t1=threading.Thread(target=nsum_elements)
# # t2=threading.Thread(target=letter)


# t1.start()
# t1.join



# print("\nfinished ")




import threading

# List of numbers
List = [2, 4, 6, 1, 2, 8, 10, 7, 3, 5, 9, 12, 15]

# Function to compute sum of elements in a chunk of the list
def nsum_elements(start, end):
    chunk_sum = sum(List[start:end])
    print(f"Sum of elements from index {start} to {end-1}: {chunk_sum}")
    return chunk_sum


def main():
    # Divide the list into two parts
    middle = len(List) // 2
    
    # Create two threads, one for each chunk of the list
    thread1 = threading.Thread(target=nsum_elements, args=(0, middle))
    thread2 = threading.Thread(target=nsum_elements, args=(middle, len(List)))

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print("Finished computing the sum.")

if __name__ == "__main__":
    main()

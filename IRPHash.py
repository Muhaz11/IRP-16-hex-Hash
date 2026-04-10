MAX_SIZE = 2 ** 64 #So, our hexadecimal hash value is 16 characters long

text = input("Please enter the message you would like to hash: ")

#This list contains the first 50 primes
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]

total = 0

#Goes through every character in the text and weights it by the corresponding prime
for i in range(len(text)):
    total += ord(text[i]) * primes[i % 50]

    total  = total * (total % primes[i % 50] + 1)
    total ^= total >> 3
    total ^= total << 11
    total = total % MAX_SIZE

#A conditional final calculation
if total % 2 == 1:
    total = total * 5 - 11
else:
    total = total * 7 + 3

total = total % MAX_SIZE 


print(f"{total:016x}")


#1. Write a program that accepts a list from user and print the alternate element of list. 
def print_alternate_elements(input_list):
def print_alternate_elements(input_list):
    for i in range(0, len(input_list), 2):
        print(input_list[i])

def main():
    user_input = input("Enter elements of the list separated by spaces: ")
    user_list = user_input.split()
    print("Alternate elements of the list:")
    print_alternate_elements(user_list)

if __name__ == "__main__":
    main()

#2. Write a program that accepts a list from user. Your program should reverse the content of list and display it. Do not use reverse() method. 

def print_reverse_list(input_list):
    for i in range (len(input_list)-1,-1,-1):
        print(input_list[i])
def main():
    user_input= input("Enter elements of list seperated by spaces: ")
    user_list = user_input.split()
    print("Reverse list")
    print_reverse_list(user_list)
if __name__=="__main__":
    main()
#3. Find and display the largest number of a list without using built-in function max(). Your program should ask the user to input values in list from keyboard. 

def largest_no_of_list(input_list):
    largest_no = input_list[0]
    for number in input_list[1:]:
        if number>largest_no:
            largest_no=number
    return(largest_no)
def main():
    user_input = input("Enter integers list separated by spaces: ")
    user_list = [int(x) for x in user_input.split()]
    largest_no = largest_no_of_list(user_list)
    print("The largest number is:", largest_no)
    
if __name__=="__main__":
    main()
 #Write a program that input a string and ask user to delete a given word from a string. 

s = input("Enter a string: ")
d = input("Enter a string you want to delete: ")
index = s.find(d)
if index != -1:  
    new_s = s[:index]+s[index+len(d):]  
    print("Modified string:", new_s)
else:
    print("Substring not found in the string.")
#Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. It should print the date in the form 
#March 12, 2021. 
d = input("Enter a date in format mm/dd/yyyy: ")
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month, day, year = d.split('/')

month_num = int(month)
day_num = int(day)

month_name = month_names[month_num - 1]
print(month_name, day_num, ",", year)
#Write a program with a function that accepts a string from keyboard and create a new string after converting character of each word 
#capitalized. For instance, if the sentence is "stop and smell the roses." the output should be "Stop And Smell The Roses" 
s=input("enter a string")
p=s.title()
print(p)
#4. Find the sum of each row of matrix of size m x n. For example for the following matrix output will be like this: 
#2117 12 52915 
#Sum of row 1 = 32 Sum of row 2 = 31 Sum of row 3 = 63 

n = int(input("Enter the number of rows: ")) 
m = int(input("Enter the number of columns: ")) 
  
matrix = [] 

print("Enter values in matrix:") 

# For user input 
for i in range(n):
    data = input().split()  # Split input string into a list of numbers
    data = list(map(int, data))  # Convert list of strings to list of integers
    matrix.append(data) 

# For printing row-wise sum 
for i in range(n):
    row_sum = sum(matrix[i])
    print('Sum of row', i+1, ':', row_sum)
#9. Write a program to add two matrices of size n x m. 
n = int(input("Enter the number of rows: ")) 
m = int(input("Enter the number of columns: ")) 
# Input matrix 1
print("Enter values for matrix 1:") 
matrix1 = []
for i in range(n):
    data = list(map(int, input().split()))
    matrix1.append(data) 
# Input matrix 2
print("Enter values for matrix 2:") 
matrix2 = []
for i in range(n):
    data = list(map(int, input().split()))
    matrix2.append(data) 

# Initialize result matrix with zeros
result = [[0 for _ in range(m)] for _ in range(n)]

# Add matrices
for i in range(n):
    for j in range(m):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

# Print the result matrix
print("Sum of matrices:")
for row in result:
    print(row)
#10. Write a program to multiply two matrices 
n = int(input("Enter the number of rows: ")) 
m = int(input("Enter the number of columns: ")) 

# Input matrix 1
print("Enter values for matrix 1:") 
matrix1 = []
for i in range(n):
    data = list(map(int, input().split()))
    matrix1.append(data) 

# Input matrix 2
print("Enter values for matrix 2:") 
matrix2 = []
for i in range(n):
    data = list(map(int, input().split()))
    matrix2.append(data) 

# Initialize result matrix
result = [[0 for _ in range(m)] for _ in range(n)]    

# Matrix multiplication
for i in range(n):  # iterate through rows of matrix1
    for j in range(m):  # iterate through columns of matrix2
        for k in range(n):  # iterate through columns of matrix1 or rows of matrix2
            result[i][j] += matrix1[i][k] * matrix2[k][j]

# Print result
print("Result of matrix multiplication:")
for row in result:
    print(row)
    #LOOPS
 #1Write a Python program to print the numbers from 1 to 10 using a for loop. 
for i in range(1,11):
    print(i)
#2. Write a Python program to print the numbers from 20 to 1 using a while loop. 
x = 20
while x >= 1:
    print(x)
    x -= 1
    
#3. Write a program to print even numbers from 1 to 10. 
for i in range(1,11):
    if i % 2 ==0:
        print(i)
#4. Write a program that prompts the user to enter a number n and prints all the numbers from 1 to n. 
n=int(input("enter a number:"))
for i in range(1,n+1):
    print(i)
#5. Write a program that prompts the user to enter a number n, and then prints all the odd numbers between 1 and n. 
n=int(input("enter a number:"))
for i in range (1,n+1):
    if i % 2!=0:
        print(i)    
#6. Write a program that prints 'Happy Birthday!' five times on screen. 
for i in range(1,6):
    print('Happy Birthday!')
#7. Write a program that takes a number n as input from the user and generates the first n terms of the series formed by squaring the 
##natural numbers. Sample output Enter a number: 6 The first 6 terms of the series are: 149 16 25 36 
n = int(input("Enter a number: "))

print("The first", n, "terms of the series are:")
for i in range(1, n + 1):
    print(i ** 2, end=" ")
#7. Write a program that prompts the user to input a number and prints its multiplication table
n=int(input("enter a number:"))
print("the multiplication table of ",n)
for i in range (1,11):
    print(i*n)
#8.  Write a Python program to print the first 8 terms of an arithmetic progression starting with 3 and having a common difference of 4. The 
#program should output the following sequence: 3 7 11 15 19 23 27 31 
s = 3
common_difference = 4
terms = 8

# Print the first 8 terms of the arithmetic progression
print("The first", terms, "terms of the arithmetic progression are:")
for i in range(terms):
    term = s + i * common_difference
    print(term, end=" ")


#9. Write a Python program to print the first 6 terms of a geometric sequence starting with 2 and having a common ratio of 3. The program should output the following sequence: 2 6 18 54 162 486 
n=int(input("enter no of terms"))
r=3
for i in range(0,n):
    terms =2*r**i
    print(terms,end=" ")


#10. Write a program that asks the user for a positive integer value. The program should calculate the sum of all the integers from 1 up to the number entered. For example, if the user enters 20, the loop will find the sum of 1, 2, 3, 4, 20. 
n=int(input("enter a number:"))
s=0
for i in range(1,n+1):
    s+=i
print(s)

#11. write a program that takes a positive integer N as input and calculates the sum of the reciprocals of all numbers from 1 up to N. The program should display the final sum. Output of the program should be like: Enter a positive integer: 5 The sum of reciprocals from 1 to 5 is: 2.28 
n=int(input("enter a number:"))
result=0
for i in range(1,n+1):
    result +=(1/i)
print("The sum of reciprocals from 1 to",n,"is" ,result)    
#12. Write a program that prompts the user to enter a number and repeats this process 5 times. The program should accumulate the numbers entered and then display the final running total. Sample Output: Enter a number: 10 Enter a number: 15 Enter a number: 35 Enter a number: 40 Enter a number: 50 The final running total is: 150 
total = 0
for i in range(5):
    num = int(input("Enter a number: "))
    total += num

print("The final running total is:", total)

#13. Write a program that prompts the user to enter a positive integer and calculates its factorial. The factorial of a positive integer 'n' is denoted as 'n!' and is calculated by multiplying all the integers from 1 to 'n' together. For example, the factorial of 5 (denoted as 5!) is calculated as 1 x 2 x 3 x 4 x 5. The program should display the factorial value if the input is a positive number, or display a message stating that the factorial does not exist for negative numbers. Additionally, for an input of zero, the program should output that the factorial of 0 is 1. 

n=int(input("enter a number:"))
if n < 0:
    print("Factorial of negative number does not exist")
elif n == 0:
    print("Factorial of zero is 1")
else:    
   factorial = 1
   for i in range(1,n+1):
       factorial *=i
   print(factorial)    

#14. Write a Python program that prompts the user to enter a base number and an exponent, and then calculates the power of the base to the exponent. The program should not use the exponentiation operator (**) or the math.pow() function. The program should handle both positive and negative exponents. 
n=int(input("enter a number:"))
e=int(input("enter an exponent:"))
r=1
if e>0:
    for i in range(e):
        r *=n
elif e < 0:
    for i in range(-e):
        r /=n
else :
    r=1
print("result",r)    
    





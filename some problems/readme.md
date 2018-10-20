1. [x] 1.1) Write a program that creates a singly linked list in which every node, besides the next pointer, contains a variable of type struct/class which will contain some data about a student. The function will return the address of the first node in the list. Read input for:
    - name: 20 chars
    - surname: 20 chars
    - a vector that will contain 3 grades of the student  
    I did not bother with input validation. I just wanted to see the program working. Also, the grades are not from input, but are randomly generated.  
2. [x] 1.2) Write a program that will display the name, surname and the average grade of each student from the list of the previous exercise. The function will receive as a parameter the first element in the list.
3. [x] 1.3) Write a function that returns the average grade of all students in the linked list
4. [x] 2) Write a program that creates and outputs a singly linked list. Each node contains a next pointer and a number <= 100000. The numbers are found, all on one line, in a text file.
5. [x] 3) Write a program that creates and prints two singly linked lists. The first one will contain, in the reading order, the even numbers and the second will contain odd numbers, in the same order. The numbers are read from a text file. All of them are on a single line, separated by a single space. Ex: 0 2 5 9 8 3 6 7 1, one list will be: 0 2 8 6, the second: 5 9 3 7 1
6. [x] 3.1) Write a subprogram that creates a text file with the data from the two linked lists from before. The first line will contain the data from the first list, the second line the data from the second list.
7. [x] 4) Write a subprogram that adds a new node AT THE END of a singly linked list. Each node contains a pointer to the next node and a real number in it.
8. [x] 4.1) Write a subprogram that adds a new node AT THE BEGINNING of a singly linked list.Each node contains a pointer to the next node and a real number in it.
9. [x] 5) The nodes of a singly linked list contain, besides the pointer to the next node, a number of 1 digit. The list has at least 1 node and a maximum of 6 nodes. Write a function calculate and show to compute the value by concatinating the value of each node in the reading order. Ex: the function returns **956** and the list is ```0 -> 9 -> 5 -> 6```
10. [x] 6) By concatinating two singly linked list, a third singly linked list is greated containing, in order, the nodes of the first list, followed by the nodes of the second list. Write a function that concatinates two singly linked lists.
11. [x] 7) Write a program that stores a matrix with **m** rows and **n** columns and creates **m** singly linked lists where each list stores the elements of each row. **my solution may not be the best in terms of optimization**
12. [x] 8) A singly linked list stores a single character in each node. Write a function that tests if the result from concatinating the lists items is a palindrom or not.
13. [ ] 9) Read a permutation of numbers from 1,2,....,n. Use a circular linked list, print all its circular permutations. Ex: read 1 2 3 => print 1 2 3, 2 3 1, 3 1 2
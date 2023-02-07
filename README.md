# Lab 2
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Julie Deng
- Ellen Ko

## Lab Question Answers

Question 1: How did the reliability of UDP change when you added 50% loss to your local environment? Why did this occur?
Only half the numbers ended up getting sent through. This is because the 50% loss meant that there was more congestion in the network. 
Question 2: How did the reliability of TCP change? Why did this occur?
All the numbers still get sent through but the speed that it gets sent through at slows down drastically. This is because TCP still ensure that everything that gets sent through is received on the other end. s 
Question 3: How did the speed of the TCP response change? Why might this happen?
The speed change is because it takes more time to recover and acknowledge the message. 

1) What is argc and *argv[]?
argc is an integer that indicates how many arguments were entered and argv is a variable that contains the
arguments passed to the program 
2) What is a UNIX file descriptor and file descriptor table?
A UNIX file descriptor is an unsigned integer used by a process to identify an open file. A file descriptor table gives the mapping between the descriptor used to refer to the file and the data structure inside the kernel that represents the actual file connection.
3) What is a struct? What's the structure of sockaddr_in?
Structs are a way to group related variables under one name in a block of memory. The different variables can then be accessed by a single pointer or the struct defined name. Sockaddr_in contains a short, an unsigned short, a struct in_addr(which contains a unsigned long), and a char. 
4) What are the input parameters and return value of socket()
The socket function takes in a domain(int), which specifies the communications domain where the socket is created, a type(int), which specifies the type of socket to be created, and a protocol(int) which specifies a particular protocol to be used with the socket. The return value of socket is a non-negative integer, the socket file descriptor.
5) What are the input parameters of bind() and listen()?
The input parameters of bind are the socket descriptor, the address, which is the pointer to a sockaddr structure containing the name that is going to be bound to socket, and address_len, which is the size of the address in bytes. The input parameters of listen are s(int) and backlog(int). s is a descriptor identifying a bound, unconnected socket, and backlog is the maximum length that the queue of pending connections may grow to. 
6) Why use while(1)? Based on the code below, what problems might occur if there are multiple simultaneous connections to handle?
Te while loop makes sure that the server is always running and available. If there are multiple connections to handle and if there is an error in more than one it can be difficult to differentiate the socket that the error is coming from. 
7)Research how the command fork() works. How can it be applied here to better handle multiple connections?
The fork command creates a new process by duplicating the calling process. This allows the server to better handle multiple connections because it create more memory space for the processes to run. 

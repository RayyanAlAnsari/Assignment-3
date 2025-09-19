# Assignment-3
Assessment 3: Programming Principles and Concepts
# Requisition System – Design Principles Analysis

Overview: This project is a simple Python program for collecting info, approving, and displaying staff requisitions.  
Below is an analysis of how software design principles are used and where they could be used in the future to make the code better.

# USE OF SOFTWARE DESIGN PRINCIPLES

### KISS (Keep It Simple Stupid)
KISS is used several times throughout the code. all of the times it was used, the functions used clear logic and descriptive variable names. The coding was very simple and easy to understand, and it also makes the program easy to read, modify and debug (requisiton_approval only uses if/else to determine approval status)

### Clean Code over Clever Code
Clean code over clever code was used several times in the program functions. instead of complex and difficult lines, the code has well named methods and the loops were well coded. this helped in priorotizing readability and maintainibility over complex lines of codes

### YAGNI (You Aren’t Gonna Need It)
YAGNI cannot be applied because only essential and important codes are used in the program, no unnecessary functionality is added, which makes the program good for future   

### Single Responsibility (SR)
Single reponsibility can be applied at the start of the code because there was more than one task. It stores individual requisition data, manage user input and maintain statistic. So Single Responsibility can be applied to improve the code. all of these can be seperated into different classes based on each criteria, that will help in reducing coupling and also help in making testing easier 

### Open/Closed Principle (OCP)
Open/closed can be applied in one of the functions, the code can be improved in many ways. the problem in the code was that if later the user wants to different thresholds or more than one step for approvals then the function method must be modified. An extension will help in improving the code without changing existing code  

### DRY (Don’t Repeat Yourself)
DRY can be applied at the end of the program to reduce the repetition. A simple loop can fix the function and remove the duplication 

## Conclusion
The currents code shows different ways where software design are used and where they can be implemented to make the code more efficient, and easy to maintain, read, fix, and debug. Implementing this can help learn more and also make the program more better 

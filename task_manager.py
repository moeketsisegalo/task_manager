#Capstone Project II_task_manager.py
import linecache
import datetime
#creating a program that reads from two textfiles namely "user.txt" and "tasks.txt"
#The program will register new users,add tasks,and view all tasks and generate reports using clean code to display it in a easy to read format
#only the admin is able to register a user and display statistics

#define the function reg_user that will be used to register the user when the function is called.
def reg_user():
     #open the user.txt in a+ mode opens file for reading and writing
    file = open("user.txt","a+")
    #Request input of a new username and make case lower()
    new_user = input("Please enter a new username: ").lower()
    #prevent user from registering a user that already exists
    with open("user.txt") as file:
        for line in file:
        #create variables "key" and "value" then use rstrip("\n") to remove the new line and split()function to split at the comma
        #Therefore, once "\n" is removed, it will return the list of string which are separated by ",".
            (key, value) = line.rstrip("\n").split(",")
            #the first string varaible will be a key and the next will be a value and i used replace()function to remove the space within the password
            empty_dictionary[(key)] = value.replace(" ","")
            if new_user in empty_dictionary:
                #Present the relevant log in message using print()function
                print("User Already Registered!") 
                exit()
    #Request input of a new password                
    new_password = input("Please enter a new password: ")
     #Request input of password confirmation. 
    pass_confirmation = input("Please confirm the password: ")
    #Check if the new password and confirmed password are the same.
    if new_password == pass_confirmation:
        #print user succesfully registered             
        print("You have succesfully been registered")
    elif new_password != pass_confirmation :
        #present a relevant message if they do not match        
        print("The password does not match")  
        # break
        # If they are the same, add them to the user.txt file,add a new line and comma(",")
        file.write('\n' + new_user + ",")
        #also add passowrd to text file and make space after the comma using (" ")
        file.write(" " + new_password)
#define the function add task which will be used to add tasks
def add_task():
    file = open("tasks.txt","a+")
    #Prompt the user a username of the person whom the task is assigned to
    user_name = input("please enter the username of the person whom the task is assigned to: ")
    #prompt the user the title of a task
    task_title = input("please add the title of the task: ")
    #prompt the user the description of the task 
    task_description = input("please add the description of the task: ")
    #prompt the user the due date of the task
    due_date = input("please add the due date of the task: ")
    #Then get the current date
    date_assigned = input("Please enter assigned date date: ")
    # You must remember to include the 'No' to indicate if the task is complete.
    task_completed = input("Yes or No")
    #Add the data to the file task.txt using write()function and add the commas and line spacing accordingly
    file.write("\n" + user_name + ", " + task_title + ", " + task_description + ", " + date_assigned + ", " + due_date + ", " + task_completed )
    print("the task has been added ") #print task has been added
#define the function view all that will be useed to view all the tasks 
def view_all():
    #Read the file using a for loop
    file = open("tasks.txt","r")
    for tasks in file:
        #Split that line where there is comma and space.
        tasks_only = tasks.split(",")
        #print the results in the format shown in the Output 2 using indexing from a list
        print(f"Task:             {tasks_only[1]}")
        print(f"assigned to:       {tasks_only[0]}")
        print(f"date assigned:    {tasks_only[3]}")
        print(f"Due date:         {tasks_only[4]}")
        print(f"Task Complete?:   {tasks_only[5]}")
        print(f"task description: \n{tasks_only[2]}")
        print()#Print a new line     
#define the function view mine that will be used to view tasks of the person logged in
def view_mine():
    #show task number
    with open("tasks.txt","r") as file:
        #read the lines of the file
        lines = file.readlines()
        #using the enumerate()function to count the values of the lines and start counting at 1
        for count, values in enumerate(lines,start=1):
            #split the values at the comma. 
            split_values = values.split(",")
            #task number assigned to 1. 
            task_number = 1
            #start counting
            task_number += count
            # print the output in a easy to read manner.
            print(f"Task Number       {count}")
            print(f"Task:             {split_values[1]}")
            print(f"assigned to:       {split_values[0]}")
            print(f"date assigned:    {split_values[3]}")
            print(f"Due date:         {split_values[4]}")
            print(f"Task Complete?:   {split_values[5]}")
            print(f"task description: \n{split_values[2]}")
            print()#Print a new line
   
    #run a while loop to make it easy to break out the loop         
    while True:
    #code to show the task selected or -1 to return to the main menu.
        task_lines = int(input("enter task num you want to edit or -1 to return to the main menu:"))
        #if user inputs -1 break out the loop
        if task_lines == -1: 
            break
        #else if the user does not input -1 then follow instruction
        elif task_lines != -1:
            # read from the line the user selected in "task_lines"
            line_num = linecache.getline("tasks.txt", task_lines)
            print()#print a new line
            #remove the new line
            remove_new_line = line_num.strip("\n")
            #split everything in a comma 
            split_alles = remove_new_line.split(",")
            #print the output in a easy to read format
            print("*************************************")
            print(f"You have selected task: {task_lines}")
            print()
            print(f"Task:             {split_alles[1]}")
            print(f"Task assigned to : {split_alles[0]}")
            print(f"date assigned:    {split_alles[3]}")
            print(f"Due date:         {split_alles[4]}")
            print(f"Task Complete?:   {split_alles[5]}")
            print(f"task description: \n{split_alles[2]}")
            print("***************************************")
            #This block of code will be used to edit the tasks 
            #if the index[5] in the file is yes then break out loop and print the relevant message
            if split_alles[5] == " Yes":
                print("Task already completed, you cannot edit the task.")
                break
            #if the index[5] in the file is No then edit the task
            elif split_alles[5] == " No":
                #prompt the user to mark the task as complete and use capitalize()function to make first letter a capital letter
                task_completed = input("Would you like to mark the task as complete? enter Yes/No: ").capitalize()
                # open file in read mode
                file = open("tasks.txt", "r")
                #create variable replaced content with an empty string
                replaced_content = ""
                # line_number is assigned to task lines
                line_number = task_lines
                #loop counter
                i = 1
                # looping through the file
                for line in file:
                    # stripping line break
                    line = line.strip()
                    # replacing the text if the line number is reached
                    if i == line_number:
                        new_line = line.replace(split_alles[5]," " + task_completed)
                    else:
                        new_line = line
                    # concatenate the new string and add an end-line break
                    replaced_content = replaced_content + new_line + "\n"
                    # Increase loop counter
                    i = i + 1
                # close the file
                file.close()
                # Open file in write mode
                write_file = open("tasks.txt", "w")
                # overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                # close the file
                write_file.close() 
                print("Task Completed has been updated")
                
                #edit the user_name
                #prompt the user to enter a new user name or to keep to assigned user, enter the same user name and lower()function to make it low case letters
                new_user_name = input("enter the a new username to assigned task or current user_name to keep assigned to yourself").lower()
                # open file in read mode
                file = open("tasks.txt", "r")
                #create variable replaced content with an empty string
                replaced_name = ""
                line_number = task_lines
                #loop counter
                i = 1
                # looping through the file
                for line in file:
                    # stripping line break
                    line = line.strip()
                    # replacing the text if the line number is reached
                    if i == line_number:
                        new_line = line.replace(split_alles[0]," "+ new_user_name)
                    else:
                        new_line = line
                    # concatenate the new string and add an end-line break
                    replaced_name = replaced_name + new_line + "\n"
                    # Increase loop counter
                    i = i + 1
                # close the file
                file.close()
                # Open file in write mode
                write_file = open("tasks.txt", "w")
                # overwriting the old file contents with the new/replaced content
                write_file.write(replaced_name)
                # close the file
                write_file.close() 
                # new_date = input("enter a new due date for the assignment: ").lower()
                print("user name has been updated")  
                         
                #edit the due date 
                #prompt the user to input date 
                new_due_date = input("Please enter a new due date,with the format: date|month|Year: ")
                # open file in read mode
                file = open("tasks.txt", "r")
                replaced_date = ""
                line_number = task_lines
                #loop counter
                i = 1
                # looping through the file
                for line in file:
                    # stripping line break
                    line = line.strip()
                    # replacing the text if the line number is reached
                    if i == line_number:
                        new_line = line.replace(split_alles[4]," " + new_due_date)
                    else:
                        new_line = line
                    # concatenate the new string and add an end-line break
                    replaced_date = replaced_date + new_line + "\n"
                    # Increase loop counter
                    i = i + 1
                # close the file
                file.close()
                # Open file in write mode
                write_file = open("tasks.txt", "w")
                # overwriting the old file contents with the new/replaced content
                write_file.write(replaced_date)
                # close the file
                write_file.close() 
                # new_date = input("enter a new due date for the assignment: ").lower()
                print("Due date has been updated")
        #break out the loop
        break
#define the function generate reports
def generate_reports():
    #count number of tasks using the len()function by reading lines of the line
    with open("tasks.txt","r") as file:
        number_of_tasks = len(file.readlines())
    
    #count the number of tasks completed
    #open file using open ()function then read()function to read the contents of the file
    file = open("tasks.txt")
    read_file = file.read()
    #I used the count()function to count the number of tasks completed if Task is marked yes for completed
    number_of_completed_task = read_file.count("Yes")
    #close the file
    file.close()
    
    #count the number of incomplete tasks
    #open file using open ()function then read()function to read the contents of the file
    file = open("tasks.txt")
    read_file = file.read()
    #I used the count()function to count the number of tasks completed if Task is marked yes for completed
    incomplete_task = read_file.count("No") 
    print("***Report Generated***")
    # file.close()
    print()
    #assign the variables to zero
    task_overdue = 0
    task_incomplete = 0 
        #count the number of tasks that are incomplete and overdue
        #getting the due date of the task and number of tasks incompleted    
        #Function to convert string to datetime
    def convert(date_time):
        #date format
        format = ' %d %b %Y'
        #convert the string to a datetime 
        datetime_str = datetime.datetime.strptime(date_time, format)
        return datetime_str
    #open the file in read mode
    with open("tasks.txt","r") as file:
        #read the lines of the file using a for loop
        for lines in file:
            # strip the new lines and split at the comma using split()function
            strip_it = lines.strip("\n")
            split_it = strip_it.split(",")
            #Getting the due date
            date_time = split_it[4]
            due_date = convert(date_time)
            #Getting assigned date
            date_time2 = split_it[3]
            date_assigned = convert(date_time2)
            # get the current date and time
            # now = datetime.datetime.now()
            #if index[5] == "No" of files incomplete and tasks that are over and if found count in the task_over varibale 
            if split_it[5] == " No" and date_assigned < due_date :
                task_overdue += 1

    #The percentage of incomplete tasks 
    #count the number of tasks completed
    #open the file 
    file = open("tasks.txt")
    #read the file
    read_file = file.read()
    #count how many tasks are incomplete using count()function
    num_completed = read_file.count("No") 
    #close the file
    file.close()
    #open the file in read mode
    with open("tasks.txt","r") as file:
        #get the length of the lines to the number of tasks
        num_task = len(file.readlines())
         #number of completed tasks / number of task * 100
        percentage_incomplete = (num_completed / num_task) * 100
    #the percentage of tasks over due
    #number of tasks over due / number of tasks * 100
    percentage_overdue = task_overdue / num_task * 100
    
    #open the file in write mode to create a file named task_overview.txt
    with open("task_overview.txt","w") as file:
        #use the write function to write the report in a easy to read format
        file.write(f"*****************************Task OverView Reports**************************************\n")
        file.write(f"The total number of tasks generated:               {number_of_tasks}\n")
        file.write(f"The total number of tasks completed:               {number_of_completed_task}\n")
        file.write(f"The total number of incomplete tasks:              {incomplete_task}\n")
        file.write(f"The total number of incomplete tasks and overdue : {task_overdue}\n")
        file.write(f"The percentage of tasks that are incomplete:       {round(percentage_incomplete)}%\n")
        file.write(f"The percentage of tasks overdue :                  {round(percentage_overdue)}%\n")
        file.write(f"*****************************************************************************")
        
    #The total number of users
    #open the file    
    file = open ("user.txt")
    #read the number of lines to get the number of users
    read__user_file = file.readlines()
    #number of users is the length of the lines
    num_of_users =  len(read__user_file)
    #close the file
    file.close()
    
    #The total number of tasks assigned to the user
    #find tasks assigned to entered username
    file = open("tasks.txt")
    read_file = file.read()
    user_task_num = read_file.count(entered_username)
    file.close()
  
    #The percenatage of the total number of tasks that have been assigned to that user
    #if the number of tasks is not zero the follow instruction
    if number_of_tasks != 0:
        #number of tasks assigned to user / number of tasks * 100
        user_percentage_task = user_task_num / number_of_tasks * 100 
    else:
        #I used the else statement as a defensive program so the user does not divide by zero but concludes that the final output user percentage is zero
        user_percentage_task = 0
        print("The user has no tasks assigned")   
        
    #the percenatage of the tasks assigned to that user that have been completed
    #a integer variable assigned zero
    counter = 0
    #a float variable assigned to zero
    percentage_assigned_completed = 0
    #open the file
    with open("tasks.txt") as file:
        #read the lines of the file
        for line in file:
            #strip the new line and split at the comma so it becomes a list for index arraying
            strip_line = line.strip("\n")
            split_line = strip_line.split(",")
            #if the user name logged in is inside the empty dictionary and the index[5] string is " Yes" then increase the counter
            if entered_username in empty_dictionary and empty_dictionary[entered_username] == entered_password and split_line[5] == " Yes" and entered_username == split_line[0]:
                counter += 1
                #if the total number of task is not zero
                if user_task_num != 0:
                    #number of completed tasks / number of tasks assigned to user * 100
                    percentage_assigned_completed = (counter / user_task_num) * 100
                    # break
                else:
                    #I used the else statement as a defensive program so the user does not divide by zero but concludes that the final output for the percenatge of the tasks assigned to user
                    percentage_assigned_completed = 0

    # # the percenatage of the tasks assigned to that user that must still be completed
    #integer variable assigned to zero
    counter2 = 0
    #float varaible assigned to zero
    percentage_assigned_incompleted = 0
    #open the file
    with open("tasks.txt") as file:
        #read the lines in the file.
        for lines in file:
            #strip the new line and split at the comma
            strip_line1 = lines.strip("\n")
            split_line2= strip_line1.split(",")
            #if the user name logged in is inside the empty dictionary and the index[5] string is " No" then increase the counter
            if entered_username in empty_dictionary and empty_dictionary[entered_username] == entered_password and split_line2[5] == " No" and entered_username == split_line2[0]:
                counter2 += 1
                #if the total number of tasks assigned to the user is not equal to zero
                if user_task_num != 0:
                    # number of incomplete task / number of tasks assigned to user * 100
                    percentage_assigned_incompleted = (counter2 / user_task_num) * 100
                else:
                    #I used the else statement as a defensive program so the user does not divide by zero but concludes that the final output for the percenatge of the tasks assigned to user
                    percentage_assigned_incompleted = 0
                    
    # The percenatage of tasks that are not completed by the user and are overdue
    #an integer variable assigned to zero
    percent_overdue_counter = 0
    #a float variable assigned to zero
    percent_user_overdue = 0  
    #open the file
    with open("tasks.txt") as file:
        #read ythe lines of the file
        for line in file:
            #strip the new line and split at the comma
            my_strip_line = line.strip("\n")
            my_split_line = my_strip_line.split(",")
            #if the user name logged in and index[5] in the lines is No and the datetime is less than the current time the increase counter
            if entered_username in empty_dictionary and empty_dictionary[entered_username] == entered_password and my_split_line[5] == " No" and date_assigned > due_date and entered_username == my_split_line[0] :
                percent_overdue_counter += 1
                #if the num of task is not equal to zero
                if user_task_num != 0 :
                    # NUmber of tasks overdue / number of tasks not completed * 100
                    percent_user_overdue = (percent_overdue_counter / user_task_num) * 100
                else:
                    #defensive programming method to assign zero to percent of tasks not completed and overdue
                    percent_user_overdue = 0  
    #open the file in write mode
    with open("user_overview.txt","w") as file:
        #use the write function to write the report in a easy to read format
        file.write(f"****************************************User Overview Reports*************************************************************\n")
        file.write(f"This report is for the user:                                                {entered_username}\n")
        file.write(f"total number of users:                                                      {num_of_users}\n")
        file.write(f"Total amount of task generated :                                            {number_of_tasks}\n")
        file.write(f"Total number of tasks assigned to the user:                                 {user_task_num}\n")
        file.write(f"Percentage of total number of tasks that have been assigned to the user:    {round(user_percentage_task)}%\n")
        file.write(f"Percenatage of the tasks assigned to that user that have been completed:    {round(percentage_assigned_completed)}%\n")
        file.write(f"Percenatage of the tasks assigned to that user that must still be completed:{round(percentage_assigned_incompleted)}%\n")
        file.write(f"Total percentage of user tasks not completed and are overdue::              {round(percent_user_overdue)}%\n")
        file.write("****************************************************************************************************************************")
    
#Creating an empty dictionary to store the data in "user.txt"
empty_dictionary = {}
with open("user.txt","r") as f:
    #use for loop to read the user.txt file
    for line in f:
        #create variables "key" and "value" then use rstrip("\n") to remove the new line and split()function to split at the comma
        #Therefore, once "\n" is removed, it will return the list of string which are separated by ",".
        (key, value) = line.rstrip("\n").split(",")
        #the first string varaible will be a key and the next will be a value and i used replace()function to remove the space within the password
        empty_dictionary[(key)] = value.replace(" ","")
#prompt the user to enter a username
print("Enter username:")
entered_username = input()
#prompt the user to enter a password
print("Enter password:")
entered_password = input()
#run a while loop to verify the log in details
while True:
    #if the username is in the dictionary and the same username is equal to the user password log in to the program
    if entered_username in empty_dictionary and empty_dictionary[entered_username] == entered_password:
        print("Successful login!") #Present the relevant log in message using print()function
        break
    else: #else statement and within the else state print the relevant message if log in details is incorrect
        print("Wrong username or password!, run the program and try again!")
        #exit()function exits the program when the user has entered the wrong log in details.
        exit()
#print an empty line
print()
#run another while loop which im going to use to present the menu 
while True:
    #presenting the menu to the user
    #an if statement for compulsory task 2 which is used to display the statistics to the admin only.
    #if the user is admin present the menu to display statistics
    if entered_username == "admin":
        print("Only admin can select this option: enter 'ds' to display stats")
        print() #Print an empty line
        print("select one of the following options below")  
        print("enter 'r' to register as a user")             # r - Registering a user
        print("enter 'a' to add a task")                     # a - Adding a task
        print("enter 'va' to view all the tasks")            # va - View all tasks
        print("enter 'vm' to view user tasks")               #view user tasks that is logged in
        print("enter 'gr' to generate reports")              #generate reports
        print("enter 'ds' to display statistics")            #display statistics
        print(" enter 'e' to exit")                          #e - Exit 
        
    elif entered_username != "admin":
        print("Only admin can select this option: enter 'ds' to display stats")
        print() #Print an empty line
        print("select one of the following options below")  
        print("enter 'r' to register as a user")             # r - Registering a user
        print("enter 'a' to add a task")                     # a - Adding a task
        print("enter 'va' to view all the tasks")            # va - View all tasks
        print("enter 'vm' to view user tasks")               #view user tasks that is logged in
        print("enter 'gr' to generate reports")              #generate reports
        print("enter 'ds' to display statistics")            #display statistics
        print(" enter 'e' to exit")                          #e - Exit 
                                 
    #prompt the user to input the desired option from the menu and make input not case sensitive using lowercase()function
    menu = input("Select one of the following Options :").lower()
    print() #print an empty line
    #In this block of code,"r" will to add a new user to the user.txt file 
    if menu == 'r':
        pass
         #an if statement that makes the admin be the only user to register users according to compulsory task 2
    #if the "entered_username" is not admin break out the loop..
        if entered_username != "admin":
            print("Only the admin can register a user") #Present relevant message using print()function
            exit()
        reg_user()
   #In this block of code,it will allow a user to add a new task to tasks.txt file
    elif menu == 'a':
        pass
        #open tasks.txt in a+("for reading and writing")
        add_task()
        print()#print an empty line   
# In this block of code, the program will read the task from task.txt file and view all the tasks
    elif menu == 'va':
        pass
        #open the tasks file in read mode
        view_all()
#In this block of code, the program will read the task from task.txt file and view tasks of the user that is logged in
    elif menu == 'vm':
        pass
        view_mine()
#in this 
    elif menu == 'gr':
        pass
        generate_reports()
    #in this block of code,the admin user will be able to display the statistics of the number of user and number of tasks
    elif menu == "ds":
        #open the user text file in read mode using open()function as file
        with open("task_overview.txt","r") as file:
            for lines in file:
                print(lines)
                print()
                print()
        with open("user_overview.txt","r") as file2:
            for lines in file2:
                print(lines)
        
#this block of code will exit the loop
    elif menu == 'e':
        print('Goodbye!!!')
        exit() #exit the program using exit()function
#if user inputs incorrect choice from the menu present the relevant message in the else statement
    else:
        print("You have made a wrong choice, Please Try again")


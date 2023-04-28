#first we need to input the textbox that we will use in this program which is (mylife.txt)
with open("mylife.txt", "w") as file:
#The user is prompted for input using a while loop in this method, and each line is written to the file "mylife.txt" with a newline character at the end.
#If the user does not wish to enter any further lines, an if statement is used to determine whether the loop should end and the file should be closed.
    while True:
            line = input("Enter line: ")
# write the line to the file, with a newline character at the end
            file.write(line + "\n") 

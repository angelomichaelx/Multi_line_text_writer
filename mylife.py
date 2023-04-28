# Michael Angelo P. Biag
#BSCPE 1-4
#Write a method in python to write multiple line of text contents into a text file mylife.txt. See sample output:
#Enter line: Beautiful is better than ugly. Are there more lines y/n? y
#Enter line: Explicit is better than implicit. Are there more lines y/n? y
#Enter line: Simple is better than complex. Are there more lines y/n? n

#first we need to input the textbox that we will use in this program which is (mylife.txt)
with open("mylife.txt", "w") as file:
#The user is prompted for input using a while loop in this method, and each line is written to the file "mylife.txt" with a newline character at the end.
#If the user does not wish to enter any further lines, an if statement is used to determine whether the loop should end and the file should be closed.
    while True:
            line = input("\033[0;34mEnter line: ")
# write the line to the file, with a newline character at the end
            file.write(line + "\n") 
#it will ask you if you want to add more lines by answering y = yes and n = no
            more_lines = input("\033[1;32mAre there more lines y/n? ")
# if there are no lines and answered by 'n' n means NO so the program will stop
            if more_lines.lower() == 'n':
                  break

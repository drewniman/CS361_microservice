# Drew's Microservice Communication Contract

### How to REQUEST data:
Write the word "run" to the text file number.txt

Example:

with open("number.txt", "w") as f:

&emsp; f.write("run")

### How to RECEIVE data:
Read the contents of number.txt (should be a string containing a single integer)

Example:

with open("number.txt", "r+") as f:

&emsp; random_int = f.readline()      (stores the random integer in a variable to be used by main program)

&emsp; f.truncate(0)                            (leave the text file blank until next microservice call)

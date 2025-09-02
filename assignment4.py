#Task 1

try:
    with open("sample.txt",'r') as file:
        print("Reading file content:")
        n=1
        for lines in file:
            print("line",n,':',lines)
            n=n+1
except FileNotFoundError:
    print("Error: This file'sample.txt' was not found.")


#TASK 2

    
with open("output.txt",'w') as writ:
        writ.write(input("Enter text to write to the file:")+"\n")
        print("Data successfully written to output.txt."+"\n")
try:
    with open("output.txt","a") as app:
        app.write(input("Enter additional text to append:")+"\n")
        print("Data Successfully appended"+"\n")
except Exception as e1:
    print("error:",type(e1).__name__)
finally:
    with open("output.txt",'r') as rd:
        rd1=rd.read()
        print("Final content of output.txt:\n"+rd1)
    

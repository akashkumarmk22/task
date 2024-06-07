def capitalize_lines():
    print("Enter the text : ")
    lines = []
    
    while True:
        line = input()
        if line == "":
            break
        lines.append(line.upper())
    
    for line in lines:
        print(line)
 
# Run the function
capitalize_lines()

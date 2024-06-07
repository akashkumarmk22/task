def capitalize_lines():
    print("Enter the text : ")
    lines = []
    
    while True:
        # checking the condition 

        line = input()
        if line == "":
            break
        lines.append(line.upper())
    
    for line in lines: #//"Hello "
        print(line)
 
# Run the function
capitalize_lines()
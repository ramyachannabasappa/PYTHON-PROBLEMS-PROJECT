def add(inp_type, *args):
    if inp_type == "int":
        total = 0
        for x in args:
            total += int(x)
        print(total)

    elif inp_type == "str":
        result = ""
        for x in args:
            result += x
        print(result)


# -------- Main Program with Prompts --------
inp_type = input("Enter the data type (int/str): ")
inp1 = input("Enter inp1: ")
inp2 = input("Enter inp2: ")
inp3 = input("Enter inp3: ")

add(inp_type, inp1)
add(inp_type, inp1, inp2)
add(inp_type, inp1, inp2, inp3)

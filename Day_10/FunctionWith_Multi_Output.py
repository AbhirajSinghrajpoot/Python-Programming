def formated_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    full_name = f"{f_name} {l_name}"
    return full_name.title()
print(formated_name(input("What is your first name? "), input("What is your last name? ")))
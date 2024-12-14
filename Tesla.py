# from Rock_Paper_Scissors import RPS #
import os
import time
from colorama import Fore #type: ignore
import ollama #type: ignore
import subprocess

#####################################################
##                Clear The Screen                 ##
#####################################################

os.system('cls' if os.name == 'nt' else 'clear')

#####################################################
##                   Variables                     ##
#####################################################

a = None
b = None
c = None
d = None
e = None
exit_password_check = False
orig_pass = 'tesla'
venv = None
DEFAULT_MODEL = 'llama3.2:1b'
DEFAULT_SIZE = '1 Billion Parameters (Est. 1.3GB)'
DEFAULT_SPEED = '11.07 tokens per second'

#####################################################
##                    keywords                     ##
#####################################################

def add(Num1: float, Num2: float):
    print()
    sum = Num1 + Num2
    print(f"{Num1} + {Num2} = {sum}")

def sub(Num1: float, Num2: float):
    print()
    sum = Num1 - Num2
    print(f"{Num1} - {Num2} = {sum}")

def mul(Num1: float, Num2: float):
    print()
    sum = Num1 * Num2
    print(f"{Num1} x {Num2} = {sum}")

def div(Num1: float, Num2: float):
    print()
    sum = Num1 / Num2
    print(f"{Num1} / {Num2} = {sum}")

def merge(a: str, b: str):
    print()
    print(f"{a + b}")

def for_loop(self, Number_of_iterations_end):
    print()
    for i in range(0, Number_of_iterations_end):
        print(self)

def read_var(self):
    self = self.lower()

    if self == "a":
        print(f"A is set to {a}")

    elif self == "b":
        print(f"B is set to {b}")

    elif self == "c":
        print(f"C is set to {c}")

    elif self == "d":
        print(f"D is set to {d}")

    elif self == "e":
        print(f"E is set to {e}")

    else:
        print(Fore.LIGHTRED_EX + "ERROR:" + Fore.MAGENTA+ f" The Register {self} does not exist or do not have the required permissions to read or write. Please contact the Admin and to add new a register compatibility or give the required permissions.")

def say():
    say = input("What do you want to say?:")
    print("compiling ...\n")
    time.sleep(0.2)
    print(say,"\n")

def if_ngn(num1, num2, is_True, is_False):
    if num1 > num2:
        print(is_True)
    else:
        print(is_False)

def if_nln(num1, num2, is_True, is_False):
    if num1 < num2:
        print(is_True)
    else:
        print(is_False)

def if_nen(num1, num2, is_True, is_False):
    if num1 == num2:
        print(is_True)
    else:
        print(is_False)

def if_n_ne_n(num1, num2, is_True, is_False):
    if num1!= num2:
        print(is_True)
    else:
        print(is_False)

def if_n_le_n(num1, num2, is_True, is_False):
    if num1 <= num2:
        print(is_True)
    else:
        print(is_False)

def if_n_ge_n(num1, num2, is_True, is_False):
        if num1 >= num2:
            print(is_True)
        else:
            print(is_False)

def if_vgv(var1, var2, is_True, is_False):
    if var1 > var2:
        print(is_True)
    elif var1 < var2:
        print(is_False)
    else:
        exit(1)

def if_vlv(var1, var2, is_True, is_False):
    if var1 < var2:
        print(is_True)
    elif var1 > var2:
        print(is_False)
    else:
        exit(1)

def if_v_eq_v(var1, var2, is_True, is_False):
    if var1 == var2:
        print(is_True)
    elif var1 != var2:
        print(is_False)
    else:
        exit(1)

def if_v_ne_v(var1, var2, is_True, is_False):
    if var1 != var2:
        print(is_True)
    elif var1 == var2:
        print(is_False)
    else:
        exit(1)

def if_v_le_v(var1, var2, is_True, is_False):
    if var1 <= var2:
        print(is_True)
    elif var1 >= var2:
        print(is_False)
    else:
        exit(1)

def if_v_ge_v(var1, var2, is_True, is_False):
    if var1 >= var2:
        print(is_True)
    elif var1 <= var2:
        print(is_False)
    else:
        exit(1)


def passwd():
    global orig_pass
    orig_pass = input("Enter Your Passwd for" + Fore.RED + " root: " + Fore.CYAN)
    print(f"This will be your passwd: {orig_pass}")
    print("You will have to use this passwd to exit out of Tesla")
    print()

def say_var(variable_to_say):
    if variable_to_say.lower() == 'a':
        print(variable_to_say)
    else:
        print('That\'s not registered variable, please try again.')

def start_ollama_silently():
    # Redirect stdout and stderr to os.devnull to suppress output
    with open(os.devnull, 'w') as devnull:
        subprocess.Popen(["ollama", "start"], stdout=devnull, stderr=devnull)
        return subprocess
    # print("Ollama has been started silently (no output).")

#####################################################
##                      Loop                       ##
#####################################################

run = True

print("Welcome to Tesla")
print("Type " + Fore.MAGENTA + "\'help()\' "+ Fore.WHITE + "for more information\n")

while run == True:
    cmd = input(Fore.GREEN+ 'Tesla' + Fore.WHITE + '@' + Fore.LIGHTBLUE_EX+'Terminal: \\$-> ' + Fore.LIGHTCYAN_EX)

    if not cmd.strip():
        continue

######################################################
##              keyword inspection                  ##
######################################################

    if cmd == "help()":
        print("Type add for addition, sub for subtraction, mul for multiplication, div for division and exit[tesla: 0] to exit Tesla.  For more keywords, type \'keywords{tokens: /~}\' ")

    elif cmd == "keywords{tokens: /~}":
        print("\nhelp(),"
              "\nexit,"
              "\nkeywords{tokens: /~},"
              "\nkey" + Fore.LIGHTRED_EX + " [ For Devoloping Only ]" + Fore.LIGHTCYAN_EX + ","
              "\nadd,"
              "\nsub,"
              "\nmul,"
              "\ndiv,"
              "\nfor loop(),"
              "\nvar,"
              "\nread var(),"
              "\nsay(),"
              "\nsay(var)"
              "\nif(),"
              "\nif(clear),"
              "\nif(help),"
              "\nif(keys) "+ Fore.LIGHTRED_EX + "[ under development ]" + Fore.LIGHTCYAN_EX + ","
              "\nif(conditions),"
              "\npasswd,"
              "\nmerge(),"
              "\nclear,"
              "\nvenv(python),"
              "\npy"+ Fore.LIGHTBLUE_EX + " [ Access the Python shell ]" + Fore.LIGHTCYAN_EX + ","
              "\npython"+ Fore.LIGHTBLUE_EX + " [ Access the Python shell ]" + Fore.LIGHTCYAN_EX + ","
              "\nfile(tesla)"+ Fore.GREEN +" [ Access the files of Tesla ]" + Fore.LIGHTCYAN_EX + ","
              "\n")


    elif cmd == "key":
        print("\nhelp(),"
              "\nexit,"
              "\nkeywords{tokens: /~},"
              "\nkeys" + Fore.LIGHTRED_EX + " [ For Devolopment ]" + Fore.LIGHTCYAN_EX + ","
              "\nadd,"
              "\nsub,"
              "\nmul,"
              "\ndiv,"
              "\nfor loop(),"
              "\nvar,"
              "\nread var(),"
              "\nsay(),"
              "\nsay(var)"
              "\nif(),"
              "\nif(clear),"
              "\nif(help),"
              "\nif(keys) "+ Fore.LIGHTRED_EX + "[ under development ]" + Fore.LIGHTCYAN_EX + ","
              "\nif(conditions),"
              "\npasswd,"
              "\nmerge(),"
              "\nclear,"
              "\nvenv(python),"
              "\npy"+ Fore.LIGHTBLUE_EX + " [ Access the Python shell ]" + Fore.LIGHTCYAN_EX + ","
              "\npython"+ Fore.LIGHTBLUE_EX + " [ Access the Python shell ]" + Fore.LIGHTCYAN_EX + ","
              "\nfile(tesla)"+ Fore.GREEN +" [ Access the files of Tesla ]" + Fore.LIGHTCYAN_EX + ","
              "\n")

    elif cmd == "exit":

        if exit_password_check == True:
            exit_pass = input("Enter passwd: ")

            if exit_pass == orig_pass:
                print(Fore.RED + "Please Ignore the error message :)")
                exit()
            else:
                print("Incorrect Passwd")
                print("To make a new passwd, Enter \'passwd\'")

        else:
            if venv != None:
                print('\nPlease type the letter \'y\' when prompted and press the \'Enter\' key to exit.')
                os.system(f'conda remove --name {venv} --all')
                print('\nExiting...' + Fore.WHITE)

            print(Fore.WHITE)
            exit()


    elif cmd == "add":
        number_1 = float(input("Enter 1st number: "))
        number_2 = float(input("Enter 2st number: "))
        add(number_1, number_2)

    elif cmd == "sub":
        number_1 = float(input("Enter 1st number: "))
        number_2 = float(input("Enter 2st number: "))
        sub(number_1, number_2)

    elif cmd == "mul":
        number_1 = float(input("Enter 1st number: "))
        number_2 = float(input("Enter 2st number: "))
        mul(number_1, number_2)

    elif cmd == "div":
        number_1 = float(input("Enter 1st number: "))
        number_2 = float(input("Enter 2st number: "))
        div(number_1, number_2)

    elif cmd == "merge()":
        a = input("Enter 1st string: ")
        b = input("Enter 2nd string: ")
        merge(a, b)

    elif cmd == "for loop()":
        arg1 = input("Enter 1st Argument(anything): ")
        arg2 = int(input("Enter 2nd Argument(integer[How many iterations?]): "))
        for_loop(arg1, arg2)

    elif cmd == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')

    elif cmd == "cls":
        os.system('cls' if os.name == 'nt' else 'clear')

    elif cmd == "read var()":
        vars = input("Which variable do you wish to read(A, B, C, D, E)?:")
        read_var(vars)

    elif cmd == "var":
        print("Please don\'t put wrong values. Tesla will crash.")
        var = input("Which variable name do you wish to be yours(A, B, C, D, E)?:")
        type = input("Which Type of variable(int, str, float, bool)?: ")
        type = type.lower()
        var = var.lower()
        if type == "int":
            if var == "a":
                value = int(input("Enter a integer value: "))
                a = value
                print(f"A is set to {value}")

            elif var == "b":
                value = int(input("Enter a integer value: "))
                b = value
                print(f"B is set to {value}")

            elif var == "c":
                value = int(input("Enter a integer value: "))
                c = value
                print(f"C is set to {value}")

            elif var == "d":
                value = int(input("Enter a integer value: "))
                d = value
                print(f"D is set to {value}")

            elif var == "e":
                value = int(input("Enter a integer value: "))
                e = value
                print(f"E is set to {value}")
            else:
                print(f"\nVariable name {var} does not exist.\nPlease try again.")
        elif type == "str":
            if var == "a":
                value = input("Enter a string value: ")
                a = value
                print(f"A is set to \'{value}\'")

            if var == "b":
                value = input("Enter a string value: ")
                b = value
                print(f"B is set to \'{value}\'")

            if var == "c":
                value = input("Enter a string value: ")
                c = value
                print(f"C is set to \'{value}\'")

            if var == "d":
                value = input("Enter a string value: ")
                d = value
                print(f"D is set to \'{value}\'")

            if var == "e":
                value = input("Enter a string value: ")
                e = value
                print(f"E is set to \'{value}\'")
        elif type == "float":
            if var == "a":
                value = float(input("Enter a floating point value: "))
                a = value
                print(f"A is set to \'{value}\'")

            if var == "b":
                value = float(input("Enter a floating point value: "))
                b = value
                print(f"B is set to \'{value}\'")

            if var == "c":
                value = float(input("Enter a floating point value: "))
                c = value
                print(f"C is set to \'{value}\'")

            if var == "d":
                value = float(input("Enter a floating point value: "))
                d = value
                print(f"D is set to \'{value}\'")

            if var == "e":
                value = float(input("Enter a floating point value: "))
                e = value
                print(f"E is set to \'{value}\'")
        elif type == "bool":
            if var == "a":
                value = input("Enter a boolean value: ")
                a = value
                a = a.lower()
                if a == "true" or "1":
                    print("A is set to \'True\'")
                elif a == 'false' or '0':
                    print("A is set to \'False\'")

            if var == "b":
                value = (input("Enter a boolean value: "))
                b = value
                b = b.lower()
                if b == "true" or "1":
                    print("A is set to \'True\'")
                elif b == 'false' or '0':
                    print("A is set to \'False\'")


            if var == "c":
                value = input("Enter a boolean value: ")
                c = value
                c = c.lower()
                if c == "true" or "1":
                    print("A is set to \'True\'")
                elif c == 'false' or '0':
                    print("A is set to \'False\'")

            if var == "d":
                value = input("Enter a boolean value: ")
                d = value
                d = d.lower()
                if d == "true" or "1":
                    print("A is set to \'True\'")
                elif d == 'false' or '0':
                    print("A is set to \'False\'")

            if var == "e":
                value = input("Enter a boolean value: ")
                e = value
                e = e.lower()
                if e == "true" or "1":
                    print("A is set to \'True\'")
                elif e == "false" or '0':
                    print("A is set to \'False\'")
        else:
            print(f'\nThe variabe Type \'{type}\' does not exist.\nPlease try again and type the variable type correctly.\n')

    elif cmd == "read var()":
        vars = input("Which variable do you wish to read(A, B, C, D, E)?: ")
        read_var(vars)

    #elif cmd == "RPS":
        #RPS.rps()
        #Finish Later
        #un comment import for RPS

    elif cmd == "say()":
        say()

    elif cmd == "say(var)":
        variable_to_say = input("Which is the variable you want to say: ")

        say_var(variable_to_say)

    elif cmd == "if()":

        condition = input("Condition: ")

        if(condition == "n > n"):
            n1 = int(input("Enter the 1st number: "))
            n2 = int(input("Enter The 2nd number: "))

            is_true = input("What should Tesla do if the condition is true: ")
            is_false = input("What should Tesla do if the condition is false: ")

            if is_true == "say()":
                Say = input("What do you want to say if the condition is true?: ")
            if is_false == "say()":
                SaY = input("What do you want to say if the condition is false?: ")

            if_ngn(n1, n2, Say, SaY)

        elif(condition == "n < n"):
            n1 = int(input("Enter the 1st number: "))
            n2 = int(input("Enter The 2nd number: "))

            is_true = input("What should Tesla do if the condition is true: ")
            is_false = input("What should Tesla do if the condition is false: ")

            if is_true == "say()":
                Say = input("What do you want to say if the condition is true?: ")
            if is_false == "say()":
                SaY = input("What do you want to say if the condition is false?: ")

            if_nln(n1, n2, Say, SaY)

        elif(condition == "n = n"):
            n1 = int(input("Enter the 1st number: "))
            n2 = int(input("Enter The 2nd number: "))

            is_true = input("What should Tesla do if the condition is true: ")
            is_false = input("What should Tesla do if the condition is false: ")

            if is_true == "say()":
                Say = input("What do you want to say if the condition is true?: ")
            if is_false == "say()":
                SaY = input("What do you want to say if the condition is false?: ")

            if_nen(n1, n2, Say, SaY)

        elif(condition == "n ?= n"):
            n1 = int(input("Enter the 1st number: "))
            n2 = int(input("Enter The 2nd number: "))

            is_true = input("What should Tesla do if the condition is true: ")
            is_false = input("What should Tesla do if the condition is false: ")

            if is_true == "say()":
                Say = input("What do you want to say if the condition is true?: ")
            if is_false == "say()":
                SaY = input("What do you want to say if the condition is false?: ")

            if_n_ne_n(n1, n2, Say, SaY)

        elif(condition == "n < = n"):
            n1 = int(input("Enter the 1st number: "))
            n2 = int(input("Enter The 2nd number: "))

            is_true = input("What should Tesla do if the condition is true: ")
            is_false = input("What should Tesla do if the condition is false: ")

            if is_true == "say()":
                Say = input("What do you want to say if the condition is true?: ")
            if is_false == "say()":
                SaY = input("What do you want to say if the condition is false?: ")

            if_n_le_n(n1, n2, Say, SaY)

        elif(condition == "n > = n"):
            n1 = int(input("Enter the 1st number: "))
            n2 = int(input("Enter The 2nd number: "))

            is_true = input("What should Tesla do if the condition is true: ")
            is_false = input("What should Tesla do if the condition is false: ")

            if is_true == "say()":
                Say = input("What do you want to say if the condition is true?: ")
            if is_false == "say()":
                SaY = input("What do you want to say if the condition is false?: ")

            if_n_ge_n(n1, n2, Say, SaY)

        if(condition == "var > var"):
            v1 = input("Enter the 1st variable: ")
            v2 = input("Enter The 2nd variable: ")

            is_true = input("What should Tesla do if the condition is true: ")
            is_false = input("What should Tesla do if the condition is false: ")

            if is_true == "say()":
                Say = input("What do you want to say if the condition is true?: ")
            if is_false == "say()":
                SaY = input("What do you want to say if the condition is false?: ")

            if_vgv(v1, v2, Say, SaY)

        elif(condition == "var < var"):
            v1 = input("Enter the 1st variable: ")
            v2 = input("Enter The 2nd variable: ")

            is_true = input("What should Tesla do if the condition is true: ")
            is_false = input("What should Tesla do if the condition is false: ")

            if is_true == "say()":
                Say = input("What do you want to say if the condition is true?: ")
            if is_false == "say()":
                SaY = input("What do you want to say if the condition is false?: ")

            if_vlv(v1, v2, Say, SaY)

        elif(condition == "var = var"):
            v1 = input("Enter the 1st variable: ")
            v2 = input("Enter The 2nd variable: ")

            is_true = input("What should Tesla do if the condition is true: ")
            is_false = input("What should Tesla do if the condition is false: ")

            if is_true == "say()":
                Say = input("What do you want to say if the condition is true?: ")
            if is_false == "say()":
                SaY = input("What do you want to say if the condition is false?: ")

            if_v_eq_v(v1, v2, Say, SaY)

        elif(condition == "var not var"):
            v1 = input("Enter the 1st variable: ")
            v2 = input("Enter The 2nd variable: ")

            is_true = input("What should Tesla do if the condition is true: ")
            is_false = input("What should Tesla do if the condition is false: ")

            if is_true == "say()":
                Say = input("What do you want to say if the condition is true?: ")
            if is_false == "say()":
                SaY = input("What do you want to say if the condition is false?: ")

            if_v_ne_v(v1, v2, Say, SaY)

        elif(condition == "var le var"):
            v1 = input("Enter the 1st variable: ")
            v2 = input("Enter The 2nd variable: ")

            is_true = input("What should Tesla do if the condition is true: ")
            is_false = input("What should Tesla do if the condition is false: ")

            if is_true == "say()":
                Say = input("What do you want to say if the condition is true?: ")
            if is_false == "say()":
                SaY = input("What do you want to say if the condition is false?: ")

            # Generate var <= var
            if_v_le_v(v1, v2, Say, SaY)

        elif(condition == "var ge var"):
            v1 = input("Enter the 1st variable: ")
            v2 = input("Enter The 2nd variable: ")

            is_true = input("What should Tesla do if the condition is true: ")
            is_false = input("What should Tesla do if the condition is false: ")

            if is_true == "say()":
                Say = input("What do you want to say if the condition is true?: ")
            if is_false == "say()":
                SaY = input("What do you want to say if the condition is false?: ")

            if_v_ge_v(v1, v2, Say, SaY)

    elif cmd == "if(help)":
        print("Type \'if()\' to start a if statement, \'if(help)\' to print this message, \'if(clear)\' to clear the if statement cache" + Fore.LIGHTRED_EX + "[Developer Need]" + Fore.LIGHTCYAN_EX)
        print()
        print("If you wish to exit the program, type \'exit[tesla: 0]\' after making a passwd by typing \'passwd\'")
        print()

    elif cmd == "if(clear)":
        is_true = None
        is_false = None
        print()

    elif cmd.strip() == "python":
        os.system('python')

    elif cmd.strip() == "py":
        os.system('python')

    elif cmd.strip() == "venv(python)":
        venv = input('Name of the environment(No whitespaces): ')
        conda = f'conda create --name {venv}'
        os.system(conda)

    elif cmd.strip() == f'conda activate {venv}':
            os.system(f'conda activate {venv}')
            print('\nConda Virtual Environment is running.\n')

    elif cmd.strip() == "file(tesla)":
        os.system('tesla')

    elif cmd == "passwd":
        passwd()

    elif cmd == "llama":
        start_ollama_silently()
        print('Type \'/bye\' to exit or type \'/specs\' to display the llm specifications.\n')

        while run:

            content = input('You: ')

            if content == '/bye':
                print('llama: Bye!')
                break

            elif content == '/specs':
                print('\nModel: ' + DEFAULT_MODEL)
                print('Size: ' + DEFAULT_SIZE)
                print('Estimated speed: ' + DEFAULT_SPEED, end="\n\n")
                continue

            response = ollama.chat(model=DEFAULT_MODEL, messages=[
                {
                    'role': 'user',
                    'content': content
                },
            ])

            print('llama: ' + response['message']['content'], end="\n\n")

    elif cmd == "ollama":
        start_ollama_silently()
        print('Type \'/bye\' to exit or type \'/specs\' to display the llm specifications.\n')

        while run:

            content = input('You: ')

            if content == '/bye':
                print('llama: Bye!\n')
                break

            elif content == '/specs':
                print('\nModel: ' + DEFAULT_MODEL)
                print('Size: ' + DEFAULT_SIZE)
                print('Estimated speed: ' + DEFAULT_SPEED, end="\n\n")
                continue
                
            response = ollama.chat(model=DEFAULT_MODEL, messages=[
                {
                    'role': 'user',
                    'content': content
                },
            ])

            print('llama: ' + response['message']['content'], end="\n\n")
            
    elif cmd == "llm:choose":
        print('Models Available: \n\n-> llama:1b \n-> llama\n-> gemma\n-> qwen\n')
        model = input('Model to choose: ')
        
        if model.lower() == 'llama:1b':
            DEFAULT_MODEL = 'llama3.2:1b'
            DEFAULT_SIZE = '1.3 GB (est. 1 Billion parameters)'
            DEFAULT_SPEED = '11.07 Tokens Per Second'
            print(f'{model} has been set as the default model.\n')
            
        elif model.lower() == 'llama':
            DEFAULT_MODEL = 'llama3.2'
            DEFAULT_SIZE = '2 GB (est. 3 Billion parameters)'
            DEFAULT_SPEED = '6.17 Tokens Per Second'
            print(f'{model} has been set as the default model.\n')
            
        elif model.lower() == 'gemma':
            DEFAULT_MODEL = 'llama3.2'
            DEFAULT_SIZE = '1.6 GB (est. 2 Billion parameters)'
            DEFAULT_SPEED = '7.27 Tokens Per Second'
            print(f'{model} has been set as the default model.\n')
            
        elif model.lower() == 'qwen':
            print(Fore.RED + 'Warning: The model you have selected might show unexpeted and inaccurate details even though it will be faster.' + Fore.LIGHTCYAN_EX)
            DEFAULT_MODEL = 'qwen2.5:0.5b'
            DEFAULT_SIZE = '397 MB (est. 500 Million parameters)'
            DEFAULT_SPEED = '27.16 Tokens Per Second'
            print(f'{model} has been set as the default model.\n')        
        
    else:
        print(Fore.RED + "ERROR:"+Fore.LIGHTRED_EX+" Unknown Token.\nFor a list of keywords, type\'keywords{tokens: /~} \' ")

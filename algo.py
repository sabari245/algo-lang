import os
import openai
import colorama
import sys
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# get the file name from the command line
if len(sys.argv) < 2:
    print("Usage: python3 algo.py <file_name>")
    sys.exit(1)
file_name = sys.argv[1]

# check if the filename ends with .algo
if not file_name.endswith(".algo"):
    print("Please provide a file with .algo extension")
    sys.exit(1)

# read the contents of the file
with open(file_name, "r") as f:
    contents = f.read()
    print(colorama.Fore.GREEN + "✔" + colorama.Fore.WHITE + " File read successfully")
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="convert the algorithm to a rust program\n" + contents + "\n", 
        temperature=0.8,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    # write the response to the file
    with open(file_name.replace(".algo", ".rs"), "w") as f:
        f.write(response.choices[0].text)
        f.close()
    print(colorama.Fore.GREEN + "✔" + colorama.Fore.WHITE + " Successfully converted to rust")
    print(colorama.Fore.RESET)
# compile the rust program
os.system("rustc " + file_name.replace(".algo", ".rs") + " -o " + file_name.replace(".algo", ".exe"))
print(colorama.Fore.GREEN + "✔" + colorama.Fore.WHITE + " Successfully compiled")
print(colorama.Fore.RESET)

# print a bold yellow message "i"
print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "INFO" + colorama.Style.RESET_ALL)
# print a normal text displaying the instructions to compile and execute the rust file
print("to run the executable file:")
print(file_name.replace(".algo", ".exe"))
print(colorama.Fore.RESET)
import os
import re
import sys
import base64
import argparse

# Updated on 13/01/2024

query = None
string = None

parser = argparse.ArgumentParser(
    description='Use this command-line arguments to encode/decode very fast.',  # it's shows description to starting of help
    epilog=f"Note: Use '\\' to ignore existing file path. e.g: {os.path.basename(sys.argv[0])} -e \\file.txt",  # it's shows the epilog to the last of help
    usage=None,  # it's sets the default usage message to custom message
)

group = parser.add_mutually_exclusive_group()

group.add_argument(
    "--encode", "-e",
    dest="encode",
    metavar="\33[92mtext / file\33[0m",
    help="Encode string to base64"
)

group.add_argument(
    "--decode", "-d",
    dest="decode",
    metavar="\33[92mtext / file\33[0m",
    help="Decode base64 to string"
)

parser.add_argument(
    "--output", "-o",
    dest="output",
    metavar="file_path",
    help="Save output to a file."
)

args = parser.parse_args()  # parse specified args to the program
# print(args)

if args.encode:
    query = "encode"
    string = args.encode
elif args.decode:
    query = "decode"
    string = args.decode

if string:
    if os.path.isfile(string):
        with open(string, "rb") as f:
            string = f.read()
    else:
        if string.startswith("\\"):
            string = string.removeprefix("\\")
        string = string.encode("ascii")

output_file = args.output
if args.output:
    origin_path = os.path.split(output_file)[0]

logo = '''
\33[1;91m█▄▄ ▄▀█ █▀ █▀▀  \33[1;92m █▄▄ █ █\33[0m
\33[1;91m█▄█ █▀█ ▄█ ██▄  \33[1;92m █▄█ ▀▀█\33[0m'''

max_len_of_logo = len(re.sub(r'\x1B\[[^m]*m', '', logo).split("\n")[1])

def main(query, string, output_file):
    print(logo)
    print(max_len_of_logo  * "━", end="\n\n")
    if not query:
        query = input('[\033[1;92m?\033[0m\033[1m] What you want to do \033[1;91mEncode\033[0m\033[1m/\033[1;92mDecode\033[0m\033[1m ? [E/d] ').lower()

    if (query == "encode" or query == "e"):
        if not string:
            string = input("[\033[1;91m!\033[0m\033[1m] Enter Some string to encode:\nbase64 > ").encode("ascii")
        en = base64.b64encode(string).decode()
        if output_file:
            try:
                with open(output_file, "w") as f:
                    f.write(en)
            except FileNotFoundError:
                print(f"Path not found. --> {origin_path}")
                sys.exit(1)
            print(f"[Saved encoded base64 string to]: \33[92;4m{output_file}\33[0m file.")
        else:
            print(f"Encoded base64 string is:\n>> \33[92m{en}\33[0m")
            

    elif (query == "decode" or query == "d"):
        if not string:
            string = input("[\033[1;92m!\033[0m\033[1m] Enter Some string to decode:\nbase64 > ").encode("ascii")
        try:
            de = base64.b64decode(string).decode()
        except Exception:
            print("Invalid base64 code.")
            sys.exit(1)
        if output_file:
            try:
                with open(output_file, "w") as f:
                    f.write(en)
            except FileNotFoundError:
                print(f"Path not found. --> {origin_path}")
                sys.exit(1)
            print(f"[Saved decoded base64 string to]: \33[92;4m{output_file}\33[0m file.")
        else:
            print(f"Decoded base64 string is:\n>> \33[92m{de}\33[0m")

if __name__ == "__main__":
    try:
        main(query, string, output_file)
    except (EOFError, KeyboardInterrupt):
        pass
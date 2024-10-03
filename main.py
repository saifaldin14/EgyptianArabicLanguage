import re

# Define keyword mapping
slang_to_python = {
    'lw': 'if',
    'gheir da': 'elif',
    'mafee4': 'else',
    'ebtidi min': 'for',
    'lama': 'while',
    'esmi': 'def',
    'raga3': 'return',
    'ekteb': 'print',
    'sheel': 'input',
    'akbar': '>',
    'azghar': '<',
    'zy': '==',
    'mi4 zy': '!=',
    'wa': 'and',
    'aw': 'or',
    'mi4': 'not',
    'garrab': 'try',
    'ma zabat4': 'except',
    '7aga': 'class',
    'bedaya': '__init__',
    '//': '#',  # Comments
}

def translate(slang_code):
    python_code = []
    
    for line in slang_code.splitlines():
        stripped_line = line.lstrip()
        leading_spaces = line[:len(line) - len(stripped_line)]  # preserve the leading spaces (indentation)
        translated_line = stripped_line
        
        for slang_word, python_word in slang_to_python.items():
            translated_line = re.sub(rf'\b{slang_word}\b', python_word, translated_line)
        
        python_code.append(leading_spaces + translated_line)
    
    return "\n".join(python_code)

# Execute the translated Python code
def execute_translated_code(python_code):
    try:
        exec(python_code)
    except Exception as e:
        print(f"Error executing code: {str(e)}")

# Parser function
def arabic_parser(slang_code):
    python_code = translate(slang_code)
    
    print("Translated Python Code:\n")
    print(python_code)
    
    print("\nOutput:\n")
    execute_translated_code(python_code)

# CLI to allow slang file execution
def arabic_parser_cli(file_name):
    if not file_name.endswith('.arsl'):
        print("Invalid file extension. Please provide a .arsl file.")
        return
    
    try:
        with open(file_name, 'r') as file:
            slang_code = file.read()
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return

    arabic_parser(slang_code)

# REPL for interactive input
def slang_repl():
    print("Welcome to the Egyptian Arabic REPL. Type your code below. Type 'exit' to quit.")
    while True:
        slang_code = input(">>> ")
        if slang_code.lower() == 'exit':
            break
        arabic_parser(slang_code)

def execute_local_test():
    slang_repl()

    slang_code = """
esmi salaam():
    ekteb("Ahlan wa sahlan ya 3alam!")
    raga3 "Salam"

ism = sheel("Esmak eh? ")
ekteb(f"Ahlan, {ism}")

lw (ism zy "Ahmad"):
    ekteb("A7la esm!")
mafee4:
    ekteb("Ma3rafak4!")

salaam()
    """

    arabic_parser(slang_code)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1: # There's a file
        arabic_parser_cli(sys.argv[1]) # Execute the parser with a file
    else:
        execute_local_test() # Just run the local test

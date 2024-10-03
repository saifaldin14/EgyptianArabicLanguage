import re

# Define the slang-to-Python keyword mapping
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

# Translate slang code into Python code
def translate_slang_to_python(slang_code):
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
def slang_parser(slang_code):
    python_code = translate_slang_to_python(slang_code)
    
    print("Translated Python Code:\n")
    print(python_code)
    
    print("\nOutput:\n")
    execute_translated_code(python_code)

# CLI to allow slang file execution
def slang_parser_cli(file_name):
    if not file_name.endswith('.arsl'):
        print("Invalid file extension. Please provide a .arsl file.")
        return
    
    try:
        with open(file_name, 'r') as file:
            slang_code = file.read()
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return

    slang_parser(slang_code)

# REPL for interactive input
def slang_repl():
    print("Welcome to the Arabic Slang REPL. Type your code below. Type 'exit' to quit.")
    while True:
        slang_code = input(">>> ")
        if slang_code.lower() == 'exit':
            break
        slang_parser(slang_code)

def execute_local_test():
    slang_repl()

    slang_code = """
esmi salaam():
    ekteb("Marhaba ya 3alam!")
    raga3 "Salam"

ism = sheel("Shu esmak? ")
ekteb(f"Ahlan, {ism}")

lw (ism zy "Ahmad"):
    ekteb("Ya hala ya Ahmad!")
mafee4:
    ekteb("Ma a3rafak!")

salaam()
    """

    slang_parser(slang_code)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        slang_parser_cli(sys.argv[1])
    else:
        execute_local_test()

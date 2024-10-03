import re

# Step 1: Define the slang-to-Python keyword mapping
slang_to_python = {
    'iza': 'if',
    'ellie iza': 'elif',
    'aw': 'else',
    'min': 'for',
    'lama': 'while',
    'esmi': 'def',
    'raja3': 'return',
    'ekteb': 'print',
    'sheel': 'input',
    'akbar': '>',
    'azghar': '<',
    'mitl': '==',
    'mish mitl': '!=',
    'wa': 'and',
    'aw': 'or',
    'mish': 'not',
    'khaliha': '',  # Variables don't need keywords in Python
    'jarrib': 'try',
    'iza ma zabat': 'except',
    'taqsim': 'class',
    'eshmelo': '__init__',
    '//': '#',  # Comments
}

# Step 2: A function to translate slang code into Python code
def translate_slang_to_python(slang_code):
    # Handle multiline translation to preserve indentation
    python_code = []
    for line in slang_code.splitlines():
        translated_line = line
        # Replace slang keywords with Python equivalents
        for slang_word, python_word in slang_to_python.items():
            translated_line = re.sub(rf'\b{slang_word}\b', python_word, translated_line)
        python_code.append(translated_line)
    
    return "\n".join(python_code)

# Step 3: Function to execute the translated Python code
def execute_translated_code(python_code):
    try:
        exec(python_code)
    except Exception as e:
        print(f"Error executing code: {str(e)}")

# Step 4: The full parser function
def slang_parser(slang_code):
    # Step 4.1: Translate the slang code to Python
    python_code = translate_slang_to_python(slang_code)
    
    # Step 4.2: Print out the translated code for reference
    print("Translated Python Code:\n")
    print(python_code)
    
    # Step 4.3: Execute the translated Python code
    print("\nOutput:\n")
    execute_translated_code(python_code)

# Example Slang Code
slang_code = """
esmi salaam():
    ekteb("Marhaba ya 3alam!")
    raja3 "Salam"

khaliha ism = sheel("Shu esmak? ")
ekteb(f"Ahlan, {ism}")

iza ism mitl "Ahmad":
    ekteb("Ya hala ya Ahmad!")
aw:
    ekteb("Ma a3rafak!")

salaam()
"""

# Run the parser
slang_parser(slang_code)

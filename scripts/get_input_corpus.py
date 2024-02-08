import os
import logging
import argparse
import json
import random
import javalang
import ast
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_args() -> argparse.Namespace:
    """
    Get the arguments from the command line

    Returns:
        argparse.Namespace: The parsed arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default='../code')
    parser.add_argument('--number_of_input', type=int, default=10)
    parser.add_argument('--output_path', type=str, required=False)
    parser.add_argument('--prompt', type=str, help='Prompt to send to the model', required=True)

    
    args = parser.parse_args()

    return args

def get_file_list(path: str) -> list[str]:
    """
    Get all the files in a directory and put them in a list

    Args:
        path (str): The path to the directory

    Returns:
        list[str]: A list of all the files in the directory

    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.java') or file.endswith('.py'):
                file_list.append(os.path.join(root, file))
    return file_list


def generate_input_values(arg_types: list, number_of_input: int) -> list:
    """
    Generate input values for the function based on the argument types
    
    Args:
        arg_types (list): A list of argument types
        number_of_input (int): The number of input values to generate

    Returns:
        list: A list of input values for the function
    """
    input_values = []
    for _ in range(number_of_input): 
        args = []
        for arg_type in arg_types:
            if arg_type == 'int':
                args.append(random.randint(1, 100))
            elif arg_type == 'String':
                args.append(''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(10)))
            elif arg_type == 'double':
                args.append(random.uniform(1.0, 100.0))
            elif arg_type == 'boolean':
                args.append(random.choice([True, False]))
            elif arg_type == 'int[]':
                args.append([random.randint(1, 100) for _ in range(5)])
            else:
                # Throw an error if the argument type is not supported with the data type needed
                raise TypeError(f"Argument type {arg_type} is not supported")
        input_values.append(args)
    return input_values


def extract_java_function_info(java_code: str, number_of_input: int) -> dict:
    """
    Extract the function information from the Java code

    Args:
        java_code (str): The Java code
        number_of_input (int): The number of input values to generate
    Returns:
        dict: A dictionary containing the function information
    """
    function_info = {}
    tree = javalang.parse.parse(java_code)
    seen_args = set()
    for _, method_declaration in tree.filter(javalang.tree.MethodDeclaration):
        method_name = method_declaration.name
        arg_types = []
        for param in method_declaration.parameters:
            # Check if the parameter is an array type
            if isinstance(param.type, javalang.tree.ReferenceType) and param.type.dimensions:
                array_type = param.type.name + '[]'
                arg_types.append(array_type)
            elif isinstance(param.type, javalang.tree.BasicType) and param.type.dimensions:
                array_type = param.type.name + '[]'
                arg_types.append(array_type)
            else:
                arg_types.append(param.type.name)

        # Exclude the main method
        if method_name == 'main':
            continue
        # If the argument types are already seen, skip it
        if str(arg_types) in seen_args:
            continue
        else:
            # Add the argument types to the seen_args set if it is not seen before
            seen_args.add(str(arg_types))
            input_values = generate_input_values(arg_types, number_of_input)
            function_info[str(arg_types)] = input_values

    return function_info

def extract_python_function_info(python_code: str, number_of_input: int) -> dict:
    """
    Extract the function information from the Python code with type annotations.

    Args:
        python_code (str): The Python code, expected to include type annotations.
        number_of_input (int): The number of input values to generate (not implemented here).

    Returns:
        dict: A dictionary containing the function information, including names, argument types.
    """
    function_info = {}
    seen_args = set()

    # Parse the Python code into an AST
    tree = ast.parse(python_code)

    # Walk through the AST to find function definitions
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            method_name = node.name
            arg_types = []

            # Don't include the main method
            if method_name == 'main':
                continue

            # Get arguments and their type annotations from the function definition
            for arg in node.args.args:
                arg_name = arg.arg
                # Type annotation (Python 3.6+)
                if arg.annotation:
                    # Convert the annotation node to a string representation of the type
                    # Requires Python 3.9+ for ast.unparse, use ast.dump for earlier versions
                    arg_type = ast.unparse(arg.annotation) if hasattr(ast, 'unparse') else ast.dump(arg.annotation)
                
                    # If the argument types are already seen, skip it
                    if str(arg_types) in seen_args:
                        continue
                    else:
                        # Add the argument types to the seen_args set if it is not seen before
                        seen_args.add(str(arg_types))
                        input_values = generate_input_values(arg_types, number_of_input)
                        function_info[str(arg_types)] = input_values

    return function_info



def main():
    # --- Get arguments --- # 
    parser = argparse.ArgumentParser()
    args = get_args()
    input_path = args.input_path
    number_of_input = args.number_of_input

    # --- Get file list --- #
    logging.info('Getting file list from {}'.format(input_path))
    file_list = get_file_list(input_path)
    logging.info('File list: {}'.format(file_list))

    # --- Extract Input --- #
    logging.info('Extracting input from files')

    for file in file_list:
        logging.info('Extracting input corpus for {}'.format(file))
        with open(file, 'r') as f:
            java_code = f.read()    

        if "java" in file:
            function_info = extract_java_function_info(java_code, number_of_input)
        else: 
            logging.info('Only Java files are supported. Skipping {}'.format(file))
            continue
    # -- Write the input corpus to a file -- #
        # remove the .java extension from the file name
        file = file[:-5]
        with open(f'{file}_input.json', 'w') as f:
            json.dump(function_info, f, indent=4)
        
        logging.info('Extracted input corpus for {}'.format(file))

if __name__ == '__main__':
    main()
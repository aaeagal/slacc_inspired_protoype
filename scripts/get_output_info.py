import os
import logging
import argparse
import json
import javalang
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
import get_input_corpus
import subprocess
import ast

def run_method(file: str, method_name: str, input_values: list[str]) -> str:
    
    # Check if input_values is a list of lists or a list of individual values
    if all(isinstance(item, list) for item in input_values):
        # Flatten the list of lists and convert to strings
        flat_input_values = [str(item) for sublist in input_values for item in sublist]
    else:
        # Convert individual values to strings
        flat_input_values = [str(item) for item in input_values]

    # get file path
    filepath = os.path.dirname(file)
    file_extension = os.path.splitext(file)[1]
    class_name = os.path.basename(file).split('.')[0]

    if file_extension == '.java':
        command = ["java", "-cp", filepath, class_name, method_name] + flat_input_values

    elif file_extension == '.py':
        command = ["python3", file, method_name] + flat_input_values
    else:
        ValueError("Unsupported file type in run_method() function.")
    
    result = subprocess.run(command, capture_output=True, text=True)

    if result.stderr:
        print("Error:", result.stderr)
    return result.stdout.strip()



def getOutputInfo(code: str, input_info: dict, file: str):
    function_info = {}
    file_extension = os.path.splitext(file)[1]
    
    if file_extension == '.java':
        tree = javalang.parse.parse(code)
        for _, method_declaration in tree.filter(javalang.tree.MethodDeclaration):
            method_info = {}
            method_name = method_declaration.name
            method_info["argument_types"] = [param.type.name for param in method_declaration.parameters]
            method_info["runtime_behavior"] = {}

            # Get input values
            for input_name, input_space in input_info.items():
                # Run the method with the input values
                for input_value in input_space:
                    output = run_method(file, method_name, input_value)
                    method_info["runtime_behavior"][str(input_value)] = output
                
            function_info[method_name] = method_info

    elif file_extension == '.py':
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # if main function, skip
                if node.name == 'main':
                    continue
                # add method name to list
                method_name = node.name
                method_info = {}
                method_info["argument_types"] = [arg.arg for arg in node.args.args]
                method_info["runtime_behavior"] = {}

                # Get input values
                for input_name, input_space in input_info.items():
                    # Run the method with the input values
                    for input_value in input_space:
                        output = run_method(file, method_name, input_value)
                        method_info["runtime_behavior"][str(input_value)] = output
                
                function_info[method_name] = method_info        
    else:
        print("Unsupported file type")
        
    return function_info


def main():
    # --- Get arguments --- # 
    parser = argparse.ArgumentParser()
    args = get_input_corpus.get_args()
    input_path = args.input_path
    number_of_input = args.number_of_input
    prompt = args.prompt

    # --- Get file list --- #
    file_list = get_input_corpus.get_file_list(input_path)

    # -- Get only 0 and 1 temperature and runnable files -- #
    filtered_file_list = [file for file in file_list if "0" in file or "1" in file]
    filtered_file_list = [file for file in filtered_file_list if "Solution" in file]

    # --- Get input information from file --- #
    with open(f'/home/aeagal/slacc_inspired_protoype/data/{prompt}/original_input.json', 'r') as f:
        input_info = json.load(f)
        logging.info('Got input information from {} \n\n'.format(f'/home/aeagal/slacc_inspired_protoype/data/{prompt}/original_input.json'))

    # --- Start processing files --- # 
    for file in filtered_file_list:
        logging.info('Starting process for {}'.format(file))
        file_name = (os.path.basename(file)).lstrip()

    # --- Get input information from file --- #
        if file_name.startswith("Solution"):
             
        # --- Get output information from the file --- #
            with open(file, 'r') as f:
                code = f.read()
                logging.info('Got code from {}'.format(file))
            
            output_info = getOutputInfo(code, input_info, file)
            logging.info(f'Extracted runtime behavior from {file}\n\n')

     
        # ---  Save output information to file --- #
        with open(f'{os.path.dirname(file)}/behavior.json', 'w') as f:
            logging.info('Saving output information to {}'.format(f'{os.path.dirname(file)}/behavior.json'))
            json.dump(output_info, f, indent=4)
    
    

    logging.info('Finished processing {}'.format(file))


if __name__ == '__main__':
    main()
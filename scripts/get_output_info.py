import os
import logging
import argparse
import json
import javalang
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
import get_input_corpus
import subprocess

def run_java_method(file, method_name, input_values):
    # Check if input_values is a list of lists or a list of individual values
    
    if all(isinstance(item, list) for item in input_values):
        # Flatten the list of lists and convert to strings
        flat_input_values = [str(item) for sublist in input_values for item in sublist]
    else:
        # Convert individual values to strings
        flat_input_values = [str(item) for item in input_values]

    class_name = os.path.basename(file)
    print(f' CLASS NAME: {class_name[:-5]}')
    java_command = ["java", class_name[:-5], method_name] + flat_input_values
    result = subprocess.run(java_command, capture_output=True, text=True)
    #print(f'result: {result}\n\n')
    if result.stderr:
        print("Error:", result.stderr)
    return result.stdout.strip()

def getOutputInfo(java_code, input_info, file):
    function_info = {}
    tree = javalang.parse.parse(java_code)
    for _, method_declaration in tree.filter(javalang.tree.MethodDeclaration):
        method_name = method_declaration.name
        arg_types = []
        for param in method_declaration.parameters:
            type_name = param.type.name
            if param.type.dimensions:
                # Append '[]' for array types
                type_name += '[]'
            arg_types.append(type_name)

        arg_types_str = str(arg_types)
        print(f'arg_types: {arg_types_str}\n')
        print(f'input_info: {input_info.keys()}\n')

        if arg_types_str in input_info:
            print("Got a match!\n\n")
            input_values = input_info[arg_types_str]
            output_values = []
            for input_value in input_values:
                print(f'input_value: {input_value}')
                output_value = run_java_method(file, method_name, input_value)
                output_values.append(output_value)
            function_info[method_name] = {
                'input_types': arg_types,
                'input_values': input_values,
                'output_values': output_values
            }
        else:
            continue

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

    # --- Start processing files --- # 
    for file in file_list:  
        logging.info('Starting process for {}'.format(file))

    # --- Get input information from file --- #         
        with open(f'/home/aeagal/slacc_inspired_protoype/data/{prompt}/{file[:-5]}_input.json', 'r') as f:
            input_info = json.load(f)
            logging.info('Got input information from {} \n\n'.format(file))

    # --- Get output information from the file --- #
        with open(file, 'r') as f:
            code = f.read()
            logging.info('Got code from {}'.format(file))
        
        output_info = getOutputInfo(code, input_info, file)


    # ---  Save output information to file --- #
        with open(f'/home/aeagal/slacc_inspired_protoype/data/{prompt}/{file[:-5]}.json', 'w') as f:
            json.dump(output_info, f, indent=4)
        
        logging.info(f'Extracted output behavior from {file} and saved to {file}.json\n\n')



if __name__ == '__main__':
    main()
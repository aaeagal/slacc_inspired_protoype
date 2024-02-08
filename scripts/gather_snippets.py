import hashlib
import os
import sys
import json
import random
import openai
import re
import requests
import argparse
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ----------------------------------------------------Global Variables----------------------------------------------------

# Get API keys(OpenAI and Hugging Face)
openai.api_key = os.environ["OPENAI_API_KEY"]

APIURL = {
    "starcoder": "placeholder",
    "codellama": "https://ngc37enjcuskhoxi.us-east-1.aws.endpoints.huggingface.cloud"
}
headers = {
    "Accept" : "application/json",
    "Authorization": f'Bearer {os.environ["HuggingFace_API_KEY"]}',
    "Content-Type": "application/json"
}

# ----------------------------------------------------Functions----------------------------------------------------------

def parse_arguments() -> dict:
    """
    Parse the command line arguments

    This function parses the command line arguments and returns a dictionary
    of the parsed arguments.

    Returns:
        dict: The parsed arguments
    
    """
    # Create the parser
    parser = argparse.ArgumentParser(description='Queries the LLMs for a given prompt and returns code snippets.')

    parser.add_argument(
        '--prompt', type=str, help='Prompt to send to the model', required=True
    )
    parser.add_argument(
        '--model', type=str, help='Model (GPT vs StarCoder)', required=True
    )
    parser.add_argument(
        '--temperature', type=int, help='Temperature for the response generation', required=True
    )
    parser.add_argument(
        '--task', type=str, help='Task to perform (python2java, java2python, python)', required=True  
    )

    # Parse the arguments
    args = parser.parse_args()

    return args

def query_gpt(prompt: str, model: str, temperature: float) -> str:
    """
    Sends a query to the specified GPT model and retrieves the response.

    This function submits a prompt to the OpenAI API using the specified GPT model.
    It allows setting a temperature for the response generation, influencing the
    creativity and randomness of the output.

    Args:
        prompt (str): The input text prompt to send to the model.
        model (str): The identifier of the GPT model to be used for the response.
        temperature (float): A float value that controls the randomness of the
                             response. Lower values make the model more deterministic.

    Returns:
        str: The content of the response from the GPT model.

    The function sets a fixed maximum token limit of 2048, with top_p set to 1,
    and both frequency_penalty and presence_penalty set to 0, for the generation
    of the response.
    """

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": f'{prompt}\n'
            }
        ],
        temperature=temperature,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    return response["choices"][0]["message"]["content"]


def query_huggingface(prompt: str, model: str, temperature: float) -> str:
    """
    Sends a query to the specified Hugging Face model and retrieves the response.

    This function submits a prompt to the Hugging Face API using the specified model.

    Args:
        prompt (str): The input text prompt to send to the model.
        model (str): The identifier of the Hugging Face model to be used for the response.
        temperature (float): A float value that controls the randomness of the
                             response. Lower values make the model more deterministic.

    Returns:
        str: The content of the response from the Hugging Face model.

    """

    # Create the payload for the request
    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": temperature,
            "max_new_tokens": 2048,
            "top_p": 1,
            "frequency_penalty": 0,
        }
    }

    # Send the request to the Hugging Face model
    response = requests.post(APIURL[model], headers=headers, json=payload) 

    # Check if the response is successful
    if response.status_code != 200:
        raise Exception(f"Request failed with status {response.status_code}")

    # Try parsing the response as JSON
    try:
        return response["choices"][0]["message"]["content"]
    except ValueError:
        raise ValueError("API response could not be parsed as JSON")

def get_file_suffix(task: str) -> str:
    """
    Returns the file suffix for the given task.

    This function returns the file suffix for the given task. The file suffix
    is used to determine the file extension of the generated code snippets.

    Args:
        task (str): The task for which to generate the file suffix.

    Returns:
        str: The file suffix for the given task.
    """

    # Return the file suffix based on the task
    if task == "python2java":
        return "java"
    elif task == "java2python":
        return "py"
    elif task == "python":
        return "py"
    else:
        raise ValueError(f"Unknown file suffix in get_file_suffix: {task}")
    


def main():

    # -- Get the command line arguments -- #
    args = parse_arguments()
    task = args.task
    model = args.model
    prompt = args.prompt
    temperature = args.temperature

    # -- Get the file suffix -- #
    file_suffix = get_file_suffix(task)

    # -- Query the model -- #
    with open(f'../data/{prompt}/{model}/{task}/{temperature}/generated.{file_suffix}', 'w') as file:
        logging.info(f"Writing to file: ../data/{prompt}/{model}/{task}/{temperature}/generated.{file_suffix}")

        # unique_samples = 0
        total_samples = 0

        # hashes = set()

        while total_samples < 20:
            total_samples += 1

            # Get code snippet
            if task == "python2java":
                with open(f'../data/{prompt}/original.py', 'r') as original_file:

                    # Get the original code and create prompt
                    original_code = original_file.read()
                    model_input = f"Convert the following Python code to Java:\n{original_code}"

                    # Query the model
                    if model == "gpt-3.5-turbo" or model == "gpt-4":
                        response = query_gpt(model_input, model, temperature)
                    elif model == "starcoder" or model == "codellama":
                        response = query_huggingface(model_input, model, temperature)
                    else:
                        raise ValueError(f"Unknown model in main: {model}")

            elif task == "java2python":
                with open(f'../data/{prompt}/original.java', 'r') as original_file:

                    # Get the original code and create prompt
                    original_code = original_file.read()
                    model_input = f"Convert the following Java code to Python:\n{original_code}"

                    # Query the model
                    if model == "gpt-3.5-turbo" or model == "gpt-4":
                        response = query_gpt(model_input, model, temperature)
                    elif model == "starcoder" or model == "codellama":
                        response = query_huggingface(model_input, model, temperature)
                        # Extract the code snippet from the response
                        response = response["choices"][0]["message"]["content"]
                    else:
                        raise ValueError(f"Unknown model in main: {model}")

            elif task == "python":
                with open(f'../data/{prompt}/original.py', 'r') as original_file:

                    # Get the original code and create prompt
                    original_code = original_file.read()
                    model_input = f"Create a clone of the following code that is semantically equivalent and syntactially different: \n{original_code}"

                    # Query the model
                    if model == "gpt-3.5-turbo" or model == "gpt-4":
                        response = query_gpt(model_input, model, temperature)
                    elif model == "starcoder" or model == "codellama":
                        response = query_huggingface(model_input, model, temperature)
                    else:
                        raise ValueError(f"Unknown model in main: {model}")
            else:
                raise ValueError(f"Unknown task in main: {task}")

    # -- Check if the response is unique and write it to the file if it is unique -- #
#            hash_value = hashlib.sha256(response.encode()).hexdigest()

#            if hash_value not in hashes:
            #unique_samples += 1
#                hashes.add(hash_value)
            file.write(response)
            file.write("\n\n\n")

    # -- Log the results -- #          
            logging.info(f"Total samples: {total_samples}")
#")


if __name__ == "__main__":
    main()
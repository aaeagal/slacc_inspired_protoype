import hashlib
import os
import sys
import json
import random
import openai
import re
import requests
import argparse

# ----------------------------------------------------Global Variables----------------------------------------------------

# Get API keys(OpenAI and Hugging Face)
openai.api_key = os.environ["OPENAI_API_KEY"]
APIURL = {
    "starcoder": "placeholder",
    "huggingface": "placeholder"
}
headers = {
    "Authorization: Bearer " + os.environ["HUGGINGFACE_API_KEY"],
    "Content-Type: application/json"
}

# Independent Variables
temperatures = [0,1,2]
models = ["gpt-3.5-turbo", "gpt-4", "starcoder", "codellama"]

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

    # Add arguments
    parser.add_argument(
        'positional_argument', type=int, help='A positional integer argument'
    )
    parser.add_argument(
        '--optional_argument', type=str, help='An optional string argument', default='default_value'
    )
    parser.add_argument(
        '--flag', action='store_true', help='A boolean flag'
    )

    # Parse the arguments
    args = parser.parse_args()

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


def query_huggingface(payload: dict, model: str, temperature: float) -> dict:
    """
    Sends a query to the specified Hugging Face model with a given payload and temperature.

    This function submits a payload to a Hugging Face API model endpoint. It modifies
    the payload to include the specified temperature, which controls the randomness
    of the response. If the response status is not 200, it raises an exception.

    Args:
        payload (dict): The payload containing the data to be sent to the model.
        model (str): The identifier of the Hugging Face model to be used.
        temperature (float): A float value that controls the randomness of the
                             generated response from the model.

    Returns:
        dict: The JSON response from the Hugging Face model.

    Raises:
        Exception: If the request to the Hugging Face model fails.
        ValueError: If the API response cannot be parsed as JSON.
    """

    # Send the request to the Hugging Face model
    response = requests.post(APIURL[model], headers=headers, json=payload) 

    # Check if the response is successful
    if response.status_code != 200:
        raise Exception(f"Request failed with status {response.status_code}")

    # Try parsing the response as JSON
    try:
        return response.json()
    except ValueError:
        raise ValueError("API response could not be parsed as JSON")


def main():

    # -- Get the command line arguments -- #
    args = parse_arguments()

if __name__ == "__main__":
    main()
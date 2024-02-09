import json
import get_input_corpus
import argparse
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
import os


def calculate_similarity_between_methods(method1_behavior, method2_behavior):
    """
    Calculate the similarity between two methods based on their runtime behavior

    Args:
        method1_behavior (dict): The runtime behavior of method 1
        method2_behavior (dict): The runtime behavior of method 2

    Returns:
        float: The similarity percentage between the two methods

    """
    keys1 = set(method1_behavior.keys())
    keys2 = set(method2_behavior.keys())
    intersect_keys = keys1 & keys2
    total_keys = keys1 | keys2
    matched_count = sum(1 for k in intersect_keys if method1_behavior[k] == method2_behavior[k])
    similarity_percentage = (matched_count / len(total_keys)) * 100 if total_keys else 0
    return similarity_percentage

def main():
    # --- Get arguments --- # 
    parser = argparse.ArgumentParser()
    args = get_input_corpus.get_args()
    input_path = args.input_path
    number_of_input = args.number_of_input

    # --- Get file list --- #
    logging.info('Getting file list from {}'.format(input_path))
    file_list = get_input_corpus.get_file_list(input_path)


    # -- Get only 0 and 1 temperature and runnable files -- #
    filtered_file_list = [file for file in file_list if "0" in file or "1" in file]
    filtered_file_list = [file for file in filtered_file_list if "behavior" in file]

    # --- Get cluster information --- #
    for file in filtered_file_list:
        logging.info('Starting process for {}'.format(file))

        # Load the json file
        with open(file, 'r') as f:
            behavior_info = json.load(f)
            logging.info('Got behavior information from {}'.format(file))
        
        # Prepare a structure to hold the similarity results
        similarity_results = {}

        # Compare each method with every other method
        method_names = list(behavior_info.keys())
        for i in range(len(method_names)):
            for j in range(i + 1, len(method_names)):
                method1_name = method_names[i]
                method2_name = method_names[j]
                similarity_percentage = calculate_similarity_between_methods(
                    behavior_info[method1_name]["runtime_behavior"],
                    behavior_info[method2_name]["runtime_behavior"]
                )
                similarity_results[f"{method1_name} vs {method2_name}"] = similarity_percentage

        # Save the similarity results to a file
        with open(f'{file}_clusters.json', 'w') as f:
            logging.info('Saving similarity results to {}'.format(f'{file}_clusters.json'))
            json.dump(similarity_results, f, indent=4)


       # logging.info(f'Extracted clusters from {file} and saved to {file}_clusters.json\n\n')
if __name__ == '__main__':
    main()
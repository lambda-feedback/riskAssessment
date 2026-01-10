# Builds on BaseTestClass to allow testing of multiple risk assessment examples (from data/example_risk_assessments.py)

from ..test_classes.BaseTestClass import BaseTestClass
from ..utils.LLMCaller import LLMCaller
import pandas as pd
import numpy as np
from tabulate import tabulate
from datetime import datetime
from ..utils.GoogleSheetsWriter import GoogleSheetsWriter

class TestModelAccuracy(BaseTestClass):
    def __init__(self, 
                LLM: LLMCaller,
                list_of_input_and_expected_outputs: list,
                sheet_name: str,
                examples_gathered_or_generated_message: str,
                domain: str = None,
                is_first_test: bool = False):
        
        self.LLM = LLM
        self.list_of_input_and_expected_outputs = list_of_input_and_expected_outputs
        self.sheet_name = sheet_name
        self.examples_gathered_or_generated_message = examples_gathered_or_generated_message
        self.domain = domain
        self.is_first_test = is_first_test

    def get_expected_output_and_input_object(self, example_index):
        expected_output = self.list_of_input_and_expected_outputs[example_index].expected_output
        input_object = self.list_of_input_and_expected_outputs[example_index].prompt_input_object
        return expected_output, input_object

    def get_number_of_examples(self):
        return len(self.list_of_input_and_expected_outputs)

    def get_first_prompt_input(self):
        first_prompt_input_object = self.list_of_input_and_expected_outputs[0].prompt_input_object
        first_prompt_input = first_prompt_input_object.generate_prompt()
        return first_prompt_input
    
    def get_classes(self):
        first_prompt_input_object = self.list_of_input_and_expected_outputs[0].prompt_input_object

        classes = first_prompt_input_object.candidate_labels
        return classes
    
    def update_confusion_matrix(self, confusion_matrix, classes, pattern_matched, expected_output):

        if isinstance(pattern_matched, str) and 'No pattern found' in pattern_matched:
            return confusion_matrix # Don't change confusion matrix if no pattern found
        
        pattern_matched_index_in_class_list = classes.index(pattern_matched)
        expected_output_index_in_class_list = classes.index(expected_output)
        confusion_matrix[pattern_matched_index_in_class_list, expected_output_index_in_class_list] += 1

        return confusion_matrix
    
    def generate_confusion_matrix_string(self, confusion_matrix, classes):
        classes_as_strings = [str(e) for e in classes]
        confusion_matrix_df = pd.DataFrame(confusion_matrix, index=classes_as_strings, columns=classes_as_strings)

        confusion_matrix_df_values = confusion_matrix_df.values

        confusion_matrix_df_column_titles = confusion_matrix_df.columns
        column_titles_with_blank_space = confusion_matrix_df_column_titles.insert(0, "")

        confusion_matrix_with_column_titles = np.vstack((confusion_matrix_df_column_titles, confusion_matrix_df_values)).tolist()

        for i in range(len(confusion_matrix_with_column_titles)):
            confusion_matrix_with_column_titles[i].insert(0, column_titles_with_blank_space[i])

        confusion_matrix_string = tabulate(confusion_matrix_with_column_titles, headers='firstrow', tablefmt='grid')

        return confusion_matrix_string

    def update_output_string(self, output_string, example_index, pattern_matched, expected_output):
        result_dict = {'input': self.list_of_input_and_expected_outputs[example_index].prompt_input_object.to_string(),
                'pattern_matched': pattern_matched, 
                'expected_output': expected_output}

        output_string += f'{example_index + 1}: {str(result_dict)}\n\n'

        return output_string
    
    def update_prompt_output_strings(self, prompt_output, expected_output, pattern_matched, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, prompt_outputs_where_pattern_was_not_matched, example_index, count_correct, number_of_examples_where_pattern_in_prompt_output):
        if pattern_matched == 'No pattern found':
            prompt_outputs_where_pattern_was_not_matched += f'{example_index + 1}: {prompt_output}\nExpected output: {expected_output}\n\n'
        
        else:
            number_of_examples_where_pattern_in_prompt_output += 1

            if pattern_matched == expected_output:
                count_correct += 1

                prompt_outputs_for_correct_responses += f'{example_index + 1}: {prompt_output}\nExpected output: {expected_output}\n\n'
            
            else:
                prompt_outputs_for_incorrect_responses += f'{example_index + 1}: {prompt_output}\nExpected output: {expected_output}\n\n'

        return prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, prompt_outputs_where_pattern_was_not_matched, count_correct, number_of_examples_where_pattern_in_prompt_output

    def convert_list_of_lists_to_string(self, list_of_lists):
        # Convert each sublist to a string with newline
        sublist_strings = ['[' + ', '.join(map(str, sublist)) + ']' for sublist in list_of_lists]

        # Join the sublist strings with a newline and add outer brackets
        return '[' + ',\n'.join(sublist_strings) + ']'

    def get_model_accuracy_and_model_outputs(self):
        if self.is_first_test == True:
            purpose_of_test = input('Please enter the purpose of the test: ')
        else:
            purpose_of_test = ''

        print('Counting correct responses...')
        count_correct = 0
        number_of_examples_where_pattern_in_prompt_output = 0
        
        output_string = ''
        prompt_outputs_for_correct_responses = ''
        prompt_outputs_for_incorrect_responses = ''
        prompt_outputs_where_pattern_was_not_matched = ''

        classes = self.get_classes()
        n_classes = len(classes)

        confusion_matrix = np.zeros((n_classes, n_classes))

        n_examples = self.get_number_of_examples()

        for example_index in range(n_examples):

            expected_output, input_object = self.get_expected_output_and_input_object(example_index=example_index)

            pattern_matched, prompt_output = self.get_pattern_matched_and_prompt_output(input_object=input_object)

            confusion_matrix = self.update_confusion_matrix(confusion_matrix, classes, pattern_matched, expected_output)

            output_string = self.update_output_string(output_string, example_index, pattern_matched, expected_output)

            prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, prompt_outputs_where_pattern_was_not_matched, count_correct, number_of_examples_where_pattern_in_prompt_output = self.update_prompt_output_strings(
                                                                                                                            prompt_output=prompt_output, 
                                                                                                                            expected_output=expected_output, 
                                                                                                                            pattern_matched=pattern_matched, 
                                                                                                                            prompt_outputs_for_correct_responses=prompt_outputs_for_correct_responses, 
                                                                                                                            prompt_outputs_for_incorrect_responses=prompt_outputs_for_incorrect_responses, 
                                                                                                                            prompt_outputs_where_pattern_was_not_matched=prompt_outputs_where_pattern_was_not_matched,
                                                                                                                            example_index=example_index, 
                                                                                                                            count_correct=count_correct,
                                                                                                                            number_of_examples_where_pattern_in_prompt_output=number_of_examples_where_pattern_in_prompt_output)
            
            print(count_correct)


        accuracy = round(count_correct / n_examples * 100, 2)
        faithfulness_accuracy = round(number_of_examples_where_pattern_in_prompt_output / n_examples * 100, 2)

        return purpose_of_test, accuracy, faithfulness_accuracy, confusion_matrix, output_string, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, prompt_outputs_where_pattern_was_not_matched
    
    def get_first_prompt_input(self):
        first_input = self.list_of_input_and_expected_outputs[0].prompt_input_object
        first_prompt_input = first_input.generate_prompt()

        return first_prompt_input
    
    def save_test_results(self, 
                          purpose_of_test,
                          accuracy,
                          faithfulness_accuracy,
                          confusion_matrix,
                          output_string, 
                          prompt_outputs_for_correct_responses,
                          prompt_outputs_for_incorrect_responses,
                          prompt_outputs_where_pattern_was_not_matched,
                          first_prompt_input):

        datetime_now = datetime.now().strftime("%d-%m_%H-%M")

        model_parameters = f'Temp: {self.LLM.temperature}'
        
        num_examples = self.get_number_of_examples()

        new_line_data = [purpose_of_test, 
                        self.domain,
                         datetime_now, 
                         self.LLM.name, 
                        model_parameters, 
                        self.examples_gathered_or_generated_message,
                        accuracy, 
                        faithfulness_accuracy,
                        num_examples,
                        confusion_matrix,
                        output_string[:45000], # Google Sheets has a 50,000 character limit
                        first_prompt_input,
                        prompt_outputs_for_correct_responses[:45000],
                        prompt_outputs_for_incorrect_responses[:45000],
                        prompt_outputs_where_pattern_was_not_matched[:45000]
                        ]
        
        sheets_writer = GoogleSheetsWriter(sheet_name=self.sheet_name)
        sheets_writer.write_to_sheets(new_line_data)

    # TODO: Refactoring: As below, remove positional arguments and only use keyword arguments
    def run_test(self):
        purpose_of_test, accuracy, faithfulness_accuracy, confusion_matrix, output_string, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, prompt_outputs_where_pattern_was_not_matched = self.get_model_accuracy_and_model_outputs()

        confusion_matrix_string = self.generate_confusion_matrix_string(confusion_matrix, self.get_classes())
        
        first_prompt_input = self.get_first_prompt_input()
        self.save_test_results(purpose_of_test=purpose_of_test,
                               accuracy=accuracy,
                               faithfulness_accuracy=faithfulness_accuracy,
                               confusion_matrix=confusion_matrix_string,
                               output_string=output_string, 
                               first_prompt_input=first_prompt_input,
                               prompt_outputs_for_correct_responses=prompt_outputs_for_correct_responses,
                               prompt_outputs_for_incorrect_responses=prompt_outputs_for_incorrect_responses,
                               prompt_outputs_where_pattern_was_not_matched=prompt_outputs_where_pattern_was_not_matched)
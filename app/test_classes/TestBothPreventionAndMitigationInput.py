# Builds on TestControlMeasureClassificationPrompt.py to test % of times both prevention and mitigation correctly classified.

from ..test_classes.TestControlMeasureClassificationPrompt import TestControlMeasureClassificationPrompt
from ..utils.LLMCaller import LLMCaller
import numpy as np

class TestBothPreventionAndMitigationInput(TestControlMeasureClassificationPrompt):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list,
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list,
                    risk_assessment_control_measure_prompt_with_prevention_input_method_name: str,
                    risk_assessment_control_measure_prompt_with_mitigation_input_method_name: str,
                    domain: str = None,
                    is_first_test: bool = False,
                    ):
        
        self.LLM = LLM
        self.list_of_risk_assessment_and_expected_outputs = list_of_risk_assessment_and_expected_outputs
        self.sheet_name = sheet_name
        self.examples_gathered_or_generated_message = examples_gathered_or_generated_message
        self.candidate_labels = candidate_labels
        self.domain = domain
        self.is_first_test = is_first_test
        self.risk_assessment_control_measure_prompt_with_prevention_input_method_name = risk_assessment_control_measure_prompt_with_prevention_input_method_name
        self.risk_assessment_control_measure_prompt_with_mitigation_input_method_name = risk_assessment_control_measure_prompt_with_mitigation_input_method_name
        self.domain = domain
        self.is_first_test = is_first_test
    
    def get_first_prompt_input(self):

        prevention_prompt = self.get_first_prompt_input_with_risk_assessment_method(risk_assessment_method_name=self.risk_assessment_control_measure_prompt_with_prevention_input_method_name)
        mitigation_prompt = self.get_first_prompt_input_with_risk_assessment_method(risk_assessment_method_name=self.risk_assessment_control_measure_prompt_with_mitigation_input_method_name)
        
        return f'{prevention_prompt}\n\n{mitigation_prompt}'
    
    def get_pattern_matched_and_prompt_output(self, input_object):
        prevention_input = input_object.prevention
        mitigation_input = input_object.mitigation

        if prevention_input == '': # Indicating that there is no prevention input in the RA example
            prevention_pattern = ''
        else:
            prevention_pattern, prevention_prompt_output = self.get_pattern_matched_and_prompt_output_with_risk_assessment_method(input_object=input_object, risk_assessment_method_name=self.risk_assessment_control_measure_prompt_with_prevention_input_method_name)
        
        if mitigation_input == '':
            mitigation_pattern = ''
        else:
            mitigation_pattern, mitigation_prompt_output = self.get_pattern_matched_and_prompt_output_with_risk_assessment_method(input_object=input_object, risk_assessment_method_name=self.risk_assessment_control_measure_prompt_with_mitigation_input_method_name)
        prevention_and_mitigation_pattern = f'{prevention_pattern}, {mitigation_pattern}'
        prevention_and_mitigation_prompt_output = f'{prevention_prompt_output}\n\n{mitigation_prompt_output}'
        return prevention_and_mitigation_pattern, prevention_and_mitigation_prompt_output

    def create_condensed_confusion_matrix(self, confusion_matrix):
        classes_of_current_confusion_matrix = ['prevention, prevention', 'prevention, mitigation', 'prevention, both', 'prevention, neither', 'mitigation, prevention', 'mitigation, mitigation', 'mitigation, both', 'mitigation, neither', 'both, prevention', 'both, mitigation', 'both, both', 'both, neither', 'neither, prevention', 'neither, mitigation', 'neither, both', 'neither, neither']
        classes_of_condensed_confusion_matrix = ['prevention', 'mitigation', 'both', 'neither']

        n_current = len(classes_of_current_confusion_matrix)

        n_condensed = len(classes_of_condensed_confusion_matrix)
        condensed_confusion_matrix = np.zeros((n_condensed, n_condensed))

        for current_confusion_matrix_row_index in range(n_current):
            for current_confusion_matrix_col_index in range(n_current):
                prevention_input_predicted_class, mitigation_input_predicted_class = classes_of_current_confusion_matrix[current_confusion_matrix_row_index].split(', ')
                prevention_input_expected_class, mitigation_input_expected_class = classes_of_current_confusion_matrix[current_confusion_matrix_col_index].split(', ')

                ## Find the index of prevention_input_expected_class in classes_of_condensed_confusion_matrix
                prevention_input_expected_class_index = classes_of_condensed_confusion_matrix.index(prevention_input_expected_class)
                mitigation_input_expected_class_index = classes_of_condensed_confusion_matrix.index(mitigation_input_expected_class)

                prevention_input_predicted_class_index = classes_of_condensed_confusion_matrix.index(prevention_input_predicted_class)
                mitigation_input_predicted_class_index = classes_of_condensed_confusion_matrix.index(mitigation_input_predicted_class)

                condensed_confusion_matrix[prevention_input_predicted_class_index, prevention_input_expected_class_index] += confusion_matrix[current_confusion_matrix_row_index, current_confusion_matrix_col_index]
                condensed_confusion_matrix[mitigation_input_predicted_class_index, mitigation_input_expected_class_index] += confusion_matrix[current_confusion_matrix_row_index, current_confusion_matrix_col_index]
        
        return condensed_confusion_matrix
    
    def run_test(self):
        purpose_of_test, accuracy, faithfulness_accuracy, confusion_matrix, output_string, prompt_outputs_for_correct_responses, prompt_outputs_for_incorrect_responses, prompt_outputs_where_pattern_was_not_matched = self.get_model_accuracy_and_model_outputs()

        condensed_confusion_matrix = self.create_condensed_confusion_matrix(confusion_matrix)
        confusion_matrix_string = self.generate_confusion_matrix_string(condensed_confusion_matrix, classes=['prevention', 'mitigation', 'both', 'neither'])
        
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

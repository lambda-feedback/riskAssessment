# Builds on TestModelAccuracy class to test the accuracy of multiple prompts used in sequence, e.g. the HarmCausedAndHazardEvent and ControlMeasureClassification prompts.

from ..test_classes.TestModelAccuracy import TestModelAccuracy
from ..utils.LLMCaller import LLMCaller

class TestModelAccuracyForCombinationOfPrompts(TestModelAccuracy):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list,
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list,
                    domain: str = None,
                    is_first_test: bool = False):
        
        self.LLM = LLM
        self.list_of_risk_assessment_and_expected_outputs = list_of_risk_assessment_and_expected_outputs
        self.sheet_name = sheet_name
        self.examples_gathered_or_generated_message = examples_gathered_or_generated_message
        self.candidate_labels = candidate_labels
        self.domain = domain
        self.is_first_test = is_first_test

    # Defined in children classes below
    def get_pattern_matched_and_prompt_output(self, i):
        pass

    # Defined in children classes below
    def get_first_prompt_input(self):
        pass

    def get_classes(self):
        return self.candidate_labels
    
    def get_expected_output_and_input_object(self, example_index):
        expected_output = self.list_of_risk_assessment_and_expected_outputs[example_index].expected_output
        input_object = self.list_of_risk_assessment_and_expected_outputs[example_index].risk_assessment
        return expected_output, input_object
    
    def get_number_of_examples(self):
        return len(self.list_of_risk_assessment_and_expected_outputs)
    
    def update_output_string(self, output_string, i, pattern_matched, expected_output):
        result_dict = {'risk_assessment': self.list_of_risk_assessment_and_expected_outputs[i].risk_assessment.to_string(),
                'pattern_matched': pattern_matched, 
                'expected_output': expected_output}

        output_string += f'{i + 1}: {str(result_dict)}\n\n'

        return output_string
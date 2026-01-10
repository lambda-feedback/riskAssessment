# Builds on TestModelAccuracyForCombinationOfPrompts.py to test accuracy of control measure classification.

from ..test_classes.TestModelAccuracyForCombinationOfPrompts import TestModelAccuracyForCombinationOfPrompts
from ..utils.LLMCaller import LLMCaller

class TestControlMeasureClassificationPrompt(TestModelAccuracyForCombinationOfPrompts):
    def __init__(self, 
                    LLM: LLMCaller,
                    list_of_risk_assessment_and_expected_outputs: list,
                    sheet_name: str,
                    examples_gathered_or_generated_message: str,
                    candidate_labels: list,
                    domain: str = None,
                    is_first_test: bool = False):
        
        super().__init__(LLM, list_of_risk_assessment_and_expected_outputs, sheet_name, examples_gathered_or_generated_message, candidate_labels, domain=domain, is_first_test=is_first_test)
    
    def get_classes(self):
        return self.candidate_labels
    
    def get_hazard_event_and_harm_caused_and_prompt(self, RA):

        hazard_event_and_harm_caused_prompt_input = RA.get_harm_caused_and_hazard_event_input()
        hazard_event_and_harm_caused_prompt = hazard_event_and_harm_caused_prompt_input.generate_prompt()
        hazard_event_and_harm_caused_prompt_output, hazard_event_and_harm_caused_pattern = RA.get_prompt_output_and_pattern_matched(prompt_input_object=hazard_event_and_harm_caused_prompt_input, LLM_caller=self.LLM)

        hazard_event = hazard_event_and_harm_caused_pattern.hazard_event
        harm_caused = hazard_event_and_harm_caused_pattern.harm_caused

        return hazard_event, harm_caused, hazard_event_and_harm_caused_prompt, hazard_event_and_harm_caused_prompt_output
    
    def get_first_prompt_input_with_risk_assessment_method(self, risk_assessment_method_name):
        first_RA = self.list_of_risk_assessment_and_expected_outputs[0].risk_assessment

        hazard_event, harm_caused, hazard_event_and_harm_caused_prompt, _  = self.get_hazard_event_and_harm_caused_and_prompt(first_RA)

        if hazard_event == 'No pattern found' or harm_caused == 'No pattern found':
            return f'''Hazard Event/Harm Caused:\n{hazard_event_and_harm_caused_prompt}\n\n No pattern found for hazard event or harm caused in prompt output.'''
        
        else:
            control_measure_prompt_input = getattr(first_RA, risk_assessment_method_name)()
            control_measure_prompt = control_measure_prompt_input.generate_prompt(hazard_event=hazard_event, harm_caused=harm_caused)

            return f'''Hazard Event/Harm Caused:\n{hazard_event_and_harm_caused_prompt}\n\nControl Measure:\n{control_measure_prompt}'''
    
    def get_pattern_matched_and_prompt_output_with_risk_assessment_method(self, input_object, risk_assessment_method_name):

        hazard_event, harm_caused, _, hazard_event_and_harm_caused_prompt_output  = self.get_hazard_event_and_harm_caused_and_prompt(RA=input_object)

        if hazard_event == 'No pattern found' or harm_caused == 'No pattern found':
            return 'No pattern found', hazard_event_and_harm_caused_prompt_output

        control_measure_prompt_input = getattr(input_object, risk_assessment_method_name)()
        control_measure_prompt_output, control_measure_pattern = input_object.get_prompt_output_and_pattern_matched(prompt_input_object=control_measure_prompt_input, LLM_caller=self.LLM, harm_caused=harm_caused, hazard_event=hazard_event)

        if control_measure_pattern == 'No pattern found':
            return 'No pattern found', hazard_event_and_harm_caused_prompt_output

        prompt_output = f'''Hazard Event/Harm Caused:\n{hazard_event_and_harm_caused_prompt_output}\n\nControl Measure:\n{control_measure_prompt_output}'''

        return control_measure_pattern, prompt_output
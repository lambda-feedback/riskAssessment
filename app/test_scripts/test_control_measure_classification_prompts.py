# To run, enter in terminal: python -m app.test_scripts.test_control_measure_classification_prompts

# Script that tests the accuracy of control measure classification prompt and performs ablation study to see impact of few-shot and chain-of-thought prompting on accuracy.

from ..test_classes.TestBothPreventionAndMitigationInput import TestBothPreventionAndMitigationInput
from ..test_classes.TestPreventionInput__ControlMeasureClassifiationPrompt import TestPreventionInput__ControlMeasureClassifiationPrompt
from ..test_classes.TestMitigationInput__ControlMeasureClassifiationPrompt import TestMitigationInput__ControlMeasureClassifiationPrompt

from ..utils.LLMCaller import *
from ..data.example_risk_assessments import *

from ..test_utils.ExamplesGenerator import RiskAssessmentExamplesGeneratorForMultiplePrompts

control_measure_tests_dict = {
    ### BOTH PREVENTION AND MITIGATION
    'Both Prevention and Mitigation Input Few Shot COT': {
        'sheet_name': 'Testing Prevention and Mitigation', 
        'prevention_method_name': 'get_control_measure_prompt_with_prevention_input', 
        'mitigation_method_name': 'get_control_measure_prompt_with_mitigation_input'},

    'Both Prevention and Mitigation Input Few Shot No Cot': {
        'sheet_name': 'Testing Prevention and Mitigation Few Shot No COT', 
        'prevention_method_name': 'get_few_shot_no_chain_of_thought_control_measure_prompt_with_prevention_input', 
        'mitigation_method_name': 'get_few_shot_no_chain_of_thought_control_measure_prompt_with_mitigation_input'},

    'Both Prevention and Mitigation Input Zero Shot No COT': {
        'sheet_name': 'Testing Prevention and Mitigation Zero Shot No COT', 
        'prevention_method_name': 'get_zero_shot_no_chain_of_thought_control_measure_prompt_with_prevention_input', 
        'mitigation_method_name': 'get_zero_shot_no_chain_of_thought_control_measure_prompt_with_mitigation_input'},

    'Both Prevention and Mitigation Input Zero Shot COT': {
        'sheet_name': 'Testing Prevention and Mitigation Zero Shot COT', 
        'prevention_method_name': 'get_zero_shot_chain_of_thought_control_measure_prompt_with_prevention_input', 
        'mitigation_method_name': 'get_zero_shot_chain_of_thought_control_measure_prompt_with_mitigation_input'},

    ### PREVENTION ###
    'Prevention Input Few Shot COT': {
        'sheet_name': 'Combined Prevention Prompts', 
        'method_name': 'get_control_measure_prompt_with_prevention_input'},

    'Prevention Input Few Shot No Cot': {
        'sheet_name': 'Combined Prevention Prompts Few Shot No COT', 
        'method_name': 'get_few_shot_no_chain_of_thought_control_measure_prompt_with_prevention_input'},

    'Prevention Input Zero Shot No COT': {
        'sheet_name': 'Combined Prevention Prompts Zero Shot No COT', 
        'method_name': 'get_zero_shot_no_chain_of_thought_control_measure_prompt_with_prevention_input'},

    'Prevention Input Zero Shot COT': {
        'sheet_name': 'Combined Prevention Prompts Zero Shot COT', 
        'method_name': 'get_zero_shot_chain_of_thought_control_measure_prompt_with_prevention_input'},

    ### MITIGATION ###
    'Mitigation Input Few Shot COT': {
        'sheet_name': 'Combined Mitigation Prompts', 
        'method_name': 'get_control_measure_prompt_with_mitigation_input'},
    
    'Mitigation Input Few Shot No Cot': {
        'sheet_name': 'Combined Mitigation Prompts Few Shot No COT', 
        'method_name': 'get_few_shot_no_chain_of_thought_control_measure_prompt_with_mitigation_input'},

    'Mitigation Input Zero Shot No COT': {
        'sheet_name': 'Combined Mitigation Prompts Zero Shot No COT', 
        'method_name': 'get_zero_shot_no_chain_of_thought_control_measure_prompt_with_mitigation_input'},
    
    'Mitigation Input Zero Shot COT': {
        'sheet_name': 'Combined Mitigation Prompts Zero Shot COT', 
        'method_name': 'get_zero_shot_chain_of_thought_control_measure_prompt_with_mitigation_input'},
}

def test_prevention_combined_prompts(risk_assessments_dict, 
                                     LLM, 
                                     control_meausure_tests_dict_key,
                                     is_first_test: bool = False):
    
    risk_assessment_control_measure_prompt_with_prevention_input_method_name = control_measure_tests_dict[control_meausure_tests_dict_key]['method_name']
    sheet_name = control_measure_tests_dict[control_meausure_tests_dict_key]['sheet_name']

    risk_assessments = risk_assessments_dict['risk_assessments']
    examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=risk_assessments,
                                                          ground_truth_parameter='prevention_prompt_expected_class')
    
    examples = examples_generator.get_risk_assessment_and_expected_output_list()

    test_accuracy = TestPreventionInput__ControlMeasureClassifiationPrompt(
                                    LLM=LLM,
                                    is_first_test=is_first_test,
                                    domain=risk_assessments_dict['risk_domain'],       
                                    list_of_risk_assessment_and_expected_outputs=examples,
                                    examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                                    risk_assessment_control_measure_prompt_with_prevention_input_method_name=risk_assessment_control_measure_prompt_with_prevention_input_method_name,
                                    candidate_labels=['prevention', 'mitigation', 'neither', 'both'],
                                    sheet_name=sheet_name)

    test_accuracy.run_test()

def test_mitigation_combined_prompts(risk_assessments_dict, 
                                     LLM, 
                                     control_meausure_tests_dict_key,
                                     is_first_test: bool = False):
    
    risk_assessment_control_measure_prompt_with_mitigation_input_method_name = control_measure_tests_dict[control_meausure_tests_dict_key]['method_name']
    sheet_name = control_measure_tests_dict[control_meausure_tests_dict_key]['sheet_name']

    examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=risk_assessments_dict['risk_assessments'],
                                                          ground_truth_parameter='mitigation_prompt_expected_class')
    
    examples = examples_generator.get_risk_assessment_and_expected_output_list()

    test_accuracy = TestMitigationInput__ControlMeasureClassifiationPrompt(
                                    LLM=LLM,
                                    is_first_test=is_first_test,
                                    domain=risk_assessments_dict['risk_domain'],
                                    list_of_risk_assessment_and_expected_outputs=examples,
                                    examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                                    risk_assessment_control_measure_prompt_with_mitigation_input_method_name=risk_assessment_control_measure_prompt_with_mitigation_input_method_name,
                                    candidate_labels=['prevention', 'mitigation', 'neither', 'both'],
                                    sheet_name=sheet_name)
    
    test_accuracy.run_test()

def test_both_prevention_and_mitigation_inputs(risk_assessments_dict, 
                                               LLM, 
                                               control_meausure_tests_dict_key,
                                               is_first_test: bool = False):
    
    risk_assessment_control_measure_prompt_with_prevention_input_method_name = control_measure_tests_dict[control_meausure_tests_dict_key]['prevention_method_name']
    risk_assessment_control_measure_prompt_with_mitigation_input_method_name = control_measure_tests_dict[control_meausure_tests_dict_key]['mitigation_method_name']
    
    sheet_name = control_measure_tests_dict[control_meausure_tests_dict_key]['sheet_name']

    examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=risk_assessments_dict['risk_assessments'],
                                                          ground_truth_parameter='prevention_and_mitigation_expected_class_combined')
    
    examples = examples_generator.get_risk_assessment_and_expected_output_list()

    test_accuracy = TestBothPreventionAndMitigationInput(
                                    LLM=LLM,
                                    is_first_test=is_first_test,
                                    domain=risk_assessments_dict['risk_domain'],
                                    list_of_risk_assessment_and_expected_outputs=examples,
                                    risk_assessment_control_measure_prompt_with_prevention_input_method_name=risk_assessment_control_measure_prompt_with_prevention_input_method_name,
                                    risk_assessment_control_measure_prompt_with_mitigation_input_method_name=risk_assessment_control_measure_prompt_with_mitigation_input_method_name,
                                    examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                                    candidate_labels=['prevention, prevention', 'prevention, mitigation', 'prevention, both', 'prevention, neither', 'mitigation, prevention', 'mitigation, mitigation', 'mitigation, both', 'mitigation, neither', 'both, prevention', 'both, mitigation', 'both, both', 'both, neither', 'neither, prevention', 'neither, mitigation', 'neither, both', 'neither, neither'],
                                    sheet_name=sheet_name)
    
    test_accuracy.run_test()

def run_control_measure_tests_for_one_LLM_with_certain_prompt_techniques(
        LLM: LLMCaller,
        prompt_techniques: str):
    
    test_both_prevention_and_mitigation_inputs(
        risk_assessments_dict=physical_risks_to_individuals__data_gathered_from_version_1_deployment,
        LLM=LLM,
        is_first_test=False,
        control_meausure_tests_dict_key=f'Both Prevention and Mitigation Input {prompt_techniques}'
    )

    # test_both_prevention_and_mitigation_inputs(
    #     risk_assessments_dict=cybersecurity_risks,
    #     LLM=LLM,
    #     is_first_test=False,
    #     control_meausure_tests_dict_key=f'Both Prevention and Mitigation Input {prompt_techniques}'
    # )

    # test_both_prevention_and_mitigation_inputs(
    #     risk_assessments_dict=terrorism_risks,
    #     LLM=LLM,
    #     is_first_test=False,
    #     control_meausure_tests_dict_key=f'Both Prevention and Mitigation Input {prompt_techniques}'
    # )
    
    # test_prevention_combined_prompts(
    #     risk_assessments_dict=biohazard_risks,
    #     LLM=LLM,
    #     is_first_test=False,
    #     control_meausure_tests_dict_key=f'Prevention Input {prompt_techniques}'
    # )

    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=biohazard_risks,
    #     LLM=LLM,
    #     is_first_test=False,
    #     control_meausure_tests_dict_key=f'Mitigation Input {prompt_techniques}'
    # )

    # test_prevention_combined_prompts(
    #     risk_assessments_dict=natural_disaster_risks,
    #     LLM=LLM,
    #     is_first_test=False,
    #     control_meausure_tests_dict_key=f'Prevention Input {prompt_techniques}'
    # )

    # test_mitigation_combined_prompts(
    #     risk_assessments_dict=natural_disaster_risks,
    #     LLM=LLM,
    #     is_first_test=False,
    #     control_meausure_tests_dict_key=f'Mitigation Input {prompt_techniques}'
    # )

def run_control_measure_tests_for_one_LLM_for_all_prompt_technique_combinations(LLM: LLMCaller):
    for prompt_techniques in [
        'Few Shot COT', 
        # 'Few Shot No Cot', 
        # 'Zero Shot No COT', 
        # 'Zero Shot COT'
        ]:

        run_control_measure_tests_for_one_LLM_with_certain_prompt_techniques(
            LLM=LLM,
            prompt_techniques=prompt_techniques
        )

if __name__ == '__main__':
    # run_control_measure_tests_for_one_LLM_for_all_prompt_technique_combinations(LLM=Mixtral8x7B(temperature=0.1))
    # run_control_measure_tests_for_one_LLM_for_all_prompt_technique_combinations(LLM=Mixtral8x22B(temperature=0.1))
    # run_control_measure_tests_for_one_LLM_for_all_prompt_technique_combinations(LLM=MistralLarge(temperature=0.1))
    # run_control_measure_tests_for_one_LLM_for_all_prompt_technique_combinations(LLM=GPT_3_point_5_turbo(temperature=0.1))
    # run_control_measure_tests_for_one_LLM_for_all_prompt_technique_combinations(LLM=ClaudeSonnetLLM(system_message='', temperature=0.1))
    run_control_measure_tests_for_one_LLM_for_all_prompt_technique_combinations(LLM=GPT_4_turbo(temperature=0.1))
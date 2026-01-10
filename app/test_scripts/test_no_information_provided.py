# Script which tests the accuracy of the NoInformationProvided.py prompt

# To run, enter in terminal: python -m app.test_scripts.test_no_information_provided

from ..test_utils.InputAndExpectedOutput import InputAndExpectedOutputForSinglePrompt
from ..utils.LLMCaller import *
from ..prompts.NoInformationProvided import NoInformationProvided
from ..test_classes.TestModelAccuracy import TestModelAccuracy
from ..data.example_risk_assessments import *

no_information_provided_examples = [
    "Leave blank",
    "No data",
    "Not provided",
    "Not applicable at this time",
    "Not applicable to me",
    "Not applicable in this context",
    "Nil",
    "Blank",
    "Unspecified",
    "No content",
]

information_provided_examples = [
    # Prevention
    "Using safe climbing techniques",
    "Maintaining safe distance in traffic",
    
    # # Mitigation
    "Using proper climbing gear",
    "Wearing a helmet while biking",
]


def test_no_information_provided_prompt(risk_assessments, LLM, is_first_test: bool = False):
    examples = []

    for example in no_information_provided_examples:
        examples.append(InputAndExpectedOutputForSinglePrompt(prompt_input_object=NoInformationProvided(input=example), expected_output='no information provided'))

    for example in information_provided_examples:
        examples.append(InputAndExpectedOutputForSinglePrompt(prompt_input_object=NoInformationProvided(input=example), expected_output='control measure'))

    unique_control_measures_in_risk_domain = create_unique_set_of_control_measures(risk_assessments)
    
    for control_measure in unique_control_measures_in_risk_domain:
        examples.append(InputAndExpectedOutputForSinglePrompt(prompt_input_object=NoInformationProvided(input=control_measure), expected_output='control measure'))

    test_accuracy = TestModelAccuracy(
                        LLM=LLM,
                        is_first_test=is_first_test,
                        domain='Laboratory risks',       
                        list_of_input_and_expected_outputs=examples,
                        examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                        sheet_name='No Information Provided')
    
    test_accuracy.run_test()

if __name__ == "__main__":
    laboratory_risk_assessments = physical_risks_to_individuals__data_gathered_from_version_1_deployment['risk_assessments'] + physical_risks_to_individuals__original_student_data['risk_assessments']

    temperature = 0.1
    # test_no_information_provided_prompt(risk_assessments=laboratory_risk_assessments
    #                                 , LLM=GPT_3_point_5_turbo(temperature=temperature)
    #                                 , is_first_test=True)
    test_no_information_provided_prompt(risk_assessments=laboratory_risk_assessments
                                    , LLM=MistralLarge(temperature=temperature)
                                    , is_first_test=False)
    # test_no_information_provided_prompt(risk_assessments=laboratory_risk_assessments
    #                                 , LLM=Mixtral8x22B(temperature=temperature)
    #                                 , is_first_test=False)
    # test_no_information_provided_prompt(risk_assessments=laboratory_risk_assessments
    #                                 , LLM=Mixtral8x7B(temperature=temperature)
    #                                 , is_first_test=False)
    # test_no_information_provided_prompt(risk_assessments=laboratory_risk_assessments
    #                                 , LLM=ClaudeSonnetLLM(system_message="", temperature=temperature)
    #                                 , is_first_test=False)
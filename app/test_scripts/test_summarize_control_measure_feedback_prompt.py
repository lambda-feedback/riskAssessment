# To run, enter in terminal: python -m app.test_scripts.test_summarize_control_measure_feedback_prompt

from ..utils.LLMCaller import *
from ..test_classes.TestSummarizeControlMeasureFeedback import TestSummarizePreventionFeedback, TestSummarizeMitigationFeedback
from ..data.example_risk_assessments import cybersecurity_risks
from ..test_utils.ExamplesGenerator import RiskAssessmentExamplesGeneratorForMultiplePrompts

def test_summarize_prevention_feedback_prompt(risk_assessments_dict, LLM, is_first_test: bool = False):
    risk_assessments = risk_assessments_dict['risk_assessments']
    examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=risk_assessments,
                                                          ground_truth_parameter='always_true')
    
    examples = examples_generator.get_risk_assessment_and_expected_output_list()

    test_accuracy = TestSummarizePreventionFeedback(
                        LLM=LLM,
                        is_first_test=is_first_test,
                        domain=risk_assessments_dict['risk_domain'],       
                        list_of_risk_assessment_and_expected_outputs=examples,
                        examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                        sheet_name='Summarize Feedback',
                        candidate_labels=[True, False]
                        )
    
    test_accuracy.run_test()

def test_summarize_mitigation_feedback_prompt(risk_assessments_dict, LLM, is_first_test: bool = False):
    risk_assessments = risk_assessments_dict['risk_assessments']
    examples_generator = RiskAssessmentExamplesGeneratorForMultiplePrompts(risk_assessments=risk_assessments,
                                                          ground_truth_parameter='always_true')
    
    examples = examples_generator.get_risk_assessment_and_expected_output_list()

    test_accuracy = TestSummarizeMitigationFeedback(
                        LLM=LLM,
                        is_first_test=is_first_test,
                        domain=risk_assessments_dict['risk_domain'],       
                        list_of_risk_assessment_and_expected_outputs=examples,
                        examples_gathered_or_generated_message='Risk assessments gathered and not AI-generated',
                        sheet_name='Summarize Feedback',
                        candidate_labels=[True, False]
                        )
    
    test_accuracy.run_test()

if __name__ == "__main__":
    test_summarize_prevention_feedback_prompt(risk_assessments_dict=cybersecurity_risks
                                    , LLM=MistralLarge(temperature=0.1)
                                    , is_first_test=True)
    
    # test_summarize_mitigation_feedback_prompt(risk_assessments_dict=cybersecurity_risks
    #                                 , LLM=ClaudeSonnetLLM(system_message='', temperature=0.1)
    #                                 , is_first_test=True)

    
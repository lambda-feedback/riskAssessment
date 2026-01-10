# Low hanging fruit:
# TODO: Improve few shot prompting examples so they don't parrot back input prompt
# TODO: Try using chain of thought prompt engineering for the mitigation prompt
# TODO: Try using Llama inference endpoint
# TODO: Try using Llama inference API but specify the number of tokens you want to receive
# TODO: Update question description in lambda feedback making it clear that 
# only one mitigation, one prevention and one 'how it harms' is specified

# Add option in RiskAssessment to specify whether prevention is misclassified as mitigation, 
# is not a suitable prevention, or mitigation is misclassified as prevention, or is not a suitable mitigation

import numpy as np
from typing import Type, Any, TypedDict

from .prompts.BasePromptInput import *
from .data.RiskAssessment import RiskAssessment
from .utils.LLMCaller import *

# TODO: Functions can make this code shorter.

class Result(TypedDict):
    is_correct: bool
    feedback: str

class Params(TypedDict):
    is_feedback_text: bool
    is_risk_matrix: bool
    is_risk_assessment: bool
    LLM: str

def provide_feedback_on_risk_matrix(response):
    risk_matrix = np.array(response)

    risk_matrix_flattened = np.array(response).flatten()
    for value in risk_matrix_flattened:
        if value == '':
            return Result(is_correct=False, feedback="Please fill in all the fields")
        else:
            try:
                int_value = int(value)
            except ValueError:
                return Result(is_correct=False, feedback="Please enter an integer for all fields.")

    risk_matrix_dict = {'uncontrolled likelihood': int(risk_matrix[0, 0]),
                'uncontrolled severity': int(risk_matrix[0, 1]),
                'controlled likelihood': int(risk_matrix[1, 0]), 
                'controlled severity': int(risk_matrix[1, 1])}

    is_correct = True
    feedback = f''''''

    for key in risk_matrix_dict.keys():
        if risk_matrix_dict[key] > 4 or risk_matrix_dict[key] < 1:
            is_correct = False
            feedback += f'''\n\n\n\n\n##### The {key} is incorrect. As per the likelihood and severity conventions above, the likelihood and severity should be between 1 and 4.\n\n\n\n'''

    uncontrolled_likelihood = risk_matrix_dict['uncontrolled likelihood']
    uncontrolled_severity = risk_matrix_dict['uncontrolled severity']
    uncontrolled_risk = int(risk_matrix[0, 2])
    controlled_likelihood = risk_matrix_dict['controlled likelihood']
    controlled_severity = risk_matrix_dict['controlled severity']
    controlled_risk = int(risk_matrix[1, 2])

    feedback += '\n'

    # Comparing Uncontrolled and Controlled Rows
            
    # Likelihoods
    if is_correct == True: # Only write feedback if all previous checks have passed
        if uncontrolled_likelihood <= controlled_likelihood:
            feedback += f'''\n\n\n\n\n##### Likelihood values are incorrect. Since an effective prevention measure has been implemented ("taking care when cross the road"), the controlled likelihood should be less than the uncontrolled likelihood.\n\n\n\n'''
            is_correct = False

    # Severities
    if is_correct == True: # Only write feedback if all previous checks have passed
        if uncontrolled_severity != controlled_severity:
            feedback += f'''\n\n\n\n\n##### Severity values are incorrect. The uncontrolled and controlled severity should be the same since no mitigation measure has been implemented.\n\n\n\n''' 
            is_correct = False

    # --- Checking Uncontrolled Row ---
    
    # Likelihoods
    if is_correct == True: # Only write feedback if all previous checks have passed
        if uncontrolled_likelihood != 4:
            feedback += f'''\n\n\n\n\n##### An uncontrolled likelihood of {uncontrolled_likelihood} is incorrect. The convention is that all uncontrolled risks have a likelihood of 4. If you didn't look or listen when crossing the road, you would almost certainly be harmed.\n\n\n\n'''
            is_correct = False

    # Severities
    if is_correct == True:
        if uncontrolled_severity == 1:
            feedback += f'''\n\n\n\n\n##### An uncontrolled severity of 1 is incorrect. As by the above severity convention, a severity of 1 indicates that a car crashing into a pedestrian causes "minor injury or property damage". The harm will be greater than this.\n\n\n\n''' 
            is_correct = False

    # Multiplications
    if is_correct == True: # Only write feedback if all previous checks have passed
        if uncontrolled_likelihood * uncontrolled_severity != uncontrolled_risk:
            feedback += f'''\n\n\n\n\n##### Uncontrolled risk multiplication is incorrect. Make sure the risk is the likelihood multiplied by the severity.\n\n\n\n'''
            is_correct = False

    # --- Checking Controlled Row ---
            
    # Likelihoods
    if is_correct == True: # Only write feedback if all previous checks have passed
        if controlled_likelihood == 1:
            feedback += f'''\n\n\n\n\n##### A controlled likelihood of 1 is incorrect. A controlled likelihood of 1 indicates that the control measure is implemented passively whereas you have to activily pay attention when cross the road.\n\n\n\n'''
            is_correct = False

        if controlled_likelihood == 2:
            feedback += f'''\n\n\n\n\n##### Correct controlled likelihood. A controlled likelihood of 2 indicates that the control measure of "taking care when crossing the road" is implemented actively.\n\n\n\n''' 
        
        if controlled_likelihood == 3:
            feedback += f'''\n\n\n\n\n##### A controlled likelihood of 3 is incorrect. A controlled likelihood of 3 indicates that the control measure is not effective and the likelihood is "possible".\n\n\n\n''' 
            is_correct = False
        
        if controlled_likelihood == 4:
            feedback += f'''\n\n\n\n\n##### A controlled likelihood of 4 is incorrect. A controlled likelihood of 4 indicates that the control measure is effective and the likelihood is "likely".\n\n\n\n''' 
            is_correct = False

    # Severities
    if is_correct == True: # Only write feedback if all previous checks have passed
        if controlled_severity == 1:
            feedback += f'''\n\n\n\n\n##### A controlled severity of 1 is incorrect. As by the above severity convention, a severity of 1 indicates that a car crashing into a pedestrian causes "minor injury or property damage". The harm will be greater than this.\n\n\n\n''' 
            is_correct = False

    # Multiplications
    if is_correct == True: # Only write feedback if all previous checks have passed
        if controlled_likelihood * controlled_severity != controlled_risk:
            feedback += f'''\n\n\n\n\n##### Controlled risk multiplication is incorrect. Make sure the risk is the likelihood multiplied by the severity.\n\n\n\n'''
            is_correct = False

    return Result(is_correct=is_correct, feedback=feedback)

def provide_feedback_on_control_measure_input(control_measure_input_field: str,
                                              control_measure_prompt_input: Type[BasePromptInput],
                                              control_measure_prompt_output: str,
                                              control_measure_prompt_pattern: str,
                                              feedback_for_correct_answers: str,
                                              feedback_for_incorrect_answers: str,
                                              is_everything_correct: bool,
                                              risk_assessment: RiskAssessment,
                                              LLM_caller: Type[LLMCaller]):
    
    prevention_prompt_feedback = control_measure_prompt_input.get_longform_feedback(prompt_output=control_measure_prompt_output, start_string='Prevention Explanation', end_string='Mitigation Explanation')
    mitigation_prompt_feedback = control_measure_prompt_input.get_longform_feedback(prompt_output=control_measure_prompt_output, start_string='Mitigation Explanation', end_string='Answer')

    if control_measure_input_field == 'prevention':
        other_control_measure_input_field = 'mitigation'
        control_measure_prompt_feedback = prevention_prompt_feedback
        other_control_measure_prompt_feedback = mitigation_prompt_feedback

    if control_measure_input_field == 'mitigation':
        other_control_measure_input_field = 'prevention'
        control_measure_prompt_feedback = mitigation_prompt_feedback
        other_control_measure_prompt_feedback = prevention_prompt_feedback
    
    feedback_header = f'\n\n\n\n\n## Feedback for Input: {control_measure_input_field.capitalize()}\n\n\n\n'
    
    if control_measure_prompt_pattern == 'both':
        prompt_input_for_summarizing_control_measure_prompt_feedback = risk_assessment.get_feedback_summary_input()
        summary_of_control_measure_prompt_feedback, _ = risk_assessment.get_prompt_output_and_pattern_matched(prompt_input_object=prompt_input_for_summarizing_control_measure_prompt_feedback, LLM_caller=LLM_caller, control_measure_type=control_measure_input_field, feedback=control_measure_prompt_feedback)
        summary_of_other_control_measure_prompt_feedback, _ = risk_assessment.get_prompt_output_and_pattern_matched(prompt_input_object=prompt_input_for_summarizing_control_measure_prompt_feedback, LLM_caller=LLM_caller, control_measure_type=other_control_measure_input_field, feedback=other_control_measure_prompt_feedback)

        feedback_for_correct_answers += f'''
        {feedback_header}
        \n\n\n\n#### Feedback: {control_measure_prompt_input.get_shortform_feedback('both')}\n\n\n\n
        #### {control_measure_input_field.capitalize()} Explanation: {summary_of_control_measure_prompt_feedback}\n\n\n\n
        #### {other_control_measure_input_field.capitalize()} Explanation: {summary_of_other_control_measure_prompt_feedback}\n\n\n\n'''

    if control_measure_prompt_pattern == control_measure_input_field:
        prompt_input_for_summarizing_control_measure_prompt_feedback = risk_assessment.get_feedback_summary_input()
        summary_of_control_measure_prompt_feedback, _ = risk_assessment.get_prompt_output_and_pattern_matched(prompt_input_object=prompt_input_for_summarizing_control_measure_prompt_feedback, LLM_caller=LLM_caller, control_measure_type=control_measure_input_field, feedback=control_measure_prompt_feedback)

        feedback_for_correct_answers += f'''
        {feedback_header}
        \n\n\n\n#### Explanation: {summary_of_control_measure_prompt_feedback}\n\n\n\n'''

    if control_measure_prompt_pattern == 'neither':
        prompt_input_for_summarizing_control_measure_prompt_feedback = risk_assessment.get_feedback_summary_input()
        summary_of_control_measure_prompt_feedback, _ = risk_assessment.get_prompt_output_and_pattern_matched(prompt_input_object=prompt_input_for_summarizing_control_measure_prompt_feedback, LLM_caller=LLM_caller, control_measure_type=control_measure_input_field, feedback=control_measure_prompt_feedback)

        recommendation = control_measure_prompt_input.get_recommendation(recommendation_type='neither')
        feedback_for_incorrect_answers += f'''
        {feedback_header}
        \n\n\n\n#### Explanation: {summary_of_control_measure_prompt_feedback}\n\n\n\n
        \n\n\n\n#### Recommendation: {recommendation}\n\n\n\n'''

        is_everything_correct = False

    if control_measure_prompt_pattern == other_control_measure_input_field:
        prompt_input_for_summarizing_control_measure_prompt_feedback = risk_assessment.get_feedback_summary_input()
        summary_of_other_control_measure_prompt_feedback, _ = risk_assessment.get_prompt_output_and_pattern_matched(prompt_input_object=prompt_input_for_summarizing_control_measure_prompt_feedback, LLM_caller=LLM_caller, control_measure_type=other_control_measure_input_field, feedback=other_control_measure_prompt_feedback)

        recommendation = control_measure_prompt_input.get_recommendation(recommendation_type='misclassification')
        feedback_for_incorrect_answers += f'''
        {feedback_header}
        \n\n\n\n#### Feedback: {control_measure_prompt_input.get_shortform_feedback('misclassification')}\n\n\n\n
        \n\n\n\n#### Explanation: {summary_of_other_control_measure_prompt_feedback}\n\n\n\n
        \n\n\n\n#### Recommendation: {recommendation}\n\n\n\n'''

        is_everything_correct = False

    return feedback_for_correct_answers, feedback_for_incorrect_answers, is_everything_correct

def evaluation_function(response: Any, answer: Any, params: Params) -> Result:
    """
    Function used to evaluate a student response.
    ---
    The handler function passes three arguments to evaluation_function():

    - `response` which are the answers provided by the student.
    - `answer` which are the correct answers to compare against.
    - `params` which are any extra parameters that may be useful,
        e.g., error tolerances.

    The output of this function is what is returned as the API response
    and therefore must be JSON-encodable. It must also conform to the
    response schema.

    Any standard python library may be used, as well as any package
    available on pip (provided it is added to requirements.txt).

    The way you wish to structure you code (all in this function, or
    split into many) is entirely up to you. All that matters are the
    return types and that evaluation_function() is the main function used
    to output the evaluation response.

    """

    if params["is_feedback_text"] == True:
        return Result(is_correct=True, feedback="Thank you for your feedback")
    
    if params["is_risk_matrix"] == True:
        return provide_feedback_on_risk_matrix(response)
    
    if params['is_risk_assessment'] == True:
        LLM_name = params["LLM"]
        LLM = LLM_dictionary[LLM_name]
    
        activity, hazard, how_it_harms, who_it_harms, uncontrolled_likelihood, uncontrolled_severity, uncontrolled_risk, prevention, mitigation, controlled_likelihood, controlled_severity, controlled_risk = np.array(response).flatten()

        RA = RiskAssessment(activity=activity, hazard=hazard, who_it_harms=who_it_harms, how_it_harms=how_it_harms,
                            uncontrolled_likelihood=uncontrolled_likelihood, uncontrolled_severity=uncontrolled_severity,
                            uncontrolled_risk=uncontrolled_risk, prevention=prevention, mitigation=mitigation,
                            controlled_likelihood=controlled_likelihood, controlled_severity=controlled_severity, controlled_risk=controlled_risk,
                            prevention_prompt_expected_class='prevention', mitigation_prompt_expected_class='mitigation', risk_domain='')

        input_check_feedback_message = RA.get_input_check_feedback_message()

        if input_check_feedback_message != True:
            return Result(is_correct=False,
                        feedback=f'''\n\n\n\n\n # Feedback:\n\n\n\n\n
                                    \n\n\n\n\n## {input_check_feedback_message}\n\n\n\n\n''')
        
        likelihood_severity_risk_feedback_message = RA.get_likelihood_severity_risk_feedback_message()

        if likelihood_severity_risk_feedback_message != True:
            return Result(is_correct=False,
                        feedback=f'''\n\n\n\n\n # Feedback:\n\n\n\n\n
                                    \n\n\n\n\n## {likelihood_severity_risk_feedback_message}\n\n\n\n\n''')

        feedback_for_incorrect_answers = '\n\n\n\n# Feedback for Incorrect Answers\n\n\n\n'
        feedback_for_correct_answers = '\n\n\n\n# Feedback for Correct Answers\n\n\n\n'

        fields_for_which_no_information_provided = []

        is_everything_correct = True

        how_it_harms_in_context_prompt_input = RA.get_how_it_harms_in_context_input()
        who_it_harms_in_context_prompt_input = RA.get_who_it_harms_in_context_input()

        first_2_prompt_input_objects = [how_it_harms_in_context_prompt_input, who_it_harms_in_context_prompt_input]
        
        for prompt_input_object in first_2_prompt_input_objects:
            if is_everything_correct == True:
                prompt_output, pattern = RA.get_prompt_output_and_pattern_matched(prompt_input_object=prompt_input_object, LLM_caller=LLM)
                shortform_feedback = RA.get_shortform_feedback_from_regex_match(prompt_input_object, pattern)

                field = prompt_input_object.get_field_checked()

                if pattern not in prompt_input_object.labels_indicating_correct_input:
                    feedback_header = f''' 
                    \n\n\n## Feedback for Input: {field}\n\n\n
                    '''
                    
                    feedback = f'''
                    \n\n\n\n#### Feedback: {shortform_feedback}\n\n\n\n'''

                    longform_feedback = prompt_input_object.get_longform_feedback(prompt_output=prompt_output)
                    
                    if longform_feedback != '':
                        feedback += f'''\n\n\n\n#### Explanation: {longform_feedback}\n\n\n\n'''
                    
                    is_everything_correct = False
                    recommendation = prompt_input_object.get_recommendation()

                    feedback += f'''\n\n\n\n#### Recommendation: {recommendation}'''

                    feedback_for_incorrect_answers += feedback_header
                    feedback_for_incorrect_answers += feedback

                    return Result(is_correct=is_everything_correct, feedback=feedback_for_incorrect_answers)

        # PREVENTION CHECKS
        no_information_provided_for_prevention_prompt_input = RA.get_no_information_provided_for_prevention_input()
        no_information_provided_for_prevention_prompt_output, no_information_provided_for_prevention_pattern = RA.get_prompt_output_and_pattern_matched(prompt_input_object=no_information_provided_for_prevention_prompt_input, LLM_caller=LLM)

        if no_information_provided_for_prevention_pattern == 'no information provided' or RA.prevention == '':
            fields_for_which_no_information_provided.append('Prevention')
        
        else:
            # TODO: Avoid duplication of the following code:
            harm_caused_and_hazard_event_prompt_input = RA.get_harm_caused_and_hazard_event_input()
            harm_caused_and_hazard_event_prompt_output, harm_caused_and_hazard_event_pattern = RA.get_prompt_output_and_pattern_matched(prompt_input_object=harm_caused_and_hazard_event_prompt_input, LLM_caller=LLM)

            hazard_event = harm_caused_and_hazard_event_pattern.hazard_event
            harm_caused = harm_caused_and_hazard_event_pattern.harm_caused

            control_measure_prompt_with_prevention_input = RA.get_control_measure_prompt_with_prevention_input()
            control_measure_prompt_with_prevention_output, control_measure_prompt_with_prevention_pattern = RA.get_prompt_output_and_pattern_matched(prompt_input_object=control_measure_prompt_with_prevention_input, 
                                                                                                                                                     LLM_caller=LLM,
                                                                                                                                                     harm_caused=harm_caused, 
                                                                                                                                                     hazard_event=hazard_event)

            feedback_for_correct_answers, feedback_for_incorrect_answers, is_everything_correct = provide_feedback_on_control_measure_input(
                control_measure_input_field='prevention',
                control_measure_prompt_input=control_measure_prompt_with_prevention_input,
                control_measure_prompt_output=control_measure_prompt_with_prevention_output,
                control_measure_prompt_pattern=control_measure_prompt_with_prevention_pattern,
                feedback_for_correct_answers=feedback_for_correct_answers,
                feedback_for_incorrect_answers=feedback_for_incorrect_answers,
                is_everything_correct=is_everything_correct,
                risk_assessment=RA,
                LLM_caller=LLM
            )

        # MITIGATION CHECKS
        no_information_provided_for_mitigation_prompt_input = RA.get_no_information_provided_for_mitigation_input()
        no_information_provided_for_mitigation_prompt_output, no_information_provided_for_mitigation_pattern = RA.get_prompt_output_and_pattern_matched(prompt_input_object=no_information_provided_for_mitigation_prompt_input, LLM_caller=LLM)

        if no_information_provided_for_mitigation_pattern == 'no information provided' or RA.mitigation == '':
            fields_for_which_no_information_provided.append('Mitigation')
        else:
            # If harm_caused and hazard_event have not already been extracted.
            if no_information_provided_for_prevention_pattern == 'no information provided':

                harm_caused_and_hazard_event_prompt_input = RA.get_harm_caused_and_hazard_event_input()
                harm_caused_and_hazard_event_prompt_output, harm_caused_and_hazard_event_pattern = RA.get_prompt_output_and_pattern_matched(prompt_input_object=harm_caused_and_hazard_event_prompt_input, LLM_caller=LLM)

                hazard_event = harm_caused_and_hazard_event_pattern.hazard_event
                harm_caused = harm_caused_and_hazard_event_pattern.harm_caused
            
            control_measure_prompt_with_mitigation_input = RA.get_control_measure_prompt_with_mitigation_input()
            control_measure_prompt_with_mitigation_output, control_measure_prompt_with_mitigation_pattern = RA.get_prompt_output_and_pattern_matched(prompt_input_object=control_measure_prompt_with_mitigation_input, 
                                                                                                                                                     LLM_caller=LLM, 
                                                                                                                                                     harm_caused=harm_caused, 
                                                                                                                                                     hazard_event=hazard_event)
            
            feedback_for_correct_answers, feedback_for_incorrect_answers, is_everything_correct = provide_feedback_on_control_measure_input(
                control_measure_input_field='mitigation',
                control_measure_prompt_input=control_measure_prompt_with_mitigation_input,
                control_measure_prompt_output=control_measure_prompt_with_mitigation_output,
                control_measure_prompt_pattern=control_measure_prompt_with_mitigation_pattern,
                feedback_for_correct_answers=feedback_for_correct_answers,
                feedback_for_incorrect_answers=feedback_for_incorrect_answers,
                is_everything_correct=is_everything_correct,
                risk_assessment=RA,
                LLM_caller=LLM
            )

        if is_everything_correct == True:
            feedback_for_incorrect_answers = '# Congratulations! All your answers are correct!'
        
        if fields_for_which_no_information_provided == []:
            no_information_provided_message = ''
        else:
            no_information_provided_message = f'\n\n\n\n\n## Fields for which no information is provided and hence no feedback given: {", ".join(fields_for_which_no_information_provided)}\n\n\n\n\n'

        if fields_for_which_no_information_provided != ['Prevention', 'Mitigation']:
            hazard_event_and_harm_caused_inferred_message = f'''## The following were inferred from your answers: \n\n\n\n\n
            \n\n\n\n\n### Event that leads to harm: "{hazard_event}"\n\n\n\n\n
            \n\n\n\n\n### Harm caused to '{RA.who_it_harms}': "{harm_caused}".\n\n\n\n
            \n\n\n\n\n### If they are incorrect, please make these more explicit in the "Hazard" and "How it harms" fields.\n\n\n\n\n'''
        else:
            hazard_event_and_harm_caused_inferred_message = ''
        
        feedback_for_correct_answers += f'''
        \n\n\n\n### There are no errors in your likelihood, severity, and risk values.\n\n\n\n'''

        feedback=f'''{hazard_event_and_harm_caused_inferred_message} \n\n\n\n\n
        {feedback_for_incorrect_answers} \n\n\n\n\n
        {feedback_for_correct_answers} \n\n\n\n\n
        {no_information_provided_message}'''

        return Result(is_correct=is_everything_correct, feedback=feedback)
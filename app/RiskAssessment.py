from typing import Type
import csv


try:
    from .PromptInputs import *
    from .LLMCaller import *
    from .RegexPatternMatcher import RegexPatternMatcher
except ImportError:
    from PromptInputs import *
    from LLMCaller import *
    from RegexPatternMatcher import RegexPatternMatcher

class RiskAssessment:
    def __init__(self, activity, hazard, who_it_harms, how_it_harms,
                  uncontrolled_likelihood, uncontrolled_severity, uncontrolled_risk,
                 prevention, mitigation, controlled_likelihood, controlled_severity, controlled_risk,
                 is_prevention_correct, is_mitigation_correct):
        self.activity = activity
        self.hazard = hazard
        self.who_it_harms = who_it_harms
        self.how_it_harms = how_it_harms
        self.uncontrolled_likelihood = uncontrolled_likelihood
        self.uncontrolled_severity = uncontrolled_severity
        self.uncontrolled_risk = uncontrolled_risk
        self.prevention = prevention
        self.mitigation = mitigation
        self.controlled_likelihood = controlled_likelihood
        self.controlled_severity = controlled_severity
        self.controlled_risk = controlled_risk

        self.is_prevention_correct = is_prevention_correct
        self.is_mitigation_correct = is_mitigation_correct

    def get_word_fields(self):
        return ['activity',
                'hazard',
                'who_it_harms',
                'how_it_harms',
                'prevention',
                'mitigation']
    
    def get_integer_fields(self):
        return ['uncontrolled_likelihood',
                'uncontrolled_severity',
                'uncontrolled_risk',
                'controlled_likelihood',
                'controlled_severity',
                'controlled_risk']
    
    def get_empty_fields(self):
        empty_fields = []

        for field_name in self.get_word_fields() + self.get_integer_fields():
            if getattr(self, field_name) == '':
                empty_fields.append(field_name)
        
        return empty_fields
        
    def does_string_represent_an_integer(self, string:str):
        try:
            int(string)
            return True
        except ValueError:
            return False
        
    def does_string_represent_words(self, string:str):
        if len(string.split(' ')) > 1: # If there are multiple words, unlikely to represent a number
            return True
        else:
            return string.isalpha() # If there is only one word, check if it is a word and not a number
        
    def get_word_fields_incorrect(self):
        word_fields_incorrect = []

        for word_field_name in self.get_word_fields():
            if not self.does_string_represent_words(getattr(self, word_field_name)):
                word_fields_incorrect.append(word_field_name)
        
        return word_fields_incorrect
    
    def get_integer_fields_incorrect(self):
        integer_fields_incorrect = []

        for integer_field_name in self.get_integer_fields():
            if not self.does_string_represent_an_integer(getattr(self, integer_field_name)):
                integer_fields_incorrect.append(integer_field_name)
        
        return integer_fields_incorrect
    
    def get_input_check_feedback_message(self):
        empty_fields = self.get_empty_fields()
        word_fields_incorrect = self.get_word_fields_incorrect()
        integer_fields_incorrect = self.get_integer_fields_incorrect()
        
        feedback_message = ''

        if len(empty_fields) > 0:
            feedback_message += f'Please fill in the following fields: {empty_fields}.\n'
        
        if len(word_fields_incorrect) > 0:
            feedback_message += f'Please make sure that the following fields only contain words: {word_fields_incorrect}.\n'
        
        if len(integer_fields_incorrect) > 0:
            feedback_message += f'Please make sure that the following fields are a single integer: {integer_fields_incorrect}.\n'
        
        return feedback_message

    def convert_RiskAssessment_object_into_lambda_response_list(self):
        return list(vars(self).values())
    
    def get_activity_input(self):
        return Activity(activity=self.activity)
    
    def get_how_it_harms_input(self):
        return HowItHarms(how_it_harms=self.how_it_harms)
    
    def get_how_it_harms_in_context_input(self):
        return HowItHarmsInContext(how_it_harms=self.how_it_harms,
                          activity=self.activity,
                          hazard = self.hazard)

    def get_who_it_harms_input(self):
        return WhoItHarms(who_it_harms=self.who_it_harms)
    
    def get_who_it_harms_in_context_input(self):
        return WhoItHarmsInContext(who_it_harms=self.who_it_harms,
                            how_it_harms=self.how_it_harms,
                            activity=self.activity,
                            hazard=self.hazard)
    
    def get_prevention_input(self):
        return Prevention(prevention=self.prevention,
                          activity=self.activity,
                          hazard=self.hazard,
                          how_it_harms=self.how_it_harms,
                          who_it_harms=self.who_it_harms)
    
    def get_mitigation_input(self):
        return Mitigation(mitigation=self.mitigation,
                          activity=self.activity,
                          hazard=self.hazard,
                          how_it_harms=self.how_it_harms,
                          who_it_harms=self.who_it_harms)
    
    def get_prevention_classification_input(self):
        return PreventionClassification(
                        prevention=self.prevention,
                        activity=self.activity,
                        hazard=self.hazard,
                        how_it_harms=self.how_it_harms,
                        who_it_harms=self.who_it_harms)
    
    def get_mitigation_classification_input(self):
        return MitigationClassification(
                        mitigation=self.mitigation,
                        activity=self.activity,
                        hazard=self.hazard,
                        how_it_harms=self.how_it_harms,
                        who_it_harms=self.who_it_harms)
    
    def check_that_risk_equals_likelihood_times_severity(self, likelihood, severity, risk):
        try:
            likelihood = int(likelihood)
            severity = int(severity)
            risk = int(risk)

            if likelihood * severity == risk:
                return 'correct'
            else:
                return 'incorrect. Please check your multiplication.'
        
        except ValueError:
            return 'Please make sure that the likelihood, severity, and risk are all integers.'

    def check_uncontrolled_risk(self):
        return self.check_that_risk_equals_likelihood_times_severity(self.uncontrolled_likelihood,
                                                                self.uncontrolled_severity,
                                                                self.uncontrolled_risk)
    
    def check_controlled_risk(self):
        return self.check_that_risk_equals_likelihood_times_severity(self.controlled_likelihood,
                                                                self.controlled_severity,
                                                                self.controlled_risk)
    
    # TODO: Add ability to see prompt output percentages
    
    def get_list_of_prompt_input_objects(self):
        return [self.get_activity_input(),
                self.get_how_it_harms_input(),
                self.get_how_it_harms_in_context_input(),
                # self.get_who_it_harms_input(),
                self.get_who_it_harms_in_context_input(),
                self.get_prevention_input(),
                self.get_mitigation_input(),
                self.get_prevention_classification_input(),
                self.get_mitigation_classification_input()]
    
    def get_list_of_question_titles(self):
        question_titles = []
        
        for prompt_input_object in self.get_list_of_prompt_input_objects():
            question_titles.append(prompt_input_object.get_question_title())

        return question_titles
    
    def get_list_of_questions(self):
        questions = []

        for prompt_input_object in self.get_list_of_prompt_input_objects():
            questions.append(prompt_input_object.get_question())
        
        return questions
    
    def get_list_of_prompts(self):
        prompts = []

        for prompt_input_object in self.get_list_of_prompt_input_objects():
            prompts.append(prompt_input_object.generate_prompt())

        return prompts
    
    def get_list_of_prompt_outputs(self, LLM_caller: Type[LLMCaller]):
        prompt_outputs = []

        for prompt_input_object in self.get_list_of_prompt_input_objects():
            prompt_outputs.append(LLM_caller.get_model_output(prompt_input_object))
        
        return prompt_outputs
    
    def get_list_of_regex_matches(self, prompt_outputs):
        regex_pattern_matcher = RegexPatternMatcher()

        regex_matches = []

        for prompt_output in prompt_outputs:
            regex_match = regex_pattern_matcher.check_string_against_pattern(prompt_output)
            regex_matches.append(regex_match)
        
        return regex_matches
    
    def get_list_of_shortform_feedback_objects(self):
        shortform_feedback_objects = []

        for prompt_input_object in self.get_list_of_prompt_input_objects():
            shortform_feedback_objects.append(prompt_input_object.get_shortform_feedback())

        return shortform_feedback_objects

    def get_list_of_shortform_feedback_from_regex_matches(self, regex_matches):
        list_of_shortform_feedback = []

        shortform_feedback_objects = self.get_list_of_shortform_feedback_objects()

        for i in range(len(regex_matches)):
            if regex_matches[i] == True:
                list_of_shortform_feedback.append(shortform_feedback_objects[i].positive_feedback)
            else:
                list_of_shortform_feedback.append(shortform_feedback_objects[i].negative_feedback)
        
        return list_of_shortform_feedback
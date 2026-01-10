# Base class used to test the accuracy of different prompts

from ..utils.LLMCaller import LLMCaller
from ..utils.RegexPatternMatcher import RegexPatternMatcher

class BaseTestClass:
    def __init__(self,
                 LLM: LLMCaller,
                 expected_output,
                 prompt_input_object):
        self.LLM = LLM
        self.expected_output = expected_output
        self.prompt_input_object = prompt_input_object
    
    def get_pattern_matched_and_prompt_output(self, input_object):

        pattern_matching_method_string = input_object.pattern_matching_method
        regex_pattern_matcher = RegexPatternMatcher()
        pattern_matching_method = getattr(regex_pattern_matcher, pattern_matching_method_string)
    
        prompt_output = self.LLM.get_model_output(prompt=input_object.generate_prompt(), max_tokens=input_object.max_tokens)
        print(prompt_output)

        pattern_matched = pattern_matching_method(prompt_output)
        
        return pattern_matched, prompt_output
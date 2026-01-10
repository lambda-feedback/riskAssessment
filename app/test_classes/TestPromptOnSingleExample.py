# Builds on BaseTestClass.py to test prompt on single risk assessment example (this is used in unit tests)

from BaseTestClass import BaseTestClass
from ..utils.LLMCaller import LLMCaller

class TestPromptOnSingleExample(BaseTestClass):
    def __init__(self,
                 LLM: LLMCaller,
                 expected_output,
                 input_object):
        self.LLM = LLM
        self.expected_output = expected_output
        self.input_object = input_object
    
    def is_pattern_matched_equal_to_expected_output(self):
        pattern_matched, prompt_output = self.get_pattern_matched_and_prompt_output(self.input_object)
        
        return pattern_matched == self.expected_output
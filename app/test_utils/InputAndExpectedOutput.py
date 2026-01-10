# Class which contains a prompt input object and the expected output for the prompt.

try:
    from ..prompts.BasePromptInput import BasePromptInput
    from ..data.RiskAssessment import RiskAssessment
except:
    from ..prompts.BasePromptInput import BasePromptInput
    from ..data.RiskAssessment import RiskAssessment

class InputAndExpectedOutputForSinglePrompt:
    def __init__(self, prompt_input_object: BasePromptInput, expected_output):
        self.prompt_input_object = prompt_input_object
        self.expected_output = expected_output

class InputAndExpectedOutputForCombinedPrompts:
    def __init__(self, risk_assessment: RiskAssessment, expected_output):
        self.risk_assessment = risk_assessment
        self.expected_output = expected_output
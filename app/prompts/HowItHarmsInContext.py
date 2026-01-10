# PromptInput class that checks whether the "How it harms" input matches the "activity" and "hazard" inputs.

from ..prompts.BasePromptInput import BasePromptInput
from ..utils.RegexPatternMatcher import RegexPatternMatcher

class HowItHarmsInContext(BasePromptInput):
    def __init__(self, how_it_harms, activity, hazard):
        super().__init__()
        self.how_it_harms = how_it_harms
        self.activity = activity
        self.hazard = hazard
        self.max_tokens = 200

    def get_field_checked(self):
        return 'Hazard & How It Harms'
    
    # TODO: Scope for adding a few shot example with an 'Add more detail' output.

    def generate_prompt_without_few_shot_examples(self):
        return f'''
        Follow these instructions:
        1. In one sentence, describe the hazard: '{self.hazard}' during the activity: '{self.activity}'.
        2. In one sentence, explain whether or not '{self.how_it_harms}' is a way that this hazard causes harm. 
        3. If it is, answer True, else answer False.
        '''
    
    def generate_prompt(self):
        example_of_correct_how_it_harms = f'''
        Example Input:
        Follow these instructions:
        1. In one sentence, describe the hazard: 'Electrocution' during the activity: 'Fluids laboratory'.
        2. In one sentence, explain whether or not 'Electrocuted by mains voltage' is a way that this hazard causes harm. 
        3. If it is, answer True, else answer False.

        Output:
        Description: 'Electrocution' during a fluids laboratory can occur when an individual comes into contact with mains voltage.
        Explanation: As water is a conductor of electricity, touching electronics with wet hands can cause harm
        through electrocution as the water provides a path for electrical current to flow through the body.
        Overall Answer: True
        '''

        example_of_incorrect_how_it_harms = f'''
        Example Input:
        Follow these instructions:
        1. In one sentence, describe the hazard: 'Volcanic eruption' during the activity: 'Volcano visit'.
        2. In one sentence, explain whether or not "Heavy impact when falling onto a demonstrator and causing injury" is a way that this hazard causes harm.
        3. If it is, answer True, else answer False.

        Output:
        Description: A volcanic eruption during a volcano activity can lead to various hazards and risks.
        Explanation: "Heavy impact when falling onto a demonstrator and causing injury" is not a way that a volcanic eruption causes harm. The primary dangers of a volcanic eruption include lava flows, ash clouds, and pyroclastic flows.
        Overall Answer: False.
        '''
        return f'''
        {example_of_correct_how_it_harms}

        {example_of_incorrect_how_it_harms}

        {self.generate_prompt_without_few_shot_examples()}

        Use the following output format:
        Description: <your description>
        Explanation: <your Explanation>
        Overall Answer: <your answer>'''
    
    def get_shortform_feedback(self, feedback_type):
        if feedback_type == 'positive':
            return f"Correct! '{self.how_it_harms}' is a way that the hazard: '{self.hazard}' causes harm."
        if feedback_type == 'negative':
            return f"Incorrect. '{self.how_it_harms}' is not a way that the hazard: '{self.hazard}' causes harm."
    
    def get_longform_feedback(self, prompt_output=''):
        regex_pattern_matcher = RegexPatternMatcher()
        return regex_pattern_matcher.extract_section_of_prompt_until_new_line_or_end_of_string(prompt_output, 'Explanation')

    def get_recommendation(self):
        return f'For the "How it harms" input, enter how the hazard leads to harm, and the specific harm caused, e.g. an injury or illness.'
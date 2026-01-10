# PromptInput class that checks whether the "Who it harms" input matches the "activity", "hazard" and "how it harms" inputs.

from ..prompts.BasePromptInput import BasePromptInput
from ..utils.RegexPatternMatcher import RegexPatternMatcher

class WhoItHarmsInContext(BasePromptInput):
    def __init__(self, who_it_harms, activity, hazard, how_it_harms):
        super().__init__()
        self.who_it_harms = who_it_harms
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.max_tokens = 200

    def get_field_checked(self):
        return 'Who It Harms'
    
    def generate_prompt(self):
        
        example_of_correct_who_it_harms = f'''
        Example Input:
        Follow these instructions:
        1. In one sentence, describe the hazard: 'Getting kicked by a horse' during the activity: 'Mucking out stable', given how it harms: 'Impact injury'.
        2. In one sentence, explain whether a 'Stable hand' is someone at high risk from being harmed by this hazard.
        3. If it is possible, answer True, else answer False.

        Output:
        Description: When mucking out a stable, it is possible that the person mucking out is kicked by a horse, resulting in impact injuries.
        Explanation: It is likely that a "Stable hand" would muck out a stable and therefore they are at high risk from the horse kick them.
        Overall Answer: True
        '''

        example_of_incorrect_who_it_harms = f'''
        Example Input:
        1. In one sentence, describe the hazard: 'Ink spillage' during the activity 'Fluids laboratory', given how it harms: 'Serious eye damage.
        2. In one sentence, explain whether it is possible that a 'Stable hand' to be DIRECTLY harmed by this hazard.
        3. If it is possible, answer True, else answer False.

        Output:
        Description: Ink spillage during the fluids laboratory activity can cause serious eye damage if the ink comes into contact with the eyes.
        Explanation: A stable hand is not someone at high risk from this hazard, as they typically work with horses in a stable environment and are not involved in laboratory activities involving fluids like ink.
        Overall Answer: False
        '''
        return f'''
        {example_of_correct_who_it_harms}

        {example_of_incorrect_who_it_harms}

        Follow these instructions:
        1. In one sentence, describe the hazard: '{self.hazard}' during the activity: '{self.activity}', given how it harms: '{self.how_it_harms}'.
        2. In one sentence, explain whether '{self.who_it_harms}' is at high risk from being harmed by this hazard.
        3. If it is possible, answer True, else answer False.

        Your answer should be in the format:
        Description: <your description>
        Explanation: your_explanation
        Overall Answer: <your answer>'''
    
    def get_shortform_feedback(self, feedback_type):
        if feedback_type == 'positive':
            return f"Correct! '{self.who_it_harms}' could take part in the activity: '{self.activity}'."
        if feedback_type == 'negative':
            return f"Incorrect. '{self.who_it_harms}' could not take part in the activity: '{self.activity}'."

    def get_longform_feedback(self, prompt_output=''):
        regex_pattern_matcher = RegexPatternMatcher()
        return regex_pattern_matcher.extract_section_of_prompt_until_new_line_or_end_of_string(prompt_output, 'Explanation')
    
    def get_recommendation(self):
        return f"For the 'Who it harms' field, please enter the individuals or group at risk of harm from the hazard"  
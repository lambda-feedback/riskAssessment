# PromptInput class used to infer the "event that leads to harm" and the "harm caused" from the student's risk assessment inputs.

from .BasePromptInput import BasePromptInput

class HarmCausedAndHazardEvent(BasePromptInput):
    def __init__(self, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms
        self.max_tokens = 300

        self.pattern_matching_method = 'extract_harm_caused_and_hazard_event'

    def generate_prompt_without_few_shot_examples(self):
        return f'''
        1. Describe the harm caused: '{self.how_it_harms}' by the hazard: '{self.hazard}' during the activity: '{self.activity}'.
        The harm caused by a hazard refers to the negative consequences resulting from the hazard event.
        2. From the above description, infer the harm caused. NOTE: This is not an event, but a consequence of an event.
        3. Describe the events which lead to the harm caused. Don't refer to the harm caused.
        '''

    def generate_prompt(self):

        return f'''

        <EXAMPLE INSTRUCTIONS>
        1. The harm caused by a hazard refers to the negative consequences resulting from the hazard event. 
        Describe the harm caused: 'Could injure' for who it harms: 'Cyclists' by the hazard: 'Getting hit' during the activity: 'Riding a Bike' .
        Write your answer in the format: <activity> can lead to <hazard event>, which could result in <harm caused> for <who it harms>.
        2. Extract the harm caused.
        3. Describe the events which lead to this harm caused. Don't refer to the harm caused.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Description: Riding a bike can lead to getting hit by a car, which could lead to an impact injury for cyclists.
        Harm caused: Impact injury
        Event that leads to harm: Getting hit by a car while riding a bike
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        1. The harm caused by a hazard refers to the negative consequences resulting from the hazard event. 
        Describe the harm caused: 'Mistakes by cyclists or motorists leading to crash' for who it harms: 'cyclists' by the hazard: 'Head injury' during the activity: 'Cycle commuting'.
        Write your answer in the format: <activity> can lead to <hazard event>, which could result in <harm caused> for <who it harms>.
        2. Extract the harm caused.
        3. Describe the events which lead to this harm caused. Don't refer to the harm caused.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Description: Cycle commuting can lead to mistakes by cyclists or motorists leading to a crash, which can cause a head injury.
        Harm caused: Head injury
        Event that leads to harm: Mistakes by cyclists or motorists leading to a crash
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        1. The harm caused by a hazard refers to the negative consequences resulting from the hazard event. 
        Describe the harm caused: 'When cut the zip tie may hit an audience member' for who it harms: 'audience' by the hazard: 'Cut Zip tie may fly' during the activity: 'Using a spring contraption as a demonstration for a TPS presentation'.
        Write your answer in the format: <activity> can lead to <hazard event>, which could result in <harm caused> for <who it harms>.
        2. Extract the harm caused.
        3. Describe the events which lead to this harm caused. Don't refer to the harm caused.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Description: Using a spring contraption as a demonstration for a TPS presentation can lead to a cut zip tie flying and hitting an audience member.
        Harm caused: Impact injury to audience member
        Event that leads to harm: Cut zip tie may fly and hit an audience member

        <INSTRUCTIONS>
        1. The harm caused by a hazard refers to the negative consequences resulting from the hazard event. 
        Describe the harm caused: '{self.how_it_harms}' for '{self.who_it_harms}' by the hazard: '{self.hazard}' during the activity: '{self.activity}'.
        Write your answer in the format: <activity> can lead to <hazard event>, which could result in <harm caused> for <who it harms>.
        2. Extract the harm caused.
        3. Describe the events which lead to this harm caused. Don't refer to the harm caused.
        </INSTRUCTIONS>

        <OUTPUT>'''

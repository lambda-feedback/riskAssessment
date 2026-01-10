# PromptInput class that takes in the output from the ControlMeasureClassification prompt and shortens it to 3 sentences.

from ..prompts.BasePromptInput import BasePromptInput

class SummarizeControlMeasureFeedback(BasePromptInput):
    def __init__(self):

        self.candidate_labels = [True, False]
        self.pattern_matching_method = 'always_return_true'
        self.max_tokens = 300

    def get_context_style_tone_audience(self):
        return """<CONTEXT>
        You are a Risk Assessment expert responsible for summarizing feedback on Risk Assessment inputs.
        </CONTEXT>

        <STYLE>
        Follow the writing style of a secondary school teacher.
        </STYLE>

        <TONE>
        Use a formal tone in your outputs.
        </TONE>

        <AUDIENCE>
        Your audience is a student who is learning how to write a risk assessment.
        </AUDIENCE>"""
        
    def get_instructions(self, control_measure_type, feedback):
        return f"""<INSTRUCTIONS>
        Summarize the {control_measure_type} feedback: "{feedback}" in the following format:
        - In 2 sentences, provide an explanation as to why the control measure is or is not a {control_measure_type}. 
        - In one sentence, provide a statement of whether or not control measure is {control_measure_type} measure.
        Start the summary immediately after these instructions.
        </INSTRUCTIONS>"""
    
    def get_example(self, control_measure_type):
        if control_measure_type == 'prevention':
            return f"""<EXAMPLE INPUT>
            Thinking step by step:
            - Enhancing explosive detection capabilities, such as deploying advanced screening equipment or trained explosive detection canine units, increases the chances of identifying and intercepting explosives before they can be detonated.
            - By detecting and preventing explosives from entering the event premises, the likelihood of an explosive terrorist attack occurring is significantly reduced.
            - Therefore, enhancing explosive detection capabilities directly reduces the likelihood of the hazard event "Explosive terrorist attack during public gatherings or events" from occurring. It is a prevention measure.
            </EXAMPLE INPUT>

            <EXAMPLE OUTPUT>
            Enhancing explosive detection capabilities, such as deploying advanced screening equipment or trained explosive detection canine units allows for the detection and prevention of explosives from entering the event premises.
            Thus, the likelihood of an explosive terrorist attack occurring is significantly reduced. Hence, enhancing explosive detection capabilities is a prevention measure.
            </EXAMPLE OUTPUT>"""
        
        if control_measure_type == 'mitigation':
            return '''<EXAMPLE INPUT>
            Thinking step by step:
            - Loud noises can cause hearing damage, especially at close range and with prolonged exposure.
            - By increasing the distance between the trombone player and the audience, the intensity of the sound reaching the audience is reduced.
            - This reduced sound intensity can help reduce hearing damage caused by the loud noise.
            - Therefore, keeping a space between the player and audience removes or reduces the harm caused by "Hearing damage" for everyone present. It is a mitigation measure.
            </EXAMPLE INPUT>

            <EXAMPLE OUTPUT>
            Increasing the distance between the trombone player and the audience reduces the intensity of the sound reaching the audience.
            This helps reduce potential hearing damage from the loud noise. Hence, increasing distance between the trombone player and the audience is a mitigation measure.
            </EXAMPLE OUTPUT>'''

    def generate_prompt(self, control_measure_type, feedback):
        return f'''
        {self.get_context_style_tone_audience()}

        {self.get_example(control_measure_type=control_measure_type)}

        {self.get_instructions(control_measure_type=control_measure_type, feedback=feedback)}'''
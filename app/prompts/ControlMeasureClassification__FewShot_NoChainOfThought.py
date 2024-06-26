from ..prompts.BasePromptInput import BasePromptInput

class ControlMeasureClassification__FewShot_NoChainOfThought(BasePromptInput):
    def __init__(self, control_measure, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.control_measure = control_measure
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms
        self.max_tokens = 400

        self.pattern_matching_method = 'check_string_for_prevention_mitigation_or_neither'
        self.candidate_labels = ['prevention', 'mitigation', 'neither', 'both']
        self.labels_indicating_correct_input = ['prevention', 'both']
    
    def generate_prompt(self, hazard_event, harm_caused):

        # TODO: Should alter the mitigation explanations - sometimes a mitigation measure is done to prepare for 
        # the hazard event, not just to reduce the harm caused by the hazard event.

        all_few_shot_examples = """
        <EXAMPLE INSTRUCTIONS>
        1. In one sentence, describe the hazard given the hazard event: "Ink spillage" during the
        activity: 'Fluids laboratory' given the harm caused: "Serious eye damage" for Students.
        2. Write the Hazard Event: "Ink spillage"
        3. Write the Harm Caused: "Serious eye damage".
        4. State whether or not 'Cleaning the eyes out with water' reduces the likelihood that the hazard event: "Ink spillage" occurs.
        If so, it is a prevention measure.
        5. State whether or not 'Cleaning the eyes out with water' removes or reduces the harm caused: "Serious eye damage" for the 'Students'.
        If so, it is a mitigation measure.
        6. If it is a prevention measure, answer 'Prevention'. If it is a mitigation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: During a fluids laboratory, ink spillage on a student's face causes serious eye damage.

        Prevention Statement:
        - Cleaning the eyes with water does not reduce the likelihood of ink spillage on a student's face.
        - Therefore, cleaning the eyes with water is not a prevention measure.

        Mitigation Statement:
        - Cleaning the eyes with water can reduce the severity of the eye damage caused by an ink spillage on a student's face.
        - Therefore, cleaning the eyes with water is a mitigation measure.

        Answer: Mitigation
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        1. In one sentence, describe the hazard given the hazard event: "Student slips on water" during the
        activity: 'Fluids laboratory' given the harm caused: "Injury caused by students slipping" for Students.
        2. Write the Hazard Event: "Student slips on water"
        3. Write the Harm Caused: "Injury caused by students slipping".
        4. State whether or not 'Keeping the water tank stationary when it's full' reduces the likelihood that hazard event: "Student slips on water" occurs.
        If so, it is a prevention measure.
        5. State whether or not 'Keeping the water tank stationary when it's full' removes or reduces the harm caused: "Injury caused by students slipping" for the 'Students'.
        If so, it is a mitigation measure.
        6. If it is a prevention measure, answer 'Prevention'. If it is a mitigation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: During a fluids laboratory, water spills on the floor, causing students to slip and suffer injuries
        Hazard Event: Student slips on water
        Harm Caused: Injury caused by students slipping

        Prevention Explanation:
        - Keeping the water tank stationary when it's full reduces the likelihood of students slipping on the wet floor.
        - Therefore, keeping the water tank stationary when it's full is a prevention measure.

        Mitigation Explanation:
        - Keeping the water tank stationary when it's full does not remove or reduce the harm caused by the "Injury caused by students slipping". 
        - Therefore, keeping the water tank stationary when it's full is not a mitigation measure.

        Answer: Prevention
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        1. In one sentence, describe the hazard given the hazard event: "Car crashes into the cyclist" during the
        activity: 'Cycle commuting' given the harm caused: "Head injury" for Cyclist.
        2. Write the Hazard Event: "Car crashes into the cyclist"
        3. Write the Harm Caused: "Head injury".
        4. State whether or not 'Wear a helmet' reduces the likelihood that hazard event: "Car crashes into the cyclist" occurs.
        If so, it is a prevention measure.
        5. State whether or not 'Wear a helmet' removes or reduces the harm caused: "Head injury" for the 'Cyclist'.
        If so, it is a mitigation measure.
        6. If it is a prevention measure, answer 'Prevention'. If it is a mitigation meausure, answer 'Mitigation'.   
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: A cyclist commuting to work gets hit by a car, resulting in a head injury.
        Hazard Event: Car crashes into the cyclist
        Harm Caused: Head injury

        Prevention Explanation: 
        - Wearing a helmet does not reduce likelihood of a cyclist getting hit by a car.
        - Therefore, wearing a helmet is not a prevention measure.
        
        Mitigation Explanation: 
        - Wearing a helmet can lessen the severity of a head injury caused by a cyclist getting hit by a car.
        - Therefore, wearing a helmet is a mitigation measure.
        
        Answer: Mitigation
        </EXAMPLE OUTPUT>

        <EXAMPLE INSTRUCTIONS>
        1. In one sentence, describe the hazard given the hazard event: "Zip tie projectile hits audience member" during the
        activity: 'Fluids laboratory' given the harm caused: "Impact injury" for Students.
        2. Write the Hazard Event: "Zip tie projectile hits audience member"
        3. Write the Harm Caused: "Impact injury".
        4. State whether or not 'Keeping hand around zip tie when cutting to stop it from flying' reduces the likelihood that hazard event: "Zip tie projectile hits audience member" occurs.
        If so, it is a prevention measure.
        5. State whether or not 'Keeping hand around zip tie when cutting to stop it from flying' removes or reduces the harm caused: "Impact injury" for the 'Students'.
        If so, it is a mitigation measure.
        6. If it is a prevention measure, answer 'Prevention'. If it is a mitigation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.
        </EXAMPLE INSTRUCTIONS>

        <EXAMPLE OUTPUT>
        Hazard Description: During a fluids laboratory, a cut zip tie flies and hits a student audience member, causing an impact injury.
        Hazard Event: Zip tie projectile hits audience member
        Harm Caused: Impact injury

        Prevention Explanation: 
        - Keeping a hand around the zip tie while cutting it can reduce the likelihood of the zip tie flying and hitting an audience member.
        - Therefore, keeping a hand around the zip tie when cutting it is a prevention measure.
        
        Mitigation Explanation: 
        - If a cut zip tie were to fly and hit a student, keeping a hand around it during cutting would not reduce the severity of the "Impact injury".
        - Therefore, keeping a hand around the zip tie when cutting is not a mitigation measure.
        
        Answer: Prevention
        </EXAMPLE OUTPUT>
        """

        return f'''
        <CONTEXT>
        You are a Risk Assessment expert responsible for giving feedback on Risk Assessment inputs.
        </CONTEXT>

        <STYLE>
        Follow the writing style of a secondary school teacher.
        </STYLE>

        <TONE>
        Use a formal tone in your outputs.
        </TONE>

        <AUDIENCE>
        Your audience is a student who is learning how to write a risk assessment.
        </AUDIENCE>

        {all_few_shot_examples}

        <INSTRUCTIONS>
        Follow these instructions:
        1. In one sentence, describe the hazard given the hazard event: "{hazard_event}" during the
        activity: "{self.activity}" given the harm caused: "{harm_caused}" for {self.who_it_harms}.
        2. Write the hazard event: "{hazard_event}"
        3. Write the harm caused: "{harm_caused}"
        4. State whether or not "{self.control_measure}" reduces the likelihood that the hazard event: "{hazard_event}" occurs.
        If so, it is a prevention measure.
        5. State whether or not "{self.control_measure}" removes or reduces the harm caused: "{harm_caused}" for the "{self.who_it_harms}".
        If so, it is a mitigation measure.
        6. If it is a prevention measure, answer 'Prevention'. If it is a mitigation meausure, answer 'Mitigation'.
        If it is neither a prevention measure nor a mitigation measure, answer 'Neither'. If it is both a
        prevention measure and a mitigation measure, answer 'Both'.
        </INSTRUCTIONS>

        <OUTPUT FORMAT>
        Use the following output format:
        Hazard Description: <your hazard event description>
        Hazard Event: <hazard event>
        Harm Caused: <harm caused>
        Prevention Statement: <your prevention statement>
        Mitigation Statement: <your mitigation statement>
        Answer: <your answer>
        </OUTPUT FORMAT>
        
        <OUTPUT>
        Hazard Description: '''
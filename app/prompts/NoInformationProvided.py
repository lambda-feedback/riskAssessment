# PromptInput class that checks whether no information is provided in the "prevention" or "mitigation" input fields.

from .BasePromptInput import BasePromptInput

class NoInformationProvided(BasePromptInput):
    def __init__(self, input: str):
        super().__init__()
        self.pattern_matching_method = 'check_string_for_no_information_provided'
        self.candidate_labels = ['control measure', 'no information provided']
        self.input = input
        self.max_tokens = 200
    
    def generate_prompt(self):
        return f'''
        Follow these instructions:
        1. Classify the following input as either "No information provided" or "Control measure"

        <EXAMPLES>
        Input: "N/A" 
        Answer: No information provided

        Input: "Not Applicable" 
        Answer: No information provided

        Input: "Unknown" 
        Answer: No information provided

        Input: "None" 
        Answer: No information provided

        Input: "TBD" 
        Answer: No information provided

        Input: "To Be Determined" 
        Answer: No information provided

        Input: "Unspecified" 
        Answer: No information provided

        Input: "No Information Available" 
        Answer: No information provided

        Input: "Do Not Know" 
        Answer: No information provided

        Input: "Not specified" 
        Answer: No information provided

        Input: "Unavailable" 
        Answer: No information provided

        Input: "Not applicable" 
        Answer: No information provided

        Input: "Not known" 
        Answer: No information provided

        Input: "Wear helmet"
        Answer: Control measure

        Input: "Take care"
        Answer: Control measure

        Input: "Apply ice"
        Answer: Control measure
        </EXAMPLES>

        <OUTPUT FORMAT>
        Use the following output format:
        Answer: <your answer>
        </OUTPUT FORMAT>

        Input: "{self.input}"'''

    # TODO: Add requirement to have a generate_prompt function

    # TODO: Make it easier to add new prompts. At the moment it is too difficult. 
    # Have to change code in 2 places.

class PromptInput:
    def __init__(self):
        pass

    def generate_prompt(self):
        pass

    def to_string(self):
        class_name = self.__class__.__name__
        if hasattr(self, '__dict__'):
            attributes = ', '.join([f"{key}={value}" for key, value in self.__dict__.items()])
            return f"{class_name}({attributes})"
        else:
            return f"{class_name}()"

class Activity(PromptInput): # TODO so inherits expected_output from PromptInput
    def __init__(self, activity: str):
        super().__init__()
        self.activity = activity

    def generate_prompt(self):
        common_noun_definition = """a noun denoting a class of objects or a concept as opposed 
        to a particular individual."""

        activity_definition = """a specific action or process that involves 
        physical or mental effort."""
        
        return f'''
        The definition of activity is: "{activity_definition}". 
        In one sentence, provide a description of "{self.activity}".
        Then in one sentence compare this description of "{self.activity}" 
        with the provided definition of an activity. 
        If "{self.activity}" is an activity, is_correct = True. 
        Then write one sentence in the format: \ndict(is_correct=True/False)'''

        # dict\(\'input\'=({}), is_correct=(True|False)\)''.format(re.escape(input))

class Hazard(PromptInput):
    def __init__(self, activity: str, hazard: str):
        super().__init__()
        self.activity = activity
        self.hazard = hazard

    def generate_prompt(self):
        hazard_definition = """a dangerous phenomenon, substance, human activity or condition. 
        It may cause loss of life, injury or other health impacts, property damage, loss of livelihoods 
        and services, social and economic disruption, or environmental damage."""
        return f'''If a 'hazard' is defined as '{hazard_definition}', is the following: '{self.hazard}', 
        during the activity: '{self.activity}', an example of a 'hazard'?'''

class HowItHarms(PromptInput):
    def __init__(self, how_it_harms, activity, hazard):
        super().__init__()
        self.how_it_harms = how_it_harms
        self.activity = activity
        self.hazard = hazard
    
    def generate_prompt(self):
        # TODO: Do knowledge generation prompt for this

        return f'''In one sentence, describe the hazard: '{self.hazard}' during the 
        activity: '{self.activity}'. Then in one sentence, explain whether or not 
        '{self.how_it_harms}' is a way that this hazard causes harm. 
        If it does cause harm, is_correct = True. Then write the final sentence of your answer 
        in the format: dict(is_correct=True/False).'''

class WhoItHarms(PromptInput):
    def __init__(self, who_it_harms, how_it_harms, activity, hazard):
        super().__init__()
        self.who_it_harms = who_it_harms
        self.how_it_harms = how_it_harms
        self.activity = activity
        self.hazard = hazard

    def generate_prompt(self):
        noun_definition = "a word (other than a pronoun) used to identify any of a class of people, places, or things"

        return f'''Given that a noun is defined as: '{noun_definition}', is '{self.who_it_harms}' an example of a noun?
        If not, is '{self.who_it_harms}' likely to be harmed by hazard: '{self.hazard}' during the activity: '{self.activity}' 
        because of how the hazard causes harm: '{self.how_it_harms}'?'''

class Prevention(PromptInput):
    def __init__(self, prevention, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.prevention = prevention
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

    def generate_prompt(self):
        prevention_definition = f'an action which reduces the probability that the hazard occurs.'
        return f'''If a 'prevention measure' is defined as '{prevention_definition}', is the following: '{self.prevention}' 
        an example of a 'prevention measure' for the following hazard: '{self.hazard}' during the activity: '{self.activity}' 
        given how it harms: '{self.how_it_harms}' and who it harms: '{self.who_it_harms}'?'''

class Mitigation(PromptInput):
    def __init__(self, mitigation, activity, hazard, how_it_harms, who_it_harms):
        super().__init__()
        self.mitigation = mitigation
        self.activity = activity
        self.hazard = hazard
        self.how_it_harms = how_it_harms
        self.who_it_harms = who_it_harms

    def generate_prompt(self):
        severity_definition = """a measure of the seriousness of adverse consequences that could occur if the hazard 
        leads to an accident."""
        mitigation_definition = f'an action which reduces the severity of a hazard. Severity in this context is {severity_definition}'

        return f'''If a 'mitigation measure' is defined as '{mitigation_definition}', is the following: '{self.mitigation}' 
        an example of a 'mitigation measure' for the following hazard: '{self.hazard}' during the activity '{self.activity}' 
        given how it harms: '{self.how_it_harms}' and who it harms: '{self.who_it_harms}'?'''
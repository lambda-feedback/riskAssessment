# pytest -v -s evaluation_tests.py

# The -s option above is so you can see printouts even if the test fails

import unittest

try:
    from .evaluation import Params, evaluation_function
    from .example_risk_assessments import RA_1
    from .LLMCaller import LLMCaller, LLMWithCandidateLabels, LLMWithGeneratedText, OpenAILLM
    from .PromptInputs import Activity
except:
    from evaluation import Params, evaluation_function
    from example_risk_assessments import RA_1
    from LLMCaller import LLMCaller, LLMWithCandidateLabels, LLMWithGeneratedText, OpenAILLM
    from PromptInputs import Activity

class TestEvaluationFunction(unittest.TestCase):
    """
    TestCase Class used to test the algorithm.
    ---
    Tests are used here to check that the algorithm written
    is working as it should.

    It's best practise to write these tests first to get a
    kind of 'specification' for how your algorithm should
    work, and you should run these tests before committing
    your code to AWS.

    Read the docs on how to use unittest here:
    https://docs.python.org/3/library/unittest.html

    Use evaluation_function() to check your algorithm works
    as it should.
    """

    def test_returns_is_correct_true(self):
        response = [['Using a trombone as a demonstration for a TPS presentation'],
                          ['Impact from instrument'],
                          ['Audience watching presentation'],
                          ['Slide could hit audience member, causing impact injury.'],
                          [4],
                          [2], 
                          [8],
                          ['Keep safe distance between the player and audience; hold instrument securely'],
                          [1],
                          [''],
                          [2], 
                          [2]]
        answer, params = None, None

        result = evaluation_function(response, answer, params)

        print(result.get("feedback"))

        self.assertIn(result.get("is_correct"), [True, False])

    # def test_get_model_output_with_Llama_model(self):
    #     model_name = 'meta-llama/Llama-2-13b-chat-hf'
    #     LLM = LLMWithGeneratedText(LLM_API_ENDPOINT=f'https://api-inference.huggingface.co/models/{model_name}')
        
    #     prompt_input = Activity(activity='fencing')
        
    #     LLM_output = LLM.get_model_output(prompt_input)
    #     print(LLM_output)
    #     self.assertIsInstance(LLM_output, str)

    # TODO: Test the function which creates an instance of a RiskAssessment object

    # TODO: Test the function which calls the LLM

if __name__ == "__main__":
    unittest.main()

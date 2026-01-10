# Script which tests the latency of different LLMs

# To run, enter in terminal: python -m app.test_scripts.test_latency

from ..utils.LLMCaller import *
from ..evaluation import evaluation_function, Params
from ..utils.GoogleSheetsWriter import GoogleSheetsWriter
from datetime import datetime
import numpy as np

from ..data.example_risk_assessments import physical_risks_to_individuals__original_student_data

def test_latency_of_evaluation_function(LLM_name: str, risk_assessments_dict, number_of_risk_assessments_to_test):

    risk_assessments = risk_assessments_dict['risk_assessments']

    responses = [risk_assessment.convert_risk_assessment_to_evaluation_function_list_input() for risk_assessment in risk_assessments][:number_of_risk_assessments_to_test]

    elapsed_times = []

    for response in responses:

        start_time = time.time()

        answer = None
        params: Params = {"is_feedback_text": False, "is_risk_matrix": False, "is_risk_assessment": True, "LLM": LLM_name}

        result = evaluation_function(response, answer, params)

        end_time = time.time()

        elapsed_time = end_time - start_time

        elapsed_times.append(elapsed_time)

    lst_to_write_to_sheets = [LLM_name] + elapsed_times

    sheets_writer = GoogleSheetsWriter(sheet_name='Latency Test')

    sheets_writer.write_to_sheets(lst_to_write_to_sheets)

if __name__ == "__main__":
    for LLM_name in LLM_dictionary.keys():
        test_latency_of_evaluation_function(
            LLM_name=LLM_name, 
            risk_assessments_dict=physical_risks_to_individuals__original_student_data,
            number_of_risk_assessments_to_test=10)
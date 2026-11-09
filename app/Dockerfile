# Base image that bundles the AWS Lambda Python image with the lambda-feedback middleware (app.handler)
FROM ghcr.io/lambda-feedback/baseevalutionfunctionlayer:main-3.12

# The 3.12 image is Amazon Linux 2023, which doesn't ship `find` (used below)
RUN dnf install -y findutils && dnf clean all

WORKDIR /app

ENV PYTHONPATH=/app

# Copy and install any packages/modules needed for your evaluation script.
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the evaluation and testing scripts
COPY evaluation.py ./app/
COPY evaluation_tests.py ./app/

# Copy the preview and testing scripts
COPY preview.py ./app/
COPY preview_tests.py ./app/

# Copy additional files not included in the template repository
# that are used in evaluation.py
COPY prompts/BasePromptInput.py ./app/prompts/
COPY prompts/ControlMeasureClassification.py ./app/prompts/
COPY prompts/ControlMeasureClassification__FewShot_NoChainOfThought.py ./app/prompts/
COPY prompts/ControlMeasureClassification__ZeroShot_ChainOfThought.py ./app/prompts/
COPY prompts/ControlMeasureClassification__ZeroShot_NoChainOfThought.py ./app/prompts/
COPY prompts/HarmCausedAndHazardEvent.py ./app/prompts/
COPY prompts/HowItHarmsInContext.py ./app/prompts/
COPY prompts/WhoItHarmsInContext.py ./app/prompts/
COPY prompts/MitigationInput__ControlMeasureClassificationPrompt.py ./app/prompts/
COPY prompts/PreventionInput__ControlMeasureClassificationPrompt.py ./app/prompts/
COPY prompts/PreventionClassificationWithoutContextOfOtherInputs.py ./app/prompts/
COPY prompts/MitigationClassificationWithoutContextOfOtherInputs.py ./app/prompts/
COPY prompts/NoInformationProvided.py ./app/prompts/
COPY prompts/SummarizeControlMeasureFeedback.py ./app/prompts/
COPY data/RiskAssessment.py ./app/
COPY utils/LLMCaller.py ./app/utils/
COPY utils/RegexPatternMatcher.py ./app/utils/

# Copy Documentation
COPY docs/dev.md ./app/docs/dev.md
COPY docs/user.md ./app/docs/user.md

# Set permissions so files and directories can be accessed on AWS
RUN chmod 644 $(find . -type f)
RUN chmod 755 $(find . -type d)

# The entrypoint for AWS is to invoke the handler function within the app package.
# Python 3.12's Lambda runtime imports this as a module name, so it can't be a path.
CMD [ "app.handler" ]

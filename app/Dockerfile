# Base image that bundles AWS Lambda Python 3.8 image with some middleware functions
# FROM base-eval-tmp
FROM ghcr.io/lambda-feedback/baseevalutionfunctionlayer:main-3.8

WORKDIR /app

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

# The entrypoint for AWS is to invoke the handler function within the app package
CMD [ "/app/app.handler" ]

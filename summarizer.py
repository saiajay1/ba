from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from evaluator import llm  # Reuse the same LLM

# Define prompts for sub-agents
ceo_prompt = PromptTemplate(
    input_variables=["resume_text"],
    template="As a CEO, evaluate leadership potential in: {resume_text}"
)

cto_prompt = PromptTemplate(
    input_variables=["resume_text"],
    template="As a CTO, evaluate technical skills in: {resume_text}"
)

hr_prompt = PromptTemplate(
    input_variables=["resume_text"],
    template="As an HR, evaluate cultural fit in: {resume_text}"
)

# Create chains for each sub-agent
ceo_chain = LLMChain(llm=llm, prompt=ceo_prompt)
cto_chain = LLMChain(llm=llm, prompt=cto_prompt)
hr_chain = LLMChain(llm=llm, prompt=hr_prompt)

def summarize_resume(resume_text):
    ceo_feedback = ceo_chain.run(resume_text)
    cto_feedback = cto_chain.run(resume_text)
    hr_feedback = hr_chain.run(resume_text)
    return {
        "CEO Feedback": ceo_feedback,
        "CTO Feedback": cto_feedback,
        "HR Feedback": hr_feedback
    }
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from src.utils.llm_setup import llm

class JudgeAgent:
    def __init__(self):
        self.prompt = PromptTemplate(
            input_variables=["debate_history"],
            template="""You are an impartial judge for this debate. Review the debate history and determine the winner based on the quality of arguments, adherence to debate rules, and overall persuasiveness.

            Debate history:
            {debate_history}

            Provide your decision on who won the debate and explain your reasoning.
            Judge's Decision:"""
        )
        self.chain = LLMChain(llm=llm, prompt=self.prompt)
    
    def judge_debate(self, debate_history):
        return self.chain.run(debate_history=debate_history)
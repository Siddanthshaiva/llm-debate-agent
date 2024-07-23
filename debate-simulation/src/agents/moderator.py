from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from src.utils.llm_setup import llm

class Moderator:
    def __init__(self):
        self.prompt = PromptTemplate(
            input_variables=["debate_history", "human_input"],
            template="""You are a debate moderator. Your role is to guide the debate, ask probing questions, and ensure a fair discussion.

            Previous debate:
            {debate_history}
            
            Human: {human_input}
            Moderator:"""
        )
        self.chain = LLMChain(llm=llm, prompt=self.prompt)
    
    def moderate(self, debate_history, human_input):
        return self.chain.run(debate_history=debate_history, human_input=human_input)
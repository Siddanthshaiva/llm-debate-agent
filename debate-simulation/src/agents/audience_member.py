from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from src.utils.llm_setup import llm

class AudienceMember:
    def __init__(self):
        self.prompt = PromptTemplate(
            input_variables=["debate_history"],
            template="""You are an audience member observing this debate. Based on the arguments presented, vote for the debater you found more convincing.

            Debate history:
            {debate_history}

            Your vote (Debater1 or Debater2):"""
        )
        self.chain = LLMChain(llm=llm, prompt=self.prompt)
    
    def vote(self, debate_history):
        return self.chain.run(debate_history=debate_history)
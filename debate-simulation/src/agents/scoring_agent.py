from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from src.utils.llm_setup import llm

class ScoringAgent:
    def __init__(self):
        self.prompt = PromptTemplate(
            input_variables=["round_content"],
            template="""Score this debate round on a scale of 1-10 for each debater based on the following criteria:
            1. Argument quality
            2. Relevance to the topic
            3. Rebuttal effectiveness

            Round content:
            {round_content}

            Provide scores in the format:
            Debater1: [score]
            Debater2: [score]
            
            Ensure that [score] is a single integer between 1 and 10.
            """
        )
        self.chain = LLMChain(llm=llm, prompt=self.prompt)
    
    def score_round(self, round_content):
        return self.chain.run(round_content=round_content)
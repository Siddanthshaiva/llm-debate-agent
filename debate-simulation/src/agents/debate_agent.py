from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from src.utils.llm_setup import llm

class DebateAgent:
    def __init__(self, name, stance):
        self.name = name
        self.stance = stance
        print(self.name, self.stance)
        self.memory = ConversationBufferMemory(memory_key="chat_history", input_key="human_input")
        self.prompt = PromptTemplate(
            input_variables=["chat_history", "human_input"],
            template=f"""You are {name}, a debater with the following stance: {stance}, debate in points only.
            
            Previous conversation:
            {{chat_history}}
            
            Human: {{human_input}}
            {name}:"""
        )
        self.chain = LLMChain(llm=llm, prompt=self.prompt, memory=self.memory)
    
    def respond(self, human_input):
        return self.chain.run(human_input=human_input)
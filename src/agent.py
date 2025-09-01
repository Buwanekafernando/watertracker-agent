import os 
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv


load_dotenv()
openai_api_key = os.getenv('OPEN_API_KEY')

llm = ChatOpenAI(api_key=openai_api_key, model='gpt-4', temperature=0.5)

class WaterIntakeAgent:
    def __init__(self):
        self.history = []
    
    def analyze_intake(self, intake_ml):

        prompt = f""""
        you are a hydration assistant.The user has consumed {intake_ml} milliliters of water today.
        provide a hydration status and suggest if they need to drink more water
        """
        response = llm.invoke([HumanMessage(content=prompt)])

        return response.content
    
if __name__ == "__main__":
    agent = WaterIntakeAgent()
    intake_ml = 1500  
    feedback = agent.analyze_intake(intake_ml)
    print(f"Hydration Feedback: {feedback}")
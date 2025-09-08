import os
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv('OPEN_API_KEY')

llm = ChatOpenAI(api_key=openai_api_key, model='gpt-4', temperature=0.5)

def calculate_recommended_intake(weight_kg, age):
    base_intake = weight_kg * 35
    if age <= 30:
        factor = 1.0
    elif age <= 50:
        factor = 0.95
    else:
        factor = 0.9
    return int(base_intake * factor)

class WaterIntakeAgent:
    def __init__(self):
        self.history = []

    def analyze_intake(self, intake_ml, age, weight_kg):
        recommended = calculate_recommended_intake(weight_kg, age)
        prompt = f"""
        You are a hydration assistant. The user is {age} years old, weighs {weight_kg}kg, and has consumed {intake_ml}ml of water today.
        Based on hydration guidelines, recommend how much more they should drink and assess their hydration status.
        """
        response = llm.invoke([HumanMessage(content=prompt)])
        return response.content

if __name__ == "__main__":
    agent = WaterIntakeAgent()
    intake_ml = 1500
    age = 25
    weight_kg = 70
    feedback = agent.analyze_intake(intake_ml, age, weight_kg)
    print(f"Hydration Feedback: {feedback}")
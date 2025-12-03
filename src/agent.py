import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()
google_api_key = os.getenv('GEMINI_API_KEY')

# Updated model to gemini-1.5-flash
llm = ChatGoogleGenerativeAI(google_api_key=google_api_key, model='gemini-2.5-flash', temperature=0.5)

def calculate_recommended_intake(weight_kg, age):
    base_intake = weight_kg * 35
    if age <= 30:
        factor = 1.0
    elif age <= 50:
        factor = 0.95
    else:
        factor = 0.9
    return int(base_intake * factor)

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi, 1), category

def calculate_ideal_weight(height_cm):
    # Robinson formula (simplified for general use)
    # Men: 52 kg + 1.9 kg per inch over 5 feet
    # Women: 49 kg + 1.7 kg per inch over 5 feet
    # Averaging for simplicity or providing a range
    height_m = height_cm / 100
    min_ideal = 18.5 * (height_m ** 2)
    max_ideal = 24.9 * (height_m ** 2)
    return round(min_ideal, 1), round(max_ideal, 1)

class WaterIntakeAgent:
    def __init__(self):
        self.history = []

    def analyze_intake(self, intake_ml, age, weight_kg, height_cm):
        recommended = calculate_recommended_intake(weight_kg, age)
        bmi, category = calculate_bmi(weight_kg, height_cm)
        min_ideal, max_ideal = calculate_ideal_weight(height_cm)
        
        prompt = f"""
        You are a generic hydration and health assistant. 
        User Profile:
        - Age: {age}
        - Weight: {weight_kg}kg
        - Height: {height_cm}cm
        - BMI: {bmi} ({category})
        - Current Water Intake: {intake_ml}ml
        
        Please provide a response covering:
        1. **Hydration Analysis**: How much more water should they drink?
        2. **Weight Management**: How much water is recommended to help maintain or reach their ideal weight range ({min_ideal}-{max_ideal}kg)?
        3. **Benefits**: Briefly list 3 key benefits of proper hydration for their profile.
        4. **Schedule**: Suggest a simple water drinking schedule for the rest of the day.
        """
        response = llm.invoke([HumanMessage(content=prompt)])
        return response.content

if __name__ == "__main__":
    agent = WaterIntakeAgent()
    intake_ml = 1500
    age = 25
    weight_kg = 70
    height_cm = 175
    feedback = agent.analyze_intake(intake_ml, age, weight_kg, height_cm)
    print(f"Hydration Feedback: {feedback}")
import joblib
import numpy as np

model_path = "./research_model/Gradient_Boosting_model_predict.pkl"
model = joblib.load(model_path)

def predict_heart_disease(age, gender, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, height, weight):
    # Обчислення pulse_pressure_index та bmi
    pulse = ap_hi - ap_lo
    pulse_pressure_index = pulse / ap_hi
    bmi = weight / ((height / 100) ** 2)
    
    # Створення вхідного масиву
    input_data = np.array([[age, gender,ap_hi,ap_lo, pulse_pressure_index, cholesterol, gluc, smoke, alco, active, bmi]])
    
    # Передбачення
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[:, 1]  # Ймовірність захворювання (якщо підтримується)
    
    # Результат
    return {
        "Prediction": "Has Heart Disease" if prediction[0] == 1 else "No Heart Disease",
        "Probability of Disease": f"{probability[0] * 100:.2f}%" if len(probability) > 0 else "Not available"
    }

# Тест з параметрами
age = 19
gender = 1  # 1 для чоловіків, 0 для жінок
ap_hi = 120
ap_lo = 80
cholesterol = 1.74  # 1: нормальний, 2: трохи підвищений, 3: дуже підвищений
gluc = 4.74         # 1: нормальний, 2: трохи підвищений, 3: дуже підвищений
smoke = 0        # 1 якщо курить, 0 якщо ні
alco = 0         # 1 якщо вживає алкоголь, 0 якщо ні
active = 1       # 1 якщо фізично активний, 0 якщо ні
height = 185     # Зріст у сантиметрах
weight = 75      # Вага в кілограмах

# Передбачення
result = predict_heart_disease(age, gender, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, height, weight)
print("Результат передбачення:")
print(f"- Діагноз: {result['Prediction']}")
print(f"- Ймовірність захворювання: {result['Probability of Disease']}")
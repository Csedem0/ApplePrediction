import joblib
import pickle
from sklearn.utils import validation
from sklearn.preprocessing import StandardScaler




def pred_models_svm(Size, Weight, Sweetness, Crunchiness, Juiciness, Ripeness, Acidity):
    # Load the saved model and scaler
    loaded_model_svm = joblib.load('svm_model.pkl')
    loaded_scaler = joblib.load('scaler.pkl')

    # Scale the input data
    new_input_scaled = loaded_scaler.transform([[Size, Weight, Sweetness, Crunchiness, Juiciness, Ripeness, Acidity]])

     # Update the print statement to exclude text
    print(f"Input values: {Size}, {Weight}, {Sweetness}, {Crunchiness}, {Juiciness}, {Ripeness}, {Acidity}")

    # Get decision function values
    decision_values = loaded_model_svm.decision_function(new_input_scaled)

    # Assuming a higher decision function value corresponds to the positive class
    positive_confidence = decision_values[0]

    # Convert confidence to a percentage (you may need to adjust this based on your data)
    positive_percentage = (1 / (1 + 2.71828**(-positive_confidence))) * 100

    if positive_percentage >= 50:
        prediction_message = f"The quality of the apple is predicted to be GOOD with {positive_percentage:.2f}% confidence."
    else:
        prediction_message = f"The quality of the apple is predicted to be BAD with {100 - positive_percentage:.2f}% confidence."

    return prediction_message
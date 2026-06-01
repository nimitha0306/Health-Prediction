def predict_health(glucose, haemoglobin, cholesterol):
    """
    Simple rule-based medical risk prediction
    """

    if glucose > 160:
        return "High diabetes risk detected"
    elif cholesterol > 240:
        return "High cardiovascular risk detected"
    elif haemoglobin < 10:
        return "Possible anemia detected"
    else:
        return "Normal health indicators"
def predict_health(
        glucose,
        haemoglobin,
        cholesterol):

    remarks = []

    if glucose > 140:
        remarks.append(
            "High diabetes risk"
        )

    if cholesterol > 200:
        remarks.append(
            "High cholesterol risk"
        )

    if haemoglobin < 12:
        remarks.append(
            "Possible anemia"
        )

    if len(remarks) == 0:
        remarks.append(
            "All values appear normal"
        )

    return ", ".join(remarks)
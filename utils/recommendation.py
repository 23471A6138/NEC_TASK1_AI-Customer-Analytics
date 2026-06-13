def recommend(score):

    if score >= 70:
        return "Premium Products"

    elif score >= 40:
        return "Discount Products"

    else:
        return "Basic Products"
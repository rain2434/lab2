def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Determine weight classification
    if bmi < 18.5:
        classification = "Under Weight"
        classification_value = -1
    elif 18.5 <= bmi <= 25.0:
        classification = "Normal Weight"
        classification_value = 0
    else:
        classification = "Over Weight"
        classification_value = 1

    # Display calculated BMI and weight classification
    print("BMI = {:.2f}".format(bmi))
    print("Weight Classification:", classification)

    # Return the weight classification value
    return classification_value
def analyze_csv(file_path):
    """
    A function that analyzes a CSV file of user data and calculates average ages grouped by gender.
    """
    import csv

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        males = []
        females = []
        for row in reader:
            if row["gender"] == "male":
                males.append(int(row["age"]))
            elif row["gender"] == "female":
                females.append(int(row["age"]))
        avg_male = sum(males) / len(males) if males else 0
        avg_female = sum(females) / len(females) if females else 0
        return {"male": avg_male, "female": avg_female}


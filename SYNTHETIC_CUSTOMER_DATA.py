import csv
import os

def load_dataset():
    files = os.listdir("_SOURCE_")
    folder = "_SOURCE_"
    for num,file in enumerate(files,1):
        print(f"{num}:{file}")
    while True:
        try:
            select = int(input("Please select a file: "))
            if 1 <= select <= len(files):
                user_file = files[select - 1]
                break
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please try again.")
    path = os.path.join(folder,user_file)

    data = []

    with open(path, "r") as f:
        read = csv.reader(f)
        for num,row in enumerate(read,1):
            data.append(row)
    return data
def header_row(data):
    
    header = False
    print("\n Here are the first 5 rows of data:")
    for num,row in enumerate(data[:5],1):
        print(f"{num} : {row}")
    while True:
        header = input("Is the first row is a header?(y/n): ").strip().lower()
        if header == "y":
            return True
        elif header == "n":
            return False

        else:
            print("Please enter 'y' or 'n'.")
    return header

def display_data(data,header):
    
    print("\n Here are the first 50 rows of data:")
    start = 1 if header else 0
    for num,row in enumerate(data[start:start + 50],1):
        print(f"{num} : {row}")
    return start

def count_value_dist(data, start):
    age = {}
    income = {}
    score = {}
    visits = {}
    gender = {}
    product = {}
    
    
    for row in data[start:]:
        Age,Annual_Income,Spending_Score,Monthly_Visits,Gender,Preferred_Product = row
        age[Age] = age.get(Age, 0) + 1
        income[Annual_Income] = income.get(Annual_Income, 0) + 1
        score[Spending_Score] = score.get(Spending_Score, 0) + 1
        visits[Monthly_Visits] = visits.get(Monthly_Visits, 0) + 1
        gender[Gender] = gender.get(Gender, 0) + 1
        product[Preferred_Product] = product.get(Preferred_Product, 0) + 1

    return age, income, score, visits, gender, product



def gen_synthetic_data(data, start):
    import random
    synthetic_data = []
    real_rows = data[start:]
    
    print("\nGenerate Synthetic Data:")
    while True:
        try:
            rows = int(input("How many rows of data would you like to generate?: "))
            if rows <= 0:
                print("Please enter a positive non-zero number.")
            else:
                break
        except ValueError:
            print("Invalid input, please enter a positive non-zero number.")

    for _ in range(rows):
        base = random.choice(real_rows).copy()
        
        # numeric noise (adjust ranges as needed)
        try:
            factor = 1 + random.uniform(-0.1, 0.1)
            base[0] = str(int(max(0, int(base[0]) * factor)))
            factor = 1 + random.uniform(-0.05, 0.05)
            base[1] = str(int(max(0, int(base[1]) * factor))) # income
            factor = 1 + random.uniform(-0.08, 0.08)
            base[2] = str(int(max(0, int(base[2]) * factor)))       # score
            factor = 1 + random.uniform(-0.1, 0.1)
            base[3] = str(int(max(0, int(base[3]) * factor)))      # visits
        except:
            pass  # if conversion fails, leave as is

        synthetic_data.append(base)

    print("\nHere are the first 50 rows of synthetic data:")
    for num, row in enumerate(synthetic_data[:50], 1):
        print(f"{num} : {row}")

    return synthetic_data
    
def save_synth(synthetic_data):
    while True:
        name = input("What would you like to name the file?: ").strip().lower()
        if name == '':
            print("Cannot leave value blank, please name the file.")
        elif ".csv" not in name:
            name += ".csv"
            break
        else:
            break

    with open(name,"w", newline = '') as f:
        write = csv.writer(f)
        write.writerows(synthetic_data)
    print(f"Data saved to {name}.")

        
            
    


data = load_dataset()
header = header_row(data)
start = display_data(data,header)
age, income, score, visits, gender, product = count_value_dist(data,start)
synthetic_data = gen_synthetic_data(data, start)
save_synth(synthetic_data)

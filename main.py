with open("cars.csv", "r") as cars_file:
    facts = cars_file.read().splitlines()

    for row in facts:
        row_data = row.split(",")
        print(f"{row_data[0]} was first made in {row_data[1]} and it launched in {row_data[2]}.")
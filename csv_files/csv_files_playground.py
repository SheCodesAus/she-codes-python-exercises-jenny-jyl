# import csv
# with open("2016_pilbara.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(line)

# population = []
# with open("2016_pilbara.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:population.append(line)

# print(population)
# print()

# for age_group in population:
#     print(f"{age_group[0]} {age_group[1]}")

# writing to csv file
# with open("population.csv", mode="w", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")
#     for age_group in population:
#         csv_writer.writerow([age_group[1], age_group[0]])


# import csv

# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(f"{line[1]}, {line[2]}, {line[4]}")


# import csv

# Question 3 - with heading
# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         print(f"{line[4]}, Hex: {line[2]}, RGB: {line[1]}")

# Question 3 - without heading
# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     header = next(csv_file)
#     for line in reader:
#         print(f"{line[4]}, Hex: {line[2]}, RGB: {line[1]}")


# Question 4

# red_counter = 0
# green_counter = 0
# blue_counter = 0
# yellow_counter = 0

# with open("colours_20.csv") as colours_csv:
#     reader = csv.reader(colours_csv)
#     for row in reader:
#         if "red" in row[4]:
#             red_counter += 1
#         elif "green" in row[4]:
#             green_counter += 1
#         elif "blue" in row[4]:
#             blue_counter += 1
#         elif "yellow" in row[4]:
#             yellow_counter += 1

# print(f"Red: {red_counter}")
# print(f"Green: {green_counter}")
# print(f"Blue: {blue_counter}")
# print(f"Yellow: {yellow_counter}")


# Question 5
import csv
min_velocity = 1000000000000000
max_velocity = 0
min_galaxy = ''
max_galaxy = ''


with open("galaxies.csv") as galaxy_csv:
    reader = csv.reader(galaxy_csv)
    next(galaxy_csv)
    # print(list(reader))
    for row in reader:
        # print(row[1], row[0])
        # print(max_velocity, min_velocity)
        if int(row[1]) > max_velocity:
            max_velocity = int(row[1])
            max_galaxy = row[0]
        elif int(row[1]) < min_velocity:
            min_velocity = int(row[1])
            min_galaxy = row[0]

print(f"Galaxy {max_galaxy} has the max velocity of {max_velocity}km/sec")
print(f"Galaxy {min_galaxy} has the min velocity of {min_velocity}km/sec")

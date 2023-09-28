# coordinates = [(0.5, 0.5), (0.5, 5.5), (4.5, 5.5), (4.5, 0.5), (0.5, 1), (0.5, 1.5), (0.5, 2), (0.5, 2.5), (0.5, 3), (0.5, 3.5), (0.5, 4), (0.5, 4.5), (0.5, 5), (0.8865985843534, 5.0167517695583), (1.2409789971872, 4.573776253516), (1.524016052999, 4.2199799337513), (1.835200440328, 3.83099944959), (2.1338749025383, 3.4576563718272), (2.4262944021891, 3.0921319972636), (2.7562436771963, 2.6796954035046), (3.3637569157758, 1.9203038552803), (3.0643005832456, 2.294624270943), (3.7460915022177, 1.4423856222279), (4.0924600539432, 1.009424932571), (4.5, 1), (4.5, 1.5), (4.5, 2), (4.5, 2.5), (4.5, 3), (4.5, 3.5), (4.5, 4), (4.5, 4.5), (4.5, 5), (0.5, 0.5), (0.5, 5.5), (4.5, 5.5), (4.5, 0.5), (0.5, 1), (0.5, 1.5), (0.5, 2), (0.5, 2.5), (0.5, 3), (0.5, 3.5), (0.5, 4), (0.5, 4.5), (0.5, 5), (0.8865985843534, 5.0167517695583), (1.2409789971872, 4.573776253516), (1.524016052999, 4.2199799337513), (1.835200440328, 3.83099944959), (2.1338749025383, 3.4576563718272), (2.4262944021891, 3.0921319972636), (2.7562436771963, 2.6796954035046), (3.3637569157758, 1.9203038552803), (3.0643005832456, 2.294624270943), (3.7460915022177, 1.4423856222279), (4.0924600539432, 1.009424932571), (4.5, 1), (4.5, 1.5), (4.5, 2), (4.5, 2.5), (4.5, 3), (4.5, 3.5), (4.5, 4), (4.5, 4.5), (4.5, 5)]

# # Remove duplicates by converting to a set and back to a list
# cleaned_coordinates = list(set(coordinates))

# # Optionally, sort the coordinates if needed
# cleaned_coordinates.sort()

# # Print the cleaned list
# # for coord in cleaned_coordinates:
# #     print(coord)

# coordinates_N = []

# for coord in cleaned_coordinates:
#     coordinates_N.append((round(coord[0], 2), round(coord[1], 2)))

# print(coordinates_N)

# print(len(coordinates_N))

coordinates = [(0.5, 5.5), (0.5, 0.5), (4.5, 0.5), (4.5, 5.5), (4, 5.5), (3.5, 5.5), (3, 5.5), (2.5, 5.5), (2, 5.5), (1.5, 5.5), (1, 5.5), (0.5, 5), (0.5, 4.5), (0.5, 4), (0.5, 3.5), (0.5, 3), (1, 3), (1.5, 3), (2, 3), (2.5, 3), (3, 3), (3.5, 3), (4, 3), (4.5, 3), (4.5, 2.5), (4.5, 2), (4.5, 1.5), (4.5, 1), (4, 0.5), (3.5, 0.5), (3, 0.5), (2.5, 0.5), (2, 0.5), (1.5, 0.5), (1, 0.5)]

# Remove duplicates by converting to a set and back to a list
cleaned_coordinates = list(set(coordinates))

# Optionally, sort the coordinates if needed
cleaned_coordinates.sort()

# Print the cleaned list
# for coord in cleaned_coordinates:
#     print(coord)

coordinates_s = []

for coord in cleaned_coordinates:
    coordinates_s.append((round(coord[0], 2), round(coord[1], 2)))

print(coordinates_s)

print(len(coordinates_s))


coordinates_S = [
    (0.5, 0.5), (1, 0.5), (1.5, 0.5), (2, 0.5), (2.5, 0.5), (3, 0.5), (3.5, 0.5), 
    (4, 0.5), (4.5, 0.5), (4.5, 1), (4.5, 1.5), (4.5, 2), (4.5, 2.5), (4.5, 3),
    (4, 3), (3.5, 3), (3, 3), (2.5, 3), (2, 3), (1.5, 3), (1, 3), 
    (0.5, 3), (0.5, 3.5), (0.5, 4), (0.5, 4.5), (0.5, 5), (0.5, 5.5), (1, 5.5),   
    (1.5, 5.5), (2, 5.5), (2.5, 5.5), (3, 5.5), (3.5, 5.5), (4, 5.5), (4.5, 5.5)
    ]

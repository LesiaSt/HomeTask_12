import os
import string
from list_film import films_titles,films_awards

#Task 1.

# os.makedirs("Harry_Potter")

print(os.getcwd())

os.chdir("Harry_Potter")
location = os.getcwd()
# for film in films_titles["results"]:
#     title = film["title"]
#     title = title.replace(":","-").replace(" ","_")
#     new_path = os.path.join(location,str(title))
#     os.makedirs(new_path)

# # #Task 2.
list_characters = string.ascii_uppercase
# list_files = os.listdir()

# for dir in os.listdir():
#     list_new_path = os.path.join(location, dir)
#     print(list_new_path)
#     for char in list_characters:
#         # print(os.path.join(list_new_path, str(char)))
#         os.makedirs(os.path.join(list_new_path, str(char)))
# #
# # #Task 3.
# films_titles,films_awards
selected_awards = {}
for title_data in films_titles["results"]:
    imdb_id = title_data["imdb_id"]
    title = title_data["title"]
    awards_for_title = []
    for list in films_awards:
        for award_data in list["results"]:
            if award_data["movie"]["imdb_id"] == imdb_id:
                awards_for_title.append({
                "type": award_data["type"],
                "award_name": award_data["award_name"],
                "award": award_data["award"]
            })
    selected_awards.setdefault(title, awards_for_title)
# # print(selected_awards)


# Task 4.
sorted_data = {movie: sorted(awards, key=lambda x: x['award_name'])
               for movie, awards in selected_awards.items()}
# print(sorted_data)

# # #Task 5.
#ALL CODE
# print(location)
new_selected_awards = {}

for key, value in selected_awards.items():
    new_key = key.replace(":", "-").replace(" ", "_")
    new_selected_awards[new_key] = value
print(new_selected_awards)
#ALL CODE


print(os.listdir())
# if 'Harry_Potter_and_the_Chamber_of_Secrets' in new_selected_awards:
#     print("True")
# for dir in os.listdir():
    # print(new_selected_awards[dir][0]['award_name'])
    # if dir in new_selected_awards.items():
    #     list_new_path = os.path.join(location, dir)
    #
    #     first_letter = new_selected_awards[dir][0]["award_name"][0].upper()
    #     os.chdir(list_new_path)
    #
    #     for each in os.listdir(list_new_path):
    #         # print(each)
    #         list_new_path_1 = os.path.join(list_new_path, each)
    #         # print(list_new_path_1)
    #         if first_letter == each:
    #             # print("True")
    #             file_name = os.path.join(list_new_path_1,f"{new_selected_awards[dir][0]['award_name']}.txt")
    #             with open(file_name, mode="w") as file:
    #                 file.write(f'Award Name: {new_selected_awards[dir][0]["award_name"]}\n')

# This code!!!
# for dir, awards in new_selected_awards.items():
#     print(dir)
#     list_new_path = os.path.join(location, dir)
#     if not os.path.exists(list_new_path):
#         os.makedirs(list_new_path)
#     for award in awards:
#         award_name = award["award_name"]
#         award_type = award["award"]
#
#         first_letter = award_name[0].upper()
#         award_directory = os.path.join(list_new_path, first_letter)
#         if not os.path.exists(award_directory):
#             os.makedirs(award_directory)
#
#         file_name = os.path.join(award_directory, f'{award_name}.txt')
#         with open(file_name, mode="w", encoding="utf-8") as file:
#             file.write('')
#
#
# #Task 6.In the file with the name of each award, transfer all the names of the nominations
# # of this (award) award. ExampleVES Award File:
print(os.getcwd())

awards_by_name = {}
for dir, awards in new_selected_awards.items():
    list_new_path = os.path.join(location, dir)

    # Create the directory if it doesn't exist
    if not os.path.exists(list_new_path):
        os.makedirs(list_new_path)

    for award in awards:
        award_name = award["award_name"]
        award_type = award["award"]

        if award_name not in awards_by_name:
            awards_by_name[award_name] = []
        awards_by_name[award_name].append(award_type)
        # print(award_type)
        first_letter = award_name[0].upper()
        award_directory = os.path.join(list_new_path, first_letter)
        # print(awards_by_name[award_name]["award_type"])

        with open(os.path.join(award_directory, f'{award_name}.txt'), mode="w", encoding="utf-8") as file:
            for each_award in awards_by_name[award_name]:
                # if award_name == each:
                file.write(f'{each_award}\n')





















# read_films = open("test.py")
# new = read_films.readline()
# print(read_films.readlines())

# list_refer_txt = "potter.txt"
# print(os.listdir(list_refer_txt))
# list_refer_txt.close()

# new_obj = open("potter_3.txt", mode = "w")
# new_obj.write("potter_3.txt")
# print(new_obj.writable())
# new_obj.seek()
# print(new_obj_sata)

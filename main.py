import os
import string
import json
from list_film import films_titles,films_awards,ganres,films_data

#Task 1.
#Hide, as created the dir
# os.makedirs("Harry_Potter")

print(os.getcwd())

os.chdir("Harry_Potter")
location = os.getcwd()
#Hide, as created the dirs
# for film in films_titles["results"]:
#     title = film["title"]
#     title = title.replace(":","-").replace(" ","_")
#     new_path = os.path.join(location,str(title))
#     os.makedirs(new_path)

# Task 2.
list_characters = string.ascii_uppercase
# list_files = os.listdir()

#Hide, as created the dirs
# for dir in os.listdir():
#     list_new_path = os.path.join(location, dir)
#     print(list_new_path)
#     for char in list_characters:
#         # print(os.path.join(list_new_path, str(char)))
#         os.makedirs(os.path.join(list_new_path, str(char)))
# Task 3.

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
# print(selected_awards)


# Task 4.
sorted_data = {movie: sorted(awards, key=lambda x: x['award_name'])
               for movie, awards in selected_awards.items()}
# print(sorted_data)

# Task 5.

new_selected_awards = {}
for key, value in selected_awards.items():
    new_key = key.replace(":", "-").replace(" ", "_")
    new_selected_awards[new_key] = value
print(new_selected_awards)
# print(os.listdir())

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

# #Task 6.In the file with the name of each award, transfer all the names of the nominations
# # of this (award) award. ExampleVES Award File:
print(os.getcwd())

awards_by_name = {}
# for dir, awards in new_selected_awards.items():
#     list_new_path = os.path.join(location, dir)
#
#     if not os.path.exists(list_new_path):
#         os.makedirs(list_new_path)
#
#     for award in awards:
#         award_name = award["award_name"]
#         award_type = award["award"]
#
#         if award_name not in awards_by_name:
#             awards_by_name[award_name] = []
#         awards_by_name[award_name].append(award_type)
#         # print(award_type)
#         first_letter = award_name[0].upper()
#         award_directory = os.path.join(list_new_path, first_letter)
#
#         with open(os.path.join(award_directory, f'{award_name}.txt'),
#                   mode="w", encoding="utf-8") as file:
#             for each_award in awards_by_name[award_name]:
#                 file.write(f'{each_award}\n')


#Hometask_13
#Step 1.
ganres_dict = json.loads(ganres)
print(ganres_dict)

#Step 2.
os.chdir("..")
# os.getcwd()
# os.makedirs("Ganres_List")
os.chdir("Ganres_List")
print(os.getcwd())
# for each in ganres_dict["results"]:
#     os.makedirs(each["genre"])

#Step 3.
import csv
location_13 = os.getcwd()
print(location_13)

columns = ["title", "year", "rating", "type", "genres"]

# for ganre in os.listdir():
#     new_location = os.path.join(location_13,ganre,"film.csv")
#     print(new_location)
#     with open (new_location, "w", newline= "") as csv_file:
#         create = csv.DictWriter(csv_file, fieldnames=columns)
#         create.writeheader()

#Step 4.
# location_13 = os.getcwd()
# print(os.getcwd())
#
# for film in films_data:
#     title = film['title']
#     year = film['year']
#     rating = film['rating']
#     movie_type = film['type']
#     genres = ', '.join([g_list['genre'] for g_list in film['gen']])
#
#     for g_list in film['gen']:
#         genre = g_list ['genre']
#
#         new_file_path= os.path.join(location_13, genre, "film.csv")
#         with open(new_file_path, mode='a', newline='',encoding='utf-8') as file_csv:
#             writer = csv.writer(file_csv)
#             # if os.stat(csv_file_path).st_size == 0:
#             #     writer.writerow(['title', 'year', 'rating', 'type', 'genres'])
#             writer.writerow([title, year, rating, movie_type, genres])
#

#Task 1-2
print(os.getcwd())
os.chdir("..")
print(os.getcwd())

# os.makedirs("video_manager")
os.chdir("video_manager")
location_15 = os.getcwd()
# with open(os.path.join(location_15,"media_player.py"), "w") as file:
#     file.write("")
# with open(os.path.join(location_15,"films_worker.py"), "w") as file:
#     file.write("")


#Task 5
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
# os.makedirs("film_player/Film_storage")
os.chdir("film_player/Film_storage")
# print(os.getcwd())
#
# list_characters = string.ascii_uppercase
# print(list_characters)
#
# for word in list_characters:
#     os.makedirs(os.path.join(os.getcwd(),str(word)))















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

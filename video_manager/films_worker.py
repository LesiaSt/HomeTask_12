#Step 6
import os

class Film:
    def __init__(self, title, storage_address):
        self.title = title
        self.description = ""
        self.Director = ""
        self.storage_address = storage_address
        self.budget = 0
        self.video_link = ""

    def upload_file(self):
        first_letter = self.title[0].upper()

        directory_path = os.path.join(self.storage_address, first_letter)
        # os.chdir(directory_path)
        # print(os.getcwd())

        file_path = os.path.join(directory_path,f"{self.title}.txt")
        with open(file_path, "w") as file:
            file.write(f"Information about the movie: {self.title}")

    def get_film_address(self):
        first_letter = self.title[0].upper()
        file_path = os.path.join(self.storage_address, first_letter,f"{self.title}.txt")
        return file_path
# os.chdir("..")
# print(os.getcwd())
if __name__ == "__main__":
    film_title = "Harry_Potter"
    storage_address = "film_player\Film_storage"
    path_start = r'C:\Users\yagodales\PycharmProjects\pythonProject26'
    os.chdir(path_start)

    harry_potter_movie = Film(title=film_title, storage_address=storage_address)

    harry_potter_movie.upload_file()

    film_address = harry_potter_movie.get_film_address()
    print(f"Film Address: {film_address}")




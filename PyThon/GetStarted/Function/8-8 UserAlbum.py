"""
    Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""
# Copy from 8.7


def make_album(artist_name: str, album_title: str, n_songs=None):
    if n_songs:
        album = {
            "Title": album_title,
            "Artist name": artist_name,
            "Number of Songs": n_songs
        }
    else:
        album = {
            "Title": album_title,
            "Artist name": artist_name,
        }
    return album


is_continue = True
while is_continue:
    print("--- Album ---")
    albm_title = input("Title: ")
    artist_name = input("Artist: ")
    print(make_album(artist_name, albm_title))
    _continue = input("Continue (y/n): ")
    is_continue = (_continue == "y")

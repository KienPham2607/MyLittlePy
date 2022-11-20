"""
    Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
    Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.
"""


def make_album(artist_name: str, album_title: str, n_songs=None):
    # None-keyword means a place holder #
    # album = {}
    # album[artist_name] = album_title
    if n_songs:  # execute if n_songs assigned value
        album = {
            "Title": album_title,
            "Artist name": artist_name,
            "Number of Songs": n_songs
        }
    else:  # execute if n_songs not assigned value
        album = {
            "Title": album_title,
            "Artist name": artist_name,
        }
    return album  # or return {artist_name: album_title}


print(make_album("Joji", "25"))
print(make_album("Joji", "25", 10))

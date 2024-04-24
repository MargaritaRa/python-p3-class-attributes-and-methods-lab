class Song:
    
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.add(genre)
        Song.artists.add(artist)
        Song.genre_count[genre] = Song.genre_count.get(genre, 0) + 1
        Song.artist_count[artist] = Song.artist_count.get(artist, 0) + 1

    @classmethod
    def get_song_count(cls):
        return cls.count
    @classmethod
    def get_genres(cls):
        return cls.genres

    @classmethod
    def get_artists(cls):
        return cls.artists
    @classmethod
    def get_genre_count(cls, genre):
        return cls.genre_count.get(genre, 0)

    @classmethod
    def get_artist_count(cls, artist):
        return cls.artist_count.get(artist, 0)

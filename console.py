
from models.album import Album
from models.artist import Artist
import repositories.artist_repository as artist_repository  
import repositories.album_repository as album_repository

# album_repository.delete_all()
# artist_repository.delete_all()


artist_1 = Artist("Kurt Cobain")
artist_repository.save(artist_1)

# album_2 = Album("whatever", artist_1, "rock")
# album_repository.save(album_2)


album_1 = Album("Nevermind", artist_1, "Grunge")
album_repository.save(album_1)

# album_repository.select(1)
# artist_repository.select(1)
# artist_repository.select_all()
# album_repository.select_all()

# pdb.set_trace()

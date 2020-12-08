from models.albulm import Albulm
from models.artist import Artist
import repositories.artist_repository as artist_repository  
import repositories.albulm_repository as albulm_repository


artist_1 = Artist("Kurt Cobain")
artist_repository.save(artist_1)

albulm_1 = Albulm("Nevermind", "Grunge")
albulm_repository.save(albulm_1)
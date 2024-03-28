from pydantic import BaseModel
from datetime import date


class albumCreate(BaseModel):
    AlbumTitle: str
    ArtistId: int


class albumUpdate(albumCreate):
    pass


class albumDelete(albumCreate):
    Id: int


class album(albumCreate):
    Id: int
    DateCreated: date


class artistCreate(BaseModel):
    ArtistName: str


class artistUpdate(artistCreate):
    pass


class artistDelete(artistCreate):
    Id: int


class artist(artistCreate):
    Id: int
    DateCreated: date


class genreCreate(BaseModel):
    GenreName: str


class genreUpdate(genreCreate):
    pass


class genreDelete(genreCreate):
    Id: int


class genre(genreCreate):
    Id: int
    DateCreated: date


class mediatypeCreate(BaseModel):
    MediaTypeName: str


class mediatypeUpdate(mediatypeCreate):
    pass


class mediatypeDelete(mediatypeCreate):
    Id: int


class mediatype(mediatypeCreate):
    Id: int
    DateCreated: date


class playlistCreate(BaseModel):
    PlaylistName: str


class playlistUpdate(playlistCreate):
    pass


class playlistDelete(playlistCreate):
    Id: int


class playlist(playlistCreate):
    Id: int
    DateCreated: date


class trackCreate(BaseModel):
    TrackName: str
    AlbumId: int
    MediaTypeId: int
    GenreId: int
    Composer: str
    Milliseconds: int
    Bytes: int
    UnitPrice: float
    CurrencyId: int


class trackUpdate(trackCreate):
    pass


class trackDelete(trackCreate):
    Id: int


class track(trackCreate):
    Id: int
    DateCreated: date

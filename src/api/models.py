from pydantic import BaseModel
from datetime import date

""" Albums """
class albumCreate(BaseModel):
    AlbumTitle: str
    ArtistId: int

class albumUpdate(albumCreate):
    AlbumTitle: str | None
    ArtistId: int  | None
    #DateUpdated: date | None

class albumDelete(albumCreate):
    Id: int

class album(albumCreate):
    Id: int
    DateCreated: date

""" Artists """
class artistCreate(BaseModel):
    ArtistName: str

class artistUpdate(artistCreate):
    DateUpdated: date

class artistDelete(artistCreate):
    Id: int

class artist(BaseModel):
    Id: int
    DateCreated: date
    
""" Musical Styles """
class genreCreate(BaseModel):
    GenreName: str

class genreUpdate(genreCreate):
    DateUpdated: date

class genreDelete(genreCreate):
    Id: int

class genre(BaseModel):
    Id: int
    DateCreated: date
    
""" MediaType of Track """
class mediatypeCreate(BaseModel):
    MediaTypeName: str

class mediatypeUpdate(mediatypeCreate):
    DateUpdated: date

class mediatypeDelete(mediatypeCreate):
    Id: int

class mediatype(BaseModel):
    Id: int
    DateCreated: date

""" Suggested Mixes """
class playlistCreate(BaseModel):
    PlaylistName: str

class playlistUpdate(playlistCreate):
    DateUpdated: date

class playlistDelete(playlistCreate):
    Id: int

class playlist(BaseModel):
    Id: int
    DateCreated: date

# class customer(Base):
#     """ Customers """
#     Firstname: str
#     Lastname: str
#     Company: str
#     Address: str
#     City: str
#     State: str
#     Country: str
#     Postalcode: str
#     Phone: str
#     Fax: str
#     Email: str  # TODO Valid Email?
#     SupportRepId: str

# class employee(Base):
#     """ Employees """
#     Lastname: str
#     Firstname: str
#     Title: str
#     ReportsTo: int
#     Birthdate: str  # TODO Date
#     Hiredate: str  # TODO Date
#     Address: str
#     City: str
#     State: str
#     Country: str
#     Postalcode: str
#     Phone: str
#     Fax: str
#     Email: str  # TODO Valid Email?

# class invoice(Base):
#     """ Invoices """
#     CustomerId: int
#     InvoiceDate: str
#     BillingAddress: str
#     BillingCity: str
#     BillingState: str
#     BillingCountry: str
#     BillingPostalcode: str
#     Total: Decimal

# class invoiceitem(Base):
#     """ Invoice Items """
#     InvoiceId: int
#     TrackId: int
#     UnitPrice: Decimal
#     Quantity: int

# class track(Base):
#     """ Tracks per Album """
#     TrackName: str
#     AlbumId: int
#     MediaTypeId: int
#     GenreId: int
#     Composer: str
#     Milliseconds: int
#     Bytes: int
#     UnitPrice: Decimal



# class playlisttrack(Base):
#     """ Playlist Tracks """
#     PlaylistId: int
#     TrackId: int

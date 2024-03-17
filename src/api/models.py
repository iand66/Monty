from pydantic import BaseModel
from decimal import Decimal
from datetime import date

""" Albums """
class albumCreate(BaseModel):
    AlbumTitle: str
    ArtistId: int

class albumUpdate(albumCreate):
    #DateUpdated: date | None
    pass

class albumDelete(albumCreate):
    Id: int

class album(albumCreate):
    Id: int
    DateCreated: date

""" Artists """
class artistCreate(BaseModel):
    ArtistName: str

class artistUpdate(artistCreate):
    #DateUpdated: date
    pass

class artistDelete(artistCreate):
    Id: int

class artist(artistCreate):
    Id: int
    DateCreated: date
    
""" Musical Styles """
class genreCreate(BaseModel):
    GenreName: str

class genreUpdate(genreCreate):
    #DateUpdated: date
    pass

class genreDelete(genreCreate):
    Id: int

class genre(genreCreate):
    Id: int
    DateCreated: date
    
""" MediaType of Track """
class mediatypeCreate(BaseModel):
    MediaTypeName: str

class mediatypeUpdate(mediatypeCreate):
    #DateUpdated: date
    pass

class mediatypeDelete(mediatypeCreate):
    Id: int

class mediatype(mediatypeCreate):
    Id: int
    DateCreated: date

""" Suggested Mixes """
class playlistCreate(BaseModel):
    PlaylistName: str

class playlistUpdate(playlistCreate):
    #DateUpdated: date
    pass

class playlistDelete(playlistCreate):
    Id: int

class playlist(playlistCreate):
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
#     Email: str 
#     SupportRepId: str

# class employee(Base):
#     """ Employees """
#     Lastname: str
#     Firstname: str
#     Title: str
#     ReportsTo: int
#     Birthdate: str  
#     Hiredate: str 
#     Address: str
#     City: str
#     State: str
#     Country: str
#     Postalcode: str
#     Phone: str
#     Fax: str
#     Email: str  

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
    
""" Tracks per Album """
class trackCreate(BaseModel):
    TrackName: str
    AlbumId: int
    MediaTypeId: int
    GenreId: int
    Composer: str
    Milliseconds: int
    Bytes: int
    UnitPrice: float

class trackUpdate(trackCreate):
    #DateUpdated: date
    pass

class trackDelete(trackCreate):
    Id: int

class track(trackCreate):
    Id: int
    DateCreated: date

# class playlisttrack(Base):
#     """ Playlist Tracks """
#     PlaylistId: int
#     TrackId: int

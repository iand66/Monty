from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey, Integer, Numeric, String, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Album(Base):
    '''
    Available Albums
    '''
    __tablename__ = 'Albums'
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    AlbumTitle: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    ArtistId: Mapped[int] = mapped_column(ForeignKey('Artists.Id'), nullable=False, index=True)
    DateCreated: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now)
    Tracks = relationship('Track')

class Artist(Base):
    '''
    Recording Artists
    '''
    __tablename__ = 'Artists'
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    ArtistName: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    DateCreated: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now)
    Albums = relationship('Album')

class Genre(Base):
    '''
    Musical Styles
    '''
    __tablename__ = 'Genres'
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    GenreName: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    DateCreated: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now)
    Tracks = relationship('Track')

class Mediatype(Base):
    '''
    MediaType of Track
    '''
    __tablename__ = 'MediaTypes'
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    MediaTypeName: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    DateCreated: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now)
    Tracks = relationship('Track')

class Customer(Base):
    '''
    Customers
    '''
    __tablename__ = 'Customers'
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    Firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    Lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    Company: Mapped[str] = mapped_column(String(50))
    Address: Mapped[str] = mapped_column(String(50))
    City: Mapped[str] = mapped_column(String(25))
    State: Mapped[str] = mapped_column(String(10))
    Country: Mapped[str] = mapped_column(String(15))
    Postalcode: Mapped[str] = mapped_column(String(10))
    Phone: Mapped[str] = mapped_column(String(20))
    Fax: Mapped[str] = mapped_column(String(20))
    Email: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    SupportRepId: Mapped[int] = mapped_column(ForeignKey('Employees.Id'), index=True)
    DateCreated: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now)
    Invoices = relationship('Invoice')

class Employee(Base):
    '''
    Employees
    '''
    __tablename__ = 'Employees'
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    Lastname: Mapped[str] = mapped_column(String(20), nullable=False)
    Firstname: Mapped[str] = mapped_column(String(20), nullable=False)
    Title: Mapped[str] = mapped_column(String(30), nullable=False)
    ReportsTo: Mapped[int] = mapped_column(ForeignKey('Employees.Id'), nullable=False, index=True)
    Birthdate: Mapped[str] = mapped_column(String(16)) # TODO Date?
    Hiredate: Mapped[str] = mapped_column(String(16)) # TODO Date?
    Address: Mapped[str] = mapped_column(String(30))
    City: Mapped[str] = mapped_column(String(25))
    State: Mapped[str] = mapped_column(String(10))
    Country: Mapped[str] = mapped_column(String(10))
    Postalcode: Mapped[str] = mapped_column(String(10))
    Phone: Mapped[str] = mapped_column(String(20))
    Fax: Mapped[str] = mapped_column(String(20))
    Email: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    DateCreated: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now)
    SupportReps = relationship('Customer')
    Employees = relationship('Employee')

class Invoice(Base):
    '''
    Invoices
    '''
    __tablename__ = 'Invoices'
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    CustomerId: Mapped[int] = mapped_column(ForeignKey('Customers.Id'), nullable=False, index=True)
    InvoiceDate: Mapped[DateTime] = mapped_column(String(16)) # TODO Date?
    BillingAddress: Mapped[str] = mapped_column(String(50))
    BillingCity: Mapped[str] = mapped_column(String(25))
    BillingState: Mapped[str] = mapped_column(String(10))
    BillingCountry: Mapped[str] = mapped_column(String(20))
    BillingPostalcode: Mapped[Optional[str]] = mapped_column(String(10))
    Total: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)
    DateCreated: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now)
    InvoiceItems = relationship('Invoiceitem')

class Invoiceitem(Base):
    '''
    Invoice Items
    '''
    __tablename__ = 'InvoiceItems'
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    InvoiceId: Mapped[int] = mapped_column(ForeignKey('Invoices.Id'), nullable=False, index=True)
    TrackId: Mapped[int] = mapped_column(ForeignKey('Tracks.Id'), nullable=False, index=True)
    UnitPrice: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)
    Quantity: Mapped[int] = mapped_column(nullable=False)
    DateCreated: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now)

class Track(Base):
    '''
    Available Tracks per Album
    '''
    __tablename__ = 'Tracks'
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    TrackName: Mapped[str] = mapped_column(String(150), nullable=False)
    AlbumId: Mapped[int] = mapped_column(ForeignKey('Albums.Id'), nullable=False, index=True)
    MediaTypeId: Mapped[int] = mapped_column(ForeignKey('MediaTypes.Id'), nullable=False, index=True)
    GenreId: Mapped[int] = mapped_column(ForeignKey('Genres.Id'), nullable=False, index=True)
    Composer: Mapped[str] = mapped_column(String(200))
    Milliseconds: Mapped[int] = mapped_column(nullable=False)
    Bytes: Mapped[int] = mapped_column()
    UnitPrice: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)
    DateCreated: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now)
    PlaylistTracks = relationship('Playlisttrack')

class Playlist(Base):
    '''
    Suggested Mixes
    '''
    __tablename__ = 'Playlists'
    Id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    PlaylistName: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    DateCreated: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now)
    PlaylistTrack = relationship('Playlisttrack')

class Playlisttrack(Base):
    '''
    Playlist Tracks
    '''
    __tablename__ = 'PlaylistTracks'
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    PlaylistId: Mapped[int] = mapped_column(ForeignKey('Playlists.Id'), nullable=False, index=True)
    TrackId: Mapped[int] = mapped_column(ForeignKey('Tracks.Id'), nullable=False, index=True)
    DateCreated: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.now)

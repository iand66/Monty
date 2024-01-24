from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, DateTime
from sqlalchemy.orm import DeclarativeBase, relationship

#TODO SQLA DataTypes?

class Base(DeclarativeBase):
    pass

class Album(Base):
    #TODO Mapped Columns
    '''
    Available Albums
    '''
    __tablename__ = 'Albums'
    Id = Column(Integer, primary_key=True, nullable=False)
    AlbumTitle = Column(String(160), nullable=False, unique=True)
    ArtistId = Column(Integer, ForeignKey('Artists.Id'), nullable=False, index=True)
    DateCreated = Column(DateTime(timezone=True), default=datetime.now)
    Tracks = relationship('Track')

class Artist(Base):
    #TODO Mapped Columns
    '''
    Recording Artists
    '''
    __tablename__ = 'Artists'
    Id = Column(Integer, primary_key=True, nullable=False)
    ArtistName = Column(String(120), nullable=False, unique=True)
    DateCreated = Column(DateTime(timezone=True), default=datetime.now)
    Albums = relationship('Album')

class Customer(Base):
    #TODO Mapped Columns
    '''
    Customers
    '''
    __tablename__ = 'Customers'
    Id = Column(Integer, primary_key=True, nullable=False)
    Lastname = Column(String(20), nullable=False)
    Firstname = Column(String(40), nullable=False)
    Company = Column(String(80))
    Address = Column(String(70))
    City = Column(String(40))
    State = Column(String(40))
    Country = Column(String(40))
    Postalcode = Column(String(10))
    Phone = Column(String(24))
    Fax = Column(String(24))
    Email = Column(String(60), nullable=False, unique=True)
    SupportRepId = Column(Integer, ForeignKey('Employees.Id'), index=True)
    DateCreated = Column(DateTime(timezone=True), default=datetime.now)
    Invoices = relationship('Invoice')

class Employee(Base):
    #TODO Mapped Columns
    '''
    Employees
    '''
    __tablename__ = 'Employees'
    Id = Column(Integer, primary_key=True, nullable=False)
    Lastname = Column(String(20), nullable=False)
    Firstname = Column(String(20), nullable=False)
    Title = Column(String(30), nullable=False)
    ReportsTo = Column(Integer, ForeignKey('Employees.Id'), nullable=False, index=True)
    Birthdate = Column(String(65))
    Hiredate = Column(String(65))
    Address = Column(String(70))
    City = Column(String(40))
    State = Column(String(40))
    Country = Column(String(40))
    Postalcode = Column(String(10))
    Phone = Column(String(24))
    Fax = Column(String(24))
    Email = Column(String(60), nullable=False, unique=True)
    DateCreated = Column(DateTime(timezone=True), default=datetime.now)
    SupportReps = relationship('Customer')
    Employees = relationship('Employee')

class Genre(Base):
    #TODO Mapped Columns
    '''
    Musical Styles
    '''
    __tablename__ = 'Genres'
    Id = Column(Integer, primary_key=True, nullable=False)
    GenreName = Column(String(120), nullable=False, unique=True)
    DateCreated = Column(DateTime(timezone=True), default=datetime.now)
    Tracks = relationship('Track')

class Invoice(Base):
    #TODO Mapped Columns
    '''
    Invoices
    '''
    __tablename__ = 'Invoices'
    Id = Column(Integer, primary_key=True, nullable=False)
    CustomerId = Column(Integer, ForeignKey('Customers.Id'), nullable=False, index=True)
    InvoiceDate = Column(String(65))
    BillingAddress = Column(String(70))
    BillingCity = Column(String(40))
    BillingState = Column(String(40))
    BillingCountry = Column(String(40))
    BillingPostalcode = Column(String(10))
    Email = Column(String(60))
    Total = Column(Numeric(10, 2), nullable=False)
    DateCreated = Column(DateTime(timezone=True), default=datetime.now)
    InvoiceItems = relationship('Invoiceitem')

class Invoiceitem(Base):
    #TODO Mapped Columns
    '''
    Invoice Items
    '''
    __tablename__ = 'InvoiceItems'
    Id = Column(Integer, primary_key=True, nullable=False)
    InvoiceId = Column(Integer, ForeignKey('Invoices.Id'), nullable=False, index=True)
    TrackId = Column(Integer, ForeignKey('Tracks.Id'), nullable=False, index=True)
    UnitPrice = Column(Numeric(10, 2), nullable=False)
    Quantity = Column(Integer, nullable=False)
    DateCreated = Column(DateTime(timezone=True), default=datetime.now)

class Mediatype(Base):
    #TODO Mapped Columns
    '''
    MediaType of Track
    '''
    __tablename__ = 'MediaTypes'
    Id = Column(Integer, primary_key=True, nullable=False)
    MediaTypeName = Column(String(120), nullable=False, unique=True)
    DateCreated = Column(DateTime(timezone=True), default=datetime.now)
    Tracks = relationship('Track')

class Playlist(Base):
    #TODO Mapped Columns
    '''
    Suggested Mixes
    '''
    __tablename__ = 'Playlists'
    Id = Column(Integer, primary_key=True, nullable=False)
    PlaylistName = Column(String(120), nullable=False, unique=True)
    DateCreated = Column(DateTime(timezone=True), default=datetime.now)
    PlaylistTrack = relationship('Playlisttrack')

class Playlisttrack(Base):
    #TODO Mapped Columns
    '''
    Playlist Tracks
    '''
    __tablename__ = 'PlaylistTracks'
    Id = Column(Integer, primary_key=True, nullable=False)
    PlaylistId = Column(Integer, ForeignKey('Playlists.Id'), nullable=False, index=True)
    TrackId = Column(Integer, ForeignKey('Tracks.Id'), nullable=False, index=True)
    DateCreated = Column(DateTime(timezone=True), default=datetime.now)

class Track(Base):
    #TODO Mapped Columns
    '''
    Available Tracks per Album
    '''
    __tablename__ = 'Tracks'
    Id = Column(Integer, primary_key=True, nullable=False)
    TrackName = Column(String(200), nullable=False)
    AlbumId = Column(Integer, ForeignKey('Albums.Id'), nullable=False, index=True)
    MediaTypeId = Column(Integer, ForeignKey('MediaTypes.Id'), nullable=False, index=True)
    GenreId = Column(Integer, ForeignKey('Genres.Id'), nullable=False, index=True)
    Composer = Column(String(220))
    Milliseconds = Column(Integer, nullable=False)
    Bytes = Column(Integer)
    UnitPrice = Column(Numeric(10, 2), nullable=False)
    DateCreated = Column(DateTime(timezone=True), default=datetime.now)
    PlaylistTracks = relationship('Playlisttrack')

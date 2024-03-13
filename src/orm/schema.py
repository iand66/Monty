from datetime import date
from typing import Optional
from sqlalchemy import ForeignKey, Integer, Numeric, String, UniqueConstraint
from sqlalchemy.types import Date
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column

class Base(DeclarativeBase):
    """ Alchemy Base Class """
    pass

class Album(Base):
    """ Available Albums """
    __tablename__ = "Albums"
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    AlbumTitle: Mapped[str] = mapped_column(String(100), nullable=False)
    ArtistId: Mapped[int] = mapped_column(ForeignKey("Artists.Id"), nullable=False, index=True)
    DateCreated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    DateUpdated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    Tracks = relationship("Track")

    __table_args__ = (UniqueConstraint("AlbumTitle", "ArtistId"),)

class Artist(Base):
    """ Recording Artists """
    __tablename__ = "Artists"
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    ArtistName: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    DateCreated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    DateUpdated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    Albums = relationship("Album")

class Genre(Base):
    """ Musical Styles """
    __tablename__ = "Genres"
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    GenreName: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    DateCreated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    DateUpdated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    Tracks = relationship("Track")

class Mediatype(Base):
    """ MediaType of Track """
    __tablename__ = "MediaTypes"
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    MediaTypeName: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    DateCreated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    DateUpdated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    Tracks = relationship("Track")

class Customer(Base):
    """ Customers """
    __tablename__ = "Customers"
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    Lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    Firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    Company: Mapped[str] = mapped_column(String(50), nullable=True)
    Address: Mapped[str] = mapped_column(String(50), nullable=True)
    City: Mapped[str] = mapped_column(String(25), nullable=True)
    State: Mapped[str] = mapped_column(String(10), nullable=True)
    Country: Mapped[str] = mapped_column(String(15), nullable=True)
    Postalcode: Mapped[str] = mapped_column(String(10), nullable=True)
    Phone: Mapped[str] = mapped_column(String(20), nullable=True)
    Fax: Mapped[str] = mapped_column(String(20), nullable=True)
    Email: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    SupportRepId: Mapped[int] = mapped_column(ForeignKey("Employees.Id"), index=True)
    DateCreated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    DateUpdated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    Invoices = relationship("Invoice")

class Employee(Base):
    """ Employees """
    __tablename__ = "Employees"
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    Lastname: Mapped[str] = mapped_column(String(20), nullable=False)
    Firstname: Mapped[str] = mapped_column(String(20), nullable=False)
    Title: Mapped[str] = mapped_column(String(30), nullable=False)
    ReportsTo: Mapped[int] = mapped_column(ForeignKey("Employees.Id"), nullable=False, index=True)
    Birthdate: Mapped[Date] = mapped_column(String(16), nullable=True)
    Hiredate: Mapped[Date] = mapped_column(String(16), nullable=True)
    Address: Mapped[str] = mapped_column(String(30), nullable=True)
    City: Mapped[str] = mapped_column(String(25), nullable=True)
    State: Mapped[str] = mapped_column(String(10), nullable=True)
    Country: Mapped[str] = mapped_column(String(10), nullable=True)
    Postalcode: Mapped[str] = mapped_column(String(10), nullable=True)
    Phone: Mapped[str] = mapped_column(String(20), nullable=True)
    Fax: Mapped[str] = mapped_column(String(20), nullable=True)
    Email: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    DateCreated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    DateUpdated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    SupportReps = relationship("Customer")
    Employees = relationship("Employee")

class Invoice(Base):
    """ Invoices """
    __tablename__ = "Invoices"
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    CustomerId: Mapped[int] = mapped_column(ForeignKey("Customers.Id"), nullable=False, index=True)
    InvoiceDate: Mapped[Date] = mapped_column(String(16), nullable=True)
    BillingAddress: Mapped[str] = mapped_column(String(50), nullable=True)
    BillingCity: Mapped[str] = mapped_column(String(25), nullable=True)
    BillingState: Mapped[str] = mapped_column(String(10), nullable=True)
    BillingCountry: Mapped[str] = mapped_column(String(20), nullable=True)
    BillingPostalcode: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    Total: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)
    DateCreated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    DateUpdated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    InvoiceItems = relationship("Invoiceitem")

class Invoiceitem(Base):
    """ Invoice Items """
    __tablename__ = "InvoiceItems"
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    InvoiceId: Mapped[int] = mapped_column(ForeignKey("Invoices.Id"), nullable=False, index=True)
    TrackId: Mapped[int] = mapped_column(ForeignKey("Tracks.Id"), nullable=False, index=True)
    UnitPrice: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)
    Quantity: Mapped[int] = mapped_column(nullable=False)
    DateCreated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    DateUpdated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))

class Track(Base):
    """ Available Tracks per Album """
    __tablename__ = "Tracks"
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    TrackName: Mapped[str] = mapped_column(String(150), nullable=False)
    AlbumId: Mapped[int] = mapped_column(ForeignKey("Albums.Id"), nullable=False, index=True)
    MediaTypeId: Mapped[int] = mapped_column(ForeignKey("MediaTypes.Id"), nullable=False, index=True)
    GenreId: Mapped[int] = mapped_column(ForeignKey("Genres.Id"), nullable=False, index=True)
    Composer: Mapped[str] = mapped_column(String(200), nullable=True)
    Milliseconds: Mapped[int] = mapped_column(nullable=True)
    Bytes: Mapped[int] = mapped_column(nullable=True)
    UnitPrice: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)
    DateCreated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    DateUpdated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    PlaylistTracks = relationship("Playlisttrack")

class Playlist(Base):
    """ Suggested Mixes """
    __tablename__ = "Playlists"
    Id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    PlaylistName: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    DateCreated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    DateUpdated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    PlaylistTrack = relationship("Playlisttrack")

class Playlisttrack(Base):
    """ Playlist Tracks """
    __tablename__ = "PlaylistTracks"
    Id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    PlaylistId: Mapped[int] = mapped_column(ForeignKey("Playlists.Id"), nullable=False, index=True)
    TrackId: Mapped[int] = mapped_column(ForeignKey("Tracks.Id"), nullable=False, index=True)
    DateCreated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
    DateUpdated: Mapped[Date] = mapped_column(String(16), nullable=False, default=date.today().strftime("%Y-%m-%d"))
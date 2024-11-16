# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  November 16, 2024 19:33:12
# Database: sqlite:////tmp/tmp.dPA9owprX3-01JCV7AWJJNM498HF082MCRBFE/Clothes_Designer_Brand_Distribution/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Brand(SAFRSBaseX, Base):
    """
    description: A fashion brand associated with designers and collections.
    """
    __tablename__ = 'brand'
    _s_collection_name = 'Brand'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    establishment_year = Column(Integer)
    number_of_designs = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    CampaignList : Mapped[List["Campaign"]] = relationship(back_populates="brand")
    CollectionList : Mapped[List["Collection"]] = relationship(back_populates="brand")



class Designer(SAFRSBaseX, Base):
    """
    description: A designer who creates fashion designs for a brand.
    """
    __tablename__ = 'designer'
    _s_collection_name = 'Designer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_joined = Column(DateTime)
    balance = Column(Integer)

    # parent relationships (access parent)

    # child relationships (access children)
    CollectionList : Mapped[List["Collection"]] = relationship(back_populates="designer")
    SupplyList : Mapped[List["Supply"]] = relationship(back_populates="designer")
    ParticipationList : Mapped[List["Participation"]] = relationship(back_populates="designer")



class Location(SAFRSBaseX, Base):
    """
    description: Describes various geographic locations relevant to stores.
    """
    __tablename__ = 'location'
    _s_collection_name = 'Location'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    region = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)



class Store(SAFRSBaseX, Base):
    """
    description: Store that sells fashion designs from various collections.
    """
    __tablename__ = 'store'
    _s_collection_name = 'Store'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    StockList : Mapped[List["Stock"]] = relationship(back_populates="store")



class Supplier(SAFRSBaseX, Base):
    """
    description: Suppliers providing materials for creating fashion designs.
    """
    __tablename__ = 'supplier'
    _s_collection_name = 'Supplier'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    SupplyList : Mapped[List["Supply"]] = relationship(back_populates="supplier")



class Campaign(SAFRSBaseX, Base):
    """
    description: Marketing campaigns for brand collections.
    """
    __tablename__ = 'campaign'
    _s_collection_name = 'Campaign'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    brand_id = Column(ForeignKey('brand.id'))
    name = Column(String, nullable=False)
    start_date = Column(DateTime)
    end_date = Column(DateTime)

    # parent relationships (access parent)
    brand : Mapped["Brand"] = relationship(back_populates=("CampaignList"))

    # child relationships (access children)
    ParticipationList : Mapped[List["Participation"]] = relationship(back_populates="campaign")



class Collection(SAFRSBaseX, Base):
    """
    description: A collection of fashion designs by a designer under a specific brand.
    """
    __tablename__ = 'collection'
    _s_collection_name = 'Collection'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    designer_id = Column(ForeignKey('designer.id'))
    brand_id = Column(ForeignKey('brand.id'))
    season = Column(String, nullable=False)
    year = Column(Integer)
    total_revenue = Column(Integer)

    # parent relationships (access parent)
    brand : Mapped["Brand"] = relationship(back_populates=("CollectionList"))
    designer : Mapped["Designer"] = relationship(back_populates=("CollectionList"))

    # child relationships (access children)
    DesignList : Mapped[List["Design"]] = relationship(back_populates="collection")



class Supply(SAFRSBaseX, Base):
    """
    description: Details of supplies provided to designers for creating designs.
    """
    __tablename__ = 'supply'
    _s_collection_name = 'Supply'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    supplier_id = Column(ForeignKey('supplier.id'))
    designer_id = Column(ForeignKey('designer.id'))
    material_name = Column(String, nullable=False)
    quantity = Column(Integer)
    date_provided = Column(DateTime)

    # parent relationships (access parent)
    designer : Mapped["Designer"] = relationship(back_populates=("SupplyList"))
    supplier : Mapped["Supplier"] = relationship(back_populates=("SupplyList"))

    # child relationships (access children)



class Design(SAFRSBaseX, Base):
    """
    description: A specific fashion design within a collection.
    """
    __tablename__ = 'design'
    _s_collection_name = 'Design'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    collection_id = Column(ForeignKey('collection.id'))
    name = Column(String, nullable=False)
    type = Column(String)
    amount_sold = Column(Integer)
    unit_price = Column(Integer)
    revenue = Column(Integer)

    # parent relationships (access parent)
    collection : Mapped["Collection"] = relationship(back_populates=("DesignList"))

    # child relationships (access children)
    StockList : Mapped[List["Stock"]] = relationship(back_populates="design")



class Participation(SAFRSBaseX, Base):
    """
    description: Participation of designers in various campaigns.
    """
    __tablename__ = 'participation'
    _s_collection_name = 'Participation'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    designer_id = Column(ForeignKey('designer.id'))
    campaign_id = Column(ForeignKey('campaign.id'))

    # parent relationships (access parent)
    campaign : Mapped["Campaign"] = relationship(back_populates=("ParticipationList"))
    designer : Mapped["Designer"] = relationship(back_populates=("ParticipationList"))

    # child relationships (access children)



class Stock(SAFRSBaseX, Base):
    """
    description: Stock details for designs available at stores.
    """
    __tablename__ = 'stock'
    _s_collection_name = 'Stock'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    store_id = Column(ForeignKey('store.id'))
    design_id = Column(ForeignKey('design.id'))
    quantity = Column(Integer)

    # parent relationships (access parent)
    design : Mapped["Design"] = relationship(back_populates=("StockList"))
    store : Mapped["Store"] = relationship(back_populates=("StockList"))

    # child relationships (access children)
    SaleList : Mapped[List["Sale"]] = relationship(back_populates="stock")



class Sale(SAFRSBaseX, Base):
    """
    description: Sales transactions for specific designs at a store.
    """
    __tablename__ = 'sale'
    _s_collection_name = 'Sale'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    stock_id = Column(ForeignKey('stock.id'))
    sale_date = Column(DateTime, nullable=False)
    amount = Column(Integer, nullable=False)

    # parent relationships (access parent)
    stock : Mapped["Stock"] = relationship(back_populates=("SaleList"))

    # child relationships (access children)

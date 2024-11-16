# using resolved_model gpt-4o-2024-08-06# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from datetime import date   
from datetime import datetime

logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


class Designer(Base):
    """description: A designer who creates fashion designs for a brand."""
    __tablename__ = 'designer'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date_joined = Column(DateTime)
    balance = Column(Integer)  # Derived using logic bank



class Brand(Base):
    """description: A fashion brand associated with designers and collections."""
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    establishment_year = Column(Integer)
    number_of_designs = Column(Integer)  # Derived using logic bank



class Collection(Base):
    """description: A collection of fashion designs by a designer under a specific brand."""
    __tablename__ = 'collection'

    id = Column(Integer, primary_key=True)
    designer_id = Column(Integer, ForeignKey('designer.id'))
    brand_id = Column(Integer, ForeignKey('brand.id'))
    season = Column(String, nullable=False)
    year = Column(Integer)
    total_revenue = Column(Integer)  # Derived using logic bank



class Design(Base):
    """description: A specific fashion design within a collection."""
    __tablename__ = 'design'

    id = Column(Integer, primary_key=True)
    collection_id = Column(Integer, ForeignKey('collection.id'))
    name = Column(String, nullable=False)
    type = Column(String)
    amount_sold = Column(Integer)
    unit_price = Column(Integer)
    revenue = Column(Integer)  # Derived using logic bank as amount_sold * unit_price



class Store(Base):
    """description: Store that sells fashion designs from various collections."""
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)



class Stock(Base):
    """description: Stock details for designs available at stores."""
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('store.id'))
    design_id = Column(Integer, ForeignKey('design.id'))
    quantity = Column(Integer)



class Sale(Base):
    """description: Sales transactions for specific designs at a store."""
    __tablename__ = 'sale'

    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'))
    sale_date = Column(DateTime, nullable=False)
    amount = Column(Integer, nullable=False)



class Location(Base):
    """description: Describes various geographic locations relevant to stores."""
    __tablename__ = 'location'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    region = Column(String)



class Campaign(Base):
    """description: Marketing campaigns for brand collections."""
    __tablename__ = 'campaign'

    id = Column(Integer, primary_key=True)
    brand_id = Column(Integer, ForeignKey('brand.id'))
    name = Column(String, nullable=False)
    start_date = Column(DateTime)
    end_date = Column(DateTime)



class Participation(Base):
    """description: Participation of designers in various campaigns."""
    __tablename__ = 'participation'

    id = Column(Integer, primary_key=True)
    designer_id = Column(Integer, ForeignKey('designer.id'))
    campaign_id = Column(Integer, ForeignKey('campaign.id'))



class Supplier(Base):
    """description: Suppliers providing materials for creating fashion designs."""
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact_info = Column(String)



class Supply(Base):
    """description: Details of supplies provided to designers for creating designs."""
    __tablename__ = 'supply'

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey('supplier.id'))
    designer_id = Column(Integer, ForeignKey('designer.id'))
    material_name = Column(String, nullable=False)
    quantity = Column(Integer)
    date_provided = Column(DateTime)



# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import datetime, date

# Test data for Designer
Designer1 = Designer(id=1, name='John Doe', date_joined=datetime(2020, 5, 5), balance=10000)
Designer2 = Designer(id=2, name='Jane Smith', date_joined=datetime(2021, 7, 7), balance=15000)
Designer3 = Designer(id=3, name='Emily Johnson', date_joined=datetime(2019, 3, 3), balance=12000)
Designer4 = Designer(id=4, name='Michael Brown', date_joined=datetime(2018, 1, 1), balance=20000)

# Test data for Brand
Brand1 = Brand(id=1, name='High Fashion', establishment_year=1990, number_of_designs=50)
Brand2 = Brand(id=2, name='Modern Styles', establishment_year=2005, number_of_designs=30)
Brand3 = Brand(id=3, name='Classic Elegance', establishment_year=1980, number_of_designs=70)
Brand4 = Brand(id=4, name='Urban Wear', establishment_year=2010, number_of_designs=40)

# Test data for Collection
Collection1 = Collection(id=1, designer_id=1, brand_id=1, season='Spring', year=2022, total_revenue=50000)
Collection2 = Collection(id=2, designer_id=2, brand_id=2, season='Fall', year=2021, total_revenue=80000)
Collection3 = Collection(id=3, designer_id=3, brand_id=3, season='Summer', year=2020, total_revenue=100000)
Collection4 = Collection(id=4, designer_id=4, brand_id=4, season='Winter', year=2019, total_revenue=60000)

# Test data for Design
Design1 = Design(id=1, collection_id=1, name='Evening Gown', type='Dress', amount_sold=100, unit_price=200, revenue=20000)
Design2 = Design(id=2, collection_id=2, name='Casual Shirt', type='Top', amount_sold=150, unit_price=50, revenue=7500)
Design3 = Design(id=3, collection_id=3, name='Designer Suit', type='Suit', amount_sold=50, unit_price=400, revenue=20000)
Design4 = Design(id=4, collection_id=4, name='Winter Coat', type='Outerwear', amount_sold=120, unit_price=300, revenue=36000)

# Test data for Store
Store1 = Store(id=1, name='Central Mall', location='Downtown City')
Store2 = Store(id=2, name='Fashion Hub', location='Shopping Park')
Store3 = Store(id=3, name='Luxury Plaza', location='City Center')
Store4 = Store(id=4, name='Style Avenue', location='Suburban')

# Test data for Stock
Stock1 = Stock(id=1, store_id=1, design_id=1, quantity=50)
Stock2 = Stock(id=2, store_id=2, design_id=2, quantity=60)
Stock3 = Stock(id=3, store_id=3, design_id=3, quantity=40)
Stock4 = Stock(id=4, store_id=4, design_id=4, quantity=70)

# Test data for Sale
Sale1 = Sale(id=1, stock_id=1, sale_date=datetime(2023, 1, 10), amount=10)
Sale2 = Sale(id=2, stock_id=2, sale_date=datetime(2023, 1, 15), amount=20)
Sale3 = Sale(id=3, stock_id=3, sale_date=datetime(2023, 1, 20), amount=15)
Sale4 = Sale(id=4, stock_id=4, sale_date=datetime(2023, 1, 25), amount=25)

# Test data for Location
Location1 = Location(id=1, name='New York', region='Northeast')
Location2 = Location(id=2, name='Los Angeles', region='West Coast')
Location3 = Location(id=3, name='Chicago', region='Midwest')
Location4 = Location(id=4, name='Houston', region='South')

# Test data for Campaign
Campaign1 = Campaign(id=1, brand_id=1, name='Spring Launch', start_date=datetime(2023, 3, 1), end_date=datetime(2023, 5, 31))
Campaign2 = Campaign(id=2, brand_id=2, name='Fall Fest', start_date=datetime(2023, 9, 1), end_date=datetime(2023, 11, 30))
Campaign3 = Campaign(id=3, brand_id=3, name='Summer Sale', start_date=datetime(2023, 6, 1), end_date=datetime(2023, 8, 31))
Campaign4 = Campaign(id=4, brand_id=4, name='Winter Wonderland', start_date=datetime(2023, 12, 1), end_date=datetime(2024, 2, 28))

# Test data for Participation
Participation1 = Participation(id=1, designer_id=1, campaign_id=1)
Participation2 = Participation(id=2, designer_id=2, campaign_id=2)
Participation3 = Participation(id=3, designer_id=3, campaign_id=3)
Participation4 = Participation(id=4, designer_id=4, campaign_id=4)

# Test data for Supplier
Supplier1 = Supplier(id=1, name='Fabric World', contact_info='fabric@example.com')
Supplier2 = Supplier(id=2, name='Thread Co', contact_info='thread@example.com')
Supplier3 = Supplier(id=3, name='Zipper Queen', contact_info='zipper@example.com')
Supplier4 = Supplier(id=4, name='Button Kingdom', contact_info='button@example.com')

# Test data for Supply
Supply1 = Supply(id=1, supplier_id=1, designer_id=1, material_name='Silk', quantity=100, date_provided=datetime(2023, 2, 1))
Supply2 = Supply(id=2, supplier_id=2, designer_id=2, material_name='Cotton', quantity=150, date_provided=datetime(2023, 2, 5))
Supply3 = Supply(id=3, supplier_id=3, designer_id=3, material_name='Zippers', quantity=200, date_provided=datetime(2023, 2, 10))
Supply4 = Supply(id=4, supplier_id=4, designer_id=4, material_name='Buttons', quantity=250, date_provided=datetime(2023, 2, 15))



session.add_all([Designer1, Designer2, Designer3, Designer4, Brand1, Brand2, Brand3, Brand4, Collection1, Collection2, Collection3, Collection4, Design1, Design2, Design3, Design4, Store1, Store2, Store3, Store4, Stock1, Stock2, Stock3, Stock4, Sale1, Sale2, Sale3, Sale4, Location1, Location2, Location3, Location4, Campaign1, Campaign2, Campaign3, Campaign4, Participation1, Participation2, Participation3, Participation4, Supplier1, Supplier2, Supplier3, Supplier4, Supply1, Supply2, Supply3, Supply4])
session.commit()

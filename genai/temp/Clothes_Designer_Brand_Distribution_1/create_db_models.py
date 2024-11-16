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
    """description: Designers with unique styles and profiles."""
    __tablename__ = 'designer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    country = Column(String)


class Brand(Base):
    """description: Brands associated with designers and their collections."""
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    designer_id = Column(Integer, ForeignKey('designer.id'))

    designer_name = relationship('Designer')


class Store(Base):
    """description: Stores that retail various designer brands."""
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)


class Collection(Base):
    """description: Collections within a brand that represent seasonal releases."""
    __tablename__ = 'collection'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    season = Column(String)
    year = Column(Integer)
    brand_id = Column(Integer, ForeignKey('brand.id'))

    brand_name = relationship('Brand')


class ClothingItem(Base):
    """description: Individual clothing items that belong to different collections."""
    __tablename__ = 'clothing_item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    size = Column(String)
    price = Column(Integer)
    collection_id = Column(Integer, ForeignKey('collection.id'))

    collection_name = relationship('Collection')


class StoreInventory(Base):
    """description: Inventory records for clothing items in stores."""
    __tablename__ = 'store_inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(Integer, ForeignKey('store.id'))
    clothing_item_id = Column(Integer, ForeignKey('clothing_item.id'))
    quantity_available = Column(Integer)

    store_name = relationship('Store')
    clothing_item_name = relationship('ClothingItem')


class Country(Base):
    """description: Countries where brands are distributed."""
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)


class BrandDistribution(Base):
    """description: Tracks which brands are distributed in which countries."""
    __tablename__ = 'brand_distribution'

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand_id = Column(Integer, ForeignKey('brand.id'))
    country_id = Column(Integer, ForeignKey('country.id'))

    brand_name = relationship('Brand')
    country_name = relationship('Country')


class StoreSales(Base):
    """description: Record of sales made by stores."""
    __tablename__ = 'store_sales'

    id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(Integer, ForeignKey('store.id'))
    date_of_sale = Column(DateTime)
    total_sale_amount = Column(Integer)

    store_name = relationship('Store')


class Customer(Base):
    """description: Customers who purchase clothing items."""
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)


class CustomerPurchase(Base):
    """description: Details of purchases made by customers."""
    __tablename__ = 'customer_purchase'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    clothing_item_id = Column(Integer, ForeignKey('clothing_item.id'))
    purchase_date = Column(DateTime)
    quantity_purchased = Column(Integer)

    customer_name = relationship('Customer')
    clothing_item_name = relationship('ClothingItem')


class DesignerAward(Base):
    """description: Awards received by designers for their contributions."""
    __tablename__ = 'designer_award'

    id = Column(Integer, primary_key=True, autoincrement=True)
    designer_id = Column(Integer, ForeignKey('designer.id'))
    award_name = Column(String)
    year_received = Column(Integer)

    designer_name = relationship('Designer')


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

# Test Data for Designer\ndesigner1 = Designer(name='Armani', country='Italy')\ndesigner2 = Designer(name='Versace', country='Italy')\ndesigner3 = Designer(name='Ralph Lauren', country='USA')\ndesigner4 = Designer(name='Yves Saint Laurent', country='France')\n\n# Test Data for Brand\nbrand1 = Brand(name='Emporio Armani', designer_id=designer1.id)\nbrand2 = Brand(name='Versus', designer_id=designer2.id)\nbrand3 = Brand(name='Polo Ralph Lauren', designer_id=designer3.id)\nbrand4 = Brand(name='Saint Laurent', designer_id=designer4.id)\n\n# Test Data for Store\nstore1 = Store(name='Bloomingdales', location='NYC')\nstore2 = Store(name='Macy's', location='San Francisco')\nstore3 = Store(name='Nordstrom', location='Seattle')\nstore4 = Store(name='Harrods', location='London')\n\n# Test Data for Collection\ncollection1 = Collection(name='Spring 2023', season='Spring', year=2023, brand_id=brand1.id)\ncollection2 = Collection(name='Summer 2023', season='Summer', year=2023, brand_id=brand2.id)\ncollection3 = Collection(name='Fall 2023', season='Fall', year=2023, brand_id=brand3.id)\ncollection4 = Collection(name='Winter 2023', season='Winter', year=2023, brand_id=brand4.id)\n\n# Test Data for ClothingItem\nclothing_item1 = ClothingItem(name='Dress', size='M', price=300, collection_id=collection1.id)\nclothing_item2 = ClothingItem(name='Jacket', size='L', price=500, collection_id=collection2.id)\nclothing_item3 = ClothingItem(name='Coat', size='S', price=700, collection_id=collection3.id)\nclothing_item4 = ClothingItem(name='Jeans', size='M', price=150, collection_id=collection4.id)\n\n# Test Data for StoreInventory\nstore_inventory1 = StoreInventory(store_id=store1.id, clothing_item_id=clothing_item1.id, quantity_available=10)\nstore_inventory2 = StoreInventory(store_id=store2.id, clothing_item_id=clothing_item2.id, quantity_available=5)\nstore_inventory3 = StoreInventory(store_id=store3.id, clothing_item_id=clothing_item3.id, quantity_available=15)\nstore_inventory4 = StoreInventory(store_id=store4.id, clothing_item_id=clothing_item4.id, quantity_available=8)\n\n# Test Data for Country\ncountry1 = Country(name='USA')\ncountry2 = Country(name='Italy')\ncountry3 = Country(name='France')\ncountry4 = Country(name='UK')\n\n# Test Data for BrandDistribution\nbrand_distribution1 = BrandDistribution(brand_id=brand1.id, country_id=country1.id)\nbrand_distribution2 = BrandDistribution(brand_id=brand2.id, country_id=country2.id)\nbrand_distribution3 = BrandDistribution(brand_id=brand3.id, country_id=country3.id)\nbrand_distribution4 = BrandDistribution(brand_id=brand4.id, country_id=country4.id)\n\n# Test Data for StoreSales\nstore_sales1 = StoreSales(store_id=store1.id, date_of_sale=date(2023, 3, 15), total_sale_amount=5000)\nstore_sales2 = StoreSales(store_id=store2.id, date_of_sale=date(2023, 4, 22), total_sale_amount=7000)\nstore_sales3 = StoreSales(store_id=store3.id, date_of_sale=date(2023, 5, 5), total_sale_amount=4500)\nstore_sales4 = StoreSales(store_id=store4.id, date_of_sale=date(2023, 6, 30), total_sale_amount=6200)\n\n# Test Data for Customer\ncustomer1 = Customer(name='Alice', email='alice@example.com')\ncustomer2 = Customer(name='Bob', email='bob@example.com')\ncustomer3 = Customer(name='Charlie', email='charlie@example.com')\ncustomer4 = Customer(name='David', email='david@example.com')\n\n# Test Data for CustomerPurchase\ncustomer_purchase1 = CustomerPurchase(customer_id=customer1.id, clothing_item_id=clothing_item1.id, purchase_date=date(2023, 3, 20), quantity_purchased=2)\ncustomer_purchase2 = CustomerPurchase(customer_id=customer2.id, clothing_item_id=clothing_item2.id, purchase_date=date(2023, 4, 10), quantity_purchased=1)\ncustomer_purchase3 = CustomerPurchase(customer_id=customer3.id, clothing_item_id=clothing_item3.id, purchase_date=date(2023, 5, 17), quantity_purchased=3)\ncustomer_purchase4 = CustomerPurchase(customer_id=customer4.id, clothing_item_id=clothing_item4.id, purchase_date=date(2023, 6, 10), quantity_purchased=1)\n\n# Test Data for DesignerAward\ndesigner_award1 = DesignerAward(designer_id=designer1.id, award_name='Fashion Icon 2023', year_received=2023)\ndesigner_award2 = DesignerAward(designer_id=designer2.id, award_name='Best Creative 2023', year_received=2023)\ndesigner_award3 = DesignerAward(designer_id=designer3.id, award_name='Outstanding Designs 2023', year_received=2023)\ndesigner_award4 = DesignerAward(designer_id=designer4.id, award_name='Innovative Designs 2023', year_received=2023)


session.add_all([# Test Data for Designer\ndesigner1])
session.commit()

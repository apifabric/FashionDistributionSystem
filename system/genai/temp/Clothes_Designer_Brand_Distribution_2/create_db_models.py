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
    """
    description: This table stores information about fashion designers.
    """
    __tablename__ = 'designer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=True)
    established_date = Column(Date, nullable=True)


class Brand(Base):
    """
    description: This table stores information about brands under designers.
    """
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    designer_id = Column(Integer, ForeignKey('designer.id'))
    launch_year = Column(Integer, nullable=True)


class Store(Base):
    """
    description: This table stores information about stores.
    """
    __tablename__ = 'store'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=True)


class RetailDistribution(Base):
    """
    description: This table represents the distribution of brands to stores.
    """
    __tablename__ = 'retail_distribution'

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand_id = Column(Integer, ForeignKey('brand.id'))
    store_id = Column(Integer, ForeignKey('store.id'))
    distribution_date = Column(Date, nullable=True)


class FashionItem(Base):
    """
    description: This table stores information about fashion items.
    """
    __tablename__ = 'fashion_item'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    brand_id = Column(Integer, ForeignKey('brand.id'))
    price = Column(DECIMAL, nullable=True)
    stock_quantity = Column(Integer, nullable=True)


class Customer(Base):
    """
    description: This table stores information about customers.
    """
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)


class Order(Base):
    """
    description: This table stores information about customer orders.
    """
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    order_date = Column(DateTime, nullable=False)
    total_amount = Column(DECIMAL, nullable=True)


class OrderDetail(Base):
    """
    description: This table represents the details of each order.
    """
    __tablename__ = 'order_detail'

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'))
    fashion_item_id = Column(Integer, ForeignKey('fashion_item.id'))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL, nullable=True)
    amount = Column(DECIMAL, nullable=True)


class Promotion(Base):
    """
    description: This table stores information on promotions available at stores.
    """
    __tablename__ = 'promotion'

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand_id = Column(Integer, ForeignKey('brand.id'))
    store_id = Column(Integer, ForeignKey('store.id'))
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    discount_rate = Column(Integer, nullable=True)


class DesignerAward(Base):
    """
    description: This table stores information about awards of designers.
    """
    __tablename__ = 'designer_award'

    id = Column(Integer, primary_key=True, autoincrement=True)
    designer_id = Column(Integer, ForeignKey('designer.id'))
    award_name = Column(String, nullable=False)
    award_year = Column(Integer, nullable=False)


class Inventory(Base):
    """
    description: This table stores inventory details of fashion items in stores.
    """
    __tablename__ = 'inventory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fashion_item_id = Column(Integer, ForeignKey('fashion_item.id'))
    store_id = Column(Integer, ForeignKey('store.id'))
    quantity_in_stock = Column(Integer, nullable=True)


class CustomerFeedback(Base):
    """
    description: This table stores feedback given by customers.
    """
    __tablename__ = 'customer_feedback'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    fashion_item_id = Column(Integer, ForeignKey('fashion_item.id'))
    feedback_text = Column(String, nullable=True)
    feedback_date = Column(DateTime, nullable=False)


# ALS/GenAI: Create an SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ALS/GenAI: Prepare for sample data

from datetime import date, datetime

designer1 = Designer(id=1, name='Gucci', country='Italy', established_date=date(1921, 1, 1))
designer2 = Designer(id=2, name='Versace', country='Italy', established_date=date(1978, 1, 1))
designer3 = Designer(id=3, name='Prada', country='Italy', established_date=date(1913, 1, 1))
designer4 = Designer(id=4, name='Armani', country='Italy', established_date=date(1975, 1, 1))

brand1 = Brand(id=1, name='Gucci Mainline', designer_id=1, launch_year=1921)
brand2 = Brand(id=2, name='Versace Jeans Couture', designer_id=2, launch_year=1988)
brand3 = Brand(id=3, name='Prada Linea Rossa', designer_id=3, launch_year=1997)
brand4 = Brand(id=4, name='Emporio Armani', designer_id=4, launch_year=1981)

store1 = Store(id=1, name='Luxury Fashion', location='Paris')
store2 = Store(id=2, name='Designer Outlet', location='New York')
store3 = Store(id=3, name='High Street Beacons', location='London')
store4 = Store(id=4, name='Fashion Hub', location='Milan')

retail_distribution1 = RetailDistribution(id=1, brand_id=1, store_id=1, distribution_date=date(2020, 1, 10))
retail_distribution2 = RetailDistribution(id=2, brand_id=2, store_id=2, distribution_date=date(2020, 1, 15))
retail_distribution3 = RetailDistribution(id=3, brand_id=3, store_id=3, distribution_date=date(2020, 2, 20))
retail_distribution4 = RetailDistribution(id=4, brand_id=4, store_id=4, distribution_date=date(2020, 3, 25))

fashion_item1 = FashionItem(id=1, name='Gucci Dress', brand_id=1, price=Decimal('1500.00'), stock_quantity=20)
fashion_item2 = FashionItem(id=2, name='Versace T-shirt', brand_id=2, price=Decimal('250.00'), stock_quantity=50)
fashion_item3 = FashionItem(id=3, name='Prada Sneakers', brand_id=3, price=Decimal('700.00'), stock_quantity=30)
fashion_item4 = FashionItem(id=4, name='Armani Suit', brand_id=4, price=Decimal('2000.00'), stock_quantity=10)

customer1 = Customer(id=1, name='John Doe', email='john@example.com')
customer2 = Customer(id=2, name='Jane Smith', email='jane@example.com')
customer3 = Customer(id=3, name='Alice Brown', email='alice@example.com')
customer4 = Customer(id=4, name='Bob Martin', email='bob@example.com')

order1 = Order(id=1, customer_id=1, order_date=datetime(2023, 11, 25), total_amount=Decimal('5000.00'))
order2 = Order(id=2, customer_id=2, order_date=datetime(2023, 11, 26), total_amount=Decimal('2000.00'))
order3 = Order(id=3, customer_id=3, order_date=datetime(2023, 11, 27), total_amount=Decimal('1500.00'))
order4 = Order(id=4, customer_id=4, order_date=datetime(2023, 11, 28), total_amount=Decimal('3000.00'))

order_detail1 = OrderDetail(id=1, order_id=1, fashion_item_id=1, quantity=2, unit_price=Decimal('1500.00'), amount=Decimal('3000.00'))
order_detail2 = OrderDetail(id=2, order_id=2, fashion_item_id=2, quantity=3, unit_price=Decimal('250.00'), amount=Decimal('750.00'))
order_detail3 = OrderDetail(id=3, order_id=3, fashion_item_id=3, quantity=2, unit_price=Decimal('700.00'), amount=Decimal('1400.00'))
order_detail4 = OrderDetail(id=4, order_id=4, fashion_item_id=4, quantity=2, unit_price=Decimal('2000.00'), amount=Decimal('4000.00'))

promotion1 = Promotion(id=1, brand_id=1, store_id=1, start_date=date(2023, 11, 1), end_date=date(2023, 11, 30), discount_rate=10)
promotion2 = Promotion(id=2, brand_id=2, store_id=2, start_date=date(2023, 12, 1), end_date=date(2023, 12, 31), discount_rate=15)
promotion3 = Promotion(id=3, brand_id=3, store_id=3, start_date=date(2023, 11, 15), end_date=date(2023, 12, 15), discount_rate=20)
promotion4 = Promotion(id=4, brand_id=4, store_id=4, start_date=date(2023, 12, 10), end_date=date(2023, 12, 20), discount_rate=5)

designer_award1 = DesignerAward(id=1, designer_id=1, award_name='Best Luxury Fashion', award_year=2020)
designer_award2 = DesignerAward(id=2, designer_id=2, award_name='Innovative Design', award_year=2019)
designer_award3 = DesignerAward(id=3, designer_id=3, award_name='Sustainable Fashion', award_year=2021)
designer_award4 = DesignerAward(id=4, designer_id=4, award_name='Emerging Talent', award_year=2022)

inventory1 = Inventory(id=1, fashion_item_id=1, store_id=1, quantity_in_stock=10)
inventory2 = Inventory(id=2, fashion_item_id=2, store_id=2, quantity_in_stock=15)
inventory3 = Inventory(id=3, fashion_item_id=3, store_id=3, quantity_in_stock=20)
inventory4 = Inventory(id=4, fashion_item_id=4, store_id=4, quantity_in_stock=5)

customer_feedback1 = CustomerFeedback(id=1, customer_id=1, fashion_item_id=1, feedback_text='Loved it!', feedback_date=datetime(2023, 11, 26))
customer_feedback2 = CustomerFeedback(id=2, customer_id=2, fashion_item_id=2, feedback_text='Great fit.', feedback_date=datetime(2023, 11, 27))
customer_feedback3 = CustomerFeedback(id=3, customer_id=3, fashion_item_id=3, feedback_text='Very comfortable.', feedback_date=datetime(2023, 11, 28))
customer_feedback4 = CustomerFeedback(id=4, customer_id=4, fashion_item_id=4, feedback_text='Too expensive.', feedback_date=datetime(2023, 11, 29))


session.add_all([designer1, designer2, designer3, designer4, brand1, brand2, brand3, brand4, store1, store2, store3, store4, retail_distribution1, retail_distribution2, retail_distribution3, retail_distribution4, fashion_item1, fashion_item2, fashion_item3, fashion_item4, customer1, customer2, customer3, customer4, order1, order2, order3, order4, order_detail1, order_detail2, order_detail3, order_detail4, promotion1, promotion2, promotion3, promotion4, designer_award1, designer_award2, designer_award3, designer_award4, inventory1, inventory2, inventory3, inventory4, customer_feedback1, customer_feedback2, customer_feedback3, customer_feedback4])
session.commit()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
import sys

# Which database engine we want to communicate with
engine = create_engine('sqlite:///restaurantmenu.db')

# Make the connections between our class definitions and the corresponding tables within our database.
Base.metadata.bind = engine

# Create a sessionmaker object
DBSession = sessionmaker(bind = engine)

# Create an instance of a DBSession.
session = DBSession()

# CRUD Create
# Create a new restaurant in Restaurant table
Restaurant1 = Restaurant(name = 'Pizza Place')

session.add(Restaurant1)

session.commit()

Restaurant2 = Restaurant(name = 'Thai')

session.add(Restaurant2)

session.commit()

# Create an item in MenuItem table
cheesepizza = MenuItem(name = 'Cheese Pizza', description = 'Made with all natural ingredients and fresh mozzarella', course = 'Entree', price = '$8.99', restaurant = Restaurant1)

session.add(cheesepizza)

session.commit()

# CRUD Read
# Query the Restaurant table
# queryRestaurant = session.query(Restaurant).all()
# queryRestaurant1 = session.query(Restaurant).first()

# print([x.name for x in queryRestaurant])
# print(queryRestaurant1.name)

# Return the full SELECT statement represented by this Query, converted to a scalar subquery
print(session.query(Restaurant).as_scalar())

# Return metadata about the columns which would be returned by this Query
print(session.query(Restaurant).column_descriptions)

# Return a count of rows this the SQL formed by this Query would return
print(session.query(Restaurant).count())

# apply the given filtering criterion to a copy of this Query
# print(session.query(Restaurant).filter(Restaurant.name == 'Thai'))

# return a Query that selects from this Query’s SELECT statement
# print(session.query(Restaurant).filter(Restaurant.name.like('Th%')).from_self())

firstRestaurant = session.query(Restaurant).filter_by(name = 'Pizza Place')
print([(x.name, x.id) for x in firstRestaurant])

# CRUD Update
# .one() return exactly one result or raise an exception
updateRestaurant1 = session.query(Restaurant).filter_by(id = 103).one()
print(updateRestaurant1.name)

updateRestaurant1.name = 'Super Stir Fry'

session.add(updateRestaurant1)

session.commit()

print(updateRestaurant1.name)

# CRUD Delete
deleteRestaurant = session.query(Restaurant).filter_by(id = 13).one()

session.delete(deleteRestaurant)

session.commit()

try:
    print(session.query(Restaurant).filter_by(id = 13).one())
except:
    print(sys.exc_info()[1])




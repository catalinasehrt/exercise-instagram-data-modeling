import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Apellidos = Column(String(250))    
    Contraseña=Column(String(20)) 
    Edad = Column (String(2))
    Email= Column(String(250))

class Publicacion(Base):
    __tablename__= 'Publicacion'
    id = Column(Integer, primary_key=True)
    Usuario_id = Column(Integer,ForeignKey('Usuario.id'))
    Genero = Column(String(100))
    Relacion_usuario = relationship('Usuario')
   
  
   

class Likes (Base):
    __tablename__='Likes'
    id = Column(Integer, primary_key=True)
    Usuario_publicacion= Column(Integer,ForeignKey('Publicacion.id'))
    Usuario_id = Column(Integer,ForeignKey('Usuario.id'))
    Relacion_usuario = relationship('Usuario')
    Relacion_publicacion = relationship('Post')  
    
    
 
class Comentarios(Base):    
    __tablename__ = 'Comentarios'
    id = Column(Integer, primary_key=True)
    Usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    Usuario_publicacion = Column(Integer, ForeignKey('Publicacion.id'))
    Relacion_usuario = relationship('Usuario')
    Relacion_publicacion = relationship('Post')
   
class Seguidores(Base):
    __tablename__ = 'Seguidores'
    id = Column(Integer,primary_key=True)
    User_from_id = Column(Integer,ForeignKey('Usuario.id'))
    User_to_id = Column(String(50))
    Relacion_usuario = relationship('Usuario')

    







# class Usuario(base):
#     __tablename__ = 'Usuario'
#     id = Column(Integer,primary_key=True)
#     Nombre = Column(String(100))
#     Apellido = Column(String(100))
#     Contraseña = Column(String(50))
#     Email = Column(String(100))

# class Publicacion(base):
#     __tablename__ = 'Publicacion'
#     id = Column(Integer,primary_key=True)
#    Descripcion = Column(String(100))
#    Usuario_id = Column(Integer,ForeignKey('Usuario.id'))
#    Relacion_usuario = relationship('Usuario')
   

# class Likes(base):
#     __tablename__ = 'Likes'
#     id = Column(Integer,primary_key=True)
#     Usuario_id = Column(Integer,ForeignKey('Usuario.id'))
#     Usuario_publicacion = Column(Integer,ForeignKey('Publicacion.id'))
#     relacion_usuario = relationship('Usuario')
#     relacion_publicacion = relationship('Publicacion')
    
    

# class Comentarios(base):
#     __tablename__ ='Comentarios'
#     id = Column(Integer,primary_key=True)
#     Usuario_id = Column(Integer,ForeignKey('usuario_id'))
#     Usuario_publicacion = Column(Integer,ForeignKey('publicacion.id'))
#     Usuario_comentarios = Column(String(5000))
    



# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

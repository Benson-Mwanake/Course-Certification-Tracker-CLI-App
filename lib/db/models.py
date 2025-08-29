import os
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "certification_tracker.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, future=True, echo=False)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, future=True)
Base = declarative_base()


class Institution(Base):
    __tablename__ = "institutions"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    year = Column(Integer)
    type = Column(String)

    courses = relationship("Course", back_populates="institution")

    def __repr__(self):
        return f"<Institution {self.id}: {self.name}>"


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    institution_id = Column(Integer, ForeignKey("institutions.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text)
    duration = Column(String)

    institution = relationship("Institution", back_populates="courses")
    certifications = relationship("Certification", back_populates="course")

    def __repr__(self):
        return f"<Course {self.id}: {self.name}>"


class Certification(Base):
    __tablename__ = "certifications"

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    title = Column(String, nullable=False)
    level = Column(String)
    issue_date = Column(Date)
    expiry_date = Column(Date)

    course = relationship("Course", back_populates="certifications")

    def __repr__(self):
        return f"<Certification {self.id}: {self.title}>"


def init_db():
    Base.metadata.create_all(bind=engine)

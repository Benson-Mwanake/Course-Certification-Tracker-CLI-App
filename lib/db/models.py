import os
from datetime import date
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    Date,
    ForeignKey,
)
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
    location = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    type = Column(String, nullable=True)

    courses = relationship(
        "Course", back_populates="institution", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Institution {self.id}: {self.name} ({self.location or 'N/A'})>"


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    institution_id = Column(Integer, ForeignKey("institutions.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    duration = Column(String, nullable=True)

    institution = relationship("Institution", back_populates="courses")
    certifications = relationship(
        "Certification", back_populates="course", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Course {self.id}: {self.name}>"


class Certification(Base):
    __tablename__ = "certifications"

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    title = Column(String, nullable=False)
    level = Column(String, nullable=True)
    issue_date = Column(Date, nullable=True)
    expiry_date = Column(Date, nullable=True)

    course = relationship("Course", back_populates="certifications")

    @property
    def is_expired(self) -> bool:
        return bool(self.expiry_date and self.expiry_date < date.today())

    @property
    def days_to_expiry(self):
        if not self.expiry_date:
            return None
        return (self.expiry_date - date.today()).days

    @property
    def status(self) -> str:
        if self.expiry_date is None:
            return "No Expiry"
        if self.is_expired:
            return "Expired"
        days = self.days_to_expiry
        if days is not None and days <= 30:
            return "Expiring Soon"
        return "Valid"

    def __repr__(self):
        return f"<Certification {self.id}: {self.title} ({self.status})>"


def init_db():
    """Create tables if they do not exist."""
    Base.metadata.create_all(bind=engine)

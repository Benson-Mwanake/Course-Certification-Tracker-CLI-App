from datetime import date, timedelta
from .models import SessionLocal, init_db, Institution, Course, Certification


def seed():
    init_db()
    session = SessionLocal()

    if session.query(Institution).count() > 0:
        session.close()
        print("Database already seeded.")
        return

    ms = Institution(
        name="Moringa School", location="Nairobi", year=2014, type="Bootcamp"
    )
    uni = Institution(
        name="Example University", location="Nairobi", year=2000, type="University"
    )
    session.add_all([ms, uni])
    session.flush()

    ds = Course(
        institution_id=ms.id,
        name="Data Science",
        description="Python, SQL, ML",
        duration="6 months",
    )
    se = Course(
        institution_id=ms.id,
        name="Software Engineering",
        description="Backend + Frontend",
        duration="12 months",
    )
    ai = Course(
        institution_id=uni.id,
        name="AI Fundamentals",
        description="Intro to AI",
        duration="1 semester",
    )
    session.add_all([ds, se, ai])
    session.flush()

    today = date.today()
    session.add_all(
        [
            Certification(
                course_id=ds.id,
                title="Pandas Pro",
                level="Associate",
                issue_date=today,
                expiry_date=today + timedelta(days=30),
            ),
            Certification(
                course_id=se.id,
                title="Web APIs",
                level="Professional",
                issue_date=today,
                expiry_date=today + timedelta(days=90),
            ),
            Certification(
                course_id=ai.id,
                title="AI Ethics",
                level="Associate",
                issue_date=today,
                expiry_date=None,
            ),
        ]
    )

    session.commit()
    session.close()
    print("Database seeded!")


if __name__ == "__main__":
    seed()

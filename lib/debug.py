from lib.db.models import SessionLocal, init_db, Institution, Course, Certification


def debug():
    init_db()
    session = SessionLocal()
    print("\n--- Institutions ---")
    for inst in session.query(Institution).all():
        print(inst)
    print("\n--- Courses ---")
    for c in session.query(Course).all():
        print(c)
    print("\n--- Certifications ---")
    for cert in session.query(Certification).all():
        print(cert, "| Status:", cert.status)
    session.close()


if __name__ == "__main__":
    debug()

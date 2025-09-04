import sys
from lib.db.models import SessionLocal, init_db, Institution, Course, Certification
from lib.helpers import (
    clear_screen,
    prompt_int,
    prompt_non_empty,
    prompt_date,
    confirm,
    divider,
)


# ---------------------- Entrypoint ----------------------
def run_cli():
    init_db()
    while True:
        clear_screen()
        print("===========================================")
        print("  Course & Certification Tracker (Basic)")
        print("===========================================")
        print("1. Manage Institutions")
        print("2. Manage Courses")
        print("3. Manage Certifications")
        print("4. View Reports")
        print("5. Exit")
        print("-------------------------------------------")
        choice = input("Select an option: ").strip()

        if choice == "1":
            institutions_menu()
        elif choice == "2":
            courses_menu()
        elif choice == "3":
            certifications_menu()
        elif choice == "4":
            reports_menu()
        elif choice == "5":
            print("\nThanks for using the tracker. Goodbye! 👋")
            sys.exit(0)
        else:
            input("\nInvalid choice. Press Enter to try again...")


# ---------------------- Institutions ----------------------
def institutions_menu():
    while True:
        clear_screen()
        print("\n--- Institutions Menu ---")
        print("1. Add Institution")
        print("2. List Institutions")
        print("3. Update Institution")
        print("4. Delete Institution")
        print("5. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_institution()
        elif choice == "2":
            list_institutions(pause=True)
        elif choice == "3":
            update_institution()
        elif choice == "4":
            delete_institution()
        elif choice == "5":
            break
        else:
            input("\nInvalid choice. Press Enter to try again...")


def add_institution():
    clear_screen()
    print("Add Institution")
    name = prompt_non_empty("Name: ")
    location = input("Location (optional): ").strip() or None
    year = prompt_int("Year (e.g., 2019, blank to skip): ", allow_blank=True)
    inst_type = input("Type (e.g., Bootcamp/University, optional): ").strip() or None

    session = SessionLocal()
    try:
        inst = Institution(name=name, location=location, year=year, type=inst_type)
        session.add(inst)
        session.commit()
        print(f"\nSaved: {inst}")
    except Exception as e:
        session.rollback()
        print(f"\nError saving institution: {e}")
    finally:
        session.close()
        input("\nPress Enter to continue...")


def list_institutions(pause=False):
    session = SessionLocal()
    rows = session.query(Institution).order_by(Institution.name.asc()).all()
    divider("Institutions")
    if not rows:
        print("No institutions found.")
    else:
        for r in rows:
            print(
                f"[{r.id}] {r.name} | {r.location or 'N/A'} | Year: {r.year or '-'} | Type: {r.type or '-'}"
            )
    session.close()
    if pause:
        input("\nPress Enter to continue...")


def choose_institution(session):
    list_institutions()
    inst_id = prompt_int("\nEnter Institution ID: ")
    inst = session.get(Institution, inst_id)
    if not inst:
        print("Invalid Institution ID.")
        return None
    return inst


def update_institution():
    clear_screen()
    session = SessionLocal()
    try:
        inst = choose_institution(session)
        if not inst:
            input("\nPress Enter to continue...")
            return

        print(f"\nEditing: {inst}")
        new_name = input(f"Name [{inst.name}]: ").strip() or inst.name
        new_location = (
            input(f"Location [{inst.location or ''}]: ").strip() or inst.location
        )
        new_year_input = input(f"Year [{inst.year or ''}]: ").strip()
        new_year = int(new_year_input) if new_year_input.isdigit() else inst.year
        new_type = input(f"Type [{inst.type or ''}]: ").strip() or inst.type

        inst.name, inst.location, inst.year, inst.type = (
            new_name,
            new_location,
            new_year,
            new_type,
        )
        session.commit()
        print("\nUpdated successfully.")
    except Exception as e:
        session.rollback()
        print(f"\nError updating institution: {e}")
    finally:
        session.close()
        input("\nPress Enter to continue...")


def delete_institution():
    clear_screen()
    session = SessionLocal()
    try:
        inst = choose_institution(session)
        if not inst:
            input("\nPress Enter to continue...")
            return
        print(
            f"\nThis will delete the institution and ALL its courses & certifications:\n  {inst}"
        )
        if confirm():
            session.delete(inst)
            session.commit()
            print("Deleted.")
        else:
            print("Cancelled.")
    except Exception as e:
        session.rollback()
        print(f"\nError deleting institution: {e}")
    finally:
        session.close()
        input("\nPress Enter to continue...")


# ---------------------- Courses ----------------------
def courses_menu():
    while True:
        clear_screen()
        print("\n--- Courses Menu ---")
        print("1. Add Course")
        print("2. List Courses")
        print("3. Update Course")
        print("4. Delete Course")
        print("5. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_course()
        elif choice == "2":
            list_courses(pause=True)
        elif choice == "3":
            update_course()
        elif choice == "4":
            delete_course()
        elif choice == "5":
            break
        else:
            input("\nInvalid choice. Press Enter to try again...")


def list_courses(pause=False):
    session = SessionLocal()
    institutions = session.query(Institution).order_by(Institution.name).all()
    if not institutions:
        print("\nNo institutions yet.")
        session.close()
        if pause:
            input("\nPress Enter to continue...")
        return

    for inst in institutions:
        divider(f"{inst.name} ({inst.location or 'N/A'})")
        if not inst.courses:
            print("  (no courses)")
        else:
            for c in inst.courses:
                course_tuple = (c.id, c.name, c.duration or "-")
                print(
                    f"  [{course_tuple[0]}] {course_tuple[1]} | Duration: {course_tuple[2]}"
                )
                if c.description:
                    print(f"     - {c.description}")
    session.close()
    if pause:
        input("\nPress Enter to continue...")


def add_course():
    clear_screen()
    session = SessionLocal()
    try:
        inst = choose_institution(session)
        if not inst:
            input("\nPress Enter to continue...")
            return
        print(f"\nAdding course under: {inst.name}")
        name = prompt_non_empty("Course name: ")
        desc = input("Description (optional): ").strip() or None
        duration = input("Duration (e.g., '6 months', optional): ").strip() or None

        c = Course(
            institution_id=inst.id, name=name, description=desc, duration=duration
        )
        session.add(c)
        session.commit()
        print(f"\nSaved: [{c.id}] {c.name}")
    except Exception as e:
        session.rollback()
        print(f"\nError adding course: {e}")
    finally:
        session.close()
        input("\nPress Enter to continue...")


def choose_course(session):
    list_courses()
    cid = prompt_int("\nEnter Course ID: ")
    c = session.get(Course, cid)
    if not c:
        print("Invalid Course ID.")
        return None
    return c


def update_course():
    clear_screen()
    session = SessionLocal()
    try:
        c = choose_course(session)
        if not c:
            input("\nPress Enter to continue...")
            return

        print(f"\nEditing: [{c.id}] {c.name}")
        new_name = input(f"Name [{c.name}]: ").strip() or c.name
        new_desc = (
            input(f"Description [{c.description or ''}]: ").strip() or c.description
        )
        new_duration = input(f"Duration [{c.duration or ''}]: ").strip() or c.duration

        c.name, c.description, c.duration = new_name, new_desc, new_duration
        session.commit()
        print("\nUpdated successfully.")
    except Exception as e:
        session.rollback()
        print(f"\nError updating course: {e}")
    finally:
        session.close()
        input("\nPress Enter to continue...")


def delete_course():
    clear_screen()
    session = SessionLocal()
    try:
        c = choose_course(session)
        if not c:
            input("\nPress Enter to continue...")
            return
        if confirm(f"Delete course [{c.id}] {c.name}? [y/N]: "):
            session.delete(c)
            session.commit()
            print("Deleted.")
        else:
            print("Cancelled.")
    except Exception as e:
        session.rollback()
        print(f"\nError deleting course: {e}")
    finally:
        session.close()
        input("\nPress Enter to continue...")


# ---------------------- Certifications ----------------------
def certifications_menu():
    while True:
        clear_screen()
        print("\n--- Certifications Menu ---")
        print("1. Add Certification")
        print("2. List Certifications")
        print("3. Update Certification")
        print("4. Delete Certification")
        print("5. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_certification()
        elif choice == "2":
            list_certifications(pause=True)
        elif choice == "3":
            update_certification()
        elif choice == "4":
            delete_certification()
        elif choice == "5":
            break
        else:
            input("\nInvalid choice. Press Enter to try again...")


def list_certifications(pause=False):
    session = SessionLocal()
    certs = (
        session.query(Certification)
        .join(Course)
        .join(Institution)
        .order_by(Institution.name, Course.name, Certification.title)
        .all()
    )
    divider("Certifications")
    if not certs:
        print("No certifications found.")
    else:
        for c in certs:
            inst = c.course.institution
            print(
                f"[{c.id}] {c.title} | Level: {c.level or '-'} | Course: {c.course.name} | Inst: {inst.name}"
            )
            print(
                f"     Issued: {c.issue_date or '-'} | Expires: {c.expiry_date or '—'} | Status: {c.status}"
            )
    session.close()
    if pause:
        input("\nPress Enter to continue...")


def add_certification():
    clear_screen()
    session = SessionLocal()
    try:
        c = choose_course(session)
        if not c:
            input("\nPress Enter to continue...")
            return
        print(f"\nAdding certification under course: {c.name}")
        title = prompt_non_empty("Title: ")
        level = input("Level (optional): ").strip() or None
        issue = prompt_date(
            "Issue date (YYYY-MM-DD, blank to skip): ", allow_blank=True
        )
        expiry = prompt_date(
            "Expiry date (YYYY-MM-DD, blank if none): ", allow_blank=True
        )

        cert = Certification(
            course_id=c.id,
            title=title,
            level=level,
            issue_date=issue,
            expiry_date=expiry,
        )
        session.add(cert)
        session.commit()
        print(f"\nSaved: [{cert.id}] {cert.title} ({cert.status})")
    except Exception as e:
        session.rollback()
        print(f"\nError adding certification: {e}")
    finally:
        session.close()
        input("\nPress Enter to continue...")


def choose_certification(session):
    list_certifications()
    cid = prompt_int("\nEnter Certification ID: ")
    cert = session.get(Certification, cid)
    if not cert:
        print("Invalid Certification ID.")
        return None
    return cert


def update_certification():
    clear_screen()
    session = SessionLocal()
    try:
        cert = choose_certification(session)
        if not cert:
            input("\nPress Enter to continue...")
            return

        print(f"\nEditing: [{cert.id}] {cert.title}")
        new_title = input(f"Title [{cert.title}]: ").strip() or cert.title
        new_level = input(f"Level [{cert.level or ''}]: ").strip() or cert.level
        issue_in = input(f"Issue date [{cert.issue_date or ''}]: ").strip()
        expiry_in = input(f"Expiry date [{cert.expiry_date or ''}]: ").strip()

        if issue_in:
            from datetime import datetime

            cert.issue_date = datetime.strptime(issue_in, "%Y-%m-%d").date()
        if expiry_in:
            from datetime import datetime

            cert.expiry_date = datetime.strptime(expiry_in, "%Y-%m-%d").date()
        if expiry_in == "":
            cert.expiry_date = None

        cert.title, cert.level = new_title, new_level
        session.commit()
        print("\nUpdated successfully.")
    except Exception as e:
        session.rollback()
        print(f"\nError updating certification: {e}")
    finally:
        session.close()
        input("\nPress Enter to continue...")


def delete_certification():
    clear_screen()
    session = SessionLocal()
    try:
        cert = choose_certification(session)
        if not cert:
            input("\nPress Enter to continue...")
            return
        if confirm(f"Delete certification [{cert.id}] {cert.title}? [y/N]: "):
            session.delete(cert)
            session.commit()
            print("Deleted.")
        else:
            print("Cancelled.")
    except Exception as e:
        session.rollback()
        print(f"\nError deleting certification: {e}")
    finally:
        session.close()
        input("\nPress Enter to continue...")


# ---------------------- Reports ----------------------
def reports_menu():
    while True:
        clear_screen()
        print("\n--- Reports Menu ---")
        print("1. View All Certifications by Institution")
        print("2. View Expiring (≤30 days) / Expired")
        print("3. Back to Main Menu")
        choice = input("Select an option: ").strip()

        if choice == "1":
            report_certs_by_institution()
        elif choice == "2":
            report_expiry_overview()
        elif choice == "3":
            break
        else:
            input("\nInvalid choice. Press Enter to try again...")


def report_certs_by_institution():
    session = SessionLocal()
    institutions = session.query(Institution).order_by(Institution.name).all()
    if not institutions:
        print("\nNo data.")
        session.close()
        input("\nPress Enter to continue...")
        return

    report = {}
    for inst in institutions:
        course_list = []
        for course in inst.courses:
            certs = [
                (cert.title, cert.status) for cert in course.certifications
            ]
            course_list.append((course.name, certs))
        report[inst.name] = course_list

    divider("Certifications by Institution")
    for inst_name, courses in report.items():
        print(f"\n{inst_name}")
        if not courses:
            print("  (no courses)")
            continue
        for course_name, certs in courses:
            print(f"  Course: {course_name}")
            if not certs:
                print("    (no certifications)")
            else:
                for title, status in certs:
                    print(f"    - {title} ({status})")
    session.close()
    input("\nPress Enter to continue...")


def report_expiry_overview():
    session = SessionLocal()
    from datetime import date, timedelta

    today = date.today()
    soon = today + timedelta(days=30)

    certs = (
        session.query(Certification)
        .order_by(Certification.expiry_date.asc().nulls_last())
        .all()
    )
    divider("Expiry Overview")
    found = False
    for c in certs:
        if c.expiry_date is None:
            continue
        if c.expiry_date <= soon or c.is_expired:
            found = True
            print(
                f"[{c.id}] {c.title} | Course: {c.course.name} | Inst: {c.course.institution.name} | Expires: {c.expiry_date} | Status: {c.status}"
            )
    if not found:
        print("No expiring or expired certifications within 30 days.")
    session.close()
    input("\nPress Enter to continue...")

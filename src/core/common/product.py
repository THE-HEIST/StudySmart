from src.data_processing_module.config import Users, Assignments
from src.core.authentication.controllers import LogIn, LogOut, SignUp
from src.core.authentication.session import load_session
from src.core.common.calculate_priority import re_calculate_priority
from src.core.read.assignments import view_assignments, view_order_by_undone, view_order_by_done, view_order_all, show_study_summary
from src.core.create.assignments import add_assignment
from src.core.update.assignments import update_assignment
from src.core.update.mark_as_done import mark_completed, undo_mark_as_done

def check_priority_new_day(Assignments=Assignments):
    ass = re_calculate_priority(Assignments.all("assignments"))
    #Assignments.clear_all("assignments")
    assignments = {"last_id": Assignments.get_last_id("assignments"), "assignments": ass}
    Assignments.save(assignments)

def print_menu(items):
    print()
    header = ["No", "Function Name"]
    print("{:<5} {:<35}".format(*header))
    print("-" * 45)
    for no, name in items:
        print("{:<5} {:<35}".format(no, name))
    print()

def view_func(session=load_session(), Assignments=Assignments):
    menu = [
        (1, "View Undone Assignments"),
        (2, "View Done Assignments"),
        (3, "View All Assignments")
    ]
    print_menu(menu)
    sub_choice = int(input("Enter your choice: "))
    print()
    if sub_choice == 1:
        assignments = view_order_by_undone(session=session, Assignments=Assignments)
        view_assignments(Assignments=Assignments, assignments=assignments)
    elif sub_choice == 2:
        assignments = view_order_by_done(session=session, Assignments=Assignments)
        view_assignments(Assignments=Assignments, assignments=assignments)
    elif sub_choice == 3:
        assignments = view_order_all(session=session, Assignments=Assignments)
        view_assignments(Assignments=Assignments, assignments=assignments)

def clear_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def main(Assignments=Assignments):
    check_priority_new_day(Assignments=Assignments)
    session = load_session()
    if session:
        menu = [
            (1, "View Assignments"),
            (2, "Add Assignment"),
            (3, "Update Assignment"),
            (4, "Mark Assignment as Done"),
            (5, "Undo Mark Assignment as Done"),
            (6, "Show Study Summary"),
            (7, "Clear Terminal"),
            (0, "Exit w/o Logout"),
            (-1, "Logout")
        ]
        while True:
            username = session.get('username') if isinstance(session, dict) else session
            print(f"\nWelcome back, {username}!")
            print_menu(menu)
            try:
                choice = int(input("Enter your choice: "))
                print()
                if choice == 1:
                    view_func(session=session, Assignments=Assignments)
                elif choice == 2:
                    add_assignment()
                elif choice == 3:
                    update_assignment(assignments=view_order_all())
                elif choice == 4:
                    mark_completed(assignments=view_order_by_undone())
                elif choice == 5:
                    undo_mark_as_done(assignments=view_order_by_done())
                elif choice == 6:
                    show_study_summary(assignments=view_order_all())
                elif choice == 7:
                    clear_terminal()
                elif choice == 0:
                    break
                elif choice == -1:
                    LogOut()
                    print("\nLogged out successfully.\n")
                    break
                else:
                    print("\nInvalid choice. Please try again.\n")
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
        

from src.data_processing_module.config import Users, Assignments
from src.core.authentication.controllers import LogIn, LogOut, SignUp
from src.core.authentication.session import load_session
from src.core.common.calculate_priority import re_calculate_priority
from src.core.read.assignments import view_assignments, view_order_by_undone, view_order_by_done, view_order_all
from src.core.create.assignments import add_assignment
from src.core.update.assignments import update_assignment
from src.core.update.mark_as_done import mark_completed, undo_mark_as_done

def check_priority_new_day():
    ass = re_calculate_priority(Assignments.all("assignments"))
    Assignments.clear_all("assignments")
    Assignments.save(ass)

def view_func():
    print("""
        1. View Undone Assignments
        2. View Done Assignments
        3. View All Assignments
    """)
    sub_choice = int(input("Enter your choice: "))
    if sub_choice == 1:
        assignments = view_order_by_undone(session=session)
        view_assignments(assignments)
    elif sub_choice == 2:
        assignments = view_order_by_done(session=session)
        view_assignments(assignments)
    elif sub_choice == 3:
        assignments = view_order_all(session=session)
        view_assignments(assignments)

def clear_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    check_priority_new_day()
    session = load_session()
    if session:
        print(f"Welcome back, {session['username']}!")
        while True:
            print("""
                1. View Assignments
                2. Add Assignment
                3. Update Assignment
                4. Mark Assigment as Done
                5. Undo Mark Assignment as Done
                6. Show Study Summary
                7. Clear Terminal
                0. Exit w/o Logout
                -1. Logout
            """)
            choice = int(input("Enter your choice: "))
            if choice == 1:
                view_func()
            elif choice == 2:
                add_assignment()
            elif choice == 3:
                update_assignment()
            elif choice == 4:
                mark_completed(view_order_by_undone(session=session))
            elif choice == 5:
                undo_mark_as_done(view_order_by_done(session=session))
            elif choice == 6:
                show_study_summary(view_order_all(session=session))
            elif choice == 7:
                clear_terminal()
            elif choice == 0:
                break
            elif choice == -1:
                LogOut()
                print("Logged out successfully.")
                break
            else:
                print("Invalid choice. Please try again.")
        

from src.data_processing_module.config import Users, Assignments
from src.core.common.product import main

WELLCOME_TEXT = """
********************

WELLCOME TO STUDYSMART

********************
"""

def print_menu(items):
    header = ["No", "Function Name"]
    print("{:<5} {:<35}".format(*header))
    print("-" * 45)
    for no, name in items:
        print("{:<5} {:<35}".format(no, name))

print(WELLCOME_TEXT)

main()
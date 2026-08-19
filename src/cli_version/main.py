# This is the main program of the project. In here, we will import and combine every function for the complete game 
# To see how to make the function for the game, check outs in "./example/demo.py"

# This program will be the example one how we will combine the code together
from .example import demo
import time

start = time.now()
demo.demo_question_print_function()
demo.demo_question_answer_function()
stop = time.now()

spend = stop - start
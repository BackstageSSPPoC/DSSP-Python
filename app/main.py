from calculator import add, divide
from utils.helper import log_message

log_message("Application Started")

print("Addition Result:", add(10, 5))

# Intentional error for Jenkins AI Explain Demo
print("Division Result:", divide(10, 0))

log_message("Application Finished")
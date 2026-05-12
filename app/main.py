from calculator import add, divide

print("[LOG] Application Started")

print("Addition Result:", add(10, 5))

try:
    print("Division Result:", divide(10, 0))
except ValueError as e:
    print(f"[ERROR] {e}")

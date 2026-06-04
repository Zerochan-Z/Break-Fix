# Can you do this without looking up?
import os

# 1. Check current directory
print(os.getcwd())

# 2. Create a file if it doesn't exist
if not os.path.exists('data.csv'):
    with open('data.csv', 'w') as f:
        f.write('id,price\n1,60000')

# 3. Safely read it
try:
    with open('data.csv', 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("File still missing? Something's wrong.")
def mean(data):
   
    if len(data) >= 1:
        mean = sum(data) / len(data)
        return mean
   
    print('The data is empty.')
    return None 

print(mean([10, 20, 30]))   # Should print: 20.0
print(mean([]))              # Should print: Error message and None


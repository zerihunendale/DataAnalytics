transaction=[300,700,250,500,900]
#print(transaction)
filtered = [lis for lis in transaction if lis >=500]
print(f"Filtered {filtered}")
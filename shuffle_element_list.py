import random

original_list = ["a",5,8,"b","c",9,"d"]
shuffled_list = random.sample(original_list, len(original_list))

print("Original list:", original_list)
print("Shuffled list:", shuffled_list)

#Q. Given a set of 10 cartoons students from a python class, Tom, Jerry, Pikachu, Spidey, Doraemon, Chota Bheem, Nagraj , Balveer, Motu and Patlu, where three students went for the Plantation drive (spidey, motu and patlu), three student went to military exhibition (Nagraj, Pikachu, Spidey). Doaremon and Balveer only attend the class. Write a python script to determine 1. who attended both events. 2. who attended only one event 3. who bunked the class
# List of students in the class
students = {'Tom', 'Jerry', 'Pikachu', 'Spidey', 'Doraemon', 'Chota Bheem', 'Nagraj', 'Balveer', 'Motu', 'Patlu'}
plantation_drive = {'Spidey', 'Motu', 'Patlu'}

military_exhibition = {'Nagraj', 'Pikachu', 'Spidey'}

attended_class_only = {'Doraemon', 'Balveer'}

both_events = plantation_drive.intersection(military_exhibition)

only_one_event = plantation_drive.symmetric_difference(military_exhibition)

attended_any_event = plantation_drive.union(military_exhibition).union(attended_class_only)
bunked_class = students - attended_any_event

# Output results
print("Students who attended both events:", both_events)
print("Students who attended only one event:", only_one_event)
print("Students who bunked the class:", bunked_class)

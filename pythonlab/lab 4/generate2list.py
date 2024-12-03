# generate 2 lists . create a new list with both course code and name like ["CS1001:PYTHON",..]
# List of course codes
# List of course codes
course_codes=list(map(str,input("Enter code names :").split()))
# course_codes = ["CS1001", "CS1002", "CS1003"]

course_names=list(map(str,input("Enter course names :").split()))
# course_names = ["PYTHON", "DATA STRUCTURES", "ALGORITHMS"]

courses = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]

print(courses)


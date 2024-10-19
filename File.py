import pandas as pd

# Courses, Names, Credits, Prerequisites
# Assumes placement past MATH 112Z
cs_courses = {
    "Course Code": ["CS 210", "CS 211", "CS 212", "MATH 231", "MATH 232", "MATH 251"],
    "Course Name": ["Computer Science I", "Computer Science II", "Computer Science III",
                    "Elements of Discrete Mathematics I", "Elements of Discrete Mathematics II", "Calculus I"],
    "Credits": [4, 4, 4, 4, 4, 4],
    "Prerequisites": ["None", "CS 210", "CS 211", "MATH 251", "MATH 231", "None"],
    "Terms Offered": [["Fall", "Spring"], ["Winter", "Spring"], ["Fall", "Spring"], ["Fall", "Winter", "Spring"],
                      ["Fall", "Winter", "Spring"], ["Fall", "Winter", "Spring"]]
}


# Create a DataFrame
courses_df = pd.read_csv("CS.csv")

# Display the DataFrame
print(courses_df)

import itertools
import random

# Sample data: Lecturers, courses, groups, classrooms, and constraints
lecturers_courses = {
    'Lecturer1': {'CourseA', 'CourseB', 'CourseC'},
    'Lecturer2': {'CourseB', 'CourseD', 'CourseE'},
    'Lecturer3': {'CourseA', 'CourseD', 'CourseF'}
}

groups_courses = {
    'Group1': {'CourseA', 'CourseB'},
    'Group2': {'CourseC', 'CourseD'},
    'Group3': {'CourseE', 'CourseF'}
}

classrooms = {'Classroom1', 'Classroom2', 'Classroom3'}

# Define a 5-day week and time slots for lectures
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
time_slots = ['9:00-10:30', '10:45-12:15', '1:00-2:30', '2:45-4:15']

# Initialize schedules for lecturers, groups, courses, and classrooms
lecturer_schedule = {lecturer: {day: {time_slot: set() for time_slot in time_slots} for day in days} for lecturer in lecturers_courses}
group_schedule = {group: {day: {time_slot: set() for time_slot in time_slots} for day in days} for group in groups_courses}
course_schedule = {course: {day: {time_slot: set() for time_slot in time_slots} for day in days} for courses in lecturers_courses.values() for course in courses}
classroom_schedule = {classroom: {day: {time_slot: set() for time_slot in time_slots} for day in days} for classroom in classrooms}

# Randomly assign courses to time slots for lecturers, groups, and classrooms
for lecturer, schedule in lecturer_schedule.items():
    for day, time_slots_data in schedule.items():
        for time_slot in time_slots_data:
            random_course = random.choice(list(lecturers_courses[lecturer]))
            lecturer_schedule[lecturer][day][time_slot].add(random_course)

for group, schedule in group_schedule.items():
    for day, time_slots_data in schedule.items():
        for time_slot in time_slots_data:
            random_course = random.choice(list(groups_courses[group]))
            group_schedule[group][day][time_slot].add(random_course)

for classroom, schedule in classroom_schedule.items():
    for day, time_slots_data in schedule.items():
        for time_slot in time_slots_data:
            random_course = random.choice(list(lecturers_courses[random.choice(list(lecturers_courses))]))
            classroom_schedule[classroom][day][time_slot].add(random_course)

# Display schedules (for demonstration purposes)
print("Lecturer Schedules:")
for lecturer, schedule in lecturer_schedule.items():
    print(f"{lecturer}'s Schedule:")
    for day, time_slots_data in schedule.items():
        print(f"  {day}:")
        for time_slot, courses in time_slots_data.items():
            print(f"    {time_slot}: {', '.join(courses)}")

print("\nGroup Schedules:")
for group, schedule in group_schedule.items():
    print(f"{group}'s Schedule:")
    for day, time_slots_data in schedule.items():
        print(f"  {day}:")
        for time_slot, courses in time_slots_data.items():
            print(f"    {time_slot}: {', '.join(courses)}")

print("\nClassroom Schedules:")
for classroom, schedule in classroom_schedule.items():
    print(f"{classroom}'s Schedule:")
    for day, time_slots_data in schedule.items():
        print(f"  {day}:")
        for time_slot, courses in time_slots_data.items():
            print(f"    {time_slot}: {', '.join(courses)}")

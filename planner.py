def generate_schedule(subjects, total_hours):
    total_priority = sum(priority for _, priority in subjects)

    schedule = {}

    for subject, priority in subjects:
        allocated_time = (priority / total_priority) * total_hours
        schedule[subject] = round(allocated_time, 2)

    return schedule
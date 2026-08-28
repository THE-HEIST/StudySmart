def show_study_summary(assignments):
    total_assignments = len(assignments)
    completed_count = 0
    incomplete_count = 0

    for assignment in assignments:
        if assignment["completed"]:
            completed_count = completed_count + 1
        else:
            incomplete_count = incomplete_count + 1

    if total_assignments == 0:
        completion_rate = 0
    else:
        completion_rate = (completed_count / total_assignments) * 100

    print("Total assignments:", total_assignments)
    print("Completed:", completed_count)
    print("Incomplete:", incomplete_count)
    print(f"Completion rate: {completion_rate}%")
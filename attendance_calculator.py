# Attendance Calculation of a student for a semester

def attendace_percentage_of_each(j, hours_conducted):
    percentage = (j / hours_conducted) * 100
    return round(percentage, 2)


def cal_total_percent(total_hours_attended, total_hours_conducted):
    total_percent = (total_hours_attended / total_hours_conducted) * 100
    return total_percent


hours_conducted = float(input("Enter the total no.of hours:"))
subjects = int(input("Enter the no.of subjects:"))
total_hours_conducted = hours_conducted * subjects
hours_attended = []
for i in range(subjects):
    each_class_hours_attended = float(input("Enter no.of hours attended:"))
    hours_attended.append(each_class_hours_attended)
print(hours_attended)

attendace_percentage_of_each_sub = []
for j in hours_attended:
    each_percent = attendace_percentage_of_each(j, hours_conducted)
    attendace_percentage_of_each_sub.append(each_percent)

print(attendace_percentage_of_each_sub)

total_hours_attended = sum(hours_attended)
total_percentage = cal_total_percent(total_hours_attended, total_hours_conducted)

count = 0
for k in attendace_percentage_of_each_sub:
    if (k < 40):
        count += 1

if (count >= 2 or total_percentage < 75):
    print("Detained")
else:
    print("Can Write the exams")
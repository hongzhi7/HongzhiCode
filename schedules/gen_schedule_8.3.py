
import json

# 答疑课缩写还原映射
replace_map = {
    '生化答疑': '生物、化学答疑',
    '数化答疑': '数学、化学答疑',
    '数物答疑': '数学、物理答疑',
    '物生答疑': '物理、生物答疑',
}

# 时间安排（15个时段）
time_slots = [
    ("07:10:00", "07:40:00", False),   # 早读
    ("07:45:00", "08:25:00", False),   # 1
    ("08:50:00", "09:30:00", False),   # 2
    ("09:40:00", "10:20:00", False),   # 3
    ("10:30:00", "11:10:00", False),   # 4
    ("11:20:00", "12:00:00", True),    # 5 (IsSplitBelow: true)
    ("14:30:00", "15:10:00", False),   # 6
    ("15:20:00", "16:00:00", False),   # 7
    ("16:40:00", "17:20:00", False),   # 8
    ("17:25:00", "18:25:00", True),    # 导练 (IsSplitBelow: true)
    ("19:05:00", "19:50:00", False),   # 晚自习二
    ("20:00:00", "20:40:00", False),   # 晚自习三
    ("20:50:00", "21:30:00", False),   # 晚自习四(前)
    ("21:30:00", "22:10:00", False),   # 晚自习四(后)
]

# 课程数据（横向排布，按星期）
courses_by_day = {
    "Monday":    ["语文", "生物", "英语", "化学", "物理", "数学", "体育", "语文", "数学双定", "生物", "生物", "化学双定", "语文双定", "物理双定"],
    "Tuesday":   ["英语", "英语", "数学", "数学", "生物", "物理", "化学", "生化答疑", "物理双定", "语文", "语文", "数学双定", "英语双定", "生物双定"],
    "Wednesday": ["语文", "英语", "物理", "生物", "数学", "化学", "体育", "语文", "数化答疑", "数学", "数学", "化学双定", "语文双定", "物理双定"],
    "Thursday":  ["英语", "化学", "英语", "生物", "语文", "物理", "数学", "数物答疑", "班会", "物理", "物理", "数学双定", "英语双定", "生物双定"],
    "Friday":    ["语文", "数学", "化学", "英语", "生物", "语文", "物理", "物生答疑", "数学双定", "英语", "英语", "化学双定", "语文双定", "物理双定"],
    "Saturday":  ["英语", "英语", "数学", "物理", "化学", "生物", "体育", "语文", "语文", "化学", "化学", "数学双定", "英语双定", "生物双定"],
}

# 时段标签（仅用于判断导练时段）
slot_labels = [
    "早读", "1", "2", "3", "4", "5", "6", "7", "8", "导练", "导讲", "晚自习三", "晚自习四", "晚自习四"
]

# 构建JSON
result = {}
for day, courses in courses_by_day.items():
    day_schedule = []
    for i, (start, end, is_split) in enumerate(time_slots):
        subject = replace_map.get(courses[i], courses[i])
        label = slot_labels[i]
        # 只有导练时段后面加"导练"
        if label == "早读":
            subject = f"{subject}早读"
        if label == "导练":
            subject = f"{subject}导练"
        if label == "导讲":
            subject = f"{subject}导讲"
        day_schedule.append({
            "Subject": subject,
            "StartTime": start,
            "EndTime": end,
            "IsSplitBelow": is_split,
            "IsStrongClassOverNotificationEnabled": False
        })
    result[day] = day_schedule

# 输出美化JSON
json_output = json.dumps(result, ensure_ascii=False, indent=2)
# print(json_output)

with open(".\\schedule_8.3_bscompatible.json", 'w', encoding = 'utf-8') as f:
    f.write(json_output)


# Moataz-project
#المشروع يعرض كيفية تطبيق الخوارزميات في معالجة وتحليل البيانات اللي يمتلكها

#هنا نحط البيانات او المعلومات اللي عندنا
#نحط المعلومات و نعرفها ك متغير people

people = [
    {"Ta_Name":"Tasneem", "Ta_Age":19, "Ta_Amount _insured ($)":70},
    {"Ta_Name":"Mohammad", "Ta_Age":22, "Ta_Amount _insured ($)":90},
    {"Ta_Name":"Salim", "Ta_Age":27, "Ta_Amount _insured ($)":90},
    {"Ta_Name":"Maryam", "Ta_Age":20, "Ta_Amount _insured ($)":100},
    {"Ta_Name":"Maria", "Ta_Age":29, "Ta_Amount _insured ($)":50},
    {"Ta_Name":"Khalid", "Ta_Age":34, "Ta_Amount _insured ($)":90},
    {"Ta_Name":"Rashid", "Ta_Age":25, "Ta_Amount _insured ($)":100},
    {"Ta_Name":"Omar", "Ta_Age":21, "Ta_Amount _insured ($)":80},
    {"Ta_Name":"Salma", "Ta_Age":28, "Ta_Amount _insured ($)":120},
    {"Ta_Name":"Sultan", "Ta_Age":20, "Ta_Amount _insured ($)":100}
]

#هنا نستخدم الدالة selection_sort_people عشان نرتب المعلومات اللي في المتغير people
#طبعاً الترتيب المستخدم هو ترتيب تصاعدي
def selection_sort_people(people):
    N = len(people)
    for i in range(N):
        min_index = i
        for j in range(i+1, N):
            if people[j]['Ta_Amount _insured ($)'] < people[min_index]['Ta_Amount _insured ($)']:
                min_index = j
        people[i], people[min_index] = people[min_index], people[i]
    return people

sorted_people = selection_sort_people(people)

#و من هنا نطبع المخرجات اللي حصلنا عليها وبالترتيب المطلوب
for person in sorted_people:
    print(person)

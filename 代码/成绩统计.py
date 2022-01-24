test, final = {}, {}
people, score = input("请输入学生的人数和课程门数，并以空格进行分隔").split()
people, score = int(people), int(score)
while(people>0):
    name = input("请键入学生学号")
    test[name] = []
    grade = input("请键入此学号学生成绩，以空格分隔").split()
    sum = 0
    for i in grade:
        test[name].append(int(i))
        sum += int(i)
        final[name] = sum
    people -= 1
print(test)
print(final)

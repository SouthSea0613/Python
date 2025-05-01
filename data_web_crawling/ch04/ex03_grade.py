students = { 
    '김파이': [60, 72, 90], 
    '이파이': [80, 65, 88], 
    '박파이': [92, 90, 100], 
    '최파이': [77, 80, 74] 
}

#print(students)
#print(students.items())
for name, scores in students.items():
    #print(name)
    #print(scores)
    #print(sum(scores))
    print(name, "의 점수 합계는", sum(scores), ", 평균점수는", sum(scores)/len(scores))

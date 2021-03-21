people_number = 1
day_number = 365
none_same_probability = day_number/365
same_probability = 1 - none_same_probability

while same_probability < 0.5:
    people_number += 1
    print(people_number)
    day_number -= 1
    none_same_probability = none_same_probability*day_number/365
    same_probability = 1-none_same_probability
    print(same_probability)

print('至少有一对人的生日相同的概率为50%的人数是'+str(people_number)+'人')
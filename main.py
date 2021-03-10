import json


def print_avg():
    with open('../Microsoft/Grades.json') as g:
        with open('../Microsoft/Students.json') as s:
            grades = json.load(g)
            students = json.load(s)

            print('Average for each student:')

            for student in students:
                sum = 0
                count = 0
                for grade in grades:
                    if grade['id'] == student['id']:
                        sum += grade['grade']
                        count += 1
                if sum:
                    print('id: ', student['id'], ' name: ', student['name'], ' avg: ', sum / count)

            print('Average for each subject:')

            for grade in list(dict.fromkeys([s['subject'] for s in grades])):
                sum = 0
                count = 0
                for grd in grades:
                    if grd['subject'] == grade:
                        sum += grd['grade']
                        count += 1
                if sum:
                    print('subject: ', grade, ' avg: ', sum / count)


if __name__ == '__main__':
    print_avg()

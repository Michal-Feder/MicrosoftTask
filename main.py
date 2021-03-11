import json
import statistics


# first way: --complexity time o(n^2), complexity space o(1).
def print_avg_1():
    print('first way: --complexity time o(n^2), complexity space o(1)')
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


# second way: --complexity time o(n), complexity space o(n^2).
def print_avg_2():
    print('second way: --complexity time o(n), complexity space o(n^2)')
    with open('../Microsoft/Grades.json') as g:
        with open('../Microsoft/Students.json') as s:
            grades = json.load(g)
            students = json.load(s)

        my_map = {}

        for grd in grades:
            if my_map.get(grd['id']):
                my_map[grd['id']].append(grd['grade'])
            else:
                my_map[grd['id']] = [grd['grade']]

        print('Average for each student:')

        for std in students:
            if my_map.get(std['id']):
                print('id: ', std['id'], ' name: ', std['name'], ' avg: ', statistics.mean(my_map.get(std['id'])))

        my_map = {}
        print('Average for each subject:')

        for grd in grades:
            if my_map.get(grd['subject']):
                my_map[grd['subject']].append(grd['grade'])
            else:
                my_map[grd['subject']] = [grd['grade']]

        for grade in list(dict.fromkeys([s['subject'] for s in grades])):
            if my_map.get(grade):
                print('subject: ', grade, ' avg: ', statistics.mean(my_map.get(grade)))


if __name__ == '__main__':
    print_avg_1()
    print_avg_2()

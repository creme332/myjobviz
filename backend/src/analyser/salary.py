def salary_count(salary_list):
    count = {'Less Than 10,000': 0, '10,000 - 20,000': 0, '21,000 - 30,000': 0,
             '31,000 - 40,000': 0, '41,000 - 50,000': 0,
             '51,000 - 75,000': 0, '76,000 - 100,000': 0,
             'More Than 100,000': 0, 'Negotiable': 0, 'Not disclosed': 0
             }
    invalid_salaries = ['Not disclosed', 'Negotiable', 'See description']

    for salary in salary_list:
        if (salary not in invalid_salaries):
            if (salary not in count.keys()):
                print('Unknown salary ranges found: ', salary)  # ! throw error
            else:
                count[salary] += 1
    return count

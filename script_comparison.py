import csv


def find_comparison(l1, l2):
    list_comparison_error = []
    list_comparison_correct = []

    for i_error, row_error in enumerate(l1):
        for i_correct, row_correct in enumerate(l2):
            if i_error == i_correct:
                if i_error == 0 and i_correct == 0:
                    rep_name_column = [[i_error + 1], row_error]
                    list_comparison_error.append(rep_name_column)
                    list_comparison_correct.append(rep_name_column)
                elif row_error != row_correct:
                    rep_error = [[i_error + 1], row_error]
                    rep_correct = [[i_correct + 1], row_correct]

                    list_comparison_error.append(rep_error)
                    list_comparison_correct.append(rep_correct)
        continue

    result_list = []
    result_list.append(list_comparison_error)
    result_list.append(list_comparison_correct)
    
    return result_list if len(list_comparison_error) > 1 else None


def find_difference_elem(l1, l2):
    list_disagreements = []

    for i_error, row_error in enumerate(l1):
        for i_correct, row_correct in enumerate(l2):
            if i_error == i_correct and row_error != row_correct:

                for i, el_row_error in enumerate(row_error):
                    for j, el_row_correct in enumerate(row_correct):
                        if i == j and el_row_error != el_row_correct:
                            rep = i_error + 1, l1[0][i], el_row_error, el_row_correct
                            list_disagreements.append(rep)
                    
    return list_disagreements if len(list_disagreements) > 1 else None

def show_difference_string(list_comparison):
    if list_comparison is not None: 
        for row in list_comparison[0]:
            for el in row:
                for i in el:
                    print(i, end=' ')
            print()
    else:
        print("В этом списке нет разных строк. Списки одинаковые")

def show_difference_elem(list_disagreements):
    if list_disagreements is not None: 
        for row in list_disagreements:
            for elem in row:
                print(elem, end=' ')
            print()
    else:
        print("В этом списке нет разных элементов. Списки одинаковые")
    

def main():
    print()
    print("Сравнить и найти отличия в двух файлах. Нужно иметь два файла в формате сsv.")
    print()
    first_file = input('введите путь до первого файла= ')

    
    second_file = input('введите путь до второго файла= ')

    print()

    with open(first_file, 'r') as file_error:
        reader_error = csv.reader(file_error, delimiter='\t')

        with open(second_file, 'r') as file_correct:
            reader_correctly = csv.reader(file_correct, delimiter='\t')

            data_error = list(reader_error)
            data_correct = list(reader_correctly)

            list_comparison_end = find_comparison(data_error, data_correct)
            list_disagreements_end = find_difference_elem(data_error, data_correct)
            show_difference_string(list_comparison_end)
            show_difference_elem(list_disagreements_end)
    print()
            

main()


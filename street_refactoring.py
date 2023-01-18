
# input_test = "Насеље БОРЧА: БАТИЊОЛСКА: 16-18,22-24,28,19-21,25-29, БРАЦЕ АНДЈЕЛИЦ: 6,7,11, ДИЧИНСКА: 4,26,30-30Б,42,11Л-11Ж,27Б,37А-37Б,45,53А-55Б, ДИМИТРИЈА РУВАРЦА: 13-23, ГОЛУБИЋКА: 20-24А, ИВАНА ГАЛЕБА: 4,8А,14,1,9,17,21, ЈАКОВА НЕНАДОВИЦА: 2-2А,16-20,1-3,29-33, КАРЛОВАЦКЕ МИТРОПОЛИЈЕ: 16,24Д-26,36Г,44А-44В,1-13,17-19В, КНЕЗА АЛЕКСЕ: 100-100Е,21-21А, ЛАФОНТЕНОВА: 3, ЉУБЕ НЕНАДОВИЦА: 18-20Т,26,36,42,5,9,15-19, МАЈОРА ГАВРИЛОВИЦА: 2-24,17,23-25, МАЛИ ЗБЕГ НОВА 302: 2,6-8,12,9-11,15-17, МИЛОРАДА АРСЕНИЈЕВИЋА: 2-8,14-18,22,26-30,38,1,7,13-17,21,29,33-35, МИРКОВАЧКА: 2-16А,22-26,1,5-11,15, МИТЕ СТАЈИЦА: 18,11Б-13, МОМЦИЛА НАСТАСИЈЕВИЦА: 20-22,9-11, ПУЛИЦЕРОВА: 1-11, РАНКА МИЉИЋА: 100-102,108,124, РАСТКА НЕМАЊИЋА: 16,41-47, ВЕЉУНСКА: 11, ВЛАДИМИРА ВИСОЦКОГ: 4,1-3, ВУКАНА НЕМАЊИЋА: 12-18,22,26, ЗРЕЊАНИНСКИ ПУТ: 192-198,161-163Р,167-171,191А-191Б, Насеље БОРЧА Мали Збег: ДИЧИНСКА: 77, Насеље БОРЧА Мали Збег: БРАЦЕ АНДЈЕЛИЦ: 3, Насеље БОРЧА - Мали Збег: ДИМИТРИЈА РУВАРЦА: 2-12,16-22,1А-5, ЈАКОВА НЕНАДОВИЦА: 8,7-9,15-17,21-23,39,47, КНЕЗА АЛЕКСЕ: 2,6-10,14-20,1,5-11,15, КНИНСКЕ КРАЈИНЕ: 2-10,14,18,22-32,3-23, МАЈОРА ГАВРИЛОВИЦА: 1-1А,5, МАРИНЕ ЦВЕТАЈЕВЕ: 4-4А,9-11, МОМЦИЛА НАСТАСИЈЕВИЦА: 2-16,1-3,15-23,27-29, Насеље БОРЧА - Мали Збег: ЈУНАКА СА ЦЕРА: 17, ЉУБЕ НЕНАДОВИЦА: 2-12,1-1Б, Насеље БОРЧА -- Мали Збег: ЛАФОНТЕНОВА: 7, Насеље БОРЧА Мали Збег: ПУЛИЦЕРОВА: 2,6-8, Насеље БОРЧА Мали - Збег: КАРЛОВАЦКЕ МИТРОПОЛИЈЕ: 10,23,"
# input_test2 = "Насеље БОРЧА: БАТИЊОЛСКА: 16-18,22-24,28,19-21,25-29, БРАЦЕ АНДЈЕЛИЦ: 6,7,11, ДИЧИНСКА: 4,26,30-30Б,42,11Л-11Ж,27Б,37А-37Б,45,53А-55Б"

def street_name_parsing(input_street_txt):
    input_street_list = input_street_txt.split(", ")
    street_dict = {}
    final_list = []
    for i in input_street_list:
        i_splt = i.split(":")
        if len(i_splt) == 3:
            street_dict["Naselje"] = i_splt[0].strip()
            street_dict["Ulica"] = i_splt[1].strip()
            street_dict["Broj"] = expand_street_numbers(i_splt[2])
        elif len(i_splt) == 2:
            street_dict["Ulica"] = i_splt[0].strip()
            street_dict["Broj"] = expand_street_numbers(i_splt[1])
        final_list.append(street_dict)
        street_dict = {}

    return final_list

def expand_street_numbers(input_street_nums_text):
    # Clear trailing , and blanks
    if input_street_nums_text[0] == " " or input_street_nums_text[0] == ",":
        input_street_nums_text = input_street_nums_text[1:]
    elif input_street_nums_text[-1] == " " or input_street_nums_text[0] == ",":
        input_street_nums_text = input_street_nums_text[:-1]
    
    input_street_nums_list = input_street_nums_text.split(",")

    for idx, num in enumerate(input_street_nums_list, start=0):
        nums_range = []
        if not "-" in num:
            continue
        else:
            num_list = num.split("-")
            if len(num_list) == 2:
                first_el = num_list[0]
                second_el = num_list[1]

                if first_el.isnumeric() and second_el.isnumeric():
                    int_first_el = int(first_el)
                    int_second_el = int(second_el)

                    if int_second_el > int_first_el:
                        nums_range = ",".join(str(n) for n in range(int_first_el, int_second_el))

                    elif int_second_el < int_first_el:
                        nums_range = ",".join(str(n) for n in range(int_second_el, int_first_el))

                else:
                    nums_range = ",".join(s for s in num_list)
        
            input_street_nums_list[idx] = nums_range

    return input_street_nums_list


def reformat_street_numbers(street_dict_list):
    for idx, i in enumerate(street_dict_list, start=0):
        nums_breakdown = []
        for nums in i["Broj"]:
            splitted_nums = nums.split(",")
            nums_breakdown.extend(splitted_nums)
        i["Broj"] = nums_breakdown
    
    return street_dict_list




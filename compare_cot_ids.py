import os, sys

"""
    excel failā nevaru notestēt, ko ArcGis nevar atrast, tad mēģinu, ka ar masīvu salīdzinājumu var tikt skaidrībā, kurš cot_id IR un NAV nokopēts datu assign toolboxim (ArcGis lietotnes kontkestā)
    
    šeit run ir kad excel failā vairs nevaru to noteikt caur krāsām, jo ierakstu skaits ir tūkstoši nevis daži simti, kas arī ir daudz lai ezcelī ar iekrāsām varētu uz fikso un konkrēti atrast, kas iztrūkst vairs nē
"""

# pārbauda vai sarakstā ir tikai unikālas vērtības
# https://datascienceparichay.com/article/python-check-if-all-elements-in-a-list-are-unique/ at 08.02.2023.
#
def unique_values(input_list):
    temp = []
    for str in input_list:
        # ja jaunveidotajā sarakstā atrodas minētā vērtība, tad visam oriģ sarakstam nav vērtības kā oriģinālas
        if str in temp:
            return False
        # ja vērtība tiek sastapta pirmo reizi, tad tā tiek noglabāta kpoijas sarakstā vēlākam salīdzinājumam
        temp.append(str)
    return True

directory = fr'{os.getcwd()}\input\\'

input_file_str1 = "server_cotid.txt"
input_file_str2 = "local_cotid.txt"
count1 = 0
count2 = 0

file_not_found = False
has_dublicates = False
data_is_unique = "All data is unique"
data_have_dublicates = "Data have dublicates in"
in_data1 = []
in_data2 = []
data_not_list = []

try:
    # r -> read data from file
    # r+ -> read and modify data in file
    input_file1 = open(directory + input_file_str1, "r")
    input_file2 = open(directory + input_file_str2, "r")
    
    for line in input_file1.readlines():
        in_data1.append(line.strip())
        
    if unique_values(in_data1) == True:
        print(data_is_unique)
    else:
        has_dublicates = True
        print(fr"{data_have_dublicates} {input_file_str1}")
        
    # sys.exit(0) # for testing, just to compare values if I am not sure
        
    for line in input_file2.readlines():
        in_data2.append(line.strip())
        
    if unique_values(in_data2) == True:
        print(data_is_unique)
    else:
        has_dublicates = True
        print(fr"{data_have_dublicates} {input_file_str2}")
        
    # ja datiem ir dublikāti, lai arī nvajadzētu būt, skripts beidz darbību
    if has_dublicates == True:
        input_file1.close()
        input_file2.close()
        sys.exit()
        
    count1 = len(in_data1)
    count2 = len(in_data2)
    
    # ideja ir tāda, ka parsēšanu veic tikai caur lielāko masīvu/sarakstu un atrasto elementu izņemšanu veic mazajā
    # pirmais fails ir lielāks nekā otrais
    if count1 >= count2: 
        for i in in_data1:
            if i in in_data2:
                in_data2.remove(i)
            else:
                data_not_list.append(i)
                print(fr"Value {i} was not in list")
                
        # print(f"\n Servera input skaits {count1}:")
        # print(in_data1)
        # print(f"\n Lokālais input skaits {count2}:")
        # print(in_data2)
        print(f"\n Tas, kas nebija lokālā input sarakstā:")
        print(data_not_list)
        
    # gadījums, kad otrais fails bija lielāks nekā pirmais
    else:
        print("Servera cot_id ir jābūt ar lielāku input ierakstu skaitu")
    
except FileNotFoundError as not_found_err:
    file_not_found = True
    print(not_found_err)
finally:
    if file_not_found == False:
        input_file1.close()
        input_file2.close()
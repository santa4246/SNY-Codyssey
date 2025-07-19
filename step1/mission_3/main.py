# 수행과제
# Mars_Base_Inventory_List.csv 의 내용을 읽어 들어서 출력한다.
# Mars_Base_Inventory_List.csv 내용을 읽어서 Python의 리스트(List) 객체로 변환한다.
# 배열 내용을 적제 화물 목록을 인화성이 높은 순으로 정렬한다.
# 인화성 지수가 0.7 이상되는 목록을 뽑아서 별도로 출력한다.
# 인화성 지수가 0.7 이상되는 목록을 CSV 포멧(Mars_Base_Inventory_danger.csv)으로 저장한다.

import csv

def main():
    file_name = 'Mars_Base_Inventory_List.csv'
    try:
        ##########################################################################
        ##########################################################################
        # 수행과제 1
        # Mars_Base_Inventory_List.csv 의 내용을 읽어 들어서 출력한다.
        ##########################################################################
        f = open(file_name, "r")
        reader = csv.reader(f)

        for row in reader:
            print(row)
        ##########################################################################
        ##########################################################################
        # 수행과제 2
        # Mars_Base_Inventory_List.csv 내용을 읽어서 Python의 리스트(List) 객체로 변환한다.
        ##########################################################################
        data = list(reader)
        print(data)
        ##########################################################################
        ##########################################################################
        # 수행과제 3
        # 배열 내용을 적제 화물 목록을 인화성이 높은 순으로 정렬한다.
        ##########################################################################
        header = data[0]
        rows = data[1:]

        def to_float(val):
            try:
                return float(val)
            except ValueError:
                return 999

        sorted_rows = sorted(rows, key=lambda x: to_float(x[-1]), reverse=True)

        sorted_data = [header] + sorted_rows

        for row in sorted_data:
            print(row)
        ##########################################################################
        ##########################################################################
        # 수행과제 4
        # 인화성 지수가 0.7 이상되는 목록을 뽑아서 별도로 출력한다.
        ##########################################################################
        sorted_header = sorted_data[0]
        sorted_rows = sorted_data[1:]

        filtered_rows = []
        for sorted_row in sorted_rows:
            if float(sorted_row[4]) > 0.7:
                filtered_rows.append(sorted_row)

        filtered_data = [sorted_header] + filtered_rows

        for row in filtered_data:
            print(row)
        ##########################################################################
        ##########################################################################
        # 수행과제 5
        # 인화성 지수가 0.7 이상되는 목록을 CSV 포멧(Mars_Base_Inventory_danger.csv)으로 저장한다.
        ##########################################################################
        with open('Mars_Base_Inventory_danger.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(filtered_data)
        ##########################################################################

    except Exception as err :
        print("error: {0}".format(err))

if __name__ == "__main__":
    main()
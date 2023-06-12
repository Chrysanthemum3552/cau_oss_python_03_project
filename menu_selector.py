

def start_process(path):

    """
        1. file_manager의 read_file함수를 사용하므로 file_manager을 import한다.
        2. parking_spot_manager의 str_list_to_class_list함수를 사용하므로 parking_spot_manager도 import한다.
        3. 매개변수로 받은 path를 read_file함수에 대입하여 반환된 목록들을 str_list에 저장한다.
        4. str_list를 parking_spot객체의 리스트로 반환받기 위해  함수 str_list_to_class_list에 str_list를 대입한다.
        5. 이를 spots에 저장한다.
    """

    import file_manager
    import parking_spot_manager
    str_list=file_manager.read_file(path)
    spots=parking_spot_manager.str_list_to_class_list(str_list)

    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            """
                1번 옵션을 선택하면 parking_spot_manager 모듈의 
                print_spots 함수를 호출해야 하므로 parking_spot_manager.print_spots() 
                함수에 위에서 구한 spots를 대입하여 목록을 전부 print한다.
            """           
            parking_spot_manager.print_spots(spots) 
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                print("not implemented yet")
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                print("not implemented yet")
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                print("not implemented yet")
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                print("not implemented yet")
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                print("not implemented yet")
                # fill this block
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            """
                4를 입력하면 Exit을 표시한뒤 break를 통해 반복문을 벗어나 프로그램을 종료한다.
            """
            print("Exit")
            break
        else:
            print("invalid input")
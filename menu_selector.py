

def start_process(path):

    """
        1. file_manager의 read_file함수를 사용하므로 file_manager을 import한다. 별칭은 fmanager로 한다.
        2. parking_spot_manager의 str_list_to_class_list함수를 사용하므로 parking_spot_manager도 import한다. 별칭은 pmanager로 한다.
        3. 매개변수로 받은 path를 read_file함수에 대입하여 반환된 목록들을 str_list에 저장한다.
        4. str_list를 parking_spot객체의 리스트로 반환받기 위해  함수 str_list_to_class_list에 str_list를 대입한다.
        5. 이를 spots에 저장한다.
    """

    import file_manager as fmanager
    import parking_spot_manager as pmanager
    str_list=fmanager.read_file(path)
    spots=pmanager.str_list_to_class_list(str_list)

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
            pmanager.print_spots(spots) 
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                """
                    parking_spot_manager에서 구현한 filter_by_name을 사용한다.
                    첫번째 전달인자는 함수 선언시 구한 모든 장소를 담고있는 spots
                    두번째 전달인자는 어떤 이름이 포함되어있는 것을 검색할 것인지를 전달하는 keyword이다.
                    기존의 객체 list는 삭제해야 하므로 필터링된 자료를 그대로 spots에 덮어 씌운다.
                """
                keyword = input('type name:')
                spots=pmanager.filter_by_name(spots, keyword)
            elif select == 2:
                """
                    parking_spot_manager에서 구현한 filter_by_city를 사용한다.
                    첫번째 전달인자는 함수 선언시 구한 모든 장소를 담고있는 spots
                    두번째 전달인자는 어떤 도시 이름이 포함되어있는 것을 검색할 것인지를 전달하는 keyword이다.
                    기존의 객체 list는 삭제해야 하므로 필터링된 자료를 그대로 spots에 덮어 씌운다.
                """
                keyword = input('type city:')
                spots=pmanager.filter_by_city(spots, keyword)
            elif select == 3:
                """
                    parking_spot_manager에서 구현한 filter_by_district를 사용한다.
                    첫번째 전달인자는 함수 선언시 구한 모든 장소를 담고있는 spots
                    두번째 전달인자는 어떤 지명이 포함되어있는 것을 검색할 것인지를 전달하는 keyword이다.
                    기존의 객체 list는 삭제해야 하므로 필터링된 자료를 그대로 spots에 덮어 씌운다.
                """
                keyword = input('type district:')
                spots=pmanager.filter_by_district(spots, keyword)
            elif select == 4:
                """
                    parking_spot_manager에서 구현한 filter_by_ptype을 사용한다.
                    첫번째 전달인자는 함수 선언시 구한 모든 장소를 담고있는 spots
                    두번째 전달인자는 어떤 주차장 유형이 포함되어있는 것을 검색할 것인지를 전달하는 keyword이다.
                    기존의 객체 list는 삭제해야 하므로 필터링된 자료를 그대로 spots에 덮어 씌운다.
                """
                keyword = input('type ptype:')
                spots=pmanager.filter_by_ptype(spots, keyword)
            elif select == 5:
                """
                    위도, 경도의 최대 최소를 튜플형태로 keylocation에 저장한다.
                    parking_spot_manager에서 구현한 filter_by_location을 사용한다.
                    첫번째 전달인자는 함수 선언시 구한 모든 장소를 담고있는 spots
                    두번째 전달인자는 위도, 경도의 최대 최소 정보를 담고 있는 keylocation튜플이다.
                    기존의 객체 list는 삭제해야 하므로 필터링된 자료를 그대로 spots에 덮어 씌운다.
                """
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                keylocation = (min_lat, max_lat, min_lon, max_lon)
                spots=pmanager.filter_by_location(spots, keylocation)
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            """
                    입력값이 keywords리스트 내에 있는 문자열이면 이를 parking_spot_manager의 함수에 이 값을 넘겨준다.
                    이 함수에서 정렬을 마치고 반환한 값을 spots에 덮어 씌운다.
            """
            if keyword in keywords:
                spots = pmanager.sort_by_keyword(spots, keyword)
            else: print("invalid input")
        elif select == 4:
            """
                4를 입력하면 Exit을 표시한뒤 break를 통해 반복문을 벗어나 프로그램을 종료한다.
            """
            print("Exit")
            break
        else:
            print("invalid input")
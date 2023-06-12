class parking_spot:  
    def __init__(self, name, city, district, ptype, longitude, latitude):
        """
            parking_spot의 생성자.
            매개변수의 종류는 아래와 같다
                name : 자원명
                city : 시도
                district : 시군구
                ptype : 주차장유형
                longitude : 경도
                latitude : 위도
                  
            이를 딕셔너리 __item 필드의 value에 대입한다.
            따라서 키(key)와 값(value)은 아래와 같이 구성된다.  
                name : 자원명
                city : 시도
                district : 시군구
                ptype : 주차장유형
                longitude : 경도
                latitude : 위도    
        """
        
        self.__item = {

            'name'      : name,
            'city'      : city,
            'district'  : district,
            'ptype'     : ptype,
            'longitude' : float(longitude),
            'latitude'  : float(latitude)
        }
    
    def __str__(self):
        
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s


    def get(self, keyword='name'):
        """
            매개변수 keyword를 받아 __item 딕셔너리의 __item[keyword]를 반환한다.
            ※ 입력이 없을시 기본인수는 'name'이 된다.
        """
        return self.__item[keyword]

    
def str_list_to_class_list(str_list):
    """
        1. str_list를 매개변수로 받는다.
        2. 이를 split을 이용해 콤마(,)단위로 쪼개서 리스트 data_list에 각각 대입한다.
        3. 순번은 data_list[0]에 저장되는데 이는 요구하지 않으므로 1번부터 각각의 변수에 대입한다.
        4. 이를 클래스 객체 리스트로 변환하기 위해 클래스 parking_spot에 대입한다.
        5. 이를 spot에 저장하고 이를 append를 이용하여 class_list에 추가한다.
        6. for의 모든 과정이 끝나면 class_list를 반환한다.
    """
    class_list=[]
    for item in str_list:
        data_list=item.split(',')
        name = data_list[1]
        city = data_list[2]
        district = data_list[3]
        ptype = data_list[4]
        longitude = float(data_list[5])
        latitude = float(data_list[6])
        spot = parking_spot(name, city, district, ptype, longitude, latitude)
        class_list.append(spot)
    return  class_list



def print_spots(spots):
    """
        class_lits를 저장한 값을 받아 매개변수 spots에 저장한다.
        그 다음 len함수를 이용하여 elements의 개수를 표시한뒤 spots의 모든 데이터들을 표시한다.
    """
    print(f"---print elements({len(spots)})---")
    for data in spots:
        print(str(data))




    


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
# version#2
    # import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)
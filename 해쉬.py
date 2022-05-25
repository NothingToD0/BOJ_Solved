# 해쉬 테이블 만들기
hash_table = list([0 for i in range(10)])

#해쉬 함수 만들기 
# Division(나누기를 통한 나머지 값을 사용하는 기법)
def hash_func(key):
    return key % 5

data1 = "Andy"
data2 = "Dave"
data3 = "Trump"
data4 = "Anthor"

def storage_data(data, value):
    key = hash(data)
    hash_address = hash_func(key)

    for i in range(hash_address, len(hash_table)):
        if hash_table[index] == 0:
            hash_table[index] = [key, value]
        return
        elif hash_table[index][0] == index_key:
            hash_table[index][1] == value
            return
            
        else: hash_table[hash_address]



storage_data('Andy', '010232322')
storage_data('Dave', '010232322')
storage_data('Trump', '010232322')

def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]
    


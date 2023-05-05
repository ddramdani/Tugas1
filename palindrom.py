
class Stack(): # membuat class stack
    def __init__(self): # menginisiasi fungsi (sering disebut constructor function), tidak perlu memperhatikan argument self
        self.list = [] # membuat variable yang akan menyimpan sebuah list di dalam object/class (self). a
    def isEmpty(self): # membuat fungsi isEmpty untuk mengembalikan nilai true jika didalam list yang terdapat di object atau class (self) Stack ternyata kosong
        return self.list==[] # mengembalikan boolean dari pengecekan operator perbandingan ==
    def push(self,item): # membuat fungsi untuk 
        self.list.append(item) # akan menambahkan data dari argumen yang diambil dari parameter item. ditambahkan ke dalam list yang ada di objek Stack
    def pop(self):
        return self.list.pop()
    def peek(self):
        return self.list
    def size(self):
        return len(self.list)

def is_palindrom(text):
    stack_a = Stack()
    stack_b = Stack()
    index_awal = 0 # membuat variable yang menyimpan index ke-0
    index_akhir = len(text)-1 # membuat variable yang menyimpan index terakhir
    while index_awal<index_akhir: # selama index awal lebih kecil dari index akhir
        stack_a.push(text[index_awal])
        stack_b.push(text[index_akhir])
        index_awal+=1 # jika tidak masuk ke statement if, maka index awal akan ditambah 1. (misalkan index awal = 0, jika ditambah 1 maka index awal = 1)
        index_akhir-=1 # index akhir akan dikurangi 1 (jika index akhir = 10, jika dikurangi 1 maka index akhir = 9)

    for item in stack_a.list:
        if stack_a.pop()!=stack_b.pop():
            stack_a.pop()
            stack_b.pop()
            return False
    return True
input_user = input("masukkan kata/kalimat :> ")
print(is_palindrom(input_user))
def is_palindrom(text):
    the_text = [item for item in text if item.isalnum()]# mengecek apakah string alfabet atau numeric
    text = "".join(the_text)

import json
import os

class check_json_module():
    def __init__(self):
        self.initial_data = """{"Copies List":"Quick Copy made by Hiroxbon"}"""
        self.file =  'data.json'
        
    def main(self):
        file_check_result = self.file_check_json()
        
        if file_check_result == False:
            self.make_json()
        elif file_check_result == True:
            
            data_check_result = self.file_check_data()
            #print("ファイルの中身があるかどうか" + str(data_check_result))
            if data_check_result == False:
                self.make_json()
            elif data_check_result == True:
                pass
            
    
    def file_check_json(self):
        file = self.file
        is_dir = os.path.isfile(file)
        #print("file があるかどうか" + str(is_dir))
        return is_dir
        
    def file_check_data(self):
        file = self.file
        if  os.stat(file).st_size == 0:
            return False
        else:
            return True
            
        
    def make_json(self):
        json_file = self.file
        with open(json_file, 'a', encoding='utf-8') as file:  
            file.truncate(0) #ファイルを中身を削除 = 0 
            file.write(self.initial_data)
import os
from itertools import islice

def read_lines(file_path):
    """ฟังก์ชัน Generator สำหรับอ่านไฟล์ทีละบรรทัด"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for code_line in f:
                # ส่งข้อมูลออกมาทีละบรรทัด โดยที่สถานะของฟังก์ชันยังไม่จบ
                yield code_line.strip()
    except FileNotFoundError:
        raise FileNotFoundError(
            f"/err file don't exist: {file_path}"
        )
    
def run_code_file(code_file: str):
    
    file = read_lines(code_file)
    
    database_file = ""
    variable = []
    tables = []
    in_bracket = False
    in_flank = False
    in_square_brackets = False
    line_number = 1
    for line in file:
        tokens = line.split()
        
        if tokens[0] == "dcv":
            if tokens[3] != "=":
                return f"/err at line: {line_number} [don't have '=' (ex. dcv string name = 'name')]" 
            
            if tokens[1] == "string" and tokens[2] == "#dbf" and line_number == "1":
                database_file += tokens[4]
            else:
                return f"/err at line: {line_number}  [don't have database name in line 1 (fix: at this code to line 1 'dcv string #dbf = <database name>')]"
                
            variable.append([f"name={tokens[2]}, datatype={tokens[1]}, value={tokens[4]}"])
            
            
        if tokens[0] == "func":
            fun_name = 
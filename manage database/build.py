import os

def build_database(database_file_name: str, tables: list):
    
    table_list = "tables = ["
    table_len = len(tables)
    index = 0
    
    for table in tables:
        index += 1
        table_info = table.spilt("=")
        
        if table_info[1] not in ["int", "bool", "string", "float", "list"]:
            return "/err type is not 'int' 'bool' 'string' 'float' or 'list'"
        
        table_list += f"[{table_info[0]}, {table_info[1]}]"
        
        if index == 
    table_list += "]"
    
    if os.path.exists(database_file_name):
        with open(database_file_name, "r", encoding="utf-8") as a:
            have_data = False
            have_database_data = False
            
            for line in a:
                if line == "/already_have_data":
                    have_data = True
                    
                if line == "/already_have_database_data":
                    have_database_data = True
                    
                if have_data and have_database_data:
                    return "/err database already have data"
        
        with open(database_file_name, "w", encoding="utf-8") as f:
            f.write("/already_have_data")
            f.write("version=beta\n")
            f.write(f"database_name={database_file_name}\n")
            f.write("aut_code=cha_database\n")
            f.write(f"{table_list}\n\n")
            f.write("==============================\n\n")
            
        return "/success created database file"
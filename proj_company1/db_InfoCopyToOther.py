import pymysql
import time
# 取得寫入 Insert/更新 update  時間
localtime = time.localtime()
times = time.strftime("%Y-%m-%d %I:%M:%S", localtime)
print(times)
# 資料庫設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "infodba",
    "db": "a6_photo",
    "charset": "utf8"
}
# 資料庫設定(ex:)
db_set_from = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "infodba",
    "db": "a6_array",
    "charset": "utf8"
}
 command = "INSERT INTO tab_test (machine,PDB0,PD09,PD07,create_time,create_name,modify_time,modify_name)  VALUES" 
        + "('SDCO22','0','0','1','"+ times +"','dba','"+ times +"','dba')"
# try:
#     # 建立Connection物件
#     conn = pymysql.connect(**db_settings)
#     print("connect successful!")
#     # 建立Cursor物件
#     with conn.cursor() as cursor:
#         
       

        
#         # 執行指令
#         cursor.execute(command)
#         # 儲存變更
#         conn.commit()

#         # 新增資料SQL語法
#         command = "select * From tab_test;"# 取得所有資料
#         cursor.execute(command)
#         result = cursor.fetchall()
#         print(result)
# except Exception as ex:
#     print(ex)
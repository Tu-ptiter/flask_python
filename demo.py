import sqlite3

# import os
# os.remove('KIEMDINH.db')

conn = sqlite3.connect('KIEMDINH.db')

c = conn.cursor()

#create table
sql_create_table = """
    CREATE TABLE HOSOKIEMDINH (
	ma_hs INT PRIMARY KEY,
	ten_thiet_bi NVARCHAR(100),
	so_giay_chung_nhan INT,
	ket_qua NVARCHAR(50),
	ngay_kiem_dinh DATE,
	ma_kdv INT,
	so_che_tao INT,
	ma_kh INT,
	FOREIGN KEY (ma_kh) REFERENCES KHACHHANG(ma_kh),
	FOREIGN KEY (ma_kdv) REFERENCES KIEMDINHVIEN(ma_kdv),
	FOREIGN KEY (so_che_tao) REFERENCES THONGTINTHIETBI(so_che_tao)
)
"""
# insert
sql_insert = """
    
INSERT INTO HOSOKIEMDINH(ma_hs, ten_thiet_bi, so_giay_chung_nhan, ket_qua,ngay_kiem_dinh,ma_kdv,so_che_tao, ma_kh) 
VALUES
(1,'Điện thoại','123535','Đã KĐ','2024-03-22',14,1035,12),
(2,'Điều hòa','123213','Chưa KĐ','2024-03-23',12,1234,11),
(3,'Lapptop','123234','Đã KĐ','2021-05-16',642,1255,14),
(4,'Tivi','123455','Chưa KĐ','2024-07-12',21,2864,13),
(5,'Máy sấy tóc','123454','Đang KĐ','2024-03-23',95,3464,25),
(6,'Ipad','123453','Đã KĐ','2022-03-25',35,3809,15),
(7,'PC','123657','Chưa KĐ','2024-01-13',172,4284,16),
(8,'Máy lọc không khí','123659','Đã KĐ','2021-05-14',96,5086,17),
(9,'Máy giặt','123757','Chưa KĐ','2024-08-12',143,5276,18),
(10,'Máy sưởi','123868','Đã KĐ','2024-12-23',172,6474,19),
(11,'Lò vi sóng','123875','Chưa KĐ','2022-11-21',189,6830,20),
(12,'Điện thoại','123857','Đã KĐ','2024-05-10',243,6934,21),
(13,'Đồng hồ','123857','Chưa KĐ','2024-02-12',242,9160,22),
(14,'Bàn là','123956','Đã KĐ','2024-07-10',234,9214,23),
(15,'Quạt bàn','123575','Chưa KĐ','2023-12-15',523,9354,24);
"""

#select
sql_select = """
    SELECT * FROM cars
"""

# update
sql_update = """
    UPDATE cars 
    SET name ="insta" WHERE year = "2043"

"""

#delete
sql_delete = """
    DELETE FROM HOSOKIEMDINH

"""

sql_drop = """
    DROP TABLE HOSOKIEMDINH
"""


try:

    c.execute(sql_insert)
    conn.commit()

    # c.execute(sql_insert)
    # conn.commit()

    # c.execute(sql_select)
    # conn.commit()
     # print(c.fetchall())

    # c.execute(sql_update)
    # conn.commit()

    # c.execute(sql_delete)
    # conn.commit()

 

except:
    print('error')
conn.close()

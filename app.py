from  flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta, datetime
import sqlite3


 
app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=30)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/user")
def user():
    return render_template("user.html")


@app.route("/login",methods = ["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")
    


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

### xử lí phần KHACHHANG

@app.route('/list_customer')
def list_customer():

    con = sqlite3.connect("KIEMDINH.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT  * FROM KHACHHANG ")

    rows = cur.fetchall()
    con.close()

    return render_template("list_customer.html",rows=rows)

### INSERT DATA
@app.route("/enaddrec", methods = ['POST'])
def enaddrec():
    return render_template("newcus.html")


@app.route("/addrec", methods=['POST']) 
def addrec():
    if request.method == 'POST':
        try:
            ma_kh = request.form['ma_kh']
            ho_ten = request.form['ho_ten']
            sdt = request.form['sdt']
            dia_chi = request.form['dia_chi']


            with sqlite3.connect('KIEMDINH.db') as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO KHACHHANG (ma_kh, ho_ten, so_dien_thoai, dia_chi) VALUES (?, ?, ?, ?)", (ma_kh, ho_ten, sdt, dia_chi))
                conn.commit()
                msg = "Record successfully added to database"
        except sqlite3.IntegrityError:
            msg = "Error: Duplicate entry for primary key"
        except sqlite3.Error as e:
            msg = f"Error in the INSERT: {str(e)}"

    return render_template('render.html', msg=msg)

#### EDIT DATA KHACHHANG
@app.route("/edit", methods=['POST'])
def edit():
    if request.method == 'POST':
        try:
            id = request.form['id']

            con = sqlite3.connect("KIEMDINH.db")
            con.row_factory = sqlite3.Row

            cur = con.cursor()
            cur.execute("SELECT * FROM KHACHHANG WHERE ma_kh ="  + id)

            rows = cur.fetchall()
            
        except:
            id=None
        finally:
            con.close()
            # Send the specific record of data to edit.html
            return render_template("edit.html",rows=rows  )


@app.route("/editrec", methods=['POST','GET'])
def editrec():
    con = None
    if request.method == 'POST':
        try:
            ma_kh = request.form['ma_kh']
            ho_ten = request.form['ho_ten']
            so_dien_thoai = request.form['so_dien_thoai']
            dia_chi = request.form['dia_chi']

            with sqlite3.connect('KIEMDINH.db') as con:
                cur = con.cursor()
                cur.execute("UPDATE KHACHHANG SET ho_ten=?, so_dien_thoai=?, dia_chi=? WHERE ma_kh=?", (ho_ten, so_dien_thoai, dia_chi, ma_kh))
                con.commit()
                con.commit()
                msg = "Record successfully edited in the database"
        except Exception as e:
                if con:
                    con.rollback()
                msg = f"Error in the Edit: {str(e)}"
        finally:
            if con:
                con.close()
            return render_template('render.html',msg=msg)

#######    DELTETEEE KHACHHANG
@app.route("/delete", methods=['POST','GET'])
def delete():
    if request.method == 'POST':
        try:
            id = request.form['id']
            with sqlite3.connect('KIEMDINH.db') as con:
                    cur = con.cursor()
                    cur.execute("DELETE FROM KHACHHANG WHERE ma_kh="+ id)

                    con.commit()
                    msg = "Record successfully deleted from the database"
        except:
            con.rollback()
            msg = "Error in the DELETE"

        finally:
            con.close()
            return render_template('render.html',msg=msg)






### xử lí phần THONGTINTHIETBI
@app.route('/list_device')
def list_device():
    con = sqlite3.connect("KIEMDINH.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT  * FROM THONGTINTHIETBI  ")

    rows = cur.fetchall()
    con.close()
    return render_template("list_device.html",rows=rows)
### INSERT DATA THONGTINTHIETBI

@app.route("/dev_enaddrec", methods =['POST'])
def dev_enaddrec():
    return render_template("newdev.html")

@app.route("/dev_addrec", methods=['POST'])
def dev_addrec():
    print(request.form)
    if request.method == 'POST':
        try:
            so_che_tao = request.form['so_che_tao']
            ten_thiet_bi = request.form['ten_thiet_bi']
            ma_hieu = request.form['ma_hieu']
            nha_san_xuat = request.form['nha_san_xuat']
            nam_san_xuat = request.form['nam_san_xuat']



            with sqlite3.connect('KIEMDINH.db') as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO THONGTINTHIETBI (so_che_tao, ten_thiet_bi,ma_hieu,nha_san_xuat,nam_san_xuat) VALUES (?, ?, ?, ?,?)", (so_che_tao, ten_thiet_bi, ma_hieu, nha_san_xuat, nam_san_xuat))
                conn.commit()
                msg = "Record successfully added to database"
        except sqlite3.IntegrityError:
            msg = "Error: Duplicate entry for primary key"
        except sqlite3.Error as e:
            msg = f"Error in the INSERT: {str(e)}"

    return render_template('render.html', msg=msg)

###     EDIT DATA THONGTINTHIETBI
@app.route("/edit_dev", methods=['POST'])
def edit_dev():
    if request.method == 'POST':
        try:
            id = request.form['id']

            con = sqlite3.connect("KIEMDINH.db")
            con.row_factory = sqlite3.Row

            cur = con.cursor()
            cur.execute("SELECT * FROM THONGTINTHIETBI WHERE so_che_tao ="  + id)

            rows = cur.fetchall()
            
        except:
            id=None
        finally:
            con.close()
            # Send the specific record of data to edit.html
            return render_template("edit_dev.html", rows=rows )


@app.route("/editrec_dev", methods=['POST','GET'])
def editrec_dev():

    con = None
    if request.method == 'POST':
        try:

            so_che_tao = request.form['so_che_tao']
            ten_thiet_bi = request.form['ten_thiet_bi']
            ma_hieu = request.form['ma_hieu']
            nha_san_xuat = request.form['nha_san_xuat']
            nam_san_xuat = request.form['nam_san_xuat']

            


            with sqlite3.connect('KIEMDINH.db') as con:
                cur = con.cursor()
                cur.execute("UPDATE THONGTINTHIETBI SET ten_thiet_bi=?, ma_hieu=?, nha_san_xuat=?, nam_san_xuat =? WHERE so_che_tao=?", (ten_thiet_bi, ma_hieu, nha_san_xuat, nam_san_xuat, so_che_tao))
                con.commit()
                con.commit()
                msg = "Record successfully edited in the database"
        except Exception as e:
                if con:
                    con.rollback()
                msg = f"Error in the Edit: {str(e)}"
        finally:
            if con:
                con.close()
            return render_template('render.html',msg=msg)


### DELETE THONGTINTHIETBI
@app.route("/delete_dev", methods=['POST','GET'])
def delete_dev():
    if request.method == 'POST':
        try:

            id = request.form['id']

            with sqlite3.connect('KIEMDINH.db') as con:
                    cur = con.cursor()
                    cur.execute("DELETE FROM THONGTINTHIETBI WHERE so_che_tao ="+id)

                    con.commit()
                    msg = "Record successfully deleted from the database"
        except:
            con.rollback()
            msg = "Error in the DELETE"

        finally:
            con.close()
            # Send the transaction message to result.html
            return render_template('render.html',msg=msg)






###### xử lí phần bảng kiểm định viên
@app.route('/list_inspector')
def list_inspector():
    con = sqlite3.connect("KIEMDINH.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT  * FROM KIEMDINHVIEN  ")

    rows = cur.fetchall()
    con.close()
    return render_template("list_inspector.html",rows=rows)
## INSERT DATA

@app.route("/ins_enaddrec", methods =['POST'])
def ins_enaddrec():
    return render_template("newins.html")

@app.route("/ins_addrec", methods=['POST'])
def ins_addrec():
    if request.method == 'POST':
        try:
            ma_kdv = request.form['ma_kdv']
            ho_ten = request.form['ho_ten']
            so_dien_thoai = request.form['so_dien_thoai']
            danh_muc_thiet_bi = request.form['danh_muc_thiet_bi']
            ngay_cap_chung_chi = request.form['ngay_cap_chung_chi']
            ngay_het_han_chung_chi = request.form['ngay_het_han_chung_chi']



            with sqlite3.connect('KIEMDINH.db') as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO KIEMDINHVIEN(ma_kdv,ho_ten,so_dien_thoai,danh_muc_thiet_bi,ngay_cap_chung_chi,ngay_het_han_chung_chi) VALUES (?, ?, ?, ?,?,?)", (ma_kdv,ho_ten,so_dien_thoai,danh_muc_thiet_bi,ngay_cap_chung_chi,ngay_het_han_chung_chi))
                conn.commit()
                msg = "Record successfully added to database"
        except sqlite3.IntegrityError:
            msg = "Error: Duplicate entry for primary key"
        except sqlite3.Error as e:
            msg = f"Error in the INSERT: {str(e)}"

    return render_template('render.html', msg=msg)

###     EDIT DATA KIEMDINHVIEN
@app.route("/edit_ins", methods=['POST'])
def edit_ins():
    if request.method == 'POST':
        try:
            id = request.form['id']

            con = sqlite3.connect("KIEMDINH.db")
            con.row_factory = sqlite3.Row
        
            cur = con.cursor()
            cur.execute("SELECT * FROM KIEMDINHVIEN WHERE ma_kdv = ? ", (id,))

            rows = cur.fetchall()
            
        except:
            id=None
        finally:
            con.close()

    return render_template("edit_ins.html",rows=rows  )


@app.route("/editrec_ins", methods=['POST','GET'])
def editrec_ins():

    con = None
    if request.method == 'POST':
        try:

            ma_kdv = request.form['ma_kdv']
            ho_ten = request.form['ho_ten']
            so_dien_thoai = request.form['so_dien_thoai']
            danh_muc_thiet_bi = request.form['danh_muc_thiet_bi']
            ngay_cap_chung_chi = request.form['ngay_cap_chung_chi']
            ngay_het_han_chung_chi = request.form['ngay_het_han_chung_chi']

            


            with sqlite3.connect('KIEMDINH.db') as con:
                cur = con.cursor()
                cur.execute("UPDATE KIEMDINHVIEN SET ho_ten=?, so_dien_thoai=?, danh_muc_thiet_bi=?,ngay_cap_chung_chi = ?, ngay_het_han_chung_chi =? WHERE ma_kdv=?", (ho_ten, so_dien_thoai, danh_muc_thiet_bi, ngay_cap_chung_chi, ngay_het_han_chung_chi,ma_kdv))
                con.commit()
                msg = "Record successfully edited in the database"
        except Exception as e:
                if con:
                    con.rollback()
                msg = f"Error in the Edit: {str(e)}"
        finally:
            if con:
                con.close()
            return render_template('render.html',msg=msg)


#### DELETE KIEMDINHVIEN
@app.route("/delete_ins", methods=['POST','GET'])
def delete_ins():
    if request.method == 'POST':
        try:
            id = request.form['id']

            with sqlite3.connect('KIEMDINH.db') as con:
                    cur = con.cursor()
                    cur.execute("DELETE FROM KIEMDINHVIEN WHERE ma_kdv ="+id)

                    con.commit()
                    msg = "Record successfully deleted from the database"
        except:
            con.rollback()
            msg = "Error in the DELETE"

        finally:
            con.close()
            # Send the transaction message to result.html
            return render_template('render.html',msg=msg)










### xử lí phần HOSOKIEMDINH
@app.route('/list_profile')
def list_profile():
    con = sqlite3.connect("KIEMDINH.db")

    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute("SELECT  * FROM HOSOKIEMDINH  ")

    rows = cur.fetchall()
    con.close()
    return render_template("list_profile.html",rows=rows) 

## INSERT DATA HOSOKIEMDINH

@app.route("/pro_enaddrec", methods =['POST'])
def pro_enaddrec():
    return render_template("newpro.html")

@app.route("/pro_addrec", methods=['POST'])
def pro_addrec():
    if request.method == 'POST':
        try:
            ma_hs = request.form['ma_hs']
            ten_thiet_bi = request.form['ten_thiet_bi']
            so_giay_chung_nhan = request.form['so_giay_chung_nhan']
            ket_qua = request.form['ket_qua']
            ngay_kiem_dinh = request.form['ngay_kiem_dinh']
            ma_kdv = request.form['ma_kdv']
            so_che_tao = request.form['so_che_tao']
            ma_kh = request.form['ma_kh']




            with sqlite3.connect('KIEMDINH.db') as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO HOSOKIEMDINH(ma_hs,ten_thiet_bi,so_giay_chung_nhan,ket_qua,ngay_kiem_dinh,ma_kdv,so_che_tao,ma_kh) VALUES (?, ?, ?, ?, ?, ?, ?,?)", (ma_hs,ten_thiet_bi,so_giay_chung_nhan,ket_qua,ngay_kiem_dinh,ma_kdv,ma_kh, so_che_tao))
                conn.commit()
                msg = "Record successfully added to database"
        except sqlite3.IntegrityError:
            msg = "Error: Duplicate entry for primary key"
        except sqlite3.Error as e:
            msg = f"Error in the INSERT: {str(e)}"

    return render_template('render.html', msg=msg)

###     EDIT DATA HOSOKIEMDINH
@app.route("/edit_pro", methods=['POST'])
def edit_pro():
    if request.method == 'POST':
        try:
            id = request.form['id']

            con = sqlite3.connect("KIEMDINH.db")
            con.row_factory = sqlite3.Row
        
            cur = con.cursor()
            cur.execute("SELECT * FROM HOSOKIEMDINH WHERE ma_hs = ? ", (id,))

            rows = cur.fetchall()
            
        except:
            id=None
        finally:
            con.close()

    return render_template("edit_pro.html",rows=rows  )


@app.route("/editrec_pro", methods=['POST','GET'])
def editrec_pro():
    con = None
    if request.method == 'POST':
        try:

            ma_hs = request.form['ma_hs']
            ten_thiet_bi = request.form['ten_thiet_bi']
            so_giay_chung_nhan = request.form['so_giay_chung_nhan']
            ket_qua = request.form['ket_qua']
            ngay_kiem_dinh = request.form['ngay_kiem_dinh']
            ma_kdv = request.form['ma_kdv']
            so_che_tao = request.form['so_che_tao']
            ma_kh = request.form['ma_kh']


            

            # UPDATE a specific record in the database based on the rowid
            with sqlite3.connect('KIEMDINH.db') as con:
                cur = con.cursor()
                cur.execute("UPDATE HOSOKIEMDINH SET ten_thiet_bi=?, so_giay_chung_nhan=?, ket_qua =?, ngay_kiem_dinh=?, ma_kdv =?,ma_kh = ? ,so_che_tao =? WHERE ma_hs=?", (ten_thiet_bi, so_giay_chung_nhan,ket_qua, ngay_kiem_dinh,ma_kdv,so_che_tao,ma_kh,ma_hs))
                con.commit()

                msg = "Record successfully edited in the database"
        except Exception as e:
                if con:
                    con.rollback()
                msg = f"Error in the Edit: {str(e)}"
        finally:
            if con:
                con.close()
            return render_template('render.html',msg=msg)


#### DELETE HOSOKIEMDINH
@app.route("/delete_pro", methods=['POST','GET'])
def delete_pro():
    if request.method == 'POST':
        try:

            id = request.form['id']

            with sqlite3.connect('KIEMDINH.db') as con:
                    cur = con.cursor()
                    cur.execute("DELETE FROM HOSOKIEMDINH WHERE ma_hs ="+id)

                    con.commit()
                    msg = "Record successfully deleted from the database"
        except:
            con.rollback()
            msg = "Error in the DELETE"

        finally:
            con.close()

            return render_template('render.html',msg=msg)


if __name__ == "__main__":
    app.debug = True
    app.run(host='localhost', port= 5000) 
    
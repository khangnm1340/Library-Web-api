from datetime import datetime, timedelta
import mysql.connector

# Kết nối với cơ sở dữ liệu MySQL
def ket_noi_csdl():
    try:
        ketnoidb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="snckimbap2k5",
            database="quan_ly_thu_vien",
            charset="utf8mb4",  
            port=3306          
        )
        return ketnoidb 
    except mysql.connector.Error as e:
        print(f"Lỗi kết nối cơ sở dữ liệu: {e}")
        return None

# Lớp Sách
class Sach:
    def __init__(self, id_sach="", ten_sach="", tac_gia="", so_trang=0, nam_xuat_ban=0, trang_thai=0, chung_loai=""):
        self.id_sach = id_sach
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.so_trang = so_trang
        self.nam_xuat_ban = nam_xuat_ban
        self.trang_thai = trang_thai  # 0: có sẵn, 1: đã mượn, 2: trạng thái khác
        self.chung_loai = chung_loai

    # Thêm sách vào cơ sở dữ liệu
    def them_sach(self):
        if self.trang_thai not in [0, 1, 2]:
            print("Trạng thái không hợp lệ!")
            return
        if self.chung_loai not in ['tiểu thuyết', 'giáo khoa', 'khoa học']:
            print("Chủng loại không hợp lệ!")
            return
        ketnoidb = ket_noi_csdl()
        if ketnoidb:
            try:
                cursor = ketnoidb.cursor()
                sql = """INSERT INTO sach (id_sach, ten_sach, tac_gia, so_trang, nam_xuat_ban, trang_thai, chung_loai)
                         VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                values = (self.id_sach, self.ten_sach, self.tac_gia, self.so_trang, self.nam_xuat_ban, self.trang_thai, self.chung_loai)
                cursor.execute(sql, values)
                ketnoidb.commit()
                print("Thêm sách thành công!")
            except mysql.connector.Error as e:
                print(f"Lỗi khi thêm sách: {e}")
            finally:
                cursor.close()
                ketnoidb.close()

    # Sửa thông tin sách
    def sua_sach(self):
        if self.trang_thai not in [0, 1, 2]:
            print("Trạng thái không hợp lệ!")
            return
        if self.chung_loai not in ['tiểu thuyết', 'giáo khoa', 'khoa học']:
            print("Chủng loại không hợp lệ!")
            return
        ketnoidb = ket_noi_csdl()
        if ketnoidb:
            try:
                cursor = ketnoidb.cursor()
                sql = """UPDATE sach SET ten_sach=%s, tac_gia=%s, so_trang=%s, nam_xuat_ban=%s, trang_thai=%s, chung_loai=%s
                         WHERE id_sach=%s"""
                values = (self.ten_sach, self.tac_gia, self.so_trang, self.nam_xuat_ban, self.trang_thai, self.chung_loai, self.id_sach)
                cursor.execute(sql, values)
                ketnoidb.commit()
                print("Sửa thông tin sách thành công!")
            except mysql.connector.Error as e:
                print(f"Lỗi khi sửa sách: {e}")
            finally:
                cursor.close()
                ketnoidb.close()

    # Xóa sách khỏi cơ sở dữ liệu
    def xoa_sach(self, id_sach):
        ketnoidb = ket_noi_csdl()
        if ketnoidb:
            try:
                cursor = ketnoidb.cursor()
                sql = "DELETE FROM sach WHERE id_sach=%s"
                cursor.execute(sql, (id_sach,))
                if cursor.rowcount == 0:
                    print(f"Không tìm thấy sách với ID: {id_sach}")
                else:
                    ketnoidb.commit()
                    print("Xóa sách thành công!")
            except mysql.connector.Error as e:
                print(f"Lỗi khi xóa sách: {e}")
            finally:
                cursor.close()
                ketnoidb.close()

    # Tìm kiếm sách theo ID hoặc tên
    def tim_kiem_sach(self, tu_khoa):
        ketnoidb = ket_noi_csdl()
        if ketnoidb:
            try:
                cursor = ketnoidb.cursor()
                sql = "SELECT * FROM sach WHERE id_sach=%s OR ten_sach LIKE %s"
                cursor.execute(sql, (tu_khoa, f"%{tu_khoa}%"))
                ket_qua = cursor.fetchall()
                for sach in ket_qua:
                    print(sach)
            except mysql.connector.Error as e:
                print(f"Lỗi khi tìm kiếm sách: {e}")
            finally:
                cursor.close()
                ketnoidb.close()

    # Hiển thị danh sách tất cả sách
    def hien_thi_danh_sach_sach(self):
        ketnoidb = ket_noi_csdl()
        if ketnoidb:
            try:
                cursor = ketnoidb.cursor()
                cursor.execute("SELECT * FROM sach")
                ket_qua = cursor.fetchall()
                for sach in ket_qua:
                    print(sach)
            except mysql.connector.Error as e:
                print(f"Lỗi khi hiển thị sách: {e}")
            finally:
                cursor.close()
                ketnoidb.close()

# Lớp Thành viên
class ThanhVien:
    def __init__(self, id_thanh_vien="", ten_thanh_vien=""):
        self.id_thanh_vien = id_thanh_vien
        self.ten_thanh_vien = ten_thanh_vien

    # Thêm thành viên vào cơ sở dữ liệu
    def them_thanh_vien(self):
        ketnoidb = ket_noi_csdl()
        if ketnoidb:
            try:
                cursor = ketnoidb.cursor()
                sql = "INSERT INTO thanh_vien (id_thanh_vien, ten_thanh_vien) VALUES (%s, %s)"
                values = (self.id_thanh_vien, self.ten_thanh_vien)
                cursor.execute(sql, values)
                ketnoidb.commit()
                print("Thêm thành viên thành công!")
            except mysql.connector.Error as e:
                print(f"Lỗi khi thêm thành viên: {e}")
            finally:
                cursor.close()
                ketnoidb.close()

    # Sửa thông tin thành viên
    def sua_thanh_vien(self):
        ketnoidb = ket_noi_csdl()
        if ketnoidb:
            try:
                cursor = ketnoidb.cursor()
                sql = "UPDATE thanh_vien SET ten_thanh_vien=%s WHERE id_thanh_vien=%s"
                values = (self.ten_thanh_vien, self.id_thanh_vien)
                cursor.execute(sql, values)
                ketnoidb.commit()
                print("Sửa thông tin thành viên thành công!")
            except mysql.connector.Error as e:
                print(f"Lỗi khi sửa thành viên: {e}")
            finally:
                cursor.close()
                ketnoidb.close()

    # Xóa thành viên khỏi cơ sở dữ liệu
    def xoa_thanh_vien(self, id_thanh_vien):
        ketnoidb = ket_noi_csdl()
        if ketnoidb:
            try:
                cursor = ketnoidb.cursor()
                sql = "DELETE FROM thanh_vien WHERE id_thanh_vien=%s"
                cursor.execute(sql, (id_thanh_vien,))
                ketnoidb.commit()
                print("Xóa thành viên thành công!")
            except mysql.connector.Error as e:
                print(f"Lỗi khi xóa thành viên: {e}")
            finally:
                cursor.close()
                ketnoidb.close()

    # Tìm kiếm thành viên theo ID hoặc tên
    def tim_kiem_thanh_vien(self, tu_khoa):
        ketnoidb = ket_noi_csdl()
        if ketnoidb:
            try:
                cursor = ketnoidb.cursor()
                sql = "SELECT * FROM thanh_vien WHERE id_thanh_vien=%s OR ten_thanh_vien LIKE %s"
                cursor.execute(sql, (tu_khoa, f"%{tu_khoa}%"))
                ket_qua = cursor.fetchall()
                for tv in ket_qua:
                    print(tv)
            except mysql.connector.Error as e:
                print(f"Lỗi khi tìm kiếm thành viên: {e}")
            finally:
                cursor.close()
                ketnoidb.close()

    # Hiển thị danh sách tất cả thành viên
    def hien_thi_danh_sach_thanh_vien(self):
        ketnoidb = ket_noi_csdl()
        if ketnoidb:
            try:
                cursor = ketnoidb.cursor()
                cursor.execute("SELECT * FROM thanh_vien")
                ket_qua = cursor.fetchall()
                for tv in ket_qua:
                    print(tv)
            except mysql.connector.Error as e:
                print(f"Lỗi khi hiển thị thành viên: {e}")
            finally:
                cursor.close()
                ketnoidb.close()

# Lớp Quản lý mượn trả sách
class QuanLyMuonTra:
    def __init__(self):
        pass  

    # Mượn sách
    def muon_sach(self, id_thanh_vien, id_sach):
        ketnoidb = ket_noi_csdl()
        if ketnoidb:
            try:
                cursor = ketnoidb.cursor()
                cursor.execute("SELECT trang_thai FROM sach WHERE id_sach=%s", (id_sach,))
                trang_thai = cursor.fetchone()
                if trang_thai and trang_thai[0] == 0:
                    ngay_muon = datetime.now()
                    # Nhập ngày trả từ người dùng
                    ngay_tra_str = input("Nhập ngày trả (YYYY-MM-DD): ")
                    ngay_tra = datetime.strptime(ngay_tra_str, "%Y-%m-%d")
                    # Kiểm tra ngày trả hợp lệ
                    if ngay_tra <= ngay_muon:
                        print("Ngày trả phải sau ngày mượn!")
                        return
                    sql = """INSERT INTO muon_tra (id_thanh_vien, id_sach, ngay_muon, ngay_tra)
                             VALUES (%s, %s, %s, %s)"""
                    cursor.execute(sql, (id_thanh_vien, id_sach, ngay_muon, ngay_tra))
                    cursor.execute("UPDATE sach SET trang_thai=1 WHERE id_sach=%s", (id_sach,))
                    ketnoidb.commit()
                    print("Mượn sách thành công!")
                else:
                    print("Sách không có sẵn để mượn!")
            except mysql.connector.Error as e:
                print(f"Lỗi khi mượn sách: {e}")
            except ValueError:
                print("Định dạng ngày không đúng! Vui lòng nhập theo YYYY-MM-DD.")
            finally:
                cursor.close()
                ketnoidb.close()

    # Trả sách
    def tra_sach(self, id_thanh_vien, id_sach):
        ketnoidb = ket_noi_csdl()
        if ketnoidb:
            try:
                cursor = ketnoidb.cursor()
                cursor.execute("SELECT trang_thai FROM sach WHERE id_sach=%s", (id_sach,))
                trang_thai = cursor.fetchone()
                if trang_thai and trang_thai[0] == 1:
                    cursor.execute("DELETE FROM muon_tra WHERE id_thanh_vien=%s AND id_sach=%s",
                                 (id_thanh_vien, id_sach))
                    cursor.execute("UPDATE sach SET trang_thai=0 WHERE id_sach=%s", (id_sach,))
                    ketnoidb.commit()
                    print("Trả sách thành công!")
                else:
                    print("Sách không được mượn hoặc không tồn tại!")
            except mysql.connector.Error as e:
                print(f"Lỗi khi trả sách: {e}")
            finally:
                cursor.close()
                ketnoidb.close()

    # Hiển thị danh sách sách mượn quá hạn
    def hien_thi_sach_qua_han(self):
        ketnoidb = ket_noi_csdl()
        if ketnoidb:
            try:
                cursor = ketnoidb.cursor()
                ngay_hien_tai = datetime(2025, 6, 10, 10, 49)  
                sql = """SELECT mt.id_thanh_vien, tv.ten_thanh_vien, mt.id_sach, s.ten_sach, mt.ngay_tra
                         FROM muon_tra mt
                         JOIN thanh_vien tv ON mt.id_thanh_vien = tv.id_thanh_vien
                         JOIN sach s ON mt.id_sach = s.id_sach
                         WHERE mt.ngay_tra < %s"""
                cursor.execute(sql, (ngay_hien_tai,))
                ket_qua = cursor.fetchall()
                for qua_han in ket_qua:
                    print(qua_han)
            except mysql.connector.Error as e:
                print(f"Lỗi khi hiển thị sách quá hạn: {e}")
            finally:
                cursor.close()
                ketnoidb.close()

# Hàm chính để chạy ứng dụng
def main():
    # Tạo instance cho các lớp
    sach = Sach()
    thanh_vien = ThanhVien()
    muon_tra = QuanLyMuonTra()

    while True:
        print("\n=== ỨNG DỤNG QUẢN LÝ THƯ VIỆN ===")
        print("1. Thêm sách")
        print("2. Sửa sách")
        print("3. Xóa sách")
        print("4. Tìm kiếm sách")
        print("5. Hiển thị danh sách sách")
        print("6. Thêm thành viên")
        print("7. Sửa thành viên")
        print("8. Xóa thành viên")
        print("9. Tìm kiếm thành viên")
        print("10. Hiển thị danh sách thành viên")
        print("11. Mượn sách")
        print("12. Trả sách")
        print("13. Hiển thị sách quá hạn")
        print("14. Thoát")
        
        lua_chon = input("Nhập lựa chọn của bạn: ")
        
        if lua_chon == "1":
            id_sach = input("Nhập ID sách: ")
            ten_sach = input("Nhập tên sách: ")
            tac_gia = input("Nhập tác giả: ")
            so_trang = int(input("Nhập số trang: "))
            nam_xuat_ban = int(input("Nhập năm xuất bản: "))
            trang_thai = int(input("Nhập trạng thái (0: có sẵn, 1: đã mượn, 2: khác): "))
            chung_loai = input("Nhập chủng loại (tiểu thuyết, giáo khoa, khoa học): ")
            sach_temp = Sach(id_sach, ten_sach, tac_gia, so_trang, nam_xuat_ban, trang_thai, chung_loai)
            sach_temp.them_sach()
        
        elif lua_chon == "2":
            id_sach = input("Nhập ID sách cần sửa: ")
            ten_sach = input("Nhập tên sách mới: ")
            tac_gia = input("Nhập tác giả mới: ")
            so_trang = int(input("Nhập số trang mới: "))
            nam_xuat_ban = int(input("Nhập năm xuất bản mới: "))
            trang_thai = int(input("Nhập trạng thái mới (0: có sẵn, 1: đã mượn, 2: khác): "))
            chung_loai = input("Nhập chủng loại mới: ")
            sach_temp = Sach(id_sach, ten_sach, tac_gia, so_trang, nam_xuat_ban, trang_thai, chung_loai)
            sach_temp.sua_sach()
        
        elif lua_chon == "3":
            id_sach = input("Nhập ID sách cần xóa: ")
            sach.xoa_sach(id_sach)
        
        elif lua_chon == "4":
            tu_khoa = input("Nhập ID hoặc tên sách cần tìm: ")
            sach.tim_kiem_sach(tu_khoa)
        
        elif lua_chon == "5":
            sach.hien_thi_danh_sach_sach()
        
        elif lua_chon == "6":
            id_thanh_vien = input("Nhập ID thành viên: ")
            ten_thanh_vien = input("Nhập tên thành viên: ")
            tv_temp = ThanhVien(id_thanh_vien, ten_thanh_vien)
            tv_temp.them_thanh_vien()
        
        elif lua_chon == "7":
            id_thanh_vien = input("Nhập ID thành viên cần sửa: ")
            ten_thanh_vien = input("Nhập tên thành viên mới: ")
            tv_temp = ThanhVien(id_thanh_vien, ten_thanh_vien)
            tv_temp.sua_thanh_vien()
        
        elif lua_chon == "8":
            id_thanh_vien = input("Nhập ID thành viên cần xóa: ")
            thanh_vien.xoa_thanh_vien(id_thanh_vien)
        
        elif lua_chon == "9":
            tu_khoa = input("Nhập ID hoặc tên thành viên cần tìm: ")
            thanh_vien.tim_kiem_thanh_vien(tu_khoa)
        
        elif lua_chon == "10":
            thanh_vien.hien_thi_danh_sach_thanh_vien()
        
        elif lua_chon == "11":
            id_thanh_vien = input("Nhập ID thành viên: ")
            id_sach = input("Nhập ID sách: ")
            muon_tra.muon_sach(id_thanh_vien, id_sach)  
        elif lua_chon == "12":
            id_thanh_vien = input("Nhập ID thành viên: ")
            id_sach = input("Nhập ID sách: ")
            muon_tra.tra_sach(id_thanh_vien, id_sach)
        
        elif lua_chon == "13":
            muon_tra.hien_thi_sach_qua_han()
        
        elif lua_chon == "14":
            print("Thoát ứng dụng.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()
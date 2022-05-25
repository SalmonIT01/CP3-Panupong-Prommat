username = input("Username:")
password = input("Password:")
if username =="sompong" and password =="1150":
    print("ยินดีต้อนรับสู่ร้าน MurakamiBook")
    print("รายการสินค้า:")
    print("1.หนังสือ Norwegion Wood 350 บาท ")
    print("2.หนังสือ Sputnik SweetHeart 200 บาท ")
    print("3.หนังสือ South of The Border,West of The Sun 250 บาท ")
    print("4.หนังสือ Kafka on the Shore 600 บาท ")
    userSelect = int(input(">>>"))
    if userSelect == 1:
        book = int(input("จำนวนเล่ม:"))
        bookPrice = book*350
        result = print("ราคาทั้งหมด:",bookPrice,"บาท")
    elif userSelect == 2:
        book = int(input("จำนวนเล่ม:"))
        bookPrice = book *200
        result = print("ราคาทั้งหมด:", bookPrice, "บาท")
    elif userSelect == 3:
        book = int(input("จำนวนเล่ม:"))
        bookPrice = book *250
        result = print("ราคาทั้งหมด:", bookPrice, "บาท")
    elif userSelect == 4:
        book = int(input("จำนวนเล่ม:"))
        bookPrice = book *600
        result = print("ราคาทั้งหมด:", bookPrice, "บาท")

else:
    print("username หรือ password ผิด")
    print("โปรดลองใหม่อีกครั้ง")

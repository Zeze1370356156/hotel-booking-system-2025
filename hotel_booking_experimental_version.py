Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # hotel_booking.py

# 模拟酒店房间数据
rooms = {
    '101': {'status': 'available', 'guest': None},
    '102': {'status': 'available', 'guest': None},
    '103': {'status': 'available', 'guest': None},
}

# 显示所有房间状态
def show_rooms():
    print("房间状态：")
    for room, details in rooms.items():
        print(f"房间 {room}: {details['status']}")

# 预订房间
def book_room(room_number, guest_name):
    if rooms[room_number]['status'] == 'available':
        rooms[room_number]['status'] = 'booked'
        rooms[room_number]['guest'] = guest_name
        print(f"房间 {room_number} 已成功预订给 {guest_name}。")
    else:
        print(f"房间 {room_number} 不可用。")

# 取消预订
def cancel_booking(room_number):
    if rooms[room_number]['status'] == 'booked':
        guest_name = rooms[room_number]['guest']
        rooms[room_number]['status'] = 'available'
        rooms[room_number]['guest'] = None
        print(f"房间 {room_number} 的预订已取消（原预订人：{guest_name}）。")
    else:
        print(f"房间 {room_number} 没有预订记录。")

# 主程序
def main():
    while True:
        print("\n酒店预约系统")
        print("1. 显示房间状态")
        print("2. 预订房间")
        print("3. 取消预订")
        print("4. 退出")
        choice = input("请选择操作：")

        if choice == '1':
            show_rooms()
        elif choice == '2':
            room_number = input("请输入房间号：")
            guest_name = input("请输入客人姓名：")
            book_room(room_number, guest_name)
        elif choice == '3':
            room_number = input("请输入房间号：")
            cancel_booking(room_number)
        elif choice == '4':
            print("退出系统。")
            break
        else:
            print("无效选项，请重试。")

if __name__ == "__main__":
    main()

# hotel_booking_class.py

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = {
            '101': {'status': 'available', 'guest': None},
            '102': {'status': 'available', 'guest': None},
            '103': {'status': 'available', 'guest': None},
        }

    def display_rooms(self):
        """显示所有房间状态"""
        print(f"\n{self.name} 的房间状态：")
        for room, details in self.rooms.items():
            status = details['status']
            guest = details['guest'] if details['guest'] else "无"
            print(f"房间 {room} - 状态: {status}, 客人: {guest}")

    def book_room(self, room_number, guest_name):
        """预订房间"""
        if room_number not in self.rooms:
            print(f"房间 {room_number} 不存在。")
            return False
        
        if self.rooms[room_number]['status'] == 'available':
            self.rooms[room_number]['status'] = 'booked'
            self.rooms[room_number]['guest'] = guest_name
            print(f"房间 {room_number} 已成功预订给 {guest_name}。")
            return True
        else:
            print(f"房间 {room_number} 不可用。")
            return False

    def cancel_booking(self, room_number):
        """取消预订"""
        if room_number not in self.rooms:
            print(f"房间 {room_number} 不存在。")
            return False
        
        if self.rooms[room_number]['status'] == 'booked':
            guest_name = self.rooms[room_number]['guest']
            self.rooms[room_number]['status'] = 'available'
            self.rooms[room_number]['guest'] = None
            print(f"房间 {room_number} 的预订已取消（原预订人：{guest_name}）。")
            return True
        else:
            print(f"房间 {room_number} 没有预订记录。")
            return False

def main():
    # 创建酒店对象
    my_hotel = Hotel("星辰酒店")

    while True:
        print("\n=== 酒店预约系统 ===")
        print("1. 显示房间状态")
        print("2. 预订房间")
        print("3. 取消预订")
        print("4. 退出")

        choice = input("请选择操作：")

        if choice == '1':
            my_hotel.display_rooms()
        elif choice == '2':
            room_number = input("请输入房间号：")
            guest_name = input("请输入客人姓名：")
            my_hotel.book_room(room_number, guest_name)
        elif choice == '3':
            room_number = input("请输入房间号：")
            my_hotel.cancel_booking(room_number)
        elif choice == '4':
            print("退出系统。")
            break
        else:
            print("无效选项，请重试。")

if __name__ == "__main__":
    main()

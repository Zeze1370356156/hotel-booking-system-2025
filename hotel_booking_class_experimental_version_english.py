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
        """Display the status of all rooms"""
        print(f"\n{self.name} Room Status:")
        for room, details in self.rooms.items():
            status = details['status']
            guest = details['guest'] if details['guest'] else "None"
            print(f"Room {room} - Status: {status}, Guest: {guest}")

    def book_room(self, room_number, guest_name):
        """Book a room"""
        if room_number not in self.rooms:
            print(f"Room {room_number} does not exist.")
            return False
        
        if self.rooms[room_number]['status'] == 'available':
            self.rooms[room_number]['status'] = 'booked'
            self.rooms[room_number]['guest'] = guest_name
            print(f"Room {room_number} has been successfully booked for {guest_name}.")
            return True
        else:
            print(f"Room {room_number} is not available.")
            return False

    def cancel_booking(self, room_number):
        """Cancel a booking"""
        if room_number not in self.rooms:
            print(f"Room {room_number} does not exist.")
            return False
        
        if self.rooms[room_number]['status'] == 'booked':
            guest_name = self.rooms[room_number]['guest']
            self.rooms[room_number]['status'] = 'available'
            self.rooms[room_number]['guest'] = None
            print(f"Booking for Room {room_number} has been canceled (original guest: {guest_name}).")
            return True
        else:
            print(f"Room {room_number} has no booking record.")
            return False

def main():
    # Create a hotel object
    my_hotel = Hotel("Star Hotel")

    while True:
        print("\n=== Hotel Booking System ===")
        print("1. Display Room Status")
        print("2. Book a Room")
        print("3. Cancel Booking")
        print("4. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            my_hotel.display_rooms()
        elif choice == '2':
            room_number = input("Please enter the room number: ")
            guest_name = input("Please enter the guest's name: ")
            my_hotel.book_room(room_number, guest_name)
        elif choice == '3':
            room_number = input("Please enter the room number: ")
            my_hotel.cancel_booking(room_number)
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()

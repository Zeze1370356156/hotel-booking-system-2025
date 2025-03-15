# hotel_booking_class.py

class Hotel:
    def init(self, name):
        self.name = name
        # Fixed price for all rooms
        self.room_price = 200
        self.rooms = {
            '101': {'status': 'available', 'guest': None, 'payment': None, 'rating': None, 'review': None},
            '102': {'status': 'available', 'guest': None, 'payment': None, 'rating': None, 'review': None},
            '103': {'status': 'available', 'guest': None, 'payment': None, 'rating': None, 'review': None},
        }

    def display_rooms(self):
        """Display the status of all rooms"""
        print(f"\n{self.name} Room Status:")
        for room, details in self.rooms.items():
            status = details['status']
            guest = details['guest'] if details['guest'] else "None"
            payment = f"Paid: {details['payment']}" if details['payment'] else "Not Paid"
            rating = f"Rating: {details['rating']}" if details['rating'] else "No Rating"
            review = f"Review: {details['review']}" if details['review'] else "No Review"
            print(f"Room {room} - Status: {status}, Guest: {guest}, {payment}, {rating}, {review}")

    def book_room(self, room_number, guest_name):
        """Book a room"""
        if room_number not in self.rooms:
            print(f"Room {room_number} does not exist.")
            return False
        
        if self.rooms[room_number]['status'] == 'available':
            # Fixed price for booking
            payment_amount = self.room_price
            self.rooms[room_number]['status'] = 'booked'
            self.rooms[room_number]['guest'] = guest_name
            self.rooms[room_number]['payment'] = payment_amount
            print(f"Room {room_number} has been successfully booked for {guest_name}. Payment: {payment_amount}")
            return True
        else:
            print(f"Room {room_number} is not available.")
            return False

    def cancel_booking(self, room_number):
        """Cancel a booking (before check-in)"""
        if room_number not in self.rooms:
            print(f"Room {room_number} does not exist.")
            return False
        
        if self.rooms[room_number]['status'] == 'booked':
            guest_name = self.rooms[room_number]['guest']
            self.rooms[room_number]['status'] = 'available'
            self.rooms[room_number]['guest'] = None
            self.rooms[room_number]['payment'] = None
            print(f"Booking for Room {room_number} has been canceled (original guest: {guest_name}).")
            return True
        else:
            print(f"Room {room_number} has no booking record.")
            return False

    def check_out(self, room_number):
        """Check out and rate the room"""
        if room_number not in self.rooms:
            print(f"Room {room_number} does not exist.")
            return False
        
        if self.rooms[room_number]['status'] == 'booked':
            guest_name = self.rooms[room_number]['guest']
            # Ask for rating and review
            try:
                rating = int(input("Please rate the room (1-5): "))
                if rating < 1 or rating > 5:
                    print("Rating must be between 1 and 5.")
                    return False
            except ValueError:
                print("Invalid rating. Please enter a number between 1 and 5.")
                return False

            review = input("Please leave a review (optional): ")

            # Reset room status and record rating/review
            self.rooms[room_number]['status'] = 'available'
            self.rooms[room_number]['guest'] = None
            self.rooms[room_number]['payment'] = None
            self.rooms[room_number]['rating'] = rating
            self.rooms[room_number]['review'] = review
            print(f"Guest {guest_name} has checked out from Room {room_number}.")
            print(f"Thank you for your rating: {rating} and review: {review}")
            return True
        else:
            print(f"Room {room_number} is not booked.")
            return False
def main():
    # Create a hotel object
    my_hotel = Hotel("Star Hotel")

    while True:
        print("\n=== Hotel Booking System ===")
        print("1. Display Room Status")
        print("2. Book a Room")
        print("3. Cancel Booking (before check-in)")
        print("4. Check Out and Rate Room")
        print("5. Exit")

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
            room_number = input("Please enter the room number: ")
            my_hotel.check_out(room_number)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid option, please try again.")

if name == "main":
    main()
if __name__ == "__main__":
    main()

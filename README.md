# Hotel Booking System

This is a simple hotel booking system project implemented in Python. The project is designed using Object-Oriented Programming (OOP) and supports viewing room status, booking rooms, and canceling bookings.

## Features

1. **Display Room Status**: View the current status (available or booked) and guest information for all rooms.
2. **Book a Room**: Enter the room number and guest name to book a specific room.
3. **Cancel Booking**: Enter the room number to cancel a booked room.
4. **Exit System**: Terminate the program.
5. **Rating input**： Use a slider to select a rating from 1 to 5 stars, providing an intuitive user experience.


## Code Structure

- `Hotel` Class: Represents the hotel, containing a list of rooms and methods for operations.
- `Room` Class: Represents a room, containing the room number, status, check out and guest information.
- `main` Function: Provides a user interaction interface.






# 酒店预约系统

这是一个简单的酒店预约系统项目，使用 Python 实现。项目基于面向对象编程（OOP）设计，支持房间状态查看、房间预订和取消预订功能。

## 功能列表

1. **显示房间状态**：查看所有房间的当前状态（可用或已预订）及客人信息。
2. **预订房间**：输入房间号和客人姓名，预订指定房间。
3. **取消预订**：输入房间号，取消已预订的房间。
4. **退出系统**：结束程序运行。

## 代码结构

- `Hotel` 类：表示酒店，包含房间列表和操作方法。
- `Room` 类：表示房间，包含房间号、状态和客人信息。
- `main` 函数：提供用户交互界面。

##完整项目构架
hotel_system/
│
├── app.py                # Flask API 应用
├── models.py             # 数据库模型和Hotel类
├── hotel_cli.py          # 命令行界面
├── main.py               # 主入口文件
├── requirements.txt      # 依赖文件
└── hotel.db              # SQLite数据库文件 (运行后自动生成)


##requirements.txt 内容：
flask
flask-restx
python-dotenv

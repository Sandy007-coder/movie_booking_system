
# 🎬 Movie Booking System (CLI-Based)

This project is a CLI-based Movie Booking System developed using Python that simulates a real-world ticket booking platform. It allows users to select a city, theatre, movie, screen, timing, and seats through an interactive interface. The system includes a dynamic seat selection feature with availability tracking, a ticket booking limit for normal users with admin override, and price calculation based on screen type. Booking data is stored using an SQLite database, with additional JSON and text file backups for persistence. It also provides functionalities such as viewing, searching, and cancelling bookings with automatic seat release, making it a complete and practical booking simulation system.


## 🚀 Features

* Interactive CLI-based movie booking system
* Seat selection with real-time availability
* Ticket limit with admin override
* Price calculation based on screen type
* Booking storage using SQLite database
* Search, view, and cancel bookings
* Automatic seat release on cancellation

## 🛠️ Tools & Technologies

* Python
* SQLite (Database)
* JSON (Data Storage)
* File Handling (TXT Reports)
* Logging Module
## 📁 Project Structure

movie-booking-system/
│
├── src/
│   ├── booking.py
│   ├── database.py
│   ├── data.py
│   ├── logger.py
│   ├── utils.py
│
├── data_storage/
│   ├── bookings.db
│   ├── bookings.json
│   ├── tickets.txt
│
├── logs/
│   └── app.log
│
├── main.py
├── README.md
├── .gitignore
## ▶️ How to Run

1. Clone the repository

git clone https://github.com/Sandy007-coder/movie-booking-system.git


2. Navigate to the project folder

cd movie-booking-system

3. Run the application 

python main.py

or

python3 main.py
## 📈 Results

- Successfully simulates a real-world movie ticket booking system  
- Prevents double booking using seat tracking system  
- Supports dynamic pricing based on screen type  
- Provides booking history, search, and cancellation features  
- Generates ticket receipts in TXT and JSON formats  
- Maintains logs for tracking user actions  
## 🔮 Future Improvements

* Add GUI using Tkinter or Web interface (Flask/Django)
* Implement online payment integration
* Add user authentication system
* Improve seat visualization with graphics
* Deploy as a web application
## 🎯 Learning Outcomes

* Gained hands-on experience with Python and CLI application development
* Learned database integration using SQLite
* Implemented file handling using JSON and text files
* Designed a seat management system to prevent double booking
* Improved problem-solving and project structuring skills
## 👨‍💻 Author

Sarveswaran S

* 🎓 B.Tech CSE (Cybersecurity)
* 🔐 Cybersecurity, Python & Data Analytics Enthusiast
* 🎯 Interested in Penetration Testing, Red Teaming, and Data Analysis

🔗 GitHub: https://github.com/Sandy007-coder

🔗 LinkedIn: (https://www.linkedin.com/in/sarveswaran-cybersec?utm_source=share_via&utm_content=profile&utm_medium=member_android)
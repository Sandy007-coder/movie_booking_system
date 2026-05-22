
# 🎬 Movie Ticket Booking System | Python + SQLite

A command-line based Movie Ticket Booking System developed using Python and SQLite. This application simulates a real-world cinema booking workflow, allowing users to select cities, theatres, movies, screens, and show timings, along with interactive seat selection.
It includes features like dynamic pricing based on screen type, booking management (view, search, cancel), and persistent data storage using SQLite, JSON, and text files. The project is designed with a modular structure, logging system, and environment-based configuration, making it scalable, maintainable, and suitable for demonstrating backend development skills.

  
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

```bash
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
```
## ▶️ How to Run

1. Clone the repository

   git clone https://github.com/Sandy007-coder/movie-booking-system.git


2. Navigate to the project folder

   cd movie-booking-system

3. Run the application 

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
## 👨‍💻 Author

Sarveswaran S

* 🎓 B.Tech CSE (Cybersecurity)
* 🔐 Cybersecurity, Python & Data Analytics Enthusiast
* 🎯 Interested in Penetration Testing, Red Teaming, and Data Analysis

🔗 GitHub: https://github.com/Sandy007-coder

🔗 LinkedIn: (https://www.linkedin.com/in/sarveswaran-cybersec?utm_source=share_via&utm_content=profile&utm_medium=member_android)

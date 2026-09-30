# Hotel Room Booking System

A command-line hotel room booking system written in pure Python. It has two separate parts: a **customer side** for browsing, booking and checking out of rooms, and a **management side** protected by a username and password for managing rooms and viewing bookings.

## Overview

Small hotels often track rooms and bookings by hand, which leads to double bookings and lost records. This project shows how a simple terminal program can:

- let customers find a room that fits their group size,
- show the price and ask for confirmation before booking,
- keep track of which rooms are available or booked,
- give staff a protected area to manage rooms and see bookings.

The project uses only the Python standard library. It has no database and no external packages. All data is kept in memory while the program runs.

## Features

**Customer side (no login needed)**
- View rooms by capacity: the program asks "Room for how many people?" and lists only rooms with that capacity.
- Book a room: enter name, room number and number of nights. A booking summary with the total price is shown and the customer must confirm (`yes`/`no`).
- Check out: enter name and room number to free the room again.

**Management side (login required)**
- Login with username and password, limited to 3 attempts.
- View all rooms and their status.
- Add a new room (every answer is validated).
- Remove a room.
- View all bookings, their status (staying / checked out) and total income.

**Room data**

Rooms are stored in a nested dictionary (`rooms`), keyed by room number. Every room has at least: room number, bed type, capacity, area (m²), Wi-Fi and availability. It also stores room type, price per night, view, amenities, and whether pets and smoking are allowed. The program starts with 10 rooms.

## Technologies Used

- Python 3 (standard library only)
- Data structures: dictionaries (nested), lists
- Concepts: functions, loops, conditionals, string formatting, input validation

## Requirements

- Python 3.6 or newer (uses f-strings)
- A terminal or command prompt
- No extra libraries to install

## How to Install and Run

1. **Check that Python is installed.** Open a terminal and run:
   ```
   python --version
   ```
   On some systems the command is `python3 --version`. If Python is not installed, download it from https://www.python.org/downloads/.

2. **Get the project.** Clone the repository (replace the placeholders with the real values) and move into the folder:
   ```
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
   Alternatively, download the repository as a ZIP file from GitHub, extract it, and open a terminal in the extracted folder.

3. **Install dependencies.** None are needed, so you can skip this step.

4. **Run the program:**
   ```
   python main.py
   ```
   (or `python3 main.py` on Linux/macOS)

5. **Use the menus** by typing the number of an option and pressing Enter. Choose `3` at the welcome screen to exit.

### Configuration

The management login is set at the top of `main.py`:

| Setting | Default value |
|---|---|
| Username | `admin` |
| Password | `1234` |

Change `ADMIN_USERNAME` and `ADMIN_PASSWORD` in `main.py` to use different credentials.

## Example Walkthrough

**Booking a room as a customer**
1. Start the program and choose `1` (Customer).
2. Choose `1` (View rooms) and enter `2` to see rooms for two people.
3. Choose `2` (Book a room), enter your name, a room number such as `103`, and the number of nights.
4. Check the booking summary and type `yes` to confirm.
5. Later, choose `3` (Check out) and enter the same name and room number to free the room.

**Managing rooms as staff**
1. At the welcome screen choose `2` (Management) and log in.
2. Use `2` (Add room) to add a room, `3` (Remove room) to delete one, or `4` (View bookings) to see all bookings and total income.
3. Choose `5` to log out.

## Project Structure

```
.
├── main.py       # the whole program: data, customer menu, management menu
└── README.md     # this file
```

## Testing

There are no automated tests yet, so the program is tested manually. Run `python main.py` and check the following:

| # | Test | Expected result |
|---|---|---|
| 1 | Customer > View rooms, enter `2` | Only rooms with capacity 2 are listed |
| 2 | Customer > View rooms, enter `7` | "No rooms found for 7 person(s)." |
| 3 | Customer > View rooms, enter `abc` | "Please enter a number." (no crash) |
| 4 | Book room `103` for 3 nights, confirm with `yes` | Summary shows `86.00 x 3 = 258.00`; room becomes booked |
| 5 | Book a room and answer `no` at confirmation | "Booking cancelled." and the room stays available |
| 6 | Book room `104` (already booked) | "Sorry, that room is already booked." |
| 7 | Check out with the correct name and room number | Room becomes available again |
| 8 | Check out with a wrong name or room | "No active booking found for that name and room." |
| 9 | Management login with a wrong password 3 times | "Too many failed attempts." and return to the welcome screen |
| 10 | Management > Add room with bad input (empty text, letters or `0` for capacity, negative price) | The question is asked again; no crash |
| 11 | Management > View bookings after a booking and a check-out | Shows `(staying)` or `(checked out)` and the total income |

## Limitations

- Data is stored in memory only, so rooms and bookings reset each time the program is closed.
- The admin password is stored in plain text in the source code.
- There is a single admin account.
- Booking is by number of nights only; there are no calendar dates.

## Screenshots

*(Add screenshots of the customer menu, a booking summary and the management menu here.)*

Update Station
=========

Update Station is a GUI application for managing software updates on GhostBSD-based systems. It provides a user-friendly interface to check for updates, install updates, and handle system upgrades.

## Features

- **Tray Icon Notification**: Displays a tray icon to notify users about available updates.
- **Update Management**: Check for and install software updates with ease.
- **Boot Environment Backup**: Create and manage boot environment backups before updating.
- **Major System Upgrades**: Handle major system version upgrades seamlessly.
- **Detailed Progress Tracking**: View detailed progress of update and upgrade processes.
- **Error Handling**: Provides clear error messages and guidance if updates fail.

## Installation

1. **Install Dependencies**:
   Ensure you have the necessary dependencies installed:
   ```
   pkg install libappindicator
   ```

2. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd update-station
   ```

3. **Make the Script Executable**:
   ```
   chmod +x update-station
   ```

4. **Run the Application**:
   ```
   sudo ./update-station
   ```

## Usage

### Running the Application
To start Update Station, simply run:
```
sudo ./update-station
```

### Open Update Window Directly
To open the update window directly from the command line, use:
```
sudo ./update-station open-update
```

## Contributing

We welcome contributions! Please fork the repository and submit pull requests for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

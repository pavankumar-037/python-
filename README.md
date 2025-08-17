# 🔐 Random Password Generator

A secure and customizable password generator web application built with Python Flask backend and HTML/CSS frontend.

## ✨ Features

- **Secure Password Generation**: Uses user-provided data to create unique passwords.
- **Personalized Inputs**: Incorporates user name, birthday, and email for unique passwords.
- **Password Difficulty Levels**: Options for Easy, Medium, and Hard password generation.
- **Strong Password Policy**: Ensures inclusion of lowercase, uppercase, digits, and special characters.
- **Responsive Design**: Works on desktop and mobile devices.
- **Real-time Generation**: Instant password generation with AJAX requests.

## 🛠️ Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: GitHub for version control

## 🚀 Installation Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/pavankumar-037/python-.git
   cd python-
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python api/index.py
   ```

4. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 📁 API Endpoints

- `GET /` - Serves the main interface.
- `POST /generate` - Generates a secure password based on user inputs.

### Request Body
```json
{
  "name": "User's Name",
  "birthday": "dd/mm/yyyy",
  "gmail": "user@example.com",
  "difficulty": "easy | medium | hard"
}
```

### Response
```json
{
  "password": "GeneratedPassword123!",
  "length": 16,
  "source": "User provided data only"
}
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

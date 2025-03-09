Django URL Shortener

A simple Django-based URL Shortener that allows users to shorten long URLs and redirect them easily.

🚀 Features

Shorten long URLs with a unique short code.

Redirect short URLs to the original long URL.

Track the number of times a short URL has been accessed.

User-friendly interface for generating and managing URLs.

🛠️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/AniketGanguli/django-url-shortener.git
cd django-url-shortener

2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Apply Migrations

python manage.py migrate

5️⃣ Run the Development Server

python manage.py runserver

Now, open your browser and visit http://127.0.0.1:8000/ to use the app! 🎉

📌 Usage

Enter a long URL into the input box.

Click Shorten to generate a short URL.

Use the short URL to redirect to the original URL.

🏗️ Project Structure

urlshortener/
│── shortener/        # Main app for shortening URLs
│── staticfiles/      # Static files (CSS, JS, images)
│── templates/        # HTML templates
│── urlshortener/     # Project settings and configurations
│── db.sqlite3        # SQLite database
│── manage.py         # Django management script
│── requirements.txt  # Python dependencies

📜 License

This project is open-source under the MIT License.

📞 Contact

For any queries, feel free to reach out:

GitHub: AniketGanguli

Email: aniketganguli6@gmail.com (Replace with your actual email)

⭐ Star this repository if you find it useful! 🚀


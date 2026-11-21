import json
import csv
import configparser
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

USERS_PATH = BASE_DIR / "data" / "users.csv"
EMAILS_PATH = BASE_DIR / "data" / "emails.json"
CONFIG_FILE = BASE_DIR / "config" / "config.ini"
CSV_PATH = BASE_DIR / "export" / "accepted_users.csv"


def load_config():
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(CONFIG_FILE)

    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    if not config.has_section("processing"):
        raise FileNotFoundError(CONFIG_FILE)
    return config


def load_emails():
    with open(EMAILS_PATH, encoding="utf-8") as emails_file:
        users_emails = json.load(emails_file)
        return users_emails


def load_users():
    with open(USERS_PATH, newline="", encoding="utf-8") as users_file:
        return list(csv.DictReader(users_file, delimiter=","))


def process_users(users, emails, config):
    min_age = config["processing"].getint("min_age")
    email_required = config["processing"].getboolean("email_required")

    accepted_users = []
    rejected_users = []

    for user in users:
        user_id = user["id"]
        user["email"] = emails.get(user_id)

        reasons = []

        if email_required and not user["email"]:
            reasons.append("Email not found")

        age = try_parse_int(user["age"])
        if age is None:
            reasons.append("Could not parse age")
        elif age < min_age:
            reasons.append("Underage")

        if reasons:
            rejected_users.append({
                "id": user_id,
                "name": user["name"],
                "reason": reasons})
            continue

        accepted_users.append(user)

    return accepted_users, rejected_users


def try_parse_int(age):
    try:
        return int(age)
    except (ValueError, TypeError):
        return None


def save_accepted_users(data):
    fieldnames = ["id", "name", "surname", "age", "email"]
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(CSV_PATH, "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()

        for user in data:
            csv_writer.writerow({
                key: user.get(key)
                for key in fieldnames
            })


def main():
    users = load_users()
    emails = load_emails()
    config = load_config()
    accepted, rejected = process_users(users, emails, config)
    save_accepted_users(accepted)

    print(f"""Статистика
-   Всего пользователей прошедшие обработку: {len(accepted)+len(rejected)}
-   Успешно принято: {len(accepted)}
-   Отклонено: {len(rejected)}
""")


if __name__ == "__main__":
    main()

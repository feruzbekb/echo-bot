import requests


class Bot:
    def __init__(self, token: str) -> None:
        self.token = token
        self.last_update_id: int | None = None

    def get_updates(self) -> list[dict]:
        payload = {"offset": self.last_update_id}
        response = requests.get(
            f"https://api.telegram.org/bot{self.token}/getUpdates", params=payload
        )
        if response.status_code == 200:
            data = response.json()
            return data["result"]

        return []

    def send_message(self, chat_id: int, text: str, reply_markup: list = []) -> None:
        payload = {"chat_id": chat_id, "text": text}
        response = requests.get(
            f"https://api.telegram.org/bot{self.token}/sendMessage", params=payload
        )

    def send_photo(self, chat_id: int, photo: str | list) -> None:
        payload = {
            "chat_id": chat_id,
            "photo": photo if type(str) == str else photo[0]["file_id"],
        }
        response = requests.get(
            f"https://api.telegram.org/bot{self.token}/sendPhoto", params=payload
        )

    def send_location(self, chat_id: int, lat: float, lon: float) -> None:
        pass

    def send_contact(self, chat_id: int, phone_number: str, first_name: str) -> None:
        pass

    def send_document(self, chat_id: int, document: str) -> None:
        pass

    def send_voice(self, chat_id: int, voice: str) -> None:
        pass

    def send_video(self, chat_id: int, video: str) -> None:
        pass

    def send_dice(self, chat_id: int, dice: str) -> None:
        pass

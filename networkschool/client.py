from httpx import AsyncClient
from httpx import Cookies
from networkschool import exceptions
from datetime import date, timedelta

class NetworkSchool:
    def __init__(
        self,
        url: str,
        username: str,
        password: str
    ):
        self._client = AsyncClient(
            base_url=f'{url.rstrip("/")}',
            headers = {"User-Agent":"NetworkSchool/1.0.0"},
            verify=False
        )
        self._username = username
        self._password = password
        
    async def get_diary(self, from_date = None, to_date = None):
        if not from_date:
            today = date.today()
            from_date = today - timedelta(days=today.weekday())
        if not to_date:
            to_date = from_date + timedelta(days=5)
        async with self._client as client:
            diary = await client.post(
                "/rest/diary",
                data = {
                    "pupil_id": self._user_id,
                    "from_date": from_date,
                    "to_date": to_date
                },
            )
            return diary.json()

    async def get_total(self):
        today = date.today()
        async with self._client as client:
            total = await client.post(
                "/rest/totals",
                data = {
                    "pupil_id": self._user_id,
                    'date': today.strftime("%d.%m.%Y")
                }
            )
            print(total)
            return total.json()

    async def _login(self):
        async with self._client as client:
            sessionId = await client.get(
                "/rest/login?",
                params = {
                    "login": self._username,
                    "password": self._password
                }
            )
            sessionId_json = sessionId.json()
            if sessionId_json['success'] != True:
                raise exceptions.NetworkSchool(sessionId_json['message'])

            self._user_id = sessionId_json['childs'][0][0]

    async def __aenter__(self) -> "NetworkSchool":
        await self._login()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        return self
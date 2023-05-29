import aiohttp

class ChatbaseModel:
    captcha_code = "hadsa"

    async def GetAnswer(self, prompt: str, model: str = "gpt-4"):
        if model == "gpt-4":
            chat_id = "quran---tafseer-saadi-pdf-wbgknt7zn"
        elif model == "gpt-3.5-turbo":
            chat_id = "chatbase--1--pdf-p680fxvnm"


        async with aiohttp.ClientSession() as session:
            response = await session.post(
                "https://www.chatbase.co/api/fe/chat",
                json={"chatId": chat_id, "captchaCode": self.captcha_code, "messages": prompt}
            )
            r = await response.text()

        return r

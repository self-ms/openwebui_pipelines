from typing import List, Union


class Pipeline:
    def __init__(self):
        pass  # No setup needed

    async def on_startup(self):
        # You can load or initialize anything here if needed
        pass

    async def on_shutdown(self):
        # Cleanup resources if needed
        pass

    def pipe(
            self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, None]:
        """
        Simple pipeline that returns a text response without any database or model.
        You can customize how the response is generated here.
        """
        print("Received message:", user_message)

        # Example simple logic: reverse the message, or echo it
        response = f"You said: {user_message}"

        return response

# UChicago Trading xchange-v3-client

## Installation
To get started, pip install the exchange library:
```shell
$ pip install utcxchangelib
```

## Setup
To use the client, create a subclass of the XChangeClient object.

```python
class MyXchangeClient(xchange_client.XChangeClient):
    '''A shell client with the methods that can be implemented to interact with the xchange.'''

     def __init__(self, host: str, username: str, password: str):
        super().__init__(host, username, password)

    async def start(self, user_interface):
        asyncio.create_task(self.trade())

        # This is where Phoenixhood will be launched if desired. There is no need to change these
        # lines, you can either remove the if or delete the whole thing depending on your purposes.
        if user_interface:
            self.launch_user_interface()
            asyncio.create_task(self.handle_queued_messages())

        await self.connect()
```
You should also implement the bot handler methods that are defined. In your bots, you can choose to trade or cancel orders based on the messages received.

```python
class MyXchangeClient(xchange_client.XChangeClient):
     ...
    async def bot_handle_cancel_response(self, order_id: str, success: bool, error: Optional[str]) -> None:
        order = self.open_orders[order_id]
        print(f"{'Market' if order[2] else 'Limit'} Order ID {order_id} cancelled, {order[1]} unfilled")

    async def bot_handle_order_fill(self, order_id: str, qty: int, price: int):
        print("order fill", self.positions)

    async def bot_handle_order_rejected(self, order_id: str, reason: str) -> None:
        print("order rejected because of ", reason)

    async def bot_handle_trade_msg(self, symbol: str, price: int, qty: int):
        pass

    async def bot_handle_book_update(self, symbol: str) -> None:
        pass

    async def bot_handle_swap_response(self, swap: str, qty: int, success: bool):
        pass

    async def bot_handle_news(self, news_release: dict):
        # Parsing the message based on what type was received
        timestamp = news_release["timestamp"] # This is in exchange ticks not ISO or Epoch
        news_type = news_release['kind']
        news_data = news_release["new_data"]

        if news_type == "structured":
            subtype = news_data["structured_subtype"]
            symb = news_data["asset"]
            if subtype == "earnings":
                earnings = news_data["value"]
                ### Do something with this data ###
            else:
                new_signatures = news_data["new_signatures"]
                cumulative = news_data["cumulative"]
                ### Do something with this data ###
        else:
            ### Not sure what you would do with unstructured data.... ###
            pass
```

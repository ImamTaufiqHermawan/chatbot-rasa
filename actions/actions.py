# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from tkinter import EventType
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.forms import FormValidationAction

class ActionPizzaOrderForm(FormValidationAction):

    def name(self) -> Text:
        return "action_pizza_order_form"

    async def required_slots(        
        self,
        domain_slots: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[Text]:
        pizza_type = tracker.slots.get('pizza_type')
        pizza_amount = tracker.slots.get('pizza_amount')
        pizza_size = tracker.slots.get('pizza_size')

        print(pizza_type, pizza_amount, pizza_size)

        dispatcher.utter_message(
            text=f"ok Great. Your order is {pizza_amount} {pizza_type} pizza in {pizza_size} size. Can you please confirm your order?")

        return []
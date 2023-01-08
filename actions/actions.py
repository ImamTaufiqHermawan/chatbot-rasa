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

from rasa_sdk.forms import FormAction
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionConfirm(Action):

    def name(self) -> Text:
        return "action_confirm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        service = tracker.get_slots('service')
        p_count = tracker.get_slots('p_count')

        print(service, p_count)

        dispatcher.utter_message(text=f"Hi there, you booked {p_count} {service} tickets. Please confirm your booking")

        return []

class ActionPizzaOrderForm(FormAction):

    def name(self) -> Text:
        return "action_pizza_order_form"

    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["pizza_size", "pizza_type", "pizza_amount"]

    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        pizza_type = tracker.get_slots('pizza_type')
        pizza_size = tracker.get_slots('pizza_size')
        pizza_amount = tracker.get_slots('pizza_amount')
        
        print(pizza_type, pizza_size, pizza_amount)

        dispatcher.utter_message(text=f"ok Great. Your order is {pizza_amount} {pizza_type} pizza in {pizza_size} size. Can you please confirm your order?")
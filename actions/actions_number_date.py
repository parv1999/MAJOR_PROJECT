# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


#This is a simple example for a custom action which utters "Hello World!"

from html import entities
from re import template
from typing import Any, Text, Dict, List
import numpy as np
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

yrs = int(np.random.rand(1)*1000)

class ActionDateofBuilding(Action):

    def name(self) -> Text:
        print("Hello Action")
        return "action_number/date"

    def run(self, dispatcher: CollectingDispatcher , tracker: Tracker, domain: Dict[Text, Any] ) -> List[Dict[Text, Any]] :

        intent      = tracker.latest_message['intent']

        entities    = tracker.latest_message['entities']
        #['entities']

        #print(entities['value'])
        for e in entities:
            entity = e['value']

        dispatcher.utter_message(template="utter_number/date",building=entity,years=yrs)

        return []

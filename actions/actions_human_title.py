from html import entities
import keyword 
from re import template 
from typing import Any, Text, Dict, List 
from rasa_sdk import Action, Tracker 
from rasa_sdk.executor import CollectingDispatcher


class ActionHumanIndividual(Action):

    def name(self) -> Text:

        return "action_human/title"


    def run(self, dispatcher: CollectingDispatcher, tracker:Tracker , domain: Dict[Text,Any] ) -> List[Dict[Text,Any]]:

        intent   = tracker.latest_message['intent']

        entities = tracker.latest_message['entities']

        for e in entities:

            print(f"{e} \n")

        dispatcher.utter_message(template="utter_human/title",name="naruto",keyword="KEYWORD")    

        return []    
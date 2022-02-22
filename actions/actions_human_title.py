from html import entities
import keyword 
from re import template 
from typing import Any, Text, Dict, List 
from rasa_sdk import Action, Tracker 
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionLocation(Action):

    def name(self) -> Text:

        return "action_location"


    def run(self, dispatcher: CollectingDispatcher, tracker:Tracker , domain: Dict[Text,Any] ) -> List[Dict[Text,Any]]:

        intentt   =  (tracker.latest_message.get("response_selector", {}).get("human", {}).get("ranking",[])[0]['intent_response_key'])
        
        intent   = tracker.latest_message['intent']

        print(f"Latest itent is {intent}")

        print(f"FUll intent: f{intentt}")

        entities = tracker.latest_message['entities']

        for e in entities:

            print(f"{e} \n")


        temp_plate = "/".join["utter_location",intentt.split()[1]]

        dispatcher.utter_message(template=temp_plate,name="naruto",keyword="KEYWORD")    

        return []    
        
        # intent   = tracker.latest_message['intent']

        # entities = tracker.latest_message['entities']

        # for e in entities:

        #     print(f"{e} \n")

        # dispatcher.utter_message(template="utter_human/title",name="naruto",keyword="KEYWORD")    

        # return []    
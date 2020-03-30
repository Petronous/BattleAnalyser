# BattleAnalyser
 Analyse large Freeciv battles

 `BattleCleanser.py` takes BD.txt (Battle Details) as input and hopefully deletes all non-combat messages, output is cleanBD.txt

 `BattleCondenser.py` takes BD.txt (Battle Details) as input. (The raw console log needs to be cleansed of any other than combat messages beforehand, either through another script, or manually.) It outputs easy-to-process interBD.txt

 `BattleAnalyser.py` takes interBD.txt and makes it into Table.txt, which sums up unit type numbers used in a battle by each side.

 `BattleLossCalc.py` takes interBD.txt and calculates production loss for each side into Losses.txt. It does that through a costDict defined at the first lines of the program - this dictionary only contains units used in the Great Battle, so only some lategame stuff, but can be easily expanded.
 
 Luis' $('#game_message_area')[0].innerText typed into web console (or retrieved through other means)  is the only method I know for how to get the battlelog

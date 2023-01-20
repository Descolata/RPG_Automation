"""
Script runs Weather for Pathfinder, focusing on the Shackles but workable anywhere.
"""
import dice
import random

def stormbound_hazards(strmHazRoll, strmHazMod, pilotRoll):
    if strmHazRoll > 99:
        strmHaz = "Serious Hull Breach: The vessel's hull is punctured and it immediately begins to sink."

    elif strmHazRoll > 94:
        strmHaz = "Two Hazards: \n1)" + stormbound_hazards( sum( dice.roll("1d100") ) + strmHazMod - pilotRoll, strmHazMod, pilotRoll) + "\n\n2)" + stormbound_hazards( sum( dice.roll("1d100")  + strmHazMod - pilotRoll ), strmHazMod, pilotRoll)
    
    elif strmHazRoll > 92:
        strmHaz = "Pooped: A massive wave engulfs the vessel unexpectedly from the stern. \
                    \nTreat as a bull rush with a CMB of +30 against all characters on deck, \
                    \nrunning stern to bow. Those who fail are swept overboard. \
                    \nFor the purposes of this bull rush attempt, treat creatures as flat-footed."

    elif strmHazRoll > 90:
        strmHaz = "Submarined: The ship plunges down by the bow under a huge oncoming wave. \
                    \nTreat this as a bull rush with a CMB of +30 against all creatures on deck. \
                    \nThose who fail are swept overboard."

    elif strmHazRoll > 88:
        strmHaz = "Broached: The vessel is blown over, flat against the sea. \
                    \nThe vessel rights itself in 1d4 rounds, but creatures on deck \
                    \nmust succeed at a DC 22 Reflex save each round or fall overboard. \
                    \nUnsecured cargo and equipment falls overboard."

    elif strmHazRoll > 86:
        strmHaz = "Broken Mast: One of the vessel's masts snaps in the wind. \
                    \nThe mast falls overboard and, unless cut free from all rigging \
                    \nand allowed to float away, it pierces the hull in "+str( sum( dice.roll("2d6") ) )+" rounds. \
                    \n(see Serious Hull Breach)"

    elif strmHazRoll > 83:
        lghtngStrkRoll = sum( dice.roll("1d100") )

        if lghtngStrkRoll > 60:
            strmHaz = "Lightning Strike: The character at the highest point on deck takes"+str( sum( dice.roll("4d6") ) )+" damage."
            
        else:
            strmHaz = "Lightning Strike: A bolt strikes the vessel doing"+str( sum( dice.roll("4d6") ) )+" damage."
            
    elif strmHazRoll > 80:
        strmHaz = "Lost Lifeboat: A lifeboat/small vessel falls overboard or breaks free."

    elif strmHazRoll > 77:
        if random.random() > .5:
            strmHaz = "Spoiled Stores: Saltwater ruins "+str( sum( dice.roll("1d4") ) )+" weeks of dry stores"
        
        else:
            strmHaz = "Spoiled Stores: Saltwater ruins "+str( sum( dice.roll("1d4") ) )+" plunder"
    
    elif strmHazRoll > 74:
        strmHaz = "Sprung a Leak: The vessel springs a minor leak at a random location."

    elif strmHazRoll > 71:
        strmHaz = "Crew Member Overboard: Starting with the creature on deck closest to the stern," \
                    +"\n"+str( sum( dice.roll("1d3") ) )+" creatures adjacent to the side must make DC 16 Reflex saves in turn. \
                    \nIf one creature fails, it falls overboard and the others need not make further saves."


    elif strmHazRoll > 68:
        strmHaz = "Loose Cargo: Poorly secured items on deck break free. \
                    \nCreatures in a random 20-foot square take "+str( sum( dice.roll("3d6") ) )+" points of damage. \
                    \n(Reflex DC15 half )."

    elif strmHazRoll > 65:
        strmHaz = "Torn Sail: Strong winds tear a sail in twain. If sails have been reefed or lowered already, \
                    \ntreat this as Lashing Rigging. \
                    \n   Lashing Rigging: A rope comes loose, whipping across deck. \
                    \n   Creatures in a random 20-foot line on deck must succeed at a DC 13 Reflex save \
                    \n   or take "+str( sum( dice.roll("2d6") ) )+" points of nonlethal damage."

    elif strmHazRoll > 60:
        strmHaz = "Wind against Tide: The sea becomes a massof steep waves, \
                    \nreducing the ship's movement speed by half for 1 hour."
    
    elif strmHazRoll > 55:
        strmHaz = "Lashing Rigging: A rope comes loose, whipping across deck. \
                    \nCreatures in a random 20-foot line on deck must succeed at a DC 13 Reflex save \
                    \nor take "+str( sum( dice.roll("2d6") ) )+" points of nonlethal damage."

    elif strmHazRoll > 45:
        strmHaz = "Violent Swell: A single violent wave strikes the vessel. \
                    \nAll creatures on deck must succeed at a DC 15 Reflex save or fall prone."

    elif strmHazRoll > 40:
        strmHaz = "Jammed Rudder: Steering becomes extremely difficult. \
                    \nAll Profession (sailor) checks are made with a -10 penalty \
                    \nuntil the rudder is unjammed, either via a successful DC 15 Craft (carpentry) check \
                    \nor by casting warp wood or a similar spell."

    elif strmHazRoll > 35:
        strmHaz = "Dragged Anchor: The ship travels 100 feet in a random direction in 1 round \
                    \nand is no longer considered anchored. This hazard only affects anchored ships; \
                    \notherwise, treat as the Slippery Deck hazard. \
                    \n   Slippery Deck: A rush of water over the deck makes it more slippery than usual \
                    \n   for "+str( sum( dice.roll("1d4") ) )+" rounds. Creatures must succeed at a \
                    \n   DC 10 Acrobatics check to move safely; failure means they fall prone."

    elif strmHazRoll > 20:
        strmHaz = "Slippery Deck: A rush of water over the deck makes it more slippery than usual \
                    \nfor "+str( sum( dice.roll("1d4") ) )+" rounds. Creatures must succeed at a \
                    \nDC 10 Acrobatics check to move safely; failure means they fall prone."
    else:
        strmHaz = "No Hazard"

    return strmHaz

# Necessary variables
distanceToEye = int( input("$Distance to Eye of Abendego:") )

if distanceToEye < 50:
    eyeMod = 60
elif distanceToEye < 100:
    eyeMod = 36
elif distanceToEye < 200:
    eyeMod = 12
elif distanceToEye < 250:
    eyeMod = 8
elif distanceToEye < 300:
    eyeMod = 4
else:
    eyeMod = 0

navCheck = int( input("$Input Navigation Roll:") )

wthrRoll = sum( dice.roll("1d100") ) - navCheck

if wthrRoll > 99:
    weather = "Tornado/Waterspout"
    strmHazMod = 15
    strmHazFreq = "1 / round"
    wthrDuration = str( sum( dice.roll("1d6") ) ) + " minutes"
    verse = "Whole Damn Hymn"
    wthrFeat = "Ranged Attacks: Impossible \nSiege Attacks: Impossible \nChecked Size: Huge \nBlown Away Size: Large \nFly Penalty: -16 \nPerception: Impossible"
    wind = round( 175+125*random.random() )

elif wthrRoll > 97:
    weather = "Hurricane"
    strmHazMod = 15
    strmHazFreq = "1 / minute"
    wthrDuration = str( sum( dice.roll("4d6") ) ) + " minutes"
    verse = "9"
    wthrFeat = "Ranged Attacks: Impossible \nSiege Attacks: -8 \nChecked Size: Large \nBlown Away Size: Medium \nFly Penalty: -12 \nPerception: Impossible"
    wind = round( 75 + 99*random.random() )

elif wthrRoll > 93:
    weather = "Severe Tropical Storm"
    strmHazMod = 10
    strmHazFreq = "1 / 10 minutes"
    wthrDuration = str( sum( dice.roll("3d6") ) ) + " hours"
    wthrFeat = "Ranged Attacks: Impossible \nSiege Attacks: -4 \nChecked Size: Medium \nBlown Away Size: Small \nFly Penalty: -8 \nPerception: -8"
    if wthrRoll > 95:
        verse = "8"
        wind = round( 62+12*random.random() )
    else:
        verse = "7"
        wind = round( 51+11*random.random() )
 

elif wthrRoll > 80:
    weather = "Tropical Storm"
    strmHazMod = 0
    strmHazFreq = "1 / hour"
    wthrDuration = str( sum( dice.roll("5d4") ) ) + " hours"
    wthrFeat = "Ranged Attacks: -4 \nSiege Attacks: -- \nChecked Size: Small \nBlown Away Size: Tiny \nFly Penalty: -4 \nPerception: -4"
    if wthrRoll > 87:
        verse = 6
        wind = round( 41 + 9*random.random() )
    else:
        verse = 5
        wind = round( 31 + 9*random.random() )

elif wthrRoll > 65:
    weather = "Tropical Depression"
    strmHazMod = -10
    strmHazFreq = "1 / hour"
    wthrDuration = str( sum( dice.roll("2d4") ) ) + " hours"
    wthrFeat = "Ranged Attacks: -2 \nSiege Attacks: -- \nChecked Size: Tiny \nBlown Away Size: -- \nFly Penalty: -2 \nPerception: -4"
    if wthrRoll > 73:
        verse = 4
        wind = round ( 26 + 4*random.random() )
    else:
        verse = 3
        wind = round(21 + 4*random.random() )

elif wthrRoll > 55:
    strmHazMod = "No Hazard"
    strmHazFreq = "No Hazard"
    wthrDuration = None

    precip = round( 100*random.random() )
    if precip > 40:
        weather = "Rain"
        wthrFeat = "Perception: -4"
        verse = 2
        wind = round( 20*random.random() )
    else:  
        weather = "Fog"
        wthrFeat = "Concealment at 5 ft"
        verse = 1
        wind = round( 20*random.random() )
    
else:
    weather = "Normal"
    strmHazMod = "No Hazard"
    strmHazFreq = "No Hazard"
    wthrDuration = None
    wthrFeat = "Perfect Weather for Sailing"
    verse = 0
    wind = round( 20*random.random() )

print("Weather: "+weather)
if wthrDuration != None:
    print("Duration: "+wthrDuration)
print("Hazard Freq: "+strmHazFreq)
print("Windspeed: " + str(wind) + "mph")
print("Features: \n" + wthrFeat)

# Stormbound Hazard system
while(strmHazMod != "No Hazard"):
    pilotRoll = int( input("$Input Pilot Roll:") )
    strmHazRoll = sum( dice.roll("1d100") ) + strmHazMod - pilotRoll
    strmHaz = stormbound_hazards(strmHazRoll, strmHazMod, pilotRoll)
    print( "Stormbound Hazard: \n\n"+strmHaz )
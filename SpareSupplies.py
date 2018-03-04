__title__ = 'SpareSupplies'
__author__ = 'samvds'
__version__ = '1.1.2'

import clr
clr.AddReferenceByPartialName("Fougerite")
import Fougerite

white = "[color#FFFFFF]"
cyan = "[color#00FFFF]"
green = "[color#00FF00]"
red = "[color#FF0000]"
yellow = "[color$FFFF00]"
sysname = "LegacyLives"

class SpareSupplies:

    def On_PluginInit(self):
        Util.ConsoleLog("SpareSuppliies" + " v" + __version__ + " by " + __author__ + " loaded.", True)

    def Amount(self, arg):
        try:
            x = int(arg)
            if x <= 1:
                return 101
                #returns 101 when number is smaller than or equal to 1
            return x
            #returns a number greater than or equal to 1
        except:
            return 100
            #returns 100 when string is not a number

    def On_Command(self, Player, cmd, args):
        amount = self.Amount
        if cmd == "recycle":
            if len(args) == 0:
                Player.MessageFrom(sysname,
                                   "Use " + cyan + "/recycle \"item\" \"amount\" " + white + "- to recycle a certain amount of a specific item.")
                Player.MessageFrom(sysname,
                                   "Example given: " + cyan + "/recycle woodbarricade 5" + white + " or " + cyan + "/recycle metaldoor 2")
            elif len(args) == 1:
                if args[0] == "woodbarricade":
                    if Player.Inventory.HasItem("Wood Barricade", 1):
                        Player.Inventory.RemoveItem("Wood Barricade", 1)
                        Player.Inventory.AddItem("Wood", 30)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "woodceiling":
                    if Player.Inventory.HasItem("Wood Ceiling", 1):
                        Player.Inventory.RemoveItem("Wood Ceiling", 1)
                        Player.Inventory.AddItem("Wood Planks", 6)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "wooddoorway":
                    if Player.Inventory.HasItem("Wood Doorway", 1):
                        Player.Inventory.RemoveItem("Wood Doorway", 1)
                        Player.Inventory.AddItem("Wood Planks", 4)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "woodfoundation":
                    if Player.Inventory.HasItem("Wood Foundation", 1):
                        Player.Inventory.RemoveItem("Wood Foundation", 1)
                        Player.Inventory.AddItem("Wood Planks", 8)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "woodgate":
                    if Player.Inventory.HasItem("Wood Gate", 1):
                        Player.Inventory.RemoveItem("Wood Gate", 1)
                        Player.Inventory.AddItem("Wood", 120)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "woodgateway":
                    if Player.Inventory.HasItem("Wood Gateway", 1):
                        Player.Inventory.RemoveItem("Wood Gateway", 1)
                        Player.Inventory.AddItem("Wood", 400)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
            elif len(args) == 2:
                amount = self.Amount((args[1]))
                if amount == 100:
                    Player.MessageFrom(sysname,
                                       "Use " + cyan + "/recycle \"item\" \"amount\" " + white + "- to recycle a certain amount of a specific item.")
                elif amount == 101:
                    Player.MessageFrom(sysname, yellow + "☢ " + red + "You can't recycle \"0\" of something!")
                else: 
                    if Player.Inventory.HasItem("Wood Barricade", amount):
                        Player.Inventory.RemoveItem("Wood Barricade", amount)
                        Player.Inventory.AddItem("Wood", 30*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Wood Ceiling", amount):
                        Player.Inventory.RemoveItem("Wood Ceiling", amount)
                        Player.Inventory.AddItem("Wood Planks", 6*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Wood Doorway", amount):
                        Player.Inventory.RemoveItem("Wood Doorway", amount)
                        Player.Inventory.AddItem("Wood Planks", 4*amound)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Wood Foundation", amount):
                        Player.Inventory.RemoveItem("Wood Foundation", amount)
                        Player.Inventory.AddItem("Wood Planks", 8*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Wood Gate", amount):
                        Player.Inventory.RemoveItem("Wood Gate", amount)
                        Player.Inventory.AddItem("Wood", 120*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Wood Gateway", amount):
                        Player.Inventory.RemoveItem("Wood Gateway", amount)
                        Player.Inventory.AddItem("Wood", 400*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
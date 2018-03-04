__title__ = 'SpareSupplies'
__author__ = 'samvds'
__version__ = '1.2.1'

import clr
clr.AddReferenceByPartialName("Fougerite")
import Fougerite

white = "[color#FFFFFF]"
cyan = "[color#00FFFF]"
green = "[color#00FF00]"
red = "[color#FF0000]"
yellow = "[color#FFFF00]"
sysname = "SpareSupplies"

class SpareSupplies:

    def On_PluginInit(self):
        Util.ConsoleLog("SpareSuppliies" + " v" + __version__ + " by " + __author__ + " loaded.", True)

    def Amount(self, arg):
        try:
            x = int(arg)
            if x <= 0:
                return 101
                #returns 101 when number is smaller than 1
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
                elif args[0] == "woodpillar":
                    if Player.Inventory.HasItem("Wood Pillar", 1):
                        Player.Inventory.RemoveItem("Wood Pillar", 1)
                        Player.Inventory.AddItem("Wood Planks", 2)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "woodplanks":
                    if Player.Inventory.HasItem("Wood Planks", 1):
                        Player.Inventory.RemoveItem("Wood Planks", 1)
                        Player.Inventory.AddItem("Wood", 10)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "woodramp":
                    if Player.Inventory.HasItem("Wood Ramp", 1):
                        Player.Inventory.RemoveItem("Wood Ramp", 1)
                        Player.Inventory.AddItem("Wood Planks", 5)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "woodshelter":
                    if Player.Inventory.HasItem("Wood Shelter", 1):
                        Player.Inventory.RemoveItem("Wood Shelter", 1)
                        Player.Inventory.AddItem("Wood", 60)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "woodstairs":
                    if Player.Inventory.HasItem("Wood Stairs", 1):
                        Player.Inventory.RemoveItem("Wood Stairs", 1)
                        Player.Inventory.AddItem("Wood Planks", 5)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "woodstoragebox":
                    if Player.Inventory.HasItem("Wood Storage Box", 1):
                        Player.Inventory.RemoveItem("Wood Storage Box", 1)
                        Player.Inventory.AddItem("Wood", 30)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "woodwall":
                    if Player.Inventory.HasItem("Wood Wall", 1):
                        Player.Inventory.RemoveItem("Wood Wall", 1)
                        Player.Inventory.AddItem("Wood Planks", 4)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "woodwindow":
                    if Player.Inventory.HasItem("Wood Window", 1):
                        Player.Inventory.RemoveItem("Wood Window", 1)
                        Player.Inventory.AddItem("Wood Planks", 4)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "woodendoor":
                    if Player.Inventory.HasItem("Wooden Door", 1):
                        Player.Inventory.RemoveItem("Wooden Door", 1)
                        Player.Inventory.AddItem("Wood", 30)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "largewoodstorage":
                    if Player.Inventory.HasItem("Large Wood Storage", 1):
                        Player.Inventory.RemoveItem("Large Wood Storage", 1)
                        Player.Inventory.AddItem("Wood", 60)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "workbench":
                    if Player.Inventory.HasItem("Workbench", 1):
                        Player.Inventory.RemoveItem("Workbench", 1)
                        Player.Inventory.AddItem("Wood", 50)
                        Player.Inventory.AddItem("Stones", 8)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "furnace":
                    if Player.Inventory.HasItem("Furnace", 1):
                        Player.Inventory.RemoveItem("Furnace", 1)
                        Player.Inventory.AddItem("Wood", 20)
                        Player.Inventory.AddItem("Stones", 15)
                        Player.Inventory.AddItem("Low Grade Fuel", 10)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "campfire":
                    if Player.Inventory.HasItem("Camp Fire", 1):
                        Player.Inventory.RemoveItem("Camp Fire", 1)
                        Player.Inventory.AddItem("Wood", 5)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "repairbench":
                    if Player.Inventory.HasItem("Repair Bench", 1):
                        Player.Inventory.RemoveItem("Repair Bench", 1)
                        Player.Inventory.AddItem("Wood", 60)
                        Player.Inventory.AddItem("Stones", 12)
                        Player.Inventory.AddItem("Metal Fragments", 50)
                        Player.Inventory.AddItem("Low Grade Fuel", 6)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "metalceiling":
                    if Player.Inventory.HasItem("Metal Ceiling", 1):
                        Player.Inventory.RemoveItem("Metal Ceiling", 1)
                        Player.Inventory.AddItem("Low Quality Metal", 6)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "metaldoor":
                    if Player.Inventory.HasItem("Metal Door", 1):
                        Player.Inventory.RemoveItem("Metal Door", 1)
                        Player.Inventory.AddItem("Metal Fragments", 200)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "metaldoorway":
                    if Player.Inventory.HasItem("Metal Doorway", 1):
                        Player.Inventory.RemoveItem("Metal Doorway", 1)
                        Player.Inventory.AddItem("Low Quality Metal", 4)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "metalfoundation":
                    if Player.Inventory.HasItem("Metal Foundation", 1):
                        Player.Inventory.RemoveItem("Metal Foundation", 1)
                        Player.Inventory.AddItem("Low Quality Metal", 8)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "metalpillar":
                    if Player.Inventory.HasItem("Metal Pillar", 1):
                        Player.Inventory.RemoveItem("Metal Pillar", 1)
                        Player.Inventory.AddItem("Low Quality Metal", 2)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "metalramp":
                    if Player.Inventory.HasItem("Metal Ramp", 1):
                        Player.Inventory.RemoveItem("Metal Ramp", 1)
                        Player.Inventory.AddItem("Low Quality Metal", 5)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "metalstairs":
                    if Player.Inventory.HasItem("Metal Stairs", 1):
                        Player.Inventory.RemoveItem("Metal Stairs", 1)
                        Player.Inventory.AddItem("Low Quality Metal", 5)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "metalwall":
                    if Player.Inventory.HasItem("Metal Wall", 1):
                        Player.Inventory.RemoveItem("Metal Wall", 1)
                        Player.Inventory.AddItem("Low Quality Metal", 4)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    else:
                        Player.MessageFrom(sysname, yellow + "☢ " + red + "You don't have enough to recycle!")
                elif args[0] == "metalwindow":
                    if Player.Inventory.HasItem("Metal Window", 1):
                        Player.Inventory.RemoveItem("Metal Window", 1)
                        Player.Inventory.AddItem("Low Quality Metal", 4)
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
                    if Player.Inventory.HasItem("Wood Pillar", amount):
                        Player.Inventory.RemoveItem("Wood Pillar", amount)
                        Player.Inventory.AddItem("Wood Planks", 2*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Wood Planks", amount):
                        Player.Inventory.RemoveItem("Wood Planks", amount)
                        Player.Inventory.AddItem("Wood", 10*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Wood Ramp", amount):
                        Player.Inventory.RemoveItem("Wood Ramp", amount)
                        Player.Inventory.AddItem("Wood Planks", 5*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Wood Shelter", amount):
                        Player.Inventory.RemoveItem("Wood Shelter", amount)
                        Player.Inventory.AddItem("Wood", 60*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Wood Stairs", amount):
                        Player.Inventory.RemoveItem("Wood Stairs", amount)
                        Player.Inventory.AddItem("Wood Planks", 5*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Wood Storage Box", amount):
                        Player.Inventory.RemoveItem("Wood Storage Box", amount)
                        Player.Inventory.AddItem("Wood", 30*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Wood Wall", amount):
                        Player.Inventory.RemoveItem("Wood Wall", amount)
                        Player.Inventory.AddItem("Wood Planks", 4*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Wood Window", amount):
                        Player.Inventory.RemoveItem("Wood Window", amount)
                        Player.Inventory.AddItem("Wood Planks", 4*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Wooden Door", amount):
                        Player.Inventory.RemoveItem("Wooden Door", amount)
                        Player.Inventory.AddItem("Wood", 30*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Large Wood Storage", amount):
                        Player.Inventory.RemoveItem("Large Wood Storage", amount)
                        Player.Inventory.AddItem("Wood", 60*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Workbench", amount):
                        Player.Inventory.RemoveItem("Workbench", amount)
                        Player.Inventory.AddItem("Wood", 50*amount)
                        Player.Inventory.AddItem("Stones", 8*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Furnace", amount):
                        Player.Inventory.RemoveItem("Furnace", amount)
                        Player.Inventory.AddItem("Wood", 20*amount)
                        Player.Inventory.AddItem("Stones", 15*amount)
                        Player.Inventory.AddItem("Low Grade Fuel", 10*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Camp Fire", amount):
                        Player.Inventory.RemoveItem("Camp Fire", amount)
                        Player.Inventory.AddItem("Wood", 5*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Repair Bench", amount):
                        Player.Inventory.RemoveItem("Repair Bench", amount)
                        Player.Inventory.AddItem("Wood", 60*amount)
                        Player.Inventory.AddItem("Stones", 12*amount)
                        Player.Inventory.AddItem("Metal Fragments", 50*amount)
                        Player.Inventory.AddItem("Low Grade Fuel", 6*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Metal Ceiling", amount):
                        Player.Inventory.RemoveItem("Metal Ceiling", amount)
                        Player.Inventory.AddItem("Low Quality Metal", 6*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Metal Door", amount):
                        Player.Inventory.RemoveItem("Metal Door", amount)
                        Player.Inventory.AddItem("Metal Fragments", 200*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Metal Doorway", amount):
                        Player.Inventory.RemoveItem("Metal Doorway", amount)
                        Player.Inventory.AddItem("Low Quality Metal", 4*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Metal Foundation", amount):
                        Player.Inventory.RemoveItem("Metal Foundation", amount)
                        Player.Inventory.AddItem("Low Quality Metal", 8*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Metal Pillar", amount):
                        Player.Inventory.RemoveItem("Metal Pillar", amount)
                        Player.Inventory.AddItem("Low Quality Metal", 2*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Metal Ramp", amount):
                        Player.Inventory.RemoveItem("Metal Ramp", amount)
                        Player.Inventory.AddItem("Low Quality Metal", 5*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Metal Stairs", amount):
                        Player.Inventory.RemoveItem("Metal Stairs", amount)
                        Player.Inventory.AddItem("Low Quality Metal", 5*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Metal Wall", amount):
                        Player.Inventory.RemoveItem("Metal Wall", amount)
                        Player.Inventory.AddItem("Low Quality Metal", 4*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
                    if Player.Inventory.HasItem("Metal Window", amount):
                        Player.Inventory.RemoveItem("Metal Window", amount)
                        Player.Inventory.AddItem("Low Quality Metal", 4*amount)
                        Player.Notice("Thank you for thinking of the environment. Go green!")
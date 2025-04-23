#CryptCoin-Final Project
#David Armstrong
#Group 1
import tkinter as tk
from tkinter import ttk
current_location = "town square"
class Inventory:
    def __init__(self, coinPouch, toolPouch):
        self.coinPouch = coinPouch
        self.toolPouch = toolPouch
        
class Coin:
    def __init__(self, name, price, toughness, hp):
        self.name = name
        self.price = price
        self.toughness = toughness
        self.hp = hp
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Toughness: {self.toughness}"
    
class Player:
    def __init__(self, name, hp, money, inventory, equippedTool):
        self.name = name
        self.hp = int(hp)
        self.money = int(money)
        self.inventory = inventory
        self.equippedTool = equippedTool
    def attack(self, enemy):
        enemy.hp -= self.dmg
    def mine(self, equippedTool, coin):
        coin.hp -= equippedTool.coinDmg
        if coin.hp <= 0:
            player.inventory.coinPouch[coin.name] += 1
            add_dialogue(dialogue_text, f"you earned 1 {coin.name}")
class npc:
    def __init__(self, name):
        self.name = name
        self.reputation = reputation
        
class ShopKeeper(npc):
    def __init__(self, reputation):
        self.reputation = reputation
        super().__init__("Sherman")
        
class Enemy:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
    def attack(self, player):
        player.hp -= self.dmg
        
class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 20, 5)

class Troll(Enemy):
    def __init__(self):
        super().__init__("Troll", 30, 8)

class Dwarf(Enemy):
    def __init__(self):
        super().__init__("Dwarf", 40, 12)
        
class Shade(Enemy):
    def __init__(self):
        super().__init__("Shade", 75, 29)
        
class Tool():
    def __init__(self, name, dmg, coinDmg, price):
        self.name = name
        self.dmg = dmg
        self.coinDmg = coinDmg
        self.durability = 100
        self.price = price
    def __str__(self):
        return f"{self.name}, dmg: {self.dmg}, durability: {self.durability}, price: {self.price}"
    
coinDictionary = {
    "DOGE": Coin("Dogecoin", 0.15, 4.0, 10),
    "ADA": Coin("Cardano", 0.45, 3.8, 20),
    "DOT": Coin("Polkadot", 7.20, 6.0, 50),
    "AVAX": Coin("Avalanche", 50.00, 6.7, 200),
    "LTC": Coin("Litecoin", 95.00, 6.2, 500),
    "SOL": Coin("Solana", 140.00, 7.5, 700),
    "XMR": Coin("Monero", 160.00, 7.1, 750),
    "BNB": Coin("Binance Coin", 600.00, 8.2, 1500),
    "ETH": Coin("Ethereum", 3200.00, 8.5, 10000),
    "BTC": Coin("Bitcoin", 67000.00, 9.8, 100000)
}

toolDictionary = {
    "Axe": Tool("Axe", 15, 2, 10.00),
    "Mace": Tool("mace", 10, 4, 50.00),
    "Pickaxe": Tool("Pickaxe", 5, 15, 100.00),
    "Zweihander": Tool("Zweihander", 30, 1, 250.00),
    "GreatAxe": Tool("Great Axe", 50, 4, 500.00),
    "Drill": Tool("Drill", 8, 70, 500.00),
    "SledgeHammer": Tool("Sledge Hammer", 65, 50, 400.00),
    "GreatDrill": Tool("Great Drill", 35, 200, 1000.00)
}
game_map = {
    "town square": {"left": "shop", "right": "mine", "forward": "mayor's house"},
    "shop": {"back": "town square"},
    "mine": {"back": "town square", "forward": "mine"},
    "mayor's house": {"back": "town square"},
    # Add more areas here later
}
coinPouch = {}
toolPouch = {}
itemPouch = {}
def describe_location(dialogue_text, location):
    descriptions = {
        "town square": "You are in the bustling town square.",
        "shop": "You enter the shop. Sherman waves from the counter.",
        "mine": "You descend into the mine. The air is thick with dust.",
        "mayor's house": "You stand before the Mayor's House. It's strangely quiet.",
        # Add more locations here...
    }
    text = descriptions.get(location, f"You arrive at {location}.")
    add_dialogue(dialogue_text, text)
def show_available_directions():
    global current_location
    directions = ", ".join(game_map[current_location].keys())
    add_dialogue(dialogue_text, f"From here you can go: {directions}")
def move(direction):
    global current_location
    if direction in game_map.get(current_location, {}):
        new_location = game_map[current_location][direction]
        current_location = new_location
        describe_location(dialogue_text, new_location)
        if current_location == "town square":
            townSquare()
        elif current_location == "shop":
            shop()
        elif current_location == "mayor's house":
            pass
        elif current_location == "mine":
            pass
        show_available_directions()
    else:
        add_dialogue(dialogue_text, f"You can't go {direction} from {current_location}.")
def buy_tool(tool_name, player):
    global current_location
    if current_location == "shop":
        tool = toolDictionary.get(tool_name)
        if not tool:
            add_dialogue(dialogue_text, "That tool is not available.")
            return
        if player.money >= tool.price:
            player.money -= tool.price
            player.inventory.toolPouch[tool.name] = tool
            add_dialogue(dialogue_text, f"You bought a {tool.name} for {tool.price} coins.")
        else:
            add_dialogue(dialogue_text, "You don't have enough money.")
    else:
        add_dialogue("You are not in the shop")
def add_dialogue(dialogue_text, text):
    dialogue_text.config(state='normal')  
    dialogue_text.insert(tk.END, text + "\n")
    dialogue_text.see(tk.END)  
    dialogue_text.config(state='disabled')  
def loadData():
    with open("PlayerStats.txt", "r") as file:
        line = file.readline()
        if line:
            parts = line.strip().split(", ")
            if len(parts) == 4:
                name, hp, money = parts
    with open("PlayerInventory.dat", "rb"):
        try:
            with open(filename, "rb") as f:
                inventory = pickle.load(f)
            print("Inventory loaded.")
            return Player(name, hp, money, inventory)
        except FileNotFoundError:
            print("No saved inventory found.")
            return Inventory({}, {})
    print("Data Loaded")
    
def saveData(player):
    with open("PlayerStats.txt", 'w') as file:
        file.write(f"{player.name}, {player.hp}, {player.money}")
    with open("PlayerInventory.dat", 'wb') as file:
        pickle.dump(player.inventory, file)
    print("Data Saved.")
    
def gameStart():
    while(True):
        choice = input("(1)new game, (2)load saved game")
        if choice == "1":
            name = input("What is your name?")
            inventory = Inventory(coinPouch, toolPouch)
            player = Player(name, 50, 50, inventory, Tool("stick", 1, 1, 0))
            player.inventory.toolPouch["stick"] = player.equippedTool
            return player
        elif choice == "2":
            player = loadData()
            return player
        else:
            print("invalid choice, try again")
            
def townSquare():
    add_dialogue(dialogue_text, "You see a sign pointing left(shop), right(mine), and forwards(Mayors House)")
    add_dialogue(dialogue_text, "where do you go?")
def shop():
    add_dialogue(dialogue_text, "Welcome to my shop! I am sherman, the ShopKeeper.")
    add_dialogue(dialogue_text, "These are my wares")
    for tool, cost in toolDictionary.items():
        add_dialogue(dialogue_text, f"{tool}: {cost} CryptCoins")
def guiSetup(player):
    global dialogue_text

    root = tk.Tk()
    root.title("Game Interface")
    root.geometry("900x400")
    
    global current_location
    
        # --- Dialogue Pane ---
    dialogue_frame = ttk.Frame(root, padding=10, borderwidth=2, relief="sunken")
    dialogue_frame.grid(row=0, column=2, sticky="nsew")
    
    dialogue_text = tk.Text(dialogue_frame, height=10, wrap="word")
    dialogue_text.pack(fill=tk.BOTH, expand=True)
    with open("CryptCoin.txt", "r") as file:
        for line in file:
            dialogue_text.insert(tk.END, line)
        dialogue_text.see(tk.END)
    dialogue_text.config(state='disabled')
    current_location = "town square"
    describe_location(dialogue_text, current_location)
    townSquare()
    show_available_directions()
    
    # Use a grid layout
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=2)
    root.columnconfigure(2, weight=2)

    # --- Controls Pane ---
    control_frame = ttk.Frame(root, padding=10, borderwidth=2, relief="sunken")
    control_frame.grid(row=0, column=0, sticky="nsew")
    ttk.Label(control_frame, text="Controls", font=("Arial", 14)).pack(pady=5)
    ttk.Button(control_frame, text="← Left", command=lambda: move("left")).pack(fill='x', pady=2)
    ttk.Button(control_frame, text="→ Right", command=lambda: move("right")).pack(fill='x', pady=2)
    ttk.Button(control_frame, text="↑ Forward", command=lambda: move("forward")).pack(fill='x', pady=2)
    ttk.Button(control_frame, text="↓ Back", command=lambda: move("back")).pack(fill='x', pady=2)
    ttk.Button(control_frame, text="Attack").pack(fill='x', pady=2)
    ttk.Button(control_frame, text="Mine").pack(fill='x', pady=2)
    ttk.Label(control_frame, text="Buy Tool:").pack(pady=2)
    buy_entry = ttk.Entry(control_frame)
    buy_entry.pack(fill='x', pady=2)
    ttk.Button(control_frame, text="Buy", command=lambda: buy_tool(buy_entry.get(), player)).pack(fill='x', pady=2)

    # --- Inventory Pane ---
    inventory_frame = ttk.Frame(root, padding=10, borderwidth=2, relief="sunken")
    inventory_frame.grid(row=0, column=1, sticky="nsew")

    ttk.Label(inventory_frame, text="Inventory", font=("Arial", 14)).pack(pady=5)
    equipped_tool_var = tk.StringVar(value=f"Equipped Tool: {player.equippedTool.name}")
    ttk.Label(inventory_frame, textvariable=equipped_tool_var, font=("Arial", 10, "italic")).pack(pady=5)
    inventory_list = tk.Listbox(inventory_frame)
    inventory_list.pack(fill=tk.BOTH, expand=True)

    # Add coins to inventory list
    inventory_list.insert(tk.END, "--- Coins ---")
    coin_indices = {}
    index = inventory_list.size()
    for key, coin in player.inventory.coinPouch.items():
        display = f"{coin.name} (HP: {coin.hp})"
        inventory_list.insert(tk.END, display)
        coin_indices[index] = key
        index += 1

    # Add tools to inventory list
    inventory_list.insert(tk.END, "--- Tools ---")
    for key, tool in player.inventory.toolPouch.items():
        inventory_list.insert(tk.END, str(tool))

    tool_indices = {}
    for key, tool in player.inventory.toolPouch.items():
        inventory_list.insert(tk.END, str(tool))
        tool_indices[inventory_list.size() - 1] = key 
    def on_item_click(event):
        selected = inventory_list.curselection()
        if not selected:
            return
        index = selected[0]

        # Handle coin selling
        if index in coin_indices:
            coin_key = coin_indices[index]
            coin = player.inventory.coinPouch.pop(coin_key)
            player.money += coin.price
            add_dialogue(dialogue_text, f"You sold {coin.name} for {coin.price} coins.")
            inventory_list.delete(index)
            return

        # Handle tool equipping
        if index in tool_indices:
            tool_key = tool_indices[index]
            new_tool = player.inventory.toolPouch[tool_key]
            player.equippedTool = new_tool
            equipped_tool_var.set(f"Equipped Tool: {new_tool.name}")
            add_dialogue(dialogue_text, f"You equipped {new_tool.name}.")

    inventory_list.bind('<<ListboxSelect>>', on_item_click)

    ttk.Label(dialogue_frame, text="Dialogue", font=("Arial", 14)).pack(pady=5)


    root.mainloop()
    
player = gameStart()
guiSetup(player)







    

import discord
from discord.ext import commands
import asyncio
import pymongo
from pymongo import MongoClient
import random
import arrays
cluster = MongoClient("mongodb+srv://steven:j7257197@cluster0.gjjwq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster.get_database('Data')
records = db.Profiles
items = db.Items

##### MongoDB Database Manipulation Functions #####
def dbAdd(UID, CHARA, PITY):
    if records.count_documents({"_id":UID}) == 0:
        dataDict = {"_id" : UID, "Pulls":[(CHARA, PITY)]}
        records.insert_one(dataDict)
    else:
        records.update_one({"_id":UID}, {"$push": {"Pulls" : (CHARA, PITY)}})

def dbDelete(UID, CHARA, PITY):
    length = 0
    profile = records.find_one({"_id":UID}, {"Pulls": 1})
    data = profile["Pulls"]
    length = len(data)

    for item in data:
        if item == [CHARA, PITY]:
            data.remove(item)
            break

    if len(data) != length:
        post = {"Pulls" : profile["Pulls"]}
        records.update_one({"_id":UID}, {"$set": post})
        return 1
    else:
        return 0
##################################################



############## Discord Bot Commands ##############

### Initialization ###
client = commands.Bot(command_prefix = '!', case_Insenitive = True)
@client.event
async def on_ready():
    print('Bot is ready.')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

### Improper Function Call Handler ###
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("ERROR: Command does not exist or was called incorrectly.")

### User Inventory Output ###
@client.command(pass_context=True)
async def inventory(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.message.author
        UID = ctx.message.author.id
    else:
        UID = member.id

    profile = records.find_one({"_id":UID}, {"Pulls": 1})
    data = profile["Pulls"]
    temp = ''
    
    if profile == None:
        message = "Called inventory is empty."
        await ctx.send(message)
        return
    
    for item in data:
        temp = temp + "-" + item[0] + " " + item[1] + '\n'

    if (len(profile["Pulls"]) != 0):
        await ctx.send(temp)
    else:
        message = "Called inventory is empty."
        await ctx.send(message)

### User Inventory Item Append Function ###
@client.command(pass_context=True)
async def add(ctx, *args):
    if args == ():
        await ctx.send("Proper command syntax: !remove [Character/Item] [Pity Counter]")
        return

    item = ""
    for arg in args:
        if arg != args[-1]:
            item = item + " " + arg
    item = item[1:]
    pity = args[-1]
    uid = ctx.message.author.id
    
    existsQuery = []
    itemsList = []
    for document in items.find():
        existsQuery.append(document)
    for thing in existsQuery:
        itemsList.append(thing["_id"])
    
    if (item in itemsList):
        if (pity.isnumeric() == True) and (int(pity) <= 90) and (int(pity) >= 1):
            dbAdd(uid, item, pity)
            await ctx.send("You added " + item + '.')
        else:
            await ctx.send("Invalid pity value provided.")
    else:
        await ctx.send("Character/Item provided was not found in database.")

### Improper Add Function Call Handler ###
@add.error
async def add_error_handler(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Proper command syntax: !add [Character/Item] [Pity Counter]")

### User Inventory Item Remove Function ###
@client.command(pass_context=True)
async def remove(ctx, *args):
    if args == ():
        await ctx.send("Proper command syntax: !remove [Character/Item] [Pity Counter]")
        return

    item = ""
    for arg in args:
        if arg != args[-1]:
            item = item + " " + arg
    item = item[1:]
    pity = args[-1]
    uid = ctx.message.author.id

    existsQuery = []
    itemsList = []
    for document in items.find():
        existsQuery.append(document)
    for thing in existsQuery:
        itemsList.append(thing["_id"])
    
    if (item in itemsList):
        if (pity.isnumeric() == True) and (int(pity) <= 90) and (int(pity) >= 1):
            if (dbDelete(uid, item, pity) == 1):
                await ctx.send("You removed " + item + '.')
            else:
                await ctx.send("The item you attempted to remove could not be found.")
        else:
            await ctx.send("Invalid pity value provided.")
    else:
        await ctx.send("Character/Item provided was not found in database.")

### Improper Remove Function Call Handler ###
@remove.error
async def remove_error_handler(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Proper command syntax: !remove/add [Character/Item] [Pity Counter]")

### User Inventory Clear Function ###
@client.command(pass_context=True)
async def removeall(ctx):
    post = {"Pulls" : []}
    records.update_one({"_id":ctx.message.author.id}, {"$set": post})
    await ctx.send("Your inventory has been cleared.")

### Zhongli Shield Health Calculation ###
@client.command(pass_context=True)
async def zhonglishield(ctx, *, message=None):
    if message == None:
        await ctx.send("Proper command syntax: !zhonglishield [Max HP] [Talent Lvl]")
    message = message.split(' ')

    if (len(message) == 2) and (message[0].isnumeric() == True) and (message[1].isnumeric() == True) and (int(message[1]) <= 15 and int(message[1]) >= 1):
        health = int(message[0])
        lvl = int(message[1])
        baseShield = ((health*arrays.zsDict[lvl][1])*1.5)+arrays.zsDict[lvl][0]
        out = 'Your base shield health is: '+str(round(baseShield))+'\n\n' + '--For each hit taken by Jade Shield up to 5 hits, Jade Shield will gain an additional 5% health.' + '\n--The DEF stat of the shielded character is taken into account when calculating the damage taken by Jade Shield.'
        await ctx.send(out)
    else:
        await ctx.send("Proper command syntax: !zhonglishield [Max HP] [Talent Lvl]")

### Diona Shield Health Calculation ###
@client.command(pass_context=True)
async def dionashield(ctx, *, message=None):
    leo = 277348457533145088
    line = random.randint(1, 15)
    await ctx.send(arrays.dionaLines[line] +"\nhttps://imgur.com/FspFoCY")
    if message == None:
        await ctx.send("Proper command syntax: !dionashield [Max HP] [Talent Lvl]")
    message = message.split(' ')

    if (len(message) == 2) and (message[0].isnumeric() == True) and (message[1].isnumeric() == True) and (int(message[1]) <= 15 and int(message[1]) >= 1):
        health = int(message[0])
        lvl = int(message[1])
        baseShield = (health*arrays.dsDict[lvl][1])
        holdShield = baseShield*1.75
        basec2Shield = baseShield*1.15
        baseholdShield = holdShield*1.15
        out = 'Your base shield health is: '+str(round(baseShield)) +"(tap) "+ str(round(holdShield)) + "(hold)"+ "\nAt constellation 2: "+ str(round(basec2Shield)) +"(tap) "+str(round(baseholdShield)) +"(hold)"+"\n\n-At constellation 2, Diona's shield gains a 15% DMG absorption increase.\n-Diona's shield is 250% effective against Cryo damage."
        await ctx.send(out)
    else:
        await ctx.send("Proper command syntax: !zhonglishield [Max HP] [Talent Lvl]")

### User Gacha Stats Output ###
@client.command(pass_context=True)
async def stats(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.message.author
        UID = ctx.message.author.id
    else:
        UID = member.id
    profile = records.find_one({"_id":UID}, {"Pulls": 1})
    data = profile["Pulls"]
    
    if profile == None:
        message = "User does not exist."
        await ctx.send(message)
        return

    totalpulls = 0
    count = len(data)
    i = 0
    for item in data:
        totalpulls += int(item[1])
        i += 1

    average = round(totalpulls/count, 2)
    header = "PULL STATS\n"
    trolls = "Total rolls: " + str(totalpulls) + "\n"
    itemcount = "Items: " + str(count) + "\n"
    averg = "Average rolls per 5-star pull: " + str(average) + "\n\n"
    diff = round(average - 63)
    luck = abs(diff)

    message = header + trolls + itemcount + averg
    if ((diff <= 1) and (diff >= 1)):
        message = message + "You have about average luck. Not bad.\n"
        if (diff > 0):
            message = message + "That's " + str(luck) + " roll(s) worse than the average of 63.\n"
        elif (diff < 0):
            message = message + "That's " + str(luck) + " roll(s) better than the average of 63.\n"
        elif (diff == 0):
            message = message + "That's exactly at the average of 63.\n"

    elif (diff > 0.5):
        message = message + "You have pretty bad luck. RIP :(\n"
        message = message + "That's " + str(luck) + " roll(s) worse than the average of 63.\n"
    
    elif (diff < 0.5):
        message = message + "You have pretty good luck.\n"
        message = message + "That's " + str(luck) + " roll(s) better than the average of 63.\n"
    await ctx.send(message)

### Add Item To Catalog Command ###
@client.command(pass_context=True)
async def newitem(ctx, *args):
    types = ["char", "weap", "stdchar", "stdweap"]
    if args[0] not in types:
        await ctx.send("Please provide one of the following valid types: char, weap, stdchar, stdweap")
        return    
    if len(args) < 2:
        await ctx.send("Improper command syntax: Too few arguments\nProper command syntax: !newitem [type] [item name]")
        return 

    _type = args[0]
    item = args[1]
    for i in args:    
        if (i != args[0]) and (i != args[1]):
            item = item + " " + i
    await ctx.send("Attempted to add new item to catalog: " + item)

    if items.count_documents({"_id" : item}) == 0:
        itemDict = {"_id" : item, "type" : _type ,"aliases":[item]}
        items.insert_one(itemDict)
    else:
        message = item + " already exists."
        await ctx.send(message)

### Remove Item From Catalog Command ###
@client.command(pass_context=True)
async def removeitem(ctx, *args):
    if len(args) == 0:
        await ctx.send("Please provide an item to be removed.")
        return   
    item = args[0]
    for i in args:    
        if i != args[0]:
            item = item + " " + i

    await ctx.send("Attempted to remove item from catalog: " + item)
    query = []
    for document in items.find({"_id" : item}):
        query.append(document)

    if len(query) == 0:
        message = item + " was not found."
        await ctx.send(message)
        return
    items.delete_one({"_id" : item})

### Outputs Catalog ###
@client.command(pass_context=True)
async def catalog(ctx, *args):
    charQuery = []
    weapQuery = []
    stdcharQuery = []
    stdweapQuery = []

    for document in items.find({"type" : "char"}):
        charQuery.append(document)
 
    for document in items.find({"type" : "weap"}):
        weapQuery.append(document)

    for document in items.find({"type" : "stdchar"}):
        stdcharQuery.append(document)
    
    for document in items.find({"type" : "stdweap"}):
        stdweapQuery.append(document)
    
    charMessage = "--Character Banner--\n------------------------------"
    weapMessage = "--Weapons Banner--\n------------------------------"
    stdMessage = "--Standard Banner--\n------------------------------"
    
    for item in charQuery:
        charMessage = charMessage + "\n" + item["_id"]

    for item in weapQuery:
        weapMessage = weapMessage + "\n" + item["_id"]

    for item in stdcharQuery:
        stdMessage = stdMessage + "\n" + item["_id"]
    
    for item in stdweapQuery:
        stdMessage = stdMessage + "\n" + item["_id"]

    
    catalog = charMessage + "\n\n" + weapMessage + "\n\n" + stdMessage
    await ctx.send(catalog)


@client.command(pass_context=True)
async def profile(ctx, member: discord.Member=None):
    if member is None:
        member = ctx.message.author
        UID = ctx.message.author.id
    else:
        UID = member.id

    profile = records.find_one({"_id":UID}, {"Pulls": 1})
    data = profile["Pulls"]
    temp = ''
    
    if profile == None:
        message = "Called inventory is empty."
        await ctx.send(message)
        return

    if (len(profile["Pulls"]) == 0):
        message = "Called inventory is empty."
        await ctx.send(message)
    
    charQuery = []
    weapQuery = []

    for document in items.find({"type" : "char"}):
        charQuery.append(document["_id"])
    for document in items.find({"type" : "weap"}):
        weapQuery.append(document["_id"])
    for document in items.find({"type" : "stdchar"}):
        charQuery.append(document["_id"])
    for document in items.find({"type" : "stdweap"}):
        weapQuery.append(document["_id"])

    profcharDict = {}
    profweapDict = {}
    for item in data:
        if item[0] in charQuery:
            if item[0] in profcharDict:
                if profcharDict[item[0]] == 6:
                    continue
                else:
                    profcharDict[item[0]] += 1
            else:
                profcharDict[item[0]] = 0
        elif item[0] in weapQuery:
            if item[0] in profweapDict:
                if profweapDict[item[0]] == 5:
                    continue
                else:
                    profweapDict[item[0]] += 1
            else:
                profweapDict[item[0]] = 1

    tcharDict = dict(reversed(sorted(profcharDict.items(), key=lambda item: item[1])))
    tweapDict = dict(reversed(sorted(profweapDict.items(), key=lambda item: item[1])))
    header = "-               -Profile-               -\n------------------------------"
    for i in tcharDict.items():
        header = header + "\n" + i[0] + " C" + str(i[1])
    
    for i in tweapDict.items():
        header = header + "\n" + i[0] + " R" + str(i[1])
    await ctx.send(header)
##################################################

################# Meme Functions #################
@client.command(pass_context=True)
async def birth(ctx,  *,message=None):
    if message == None:
        message = ""
    else:
        message = " " + message
    await ctx.send("Happy birthday" + message + "!")

@client.command(pass_context=True)
async def diona(ctx, *, message=None):
    leo = 277348457533145088
    line = random.randint(1, 15)
    await ctx.send("<@" + str(leo) + ">\n" + arrays.dionaLines[line] +"\nhttps://imgur.com/FspFoCY")

@client.command() 
async def bruh(ctx):
    await ctx.send('it really is a bruh moment tho')

@client.command() 
async def sad(ctx):
    await ctx.send('I\'m being oppressed. :(')

@client.command()
async def sl(ctx, *, message=None):
    """
    A simple command that repeats the users input back to them.
    """
    message = "Solo Leveling? Is that anything like Only I Level Up?"
    await ctx.send(message)
    await ctx.message.delete()
##################################################


client.run('ODM3MDgxNjIyODY4MTMxODQw.YInXAw.UXBnGoCqPKspq8ysCR1FmvqkGKk')




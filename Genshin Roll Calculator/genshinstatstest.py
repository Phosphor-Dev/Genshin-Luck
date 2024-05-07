import genshinstats

url = "https://webstatic-sea.mihoyo.com/ys/event/im-service/index.html?im_out=true&sign_type=2&auth_appid=im_ccs&authkey_ver=1&win_direction=portrait&lang=en&device_type=pc&ext=%7b%22loc%22%3a%7b%22x%22%3a2281.572021484375%2c%22y%22%3a221.09266662597657%2c%22z%22%3a-867.79736328125%7d%2c%22platform%22%3a%22WinST%22%7d&game_version=OSRELWin1.5.1_R2866676_S2939826_D2957756&authkey=N0zhl3PmBu3gr7gvXcmyveBsJGtlqMdYNpzikgyJ7HJkRTvgqj3yhsuPfGDoz7o2BPoq2WXRj3Pd65d%2fDjGnDjdiavSMb0bTOaCN7uDXQOOgqQ36P5xKAsFoxvyFnL%2f1eJtNRL5cCYBrP4ukfLzUWckwyLlnnBrMXdL%2fLdbIeGe0z%2bumQoaxZrotLCY%2bVP2xVcLCFJMYGXChaHwAwnXp8DP%2fz1WPFdvAOTxVl2BUcvthvH3u7xGsUagOxUclSvA19ePZGmEBt%2bmiSGjiCpw1FmiIa8UfFftVLtAnzpzBy54ejfsrXEMP3Q80D%2fNmnsz8%2blo%2bPYdY6eSoHirbcX5uwjg3MeafzHguODH%2fHDg1sl5SHB1iOoT2Kw7CmyXmOKvZE%2bY2ZAXifgagerYBtWJ5bPIlzkUnWy4ylXeR7AvuRXLKwv8nbSp2B9cmM5EvnQXbYB%2f2kZkVcRPsBX291JnXGlPb%2bRsMooHkSR7KIr8zS4JXLy2bEbTu1NbA2CbbaBhdsVYgSwU6DBlInv6HSGDrRtnSUnjo2rorTYBJYcQsLsMPgjbHyX9HO3xIuvWYB54p2Wcwvkn1btt5qk39ts%2b78mlvuCv0JtwM0acnQ3om2dajovjeB4MTjsKsgO0vj03BR%2bJ45ZpCmlL54oNYNLuKfStzOU5eWfxwX9rSw0CBBkULn3N9%2bL%2ff1E5QuMFVUhmG%2bmtOAP4nAg80W%2b9eTdvCbp1JCBwR7b4%2bcrbIqJ7D6pAICs2XpKit%2bQiA2a03brw1FHL3wcjVoSvEzfJ6NponyyAQG3NTG69GsOVfSoehm%2f5R5XrzX%2f64Bx4vStGaFJZw7FZI8m2uetuSb4yCiDdE9x4slwMG4kHZCCi%2fqNjFlGCtAX4WLpFoQPHd%2f80hvPeHjU8BrOiVojtJ0Fo2GUs7fGikrnGzxVu3H6ep3KRppDHqEf0CLzyiGbeYdZeE7z%2fwBsPo%2fPnTlSPcT50oqVn2kk27%2ftjqGGNud39UCu%2fVLcQRs%2fikX%2f0RyxAH10JYnz9xSHEHhsVL1u%2fBDrXHBDDgBSyMcrivs%2fDXQTGETvz56LKBHyHsPAP%2f2RHFIJj%2fbn%2b3%2bWuUn6aCaQjQkiQB2cMX1XdV5kQ0iIQSDg3qN5X4Ty9crLhroYvlLOAwA7hWuf98a%2fWWTFDnvy%2fX68s9zRe6MmhMkW4ZUPcmwTTF6PellXulhzBLHqg6CytItX1fdKNz0QY1H2FCngvltHlN7wCwJNb569J3SkO9kpK8sykXqB96CkrT0Be2BZq31E2vQq6H%2bZZjG%2fRFMXTVZ3lbrp3w8Qdr%2bt1T0fRCkAAw%2fVoXuSuGafCH3bLYiVjbSvDMdYiRR2Ffwwr65%2b1TmoAd%2fMe7Aw%3d%3d&game_biz=hk4e_global#/"
#url ="https://webstatic-sea.mihoyo.com/ys/event/im-service/index.html?im_out=true&sign_type=2&auth_appid=im_ccs&authkey_ver=1&win_direction=portrait&lang=en&device_type=pc&ext=%7b%22loc%22%3a%7b%22x%22%3a-660.8899536132813%2c%22y%22%3a219.6246795654297%2c%22z%22%3a231.84445190429688%7d%2c%22platform%22%3a%22WinST%22%7d&game_version=OSRELWin1.5.1_R2775769_S2797188_D2808729&authkey=vUefmW5DvtAfmqsT0VZqlhkmQvHqKxS5VmdI5DIJ%2b11HZoF%2fgR9JKY3dHjQJq0JV46H1zLPN0ArzkmdvbhHfDrCKDQj10ets8w%2fEN6DKKrwW5Dg%2bmzEGLxgvCwe0p%2b%2bPNDkP0VYIfMi7IIVwT6zYqZz8ajJtFOWxUVe7Q4KutzETAY1JAHBCICoEA0nOKTKZ5Ld3IGpGHhaea%2fi84%2fytZ1X9Ua%2fymNOzZot77axus9WWn93uAY6h%2fqzQIeboOhWyQp%2fp3ChvG8grJRJeQIzlDgU80%2f56kFSRjt7mryNwR6NNosIutTDMENeg%2bgyocBaG%2fQUCxg44Bcet1jDgYJl1ioGRyZxSW3iWfR2UKFeBD1Hwv15Ls1zF%2fqqYr3o7vwioF3AnhF24TYt50Nb5WDo2i7j7TtM8l3DJM8LkGWFVJwPuob5P5fPGvGir3b0UA27b2qGbPTnTW%2b%2boigDhAZl0vonq1YT3sMMi%2b4U0iwPPKuX%2fDvnJ75q%2fjobjGGPRK2Xho9HhC%2b62TuyBUCFZPV%2bDb%2fTHPwBuHGdjqGUQBO5R74Bpl0BOJ3UvB%2bbClqWzDAy%2beMijDpSO6r6c5RggLfgN69HYN925jeQ3hdL1akbYnALygrTby6DLPtkZNOBoR5jGPUpLaWac56CZA9BgAxTM%2ba%2fbW9L7ufPkPVHZZJUmUZmhdjhoBFHLxcJg1BaVAbzlzQK1Ztkf9x0HYbRY%2bSFnHagUNXOU4JUjEQDBhN2KfKwq1e5qb0JGw6ZtUATw1Dy4r6SspkNEarUWzWk4ioj3hlYM%2foxlMkJALBukHzTxUmpu5KQVz9YPViEfcFJsVZl%2bhK9nGh2wGnoxs82c5w8lZ07gOaI7TO1dCbq8Oy0JUoiRDBHNBh%2ft3owou%2f9kmemUhfwK6nozMEen3O%2b2J%2bQta8%2fnF7J6lrSfSmPcf7KmoZoMOR%2fdlepn6ZKVqUqLfGfFUmTmylHGZRZU2IJgw1hG9SBpcOa5Z6kmMMz%2bzxtf6q8MPn5GGiX8X%2fQR4yfCFSzMXfT1sYoWLmJW%2bfhAYgb2VB499kKwKvNCzyPOBOSBMih0ciaWLmBG68dozPqC90HJFNGCrkEOLdbHWEamHpgHuXCdwIAOK6Zgz8yN6uqGeZn%2fSJFoKCNPz5nbc0d9QR6REPBgv%2bYLBlVHJS5ldEHvti%2fYiiwG%2bYFAv4Kl%2beJAYtlkazU4DoT39%2fLQLMm%2fVbG36%2bjlvR5g%2b6xM%2f7PZX8y5Dyx5m1Ob8CHUtvg67YCrF0L%2bZoLjRH%2fm5rn9jxz2cS%2bB7abFCm34sXh7%2f5%2bvHbbflrcxFrWUZF8U5xaxuwU0RHsR3Jgj7CmtH7EneWkuwMFYHGDtuMS6rRZbJguWMmsJ6g%3d%3d&game_biz=hk4e_global#/"
#url = "https://webstatic-sea.mihoyo.com/ys/event/im-service/index.html?im_out=true&sign_type=2&auth_appid=im_ccs&authkey_ver=1&win_direction=portrait&lang=en&device_type=pc&ext=%7b%22loc%22%3a%7b%22x%22%3a-660.8899536132813%2c%22y%22%3a219.6246795654297%2c%22z%22%3a231.84445190429688%7d%2c%22platform%22%3a%22WinST%22%7d&game_version=OSRELWin1.5.1_R2775769_S2797188_D2808729&authkey=vUefmW5DvtAfmqsT0VZqlhkmQvHqKxS5VmdI5DIJ%2b11HZoF%2fgR9JKY3dHjQJq0JV46H1zLPN0ArzkmdvbhHfDrCKDQj10ets8w%2fEN6DKKrwW5Dg%2bmzEGLxgvCwe0p%2b%2bPNDkP0VYIfMi7IIVwT6zYqZz8ajJtFOWxUVe7Q4KutzETAY1JAHBCICoEA0nOKTKZ5Ld3IGpGHhaea%2fi84%2fytZ1X9Ua%2fymNOzZot77axus9WWn93uAY6h%2fqzQIeboOhWyQp%2fp3ChvG8grJRJeQIzlDgU80%2f56kFSRjt7mryNwR6NNosIutTDMENeg%2bgyocBaG%2fQUCxg44Bcet1jDgYJl1ioGRyZxSW3iWfR2UKFeBD1Hwv15Ls1zF%2fqqYr3o7vwioF3AnhF24TYt50Nb5WDo2i7j7TtM8l3DJM8LkGWFVJwPuob5P5fPGvGir3b0UA27b2qGbPTnTW%2b%2boigDhAZl0vonq1YT3sMMi%2b4U0iwPPKuX%2fDvnJ75q%2fjobjGGPRK2Xho9HhC%2b62TuyBUCFZPV%2bDb%2fTHPwBuHGdjqGUQBO5R74Bpl0BOJ3UvB%2bbClqWzDAy%2beMijDpSO6r6c5RggLfgN69HYN925jeQ3hdL1akbYnALygrTby6DLPtkZNOBoR5jGPUpLaWac56CZA9BgAxTM%2ba%2fbW9L7ufPkPVHZZJUmUZmhdjhoBFHLxcJg1BaVAbzlzQK1Ztkf9x0HYbRY%2bSFnHagUNXOU4JUjEQDBhN2KfKwq1e5qb0JGw6ZtUATw1Dy4r6SspkNEarUWzWk4ioj3hlYM%2foxlMkJALBukHzTxUmpu5KQVz9YPViEfcFJsVZl%2bhK9nGh2wGnoxs82c5w8lZ07gOaI7TO1dCbq8Oy0JUoiRDBHNBh%2ft3owou%2f9kmemUhfwK6nozMEen3O%2b2J%2bQta8%2fnF7J6lrSfSmPcf7KmoZoMOR%2fdlepn6ZKVqUqLfGfFUmTmylHGZRZU2IJgw1hG9SBpcOa5Z6kmMMz%2bzxtf6q8MPn5GGiX8X%2fQR4yfCFSzMXfT1sYoWLmJW%2bfhAYgb2VB499kKwKvNCzyPOBOSBMih0ciaWLmBG68dozPqC90HJFNGCrkEOLdbHWEamHpgHuXCdwIAOK6Zgz8yN6uqGeZn%2fSJFoKCNPz5nbc0d9QR6REPBgv%2bYLBlVHJS5ldEHvti%2fYiiwG%2bYFAv4Kl%2beJAYtlkazU4DoT39%2fLQLMm%2fVbG36%2bjlvR5g%2b6xM%2f7PZX8y5Dyx5m1Ob8CHUtvg67YCrF0L%2bZoLjRH%2fm5rn9jxz2cS%2bB7abFCm34sXh7%2f5%2bvHbbflrcxFrWUZF8U5xaxuwU0RHsR3Jgj7CmtH7EneWkuwMFYHGDtuMS6rRZbJguWMmsJ6g%3d%3d&game_biz=hk4e_global#/"
authkey = genshinstats.extract_authkey(url)
#print(genshinstats.extract_authkey(url))



fscount = 0
pity = 0
print("CHARACTER")
for i in genshinstats.get_gacha_log(301,None,authkey=authkey):
    #print(f"{i['time']} - {i['name']} ({i['rarity']}* {i['type']})")
    if i['rarity'] == 5:
        fscount += 1
        print(f"{i['time']} - {i['name']} ({i['rarity']}* {i['type']})")
        pity += 1
        print(pity)
        pity = 0
    else:
        pity += 1
print("WEAPONS")
pity = 0
for i in genshinstats.get_gacha_log(302,None,authkey=authkey):
    #print(f"{i['time']} - {i['name']} ({i['rarity']}* {i['type']})")
    if i['rarity'] == 5:
        fscount += 1
        print(f"{i['time']} - {i['name']} ({i['rarity']}* {i['type']})")
        pity += 1
        print(pity)
        pity = 0
    else:
        pity += 1
print("PERMANENT")
pity = 0
for i in genshinstats.get_gacha_log(200,None,authkey=authkey):
    #print(f"{i['time']} - {i['name']} ({i['rarity']}* {i['type']})")
    if i['rarity'] == 5:
        fscount += 1
        print(f"{i['time']} - {i['name']} ({i['rarity']}* {i['type']})")
        pity += 1
        print(pity)
        pity = 0
    else:
        pity += 1
print(fscount, "bruh")
#print(type(genshinstats.get_entire_gacha_log()))

for i in genshinstats.get_gacha_types():
    print(i)
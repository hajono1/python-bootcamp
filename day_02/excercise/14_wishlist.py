#DETAILS
wishlist = [
    {
        "   Name: ": "Guitar",
        "   Info: ": "my favorite musical instrument"
    },
    {
        "   Name: ": "Projector",
        "   Info: ": "Good for watching movies"
    }
]
for order in wishlist:
    print("Item:",)

    for key, value in order.items():
        print(key, value)

import json

with open('wishlist.json', 'w') as file:
    json.dump(wishlist, file, indent=4)


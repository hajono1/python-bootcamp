#
country_codes = {
    "PH": "Philippines",
    "US": "United States",
    "JP": "Japan",
    "IND": "India",
}

country_code = input("Enter country code: ")
print(country_codes.get(country_code, "Unknown"))

for code in country_codes.keys():
    print(code)

for country in country_codes.values():
    print(country)

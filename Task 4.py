def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9
def km_to_mi(km): return km * 0.621371
def mi_to_km(mi): return mi / 0.621371
def kg_to_lb(kg): return kg * 2.20462
def lb_to_kg(lb): return lb / 2.20462

conversions = {
    "1": {"label": "C to F", "func": c_to_f, "from": "°C", "to": "°F"},
    "2": {"label": "F to C", "func": f_to_c, "from": "°F", "to": "°C"},
    "3": {"label": "KM to Miles", "func": km_to_mi, "from": "km", "to": "mi"},
    "4": {"label": "Miles to KM", "func": mi_to_km, "from": "mi", "to": "km"},
    "5": {"label": "KG to LB", "func": kg_to_lb, "from": "kg", "to": "lb"},
    "6": {"label": "LB to KG", "func": lb_to_kg, "from": "lb", "to": "kg"}
}

def main():
    while True:
        print("\nUNIT CONVERTER")
        for key, val in conversions.items():
            print(f"{key}. {val['label']}")
        print("7. Exit")

        choice = input("Select option: ")
        if choice == '7': break
        if choice in conversions:
            try:
                val = float(input(f"Enter value in {conversions[choice]['from']}: "))
                result = conversions[choice]['func'](val)
                print(f"{val:.2f} {conversions[choice]['from']} = {result:.2f} {conversions[choice]['to']}")
            except:
                print("Enter a valid number.")
        else:
            print("Invalid option.")

main()

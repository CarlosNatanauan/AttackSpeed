def compute_attack_speed(base_attack_speed, bonus_attack_speed_percent, level):
    bonus_attack_speed_decimal = bonus_attack_speed_percent / 100
    current_attack_speed = base_attack_speed * (1 + (bonus_attack_speed_decimal * (level - 1)))
    return round(current_attack_speed, 3)
                #Natanauan, Carlos   04 Task Performance 1
def main():
    while True:
        base_attack_speed = float(input("\nEnter the base attack speed: "))
        bonus_attack_speed_percent = float(input("Enter the bonus attack speed %: "))
        level = int(input("Enter the level: "))

        current_attack_speed = compute_attack_speed(base_attack_speed, bonus_attack_speed_percent, level)

        print("\n---------------------------------------------------------------")
        print("        The character's current attack speed is {}.".format(current_attack_speed))
        print("Swift as the wind, attack speed dictates the momentum of combat.")
        print("---------------------------------------------------------------\n")

        repeat = input("Do you want to enter again? (y/n): ").lower()
        if repeat != 'y':
            break

    print("\n-------------------------------------------------")
    print("       THANK YOU FOR USING THIS PROGRAM")
    print("          HOPE YOU'RE HAVING A GOOD DAY")
    print("-------------------------------------------------")

if __name__ == "__main__":
    main()

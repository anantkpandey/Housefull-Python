# aarush_kid_plan.py - Munnabhai helps Aarush & Devika plan kids
print("Aarush & Devika’s Kid Planning - Munnabhai ka Plan!")

# Your data (example - change it, bhai!)
savings = 50000          # Rupees in bank
free_time = 20           # Hours per week free
devika_ready = True      # Devika ka haan ya naa
kids_wanted = 2          # Kitne bacche chahiye

# Decision logic with if-else and logical operators
if savings >= 30000 and free_time >= 15 and devika_ready:
    print("Bacche ka time aa gaya, bhai!")
    print(f"Savings: {savings} Rs, Free Time: {free_time} hrs, Devika says: Haan!")
    if kids_wanted == 1:
        print("Ek kid—chhota *Housefull* shuru!")
    elif kids_wanted == 2:
        print("Do kid—double *dhamaka* in *Housefull*!")
    else:
        print(f"{kids_wanted} kids? Arre, pura *circus* banega!")
elif savings < 30000 and free_time >= 15 and devika_ready:
    print(f"Savings kam hai ({savings} Rs)—thodi aur kamai kar, bhai!")
elif savings >= 30000 and free_time < 15 and devika_ready:
    print(f"Time nahi hai ({free_time} hrs)—kaam se chhutti le, Aarush!")
elif savings >= 30000 and free_time >= 15 and not devika_ready:
    print("Devika taiyaar nahi—usko manao, bhai, phool leke ja!")
else:
    print("Kuch bhi set nahi—savings, time, Devika sab fix karo!")
    print(f"Savings: {savings}, Time: {free_time}, Devika: Naa")

# Munnabhai ka bonus tip
if savings > 100000 or kids_wanted <= 2:
    print("Munnabhai bolta hai: Plan solid hai, bhai—shuru ho ja!")
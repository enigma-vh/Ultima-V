import os.path


def get_offset(character):
    ''' Find the offset of a character
        1. Convert the string into a bytearray
        2. Search for its offset
    '''

    with open(os.path.expanduser('~/DOS/Ultima_5/SAVED.GAM'), "r+b") as input_file: #open the "SAVED.GAM" file from the home directory
        file = input_file.read()
        b = bytearray()
        b.extend(map(ord, character))
        offset = file.index(b)
    input_file.close()
    return offset


def Modify(offset, value, isTwoByte):
    ''' The modification function
        : if: the hexadecimal value is two-byte long
            1. A three-digit hexadecimal value
            2. A two-digit hexadecimal value
            3. A common four-digit hexadecimal value
        : else: the hexadecimal value is one-byte long
    '''

    with open(os.path.expanduser('~/DOS/Ultima_5/SAVED.GAM'), "r+b") as file: #open the "SAVED.GAM" file from the home directory
        file.seek(offset)
        hex_value = hex(value).split('x')[-1]
        if(isTwoByte):
            if(value < 4096 and value > 255):
                file.write(bytearray([int(hex_value[1:3],16)]))
                file.seek(offset+1)
                file.write(bytearray([int(hex_value[0],16)]))
            elif(value < 256):
                file.write(bytearray([int(hex_value[0:2],16)]))
                file.seek(offset+1)
                file.write(bytearray([0]))
            else:
                file.write(bytearray([int(hex_value[2:4],16)]))
                file.seek(offset+1)
                file.write(bytearray([int(hex_value[0:2],16)]))
        else:
            file.write(bytearray([value]))
    file.close()
    return 0


def mod_char(offset):
    ''' Input menu for character modification '''

    Str = int(input("Strength: "))
    Modify(offset+12, Str, False)
    Int = int(input("Intelligence: "))
    Modify(offset+14, Int, False)
    Dex = int(input("Dexterity: "))
    Modify(offset+13, Dex, False)
    HP = int(input("Health points: "))
    Modify(offset+16, HP, True)
    MAX_HP = int(input("Max health points: "))
    Modify(offset+18, MAX_HP, True)
    Exp = int(input("Experience: "))
    Modify(offset+20, Exp, True)


def mod_items():
    ''' Input menu for items and gold modification '''

    offset = 516
    gold = int(input("Gold: "))
    Modify(offset, gold, True)
    keys = int(input("Keys: "))
    Modify(offset+2, keys, False)
    skull = int(input("Skull keys: "))
    Modify(offset+7, skull, False)
    gems = int(input("Gems: "))
    Modify(offset+3, gems, False)
    badge = int(input("Black badge: "))
    Modify(offset+20, badge, False)
    carpets = int(input("Magic carpets: "))
    Modify(offset+6, carpets, False)
    axes = int(input("Magic axes: "))
    Modify(offset+60, axes, False)


def menu():
    print("\n---- CHARACTERS -------------------------------------------------------------------------------------")
    data = [['[1] Main', '[2] Shamino', '[3] Iolo', '[4] Mariah', '[5] Geoffrey', '[6] Jaana'],
            ['[7] Julia', '[8] Dupre', '[9] Katrina', '[10] Sentri', '[11] Gwenno', '[12] Johne'],
            ['[13] Gorn', '[14] Maxwell', '[15] Toshi', '[16] Saduj', '[17] Equipments']]

    col_width = max(len(word) for row in data for word in row) + 2  # padding
    for row in data:
        print("".join(word.ljust(col_width) for word in row))

    print(
        '-----------------------------------------------------------------------------------------------------' + '\n')


def main():
    menu()
    data = ['[1] Main','[2] Shamino', '[3] Iolo', '[4] Mariah', '[5] Geoffrey', '[6] Jaana',
             '[7] Julia','[8] Dupre', '[9] Katrina', '[10] Sentri', '[11] Gwenno', '[12] Johne',
             '[13] Gorn', '[14] Maxwell', '[15] Toshi', '[16] Saduj', '[17] Equipments']

    again = 'Y'
    while(again == 'Y'):
        choice = input("Enter your choice: ")
        a = ''.join([i for i in data[int(choice)-1] if i.isalpha()]) # character's name
        if choice != '17':
            mod_char(get_offset(a))
        elif choice == '17':
            mod_items()
        else:
            print("Invalid input!")
        again = input("Do you want to continue? [Y/N]  ")

    return 0


if __name__ == "__main__":
    main()


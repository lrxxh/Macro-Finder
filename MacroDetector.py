import os

def check_exist_and_print(path, msg):
    if os.path.exists(path):
        os.startfile(path)
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"[{os.path.getctime(file_path)}] {file_path}")
        print(f"\033[32m{msg} found\033[0m")
    else:
        print(f"\033[31m{msg} not found\033[0m")

check_exist_and_print(os.path.join(os.environ['LOCALAPPDATA'], 'Logitech', 'Logitech Gaming Software'), 'Logitech Gaming Software')
check_exist_and_print(os.path.join(os.environ['LOCALAPPDATA'], 'LGHUB'), 'LGHUB')
check_exist_and_print(os.path.join(os.environ['PROGRAMDATA'], 'Razer', 'Synapse', 'Accounts'), 'Razer Synapse')
check_exist_and_print('C:\\ProgramData\\Razer\\Synapse3\\Log', 'Razer Turbo')
check_exist_and_print(os.path.join(os.environ['LOCALAPPDATA'], 'Razer', 'Synapse3', 'Settings'), 'Razer Synapse 3')
check_exist_and_print(os.path.join(os.environ['PROGRAMDATA'], 'Razer', 'Razer Central', 'Accounts'), 'Razer')
check_exist_and_print(os.path.join(os.environ['APPDATA'], 'Corsair', 'Cue'), 'Corsair')
check_exist_and_print(os.path.join(os.environ['LOCALAPPDATA'], 'BY-COMBO2'), 'Glorious')
check_exist_and_print(os.path.join(os.environ['LOCALAPPDATA'], 'JM01'), 'Aukey')
check_exist_and_print('C:\\Program Files (x86)\\Bloody7\\Bloody7\\Data\\Mouse', 'Bloody7')
check_exist_and_print('C:\\Program Files (x86)\\Bloody7\\Bloody7\\UserLog\\Mouse\\TLcir_9EFF3FF4', 'Bloody7 Check 2')
check_exist_and_print(f'C:\\Users\\{os.environ["USERNAME"]}\\AppData\\Roaming\\REDRAGON\\GamingMouse', 'Redragon')
check_exist_and_print(f'C:\\Users\\{os.environ["USERNAME"]}\\Documents\\M711 Gaming Mouse', 'M711 Gaming Mouse')
input("Press Enter to continue...")

import time
import os
import pyautogui
import webbrowser

def open_cmd_and_run_commands():
    # Path to BMIS folder
    bmis_path = os.path.expanduser(r"~\\Desktop\\brgy385-copy")

    # Open first CMD for php artisan serve
    os.system('start cmd')
    time.sleep(1.5)  # Wait for CMD to open
    pyautogui.typewrite(f'cd /d "{bmis_path}"', interval=0.05)
    pyautogui.press('enter')
    pyautogui.typewrite('php artisan serve', interval=0.05)
    pyautogui.press('enter')

    # Open second CMD for npm run dev
    os.system('start cmd')
    time.sleep(1.5)
    pyautogui.typewrite(f'cd /d "{bmis_path}"', interval=0.05)
    pyautogui.press('enter')
    pyautogui.typewrite('npm run dev', interval=0.05)
    pyautogui.press('enter')


def open_xampp_and_start_services():
    # Path to XAMPP Control Panel and service scripts (adjust if installed elsewhere)
    xampp_path = r"D:\\xampp"
    apache_start = os.path.join(xampp_path, "apache_start.bat")
    mysql_start = os.path.join(xampp_path, "mysql_start.bat")
    if not os.path.exists(apache_start):
        print(f"Apache start script not found: {apache_start}")
    else:
        os.system(f'start "" "{apache_start}"')
        time.sleep(2)
    if not os.path.exists(mysql_start):
        print(f"MySQL start script not found: {mysql_start}")
    else:
        os.system(f'start "" "{mysql_start}"')
        time.sleep(2)


if __name__ == "__main__":
    try:
        open_xampp_and_start_services()
        open_cmd_and_run_commands()
        print("BMIS is now running. You can access it at http://localhost:8000")
        print("Press Ctrl+C to stop the servers.")
        # Open the default web browser to localhost:8000
        webbrowser.open('http://localhost:8000')
    except Exception as e:
        print(f"An error occurred: {e}")
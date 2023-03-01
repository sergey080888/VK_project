import screeninfo
import subprocess


class AdaptiveResolution:
    def __init__(self, path_to_settings_file):
        self.path_to_settings_file = path_to_settings_file

    def get_resolution(self):
        # Get the screen resolution of the user's monitor
        screen_info = screeninfo.get_monitors()[0]
        screen_width, screen_height = screen_info.width, screen_info.height
        print(screen_width, screen_height)
        return screen_width, screen_height

    def set_resolution(self):
        # Set the game resolution
        display_resolution = self.get_resolution()
        with open(self.path_to_settings_file) as f:
            lines = f.readlines()
        lines[8] = f'    "setting.defaultres"		"{display_resolution[0]}"\n'
        lines[9] = f'    "setting.defaultresheight"		"{display_resolution[1]}"\n'

        with open(self.path_to_settings_file, "w") as f:
            f.write("".join(lines))
        print("Настройки изменены")

    def run_steam(self):
        print("Запускается Steam")
        subprocess.call(["C:\\Program Files (x86)\\Steam\\steam.exe", "-no-browser"])


if __name__ == "__main__":
    path_to_settings_file = r"C:\Program Files (x86)\Steam\steamapps\common\Underlords\game\dac\cfg\video.txt"
    first = AdaptiveResolution(path_to_settings_file)
    first.set_resolution()
    first.run_steam()

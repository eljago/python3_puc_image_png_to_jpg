from PIL import Image
import os
from pathlib import Path
import pyperclip
import tkinter as tk

homedir = str(Path.home())
originDir = f"{homedir}/Desktop/"
targetDir = f"{homedir}/Documents/puc/Diplomado-Python-Profesional/Curso_2/Modulo_5/imagenes/"

def copy_and_convert_image():
    paths = sorted(Path(originDir).iterdir(), key=os.path.getmtime, reverse=True)

    print(f"looping files at: {originDir} ...")
    for path in paths:

        print(f"\tchecking if {path} is a file ...")
        if path.is_file():
            file_name = os.path.split(path)[-1].split('/')[-1]

            print(f"\tchecking if {file_name} file has .png extension ...")
            if file_name.endswith('.png'):

                images_paths = sorted(Path(targetDir).iterdir(), key=os.path.getmtime, reverse=True)

                print(f"\tLooping files at {targetDir}...")
                for image_path in images_paths:
                    image_file_name = os.path.split(image_path)[1]

                    print(f"\t\tchecking if {image_file_name} has the .jpg extension ...")
                    if image_file_name.endswith('.jpg'):
                        image_split = image_file_name.split('_')
                        new_name = int(image_split[-1].split('.jpg')[0]) + 1
                        image_split[-1] = str(new_name) + '.jpg'
                        new_image_path_name = '_'.join(image_split)
                        
                        new_image_path = os.path.join(targetDir, new_image_path_name)
                        try:
                            print(f"\t\topening image at: {new_image_path} ...")
                            im1 = Image.open(str(path))
                            im1.convert('RGB').save(new_image_path)
                            print("\t\timage converted  to jpg and copied to new location")

                            print(f"\t\tchecking if file exists at: {new_image_path} ...")
                            if os.path.exists(new_image_path):
                                print('\t\tchecking file size ...')
                                if os.path.getsize(new_image_path) == os.path.getsize(image_path):
                                    print('\t\tremoving new image because its the same size ...')
                                    os.remove(new_image_path)
                                    print('\t\timage removed')
                                else:
                                    print('\t\tcopying new image name to the clipboard ...')
                                    pyperclip.copy(f"![Aprendizaje de máquinas](imagenes/{new_image_path_name})")
                            else:
                                print("The file does not exist")
                        except IOError:
                            print("Error: %s does not appear to be a valid image" % str(path))
                        else:
                            pass
                        break
                break
            else:
                print("\tdoesn't end with .png\n")
        else:
            print("it's not a file\n")
    print("")


if __name__ == "__main__":
    root= tk.Tk()
    root.title("Convertir imagen")

    canvas1 = tk.Canvas(root, width = 150, height = 200, bg = 'azure3', relief = 'raised')
    canvas1.pack()

    label1 = tk.Label(root, text='Convertir\nimagen', bg = 'azure3')
    label1.config(font=('helvetica', 20))
    canvas1.create_window(80, 60, window=label1)

    browseButton_PNG = tk.Button(text="Convertir", command=copy_and_convert_image, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(80, 130, window=browseButton_PNG)

    root.mainloop()
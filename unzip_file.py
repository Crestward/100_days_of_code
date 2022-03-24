from zipfile import ZipFile as zip


file = "accounts.zip"

with zip(file, "r") as uzp:
    uzp.printdir()
    print("Extracting......")
    uzp.extractall()
    print("Done!!!")

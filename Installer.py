import os
print('''\033[1;36;40mWireless Payload Installer By S3RPENT
Your Device Must Be Rooted
If Any Question,
Contact Me On Telegram
Tg_User:@officialsakil \n''')
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("cd ..;git clone https://github.com/cfsakil/Wireless_Payload")

os.system("cd ..;chmod +x Wireless_Payload/attack.py")

print("\033[1;34;40mThanks.\nInstallation Done.\nNow Go To Home Directory[~] And Enter This Command :\nsudo python Wireless_Payload/attack.py -i wlan0 -K")

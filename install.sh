mkdir /usr/bin/msfg
echo Directory created
cp msfg.sh /usr/bin/msfg/msfg.sh
echo startup file created
cp msfvenomgenerator.py /usr/bin/msfg/msfg.py
echo script file created
echo "alias msfg='/usr/bin/msfg.sh'" >> ~/.bashrc
chmod +x /usr/bin/msfg.sh
echo Done! Restart your terminal now!
source ~/.bashrc

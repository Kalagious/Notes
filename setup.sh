echo "\033[31;1mAdding Aliases...\033[0m"
echo 'alias notes="~/Notes"' >> $1/.zshrc
echo 'alias colors="python3 ~/Notes/Colors"' >> $1/.zshrc
echo 'alias ttyupgrade="python3 ~/Notes/TTYUpgrade"' >> $1/.zshrc
echo 'alias revshells="python3 ~/Notes/RevShells"' >> $1/.zshrc
echo 'alias commonlinux="python3 ~/Notes/CommonLinux"' >> $1/.zshrc
echo 'alias privesclinux="python3 ~/Notes/PrivescChecklistLinux"' >> $1/.zshrc
echo 'alias enum="python3 ~/Notes/Enumeration"' >> $1/.zshrc

echo -n "alias box='"  >> $1/.zshrc
echo -n 'cd $(find ~/Notes/Boxes/ -name "$BoxName" | head -n 1)' >> $1/.zshrc
echo "'"  >> $1/.zshrc

echo -n "alias web='" >> $1/.zshrc
echo -n 'firefox "$IP"' >> $1/.zshrc
echo "'" >> $1/.zshrc

echo "\033[31;1mAdding NewBox.py to bin...\033[0m"
cp ./NewBox.py /bin
chmod +x /bin/NewBox.py

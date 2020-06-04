import speedtest #pip install speedtest-cli
from urllib import request

def function_for_speedTest():
    '''This whole function is for Speed Test
    with speedtest-cli, command line interface for testing INTERNET bandwidth using https://www.speedtest.net/ '''
    spdtst = speedtest.Speedtest()
    # print(dir(speedtest))
    print("SPEEDTEST Program in Python -- Powered By : speedtest.net by Ookla")
    print("Available Options\n1. Ping\n2. Upload Speed ↑\n3. Download Speed ↓\n4. All of the above + share link")
    userChoice = int(input("Enter your choice here: "))

    if userChoice == 1:
        spdtst.get_best_server()
        print(f"\nPing : {spdtst.results.ping}ms")
        if (spdtst.results.ping) < 50:
            print("Good")
        elif (spdtst.results.ping) < 100:
            print("Good to average")
        elif (spdtst.results.ping) <= 150:
            print("There may be problems with games")
        else:
            print("You may experience lag in games.")
        print(f"\nISP : {spdtst.results.client['isp']} | Client IP : {spdtst.results.client['ip']}")
        print(f"Hosted by : {spdtst.results.server['sponsor']} ({spdtst.results.server['name']}) [{round(spdtst.results.server['d'], 2)} km]")
        print(f"Country : {spdtst.results.server['country']} {spdtst.results.server['cc']}")


    elif userChoice == 2:
        print("\nSelecting best server based on Ping")
        spdtst.get_best_server()
        print("Now, testing your Upload ↑ Speed...")
        bits = spdtst.upload()
        speed_in_mb = bits / 1e+6
        speed_in_MB = bits / 8e+6
        print(f"\nISP : {spdtst.results.client['isp']} | Client IP : {spdtst.results.client['ip']}")
        print(f"Ping : {spdtst.results.ping}ms")
        print(f"Hosted by : {spdtst.results.server['sponsor']} ({spdtst.results.server['name']}) [{round(spdtst.results.server['d'], 2)} km]")
        print(f"Country : {spdtst.results.server['country']} {spdtst.results.server['cc']}")
        print(f"\nUpload Speed ↑ : {round(speed_in_mb, 2)} Mbps ({round(speed_in_MB, 2)} MBps)")
        if (speed_in_mb) < 2:
            print("Very Slow")
        elif (speed_in_mb) < 5:
            print("Slow")
        elif (speed_in_mb) < 7:
            print("Average")
        elif (speed_in_mb) < 10:
            print("Fast")
        else:
            print("Very Fast")




    elif userChoice == 3:
        print("\nSelecting best server based on Ping")
        spdtst.get_best_server()
        print("Now, testing your Download ↓ Speed...")
        bits = spdtst.download()
        speed_in_mb = bits / 1e+6
        speed_in_MB = bits / 8e+6
        print(f"\nISP : {spdtst.results.client['isp']} | Client IP : {spdtst.results.client['ip']}")
        print(f"Ping : {spdtst.results.ping}ms")
        print(f"Hosted by : {spdtst.results.server['sponsor']} ({spdtst.results.server['name']}) [{round(spdtst.results.server['d'], 2)} km]")
        print(f"Country : {spdtst.results.server['country']} {spdtst.results.server['cc']}")
        print(f"\nDownload Speed ↓ : {round(speed_in_mb, 2)} Mbps ({round(speed_in_MB, 2)} MBps)")
        if (speed_in_mb) < 3:
            print("Very Slow")
        elif (speed_in_mb) < 5:
            print("Slow")
        elif (speed_in_mb) < 10:
            print("Average")
        elif (speed_in_mb) < 15:
            print("Fast")
        else:
            print("Very Fast")

    elif userChoice == 4:
        print("\nSelecting best server based on Ping")
        spdtst.get_best_server()
        print("Now testing your Download Speed ↓ ...")
        bitsDownload = spdtst.download()
        speed_in_mbDownload = bitsDownload / 1e+6
        speed_in_MBDownload = bitsDownload / 8e+6
        print("\nNow testing your Upload Speed ↑ ...")
        bitsUpload = spdtst.upload()
        speed_in_mbUpload = bitsUpload / 1e+6
        speed_in_MBUpload = bitsUpload / 8e+6
        data = f"\nISP : {spdtst.results.client['isp']} | Client IP : {spdtst.results.client['ip']}\nPing : {spdtst.results.ping}ms\nHosted by : {spdtst.results.server['sponsor']} ({spdtst.results.server['name']}) [{round(spdtst.results.server['d'], 2)} km]\nCountry : {spdtst.results.server['country']} {spdtst.results.server['cc']}"
        data_download = f"\nDownload Speed ↓ : {round(speed_in_mbDownload, 2)} Mbps ({round(speed_in_MBDownload, 2)} MBps)"
        data_upload = f"\nUpload Speed ↑ : {round(speed_in_mbUpload, 2)} Mbps ({round(speed_in_MBUpload, 2)} MBps)"
        print(data)
        print(data_download)    # --- printing the f strings defined above here
        print(data_upload)
        print("\nShare Results : ", spdtst.results.share()) #This will print the link for .png image
        request.urlretrieve(spdtst.results.share(), "C:\\Users\\uday_\\Desktop\\results.jpg") #for saving results image to desktop NOTE : Path will be different in Linux OS for windows change the user's name


    else:
        print("Please enter a valid choice")
        function_for_speedTest()

    # Asking that whether the user wants to run the program again
    restart = input("\nDo you want to test your speed again (y/n): ")
    if restart == 'y' or restart == 'Y':
        function_for_speedTest()
    else:
        exit()

# main


if __name__ == '__main__':
    function_for_speedTest()







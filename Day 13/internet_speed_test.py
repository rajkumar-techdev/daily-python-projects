import speedtest


def test_speed():
    st=speedtest.Speedtest()
    print("Testing....... Please Wait")

    download_speed=st.download()/1_000_000  #convert to mbps
    upload_speed=st.upload()/1_000_000

    print(f"\n Download Speed{download_speed:.2f} Mbps")
    print(f"\n Upload Speed {upload_speed:.2f} Mbps")


test_speed()
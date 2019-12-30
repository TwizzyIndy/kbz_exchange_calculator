import requests
import os
from lxml import etree


def sell_usd_to_mmk(input_usd):
    # Request
    # POST https://ibanking.kbzbank.com/B001/internet

    try:
        response = requests.post(
            url="https://ibanking.kbzbank.com/B001/internet",
            headers={
                "Accept": "*/*",
                "Cookie": "JSESSIONID=iAtVHbpLW9vRFwpWgnpG0IlkYQTR4RrhhJ4mZMxEAruiyqok-Wfl!-1764904943; f5avr2111618761bbbbbbbbbbbbbbbb=DPJIMBJHNINMIDHJIJOIMCOHNDFPCEANOFMMEIHJNAGDGMJCOMACCIBLFAGANPFPGAPAGONGIBEAELJDCIOCJEPLAFODJOAIAFPFNHOGHOMNKGJJLBKNJMIAMKDJKJCJ; TS014f6f18=017da16cfc2d5270cc5af6b3c5e47abc8ab1ea0be5afde4143de62d3c6dd7293201bdecbe32979281fdd0050af816b21e5cf4fddd4; TS01c9898a=017da16cfc33044b8d7ca00970e8afaa9ebc75b01b1029b9d4421bd76e4d66dcbbeab738742c672110833505dfee853951731762af",
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "iPhone",
                "Accept-Language": "en-US",
                "fldDeviceId": "43",
                "flduseragent": "iPhone",
            },
            data={
                "fldbuycurr_txt": "MMK-Myanmar Kyats",
                "fldJSessionId": "",
                "fldsellcurr_ix": "3",
                "fldRequestId": "RRFEC62",
                "fldLangId": "eng",
                "fldSessionId": "",
                "fldamttxt": input_usd,
                "fldDeviceId": "43",
                "fldsellcurr_txt": "USD-US Dollar",
                "flduseragent": "iPhone",
                "fldpurpose_ix": "2",
                "fldpurpose_txt": "International Account Transfer",
                "fldbuycurr_ix": "1",
                "fldsellcurr": "USD",
                "fldEntityId": "B001",
                "fldtxnheading": "CALCULATOR",
                "fldbuycurr": "MMK",
                "fldfecflow": "FEC",
                "fldpurpose": "IBFTOUT",
                "fldIsBioLogin": "N",
            },
        )

        if response.status_code is not 200:
            print("response error}")

        xmlroot = etree.fromstring(response.content)
        lblRoot = xmlroot.xpath('/F/T/NT/L')
        lblMMK = lblRoot[3].attrib['v']
        # lblUpdateTime = lblRoot[4].attrib['v']

        print("Sell : ")
        print(lblMMK.split('=')[1].strip())

        # print(lblUpdateTime)

    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def buy_usd_to_mmk(input_usd):
    # buy
    # POST https://ibanking.kbzbank.com/B001/internet

    try:
        response = requests.post(
            url="https://ibanking.kbzbank.com/B001/internet",
            headers={
                "Accept": "*/*",
                "Cookie": "f5avr2111618761bbbbbbbbbbbbbbbb=IOIBEELNBCECCDBLEPJNPFCOEKHAEMABJJLHNLIFKPGDIOMCMOMEJJNMDFMAPDGHFDNJALKACIAELBAFAKLDKHFEIMCMICOFLLMIGENEDJELHBJLAKJKEHGFNKOMOFML; JSESSIONID=hU1VqvVLkKWDrE8RczP0o2C20xzCoYp9cebxyQsanGIucJrhhSZV!1922154947; TS014f6f18=017da16cfc3d00b51a5e8fda2b1efc4fbe66d4a99eafde4143de62d3c6dd7293201bdecbe3dd8fe082dda45af1fe2cd213a1bab7df; TS01c9898a=017da16cfcdc7153fced0269b439c6562d6fd42d4524303dd516e01cb1f13961e860b663e5fc4086759d8a61a9655e585d48ae2d09",
                "Connection": "keep-alive",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "iPhone",
                "Accept-Language": "en-US",
                "fldDeviceId": "43",
                "flduseragent": "iPhone",
            },
            data={
                "fldbuycurr_txt": "MMK-Myanmar Kyats",
                "fldJSessionId": "",
                "fldsellcurr_ix": "3",
                "fldRequestId": "RRFEC62",
                "fldLangId": "eng",
                "fldSessionId": "",
                "fldamttxt": input_usd,
                "fldDeviceId": "43",
                "fldsellcurr_txt": "USD-US Dollar",
                "flduseragent": "iPhone",
                "fldpurpose_ix": "1",
                "fldpurpose_txt": "Buy Foreign currency notes",
                "fldbuycurr_ix": "1",
                "fldsellcurr": "USD",
                "fldEntityId": "B001",
                "fldtxnheading": "CALCULATOR",
                "fldpurpose": "IBCASH",
                "fldbuycurr": "MMK",
                "fldfecflow": "FEC",
                "fldIsBioLogin": "N",
            },
        )
        if response.status_code is not 200:
            print("response error}")

        xmlroot = etree.fromstring(response.content)
        lblRoot = xmlroot.xpath('/F/T/NT/L')
        lblMMK = lblRoot[3].attrib['v']
        lblUpdateTime = lblRoot[4].attrib['v']

        print("Buy : ")
        print(lblMMK.split('=')[1].strip())
        print("")

        print(lblUpdateTime)
        print("")
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


def usage():
    print("")
    print("KBZ Foreign Exchange Calulator")
    print("by TwizzyIndy")
    print("12/2019")
    print("")
    print("(just used internal api. im not owner of any properties related to KBZ Company Ltd.,)")
    print("")
    print("usage:")
    print("python3 kbz_exchange_calulator.py {USD}")
    print("")
    print("")


def main():
    if len(os.sys.argv) < 2:
        usage()
        return

    sell_usd_to_mmk(os.sys.argv[1])
    buy_usd_to_mmk(os.sys.argv[1])


if __name__ == "__main__":
    main()

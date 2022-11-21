import time
from qiniu.services.qvs.camera import Camera

if __name__ == '__main__':
    access_key = 'pGWOH5rkQFmvfIO1PxSLkTphLAyHtcbC-y8W5bbL'
    secret_key = 'Eku1QAiJTrVRjrTkwcqEvUXNKRGAIt0ednYHq-1O'
    # 空间ID
    namespaceId = "jiji"

    gbId_lst = [31011500991320019173, 31011500991320018717, 31011500991320018716, 31011500991320018715,
                31011500991320018675, 31011500991320018674, 31011500991320018673, 31011500991320018672,
                31011500991320018148, 31011500991320016433]

    while True:
        current_hour = time.localtime().tm_hour
        current_min = time.localtime().tm_min

        if (current_hour == 8 or current_hour == 10 or current_hour == 13 or current_hour == 14 or current_hour == 15
            or current_hour == 16 or current_hour == 18) and (10 < current_min < 25 or 30 < current_min < 45):
            for gbId in gbId_lst:
                camera = Camera(access_key, secret_key, namespaceId, gbId, gbId)
                print("%s - %s" % (gbId, camera.info()['state']))
                if camera.info()['state'] == "online":
                    camera.record()
        time.sleep(60 * 12)

    # camera.listRecords()

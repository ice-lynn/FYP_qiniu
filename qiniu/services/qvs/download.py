# -*- coding: utf-8 -*-
# flake8: noqa
import json
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from qiniu import Auth, QiniuMacAuth, http


# 获取截图列表
def listSnapshots(access_key, secret_key, namespaceId, streamId, line, marker, start, end):
    '''
        参数名称	必填	字段类型	说明
        type	是	integer	1:实时截图对应的图片列表 2: 按需截图对应的图片列表 3:覆盖式截图对应的图片
        line	否	integer	限定返回截图的个数，只能输入1-100的整数，不指定默认返回30个，type为3可忽略
        marker	否	string	上一次查询返回的标记，用于提示服务端从上一次查到的位置继续查询，不指定表示从头查询，type为3可忽略
        start	否	integer	查询开始时间(unix时间戳,单位为秒)，type为3可忽略
        end	    否	integer	查询结束时间(unix时间戳,单位秒)，type为3可忽略
    '''
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    # url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/snapshots?type=2&start={start}&end={end}&marker={marker}&line={line}"
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/snapshots?type=2&line={line}&start={start}&end={end}"

    # 发起GET请求
    result, res = http._get_with_qiniu_mac(url, params=None, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
    # 格式化响应体
    # Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    # result = json.dumps(ret, indent=4, ensure_ascii=False)
    return res.status_code, json.loads(res.text_body)


# 获取截图列表
def listRecords(access_key, secret_key, namespaceId, streamId, line, marker, start, end):
    '''
        参数名称	必填	字段类型	说明
        line	否	integer	一次返回多少条, 最大值为100; 当超过100时，需要通过上面的marker循环读取，直到取出全部记录
        marker	否	string	上一次查询返回的标记，用于提示服务端从上一次查到的位置继续查询，不指定表示从头查询，type为3可忽略
        start	否	integer	查询开始时间(unix时间戳,单位为秒)，type为3可忽略
        end	    否	integer	查询结束时间(unix时间戳,单位秒)，type为3可忽略
        format  否   string  录制视频格式
    '''
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    # url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/recordhistories?line={line}&start={start}&end={end}"
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/recordhistories?line={line}&format=mp4"

    # 发起POST请求
    result, res = http._get_with_qiniu_mac(url, params=None, auth=auth)
    items = json.loads(res.text_body)['items']
    return res.status_code, items


def download_snapshots(access_key, secret_key, base_url, filepath):
    q = Auth(access_key, secret_key)
    # 有两种方式构造base_url的形式
    # base_url = 'http://%s/%s' % ("rfpxt0t4s.hd-bkt.clouddn.com", "")
    # 或者直接输入url的方式下载
    # base_url = 'http://domain/key'
    # 可以设置token过期时间
    private_url = q.private_download_url(base_url, expires=3600)
    urllib.request.urlretrieve(private_url, filepath)
    print("下载成功：" + filepath[filepath.rfind('\\')+1:])
    # r = requests.get(private_url)


# if __name__ == '__main__':
#     pool = ThreadPoolExecutor()
#
#     # 七牛账号 AK、SK
#     access_key = 'pGWOH5rkQFmvfIO1PxSLkTphLAyHtcbC-y8W5bbL'
#     secret_key = 'Eku1QAiJTrVRjrTkwcqEvUXNKRGAIt0ednYHq-1O'
#     # 空间ID
#     namespaceId = "jiji"
#     # # 流ID
#     # streamId = "31011500991320014931"
#     # # 设备国标Id
#     # gbId = "31011500991320014931"
#
#     # 流ID
#     streamId = "31011500991320015266"
#     # 设备国标Id
#     gbId = "31011500991320015266"
#
#     # 获取截图列表
#     code, res = listSnapshots(access_key, secret_key, namespaceId, streamId,
#                                     10, None, (int)(time.time() - 12 * 3600), (int)(time.time()))
#     print(f'{res}')
#     print(res.get("marker"))
#     if code == 200:
#         print("【截图列表获取成功】")
#         for image in res.get("items"):
#             filename = time.strftime("20%y%m%d%H%M%S", time.localtime(image.get("time"))) + ".jpg"
#             pool.submit(download_snapshots, access_key, secret_key, image.get("snap"), filename)

from qiniu import QiniuMacAuth, http
import json

# 查询设备信息
def listNamespacesInfo(access_key, secret_key, namespaceId, gbId):
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/devices/{gbId}"
    # 发起POST请求
    ret, res = http._get_with_qiniu_mac(url, params=None, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


#  启用流
def enableStreams(access_key, secret_key, namespaceId, streamId):
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/enabled"
    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, None, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 禁用流
def stopStreams(access_key, secret_key, namespaceId, streamId):
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/stop"
    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, None, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 启动设备拉流
def startDevice(access_key, secret_key, namespaceId, gbId):
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/devices/{gbId}/start"
    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, None, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 停止设备拉流
def stopDevice(access_key, secret_key, namespaceId, gbId):
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/devices/{gbId}/stop"
    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, None, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 启动设备按需录制（启动设备拉流 + 开始录像）
def startRecord(access_key, secret_key, namespaceId, streamId):
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/record/start"
    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, None, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 停止设备按需录制
def stopRecord(access_key, secret_key, namespaceId, streamId):
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/record/stop"
    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, None, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 按需截图
def takeScreenshot(access_key, secret_key, namespaceId, streamId):
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/streams/{streamId}/snap"
    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, None, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 变焦控制 - 清晰度
def controlZooming(access_key, secret_key, namespaceId, gbId, body):
    '''

    Args:
        body: {
                cmd：focusnear(焦距变近), focusfar(焦距变远),stop(停止)，
                speed：调节速度(1~10, 默认位5)
            }
    '''
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/devices/{gbId}/focus"
    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, body, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 光圈控制 - 亮度
def controlDiaphragm(access_key, secret_key, namespaceId, gbId, body):
    '''
    Args:
        body: {
                cmd：irisin(光圈变小), irisout(光圈变大),stop(停止)，
                speed：调节速度(1~10, 默认位5)
            }
    '''
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/devices/{gbId}/iris"
    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, body, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 云台控制
def controlConsole(access_key, secret_key, namespaceId, gbId, body):
    '''
    Args:
        body: {
                cmd：left(向左), right(向右), up(向上), down(向下), leftup(左上), rightup(右上), leftdown(左下),
                    rightdown(右下), zoomin(放大), zoomout(缩小),stop(停止PTZ操作)

                speed：调节速度(1~10, 默认位5)
            }
    '''
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/devices/{gbId}/ptz"
    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, body, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 预置位控制
def controlPresetBit(access_key, secret_key, namespaceId, gbId, body):
    '''
    Args:
        body: {
                cmd：set(新增预置位), goto(设置),remove(删除)
                name：预置位名称(cmd为set时有效,支持中文)
                presetId：预置位ID(cmd为goto,remove 时必须指定)
            }
    '''
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/devices/{gbId}/presets"
    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, body, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result


# 获取预置位列表
def listPresets(access_key, secret_key, namespaceId, gbId):
    auth = QiniuMacAuth(access_key, secret_key)
    # 请求URL
    url = f"http://qvs.qiniuapi.com/v1/namespaces/{namespaceId}/devices/{gbId}/presets"

    # 发起POST请求
    ret, res = http._get_with_qiniu_mac(url, params=None, auth=auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log, "text_body": res.text_body}
    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result
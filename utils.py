import re
import json
from tencentcloud.common import credential  # 这里需要安装腾讯翻译sdk
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import (
    TencentCloudSDKException,
)
from tencentcloud.tmt.v20180321 import tmt_client, models

with open("config.json", "r") as f:
    config = json.load(f)


def translate(text, source="en", target="zh") -> str:
    try:
        cred = credential.Credential(
            config["SecretId"], config["SecretKey"]
        )  # "xxxx"改为SecretId，"yyyyy"改为SecretKey
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tmt.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = tmt_client.TmtClient(cred, "ap-beijing", clientProfile)

        req = models.TextTranslateRequest()
        req.SourceText = text  # 要翻译的语句
        req.Source = source  # 源语言类型
        req.Target = target  # 目标语言类型
        req.ProjectId = 0

        resp = client.TextTranslate(req)
        data = json.loads(resp.to_json_string())
        return data["TargetText"]

    except TencentCloudSDKException as err:
        print(err)


def is_chinese(text):
    pattern = re.compile(r"^[\u4e00-\u9fa5]+$")
    return bool(pattern.match(text))


def is_english(text):
    pattern = re.compile(r"^[a-zA-Z\s]+$")
    return bool(pattern.match(text))


def deal_str(text: str):
    return text.replace("\n", "")


if __name__ == "__main__":
    pass

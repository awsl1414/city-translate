import time
import json
from utils import translate, deal_str, is_chinese, is_english

json_file = open(
    "./translate_worldcities-20210313-population-50000+.json", "w", encoding="utf-8"
    )
with open("./data.csv", "r", encoding="utf-8") as f:
    translate_dict = {}
    lines = f.readlines()

    for line in lines:
        if is_english(line):

            result = translate(deal_str(line))
            if is_chinese(result):
                translate_dict[result] = deal_str(line)
        time.sleep(0.1)

json.dump(translate_dict, json_file, ensure_ascii=False)

print("操作完成")

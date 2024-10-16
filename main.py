import pandas as pd
import jieba

def get_best_response(dict, user_input):
    # matched_keywords = [keyword for keyword in keywords_responses if keyword in user_input]

    # 假设关键词的优先级按照它们在字典中出现的顺序
    i= 0
    for keyword in dict:
        if keyword in dict:
            i = i + 1
            return dict[keyword], i

    return "抱歉，我不明白您的意思。"

def read_excel():
    # 读取Excel文件
    # file_path = 'C:\shipinhao\say.xls'  # 请替换为实际的Excel文件路径
    file_path = r'C:\shipinhao\keyword.xlsx'
    df = pd.read_excel(file_path)

    # 打印数据框，检查内容是否正确读取
    # print(df)
    if 'key' in df.columns and 'value' in df.columns:
        business_dict = pd.Series(df['value'].values, index=df['key']).to_dict()
        print(business_dict)
    else:
        print("未找到列 'key' 或 'value'")

    # 输入文本，可以是一段话或两个字
    text = r"你好，哥哥，你单身吗？"

    # 分词
    # words = jieba.lcut(text)
    res, count = get_best_response(business_dict, text)
    print("res = {0}, i = {1}".format(res, count))


    # 匹配字典键（精确匹配和部分匹配）
    # matched_keys = []
    # for key in business_dict:
    #     # 全匹配
    #     if key in words:
    #         matched_keys.append(business_dict[key])
    #     # 部分匹配
    #     elif key in text:
    #         matched_keys.append(business_dict[key])
    #
    # # 输出匹配结果
    # if matched_keys:
    #     print("匹配成功:", matched_keys[0])
    # else:
    #     print("未匹配到关键词")
    # 匹配字典键（逐词匹配）
    matched_keys = []
    # for word in words:
    #     if word in business_dict:
    #         matched_keys.append(business_dict[word])
    #
    # # 输出匹配结果
    # if matched_keys:
    #     print("匹配到的业务:", matched_keys)
    # else:
    #     print("未匹配到业务")


if __name__ == '__main__':
    read_excel()

import jieba
import pandas as pd

business_dict = {}

def get_best_response(user_input):
    # 假设关键词的优先级按照它们在字典中出现的顺序
    i = 0
    for keyword in business_dict:
        if keyword in business_dict:
            i += 1
            return business_dict[keyword], i

    return False


def parise_excel():
    global business_dict
    file_path = r'C:\shipinhao\keyword.xlsx'
    df = pd.read_excel(file_path)
    if 'key' in df.columns and 'value' in df.columns:
        business_dict = pd.Series(df['value'].values, index=df['key']).to_dict()
        print(business_dict)
        return True
    else:
        print("未找到列 'key' 或 'value'")
        return False


def word(user_msg):
    # 读取Excel文件
    res, count = get_best_response(user_msg)
    return res, count

if __name__ == '__main__':
    parise_excel()
    word("你好，哥哥，单身吗？")
import jieba

# 示例字典
business_dict = {
    "业务定制": "customization_service",
    "业务管理": "business_management",
    "业务咨询": "business_consulting"
}

# 输入文本
text = "我们公司提供业务定制服务，也有业务管理的相关解决方案"

# 分词
words = jieba.lcut(text)

# 匹配字典键（逐词匹配）
matched_keys = []
for word in words:
    if word in business_dict:
        matched_keys.append(business_dict[word])

# 输出匹配结果
if matched_keys:
    print("匹配到的业务:", matched_keys)
else:
    print("未匹配到业务")

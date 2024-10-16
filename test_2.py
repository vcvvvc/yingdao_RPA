keywords_responses = {
    "天气": "今天天气不错，记得出去走走哦！",
    "你好": "你好，有什么可以帮您的吗？",
    "帮助": "我可以帮助您解决问题，请告诉我您的问题。",
    # 更多关键词和回复...
}


def get_best_response(user_input):
    matched_keywords = [keyword for keyword in keywords_responses if keyword in user_input]

    # 假设关键词的优先级按照它们在字典中出现的顺序
    for keyword in keywords_responses:
        if keyword in matched_keywords:
            return keywords_responses[keyword]

    return "抱歉，我不明白您的意思。"


user_input = "你好吗，帮我查一下今天天气"
best_response = get_best_response(user_input)
print(best_response)

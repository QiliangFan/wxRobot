import itchat as it


def send_warning_to_group(msg="[epidemic prevention]请及时填写防疫系统!",
                          to="南开软件2017"):
    try:
        group = it.search_chatrooms(name=to)[0]
        userName = group["UserName"]
        print(userName)
        it.send(msg, toUserName=userName)
    except Exception:
        print("未找到有效群聊")
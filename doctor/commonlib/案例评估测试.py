# -*- encoding: utf-8 -*-
import sensenova
sensenova.access_key_id = "2SpQfH0B2vDdBITvHtXNhOA4o4U"
sensenova.secret_access_key = "g7REOTolH3fszG3s9rlbYp59cKAiU7fp"
stream = True # 流式输出或非流式输出
model_id = "nova-ptc-xl-v1" # 填写真实的模型ID
kb_id = 'sf959872407354d9aa022337e84c4d26c'
import sys
import pandas as pd
import getpass
import datetime
from collections import deque
import glob
import os

presets = {
    '通用对话': [
        {
        "role": "system",
        "content": "作为一个AI助手,你的任务是尊重并遵守普遍的道德和伦理原则,包括但不限于诚实、尊重、公正和责任。在回答用户问题时,你必须保证提供的信息是准确和真实的。\n不允许对任何人进行歧视或冒犯。你的任务是在保持友好、耐心和尊重的前提下,为用户提供准确和有用的信息。在回答用户的问题时,你需要尽可能地清晰、简洁并且易于理解。如果需要,你可以主动询问更多信息以更好地理解用户的问题。\n 作为一个AI助手,你的任务是保证用户的安全,你不能提供任何可能对用户造成伤害的建议或信息。包括但不限于身体健康、网络安全、个人隐私等方面。\n 作为一个AI助手,你必须保持中立,避免在政治话题上表达或暗示任何立场或观点。你的任务是提供客观、公正、无偏见的信息,帮助用户理解复杂的政治问题,但不包括推动任何政治议程或偏见。对于具有争议性的政治问题,你可以介绍不同的观点,但要保证平衡和公正。"
        }
    ],
    '人设对话: 数学解题': [
        {
        "role": "system",
        "content": "你是一个数学解题助手,你的目标是帮助用户理解和解决数学问题。你的回答对象是学习数学的学生或其他需要解决数学问题的用户。\n 特别需要注意！你的主要任务不仅仅是给出问题的答案,而是帮助用户理解问题的解决过程。你的解答应当详尽易懂,逐步演示每个步骤,使用户能够理解并自己解决类似的问题。"
        }
    ],
    '人设对话: 情感导师':
    [
        {
        "role": "system",
        "content": "作为一个情感导师,你的目标是帮助人们处理他们的情感问题,并提供建设性的建议。"
        }
    ],
    '知识问答':
    [
        {
            "role": "system",
            "content":"作为一个AI助手,你的任务是对用户的问题或者要求进行详细的回答。"
        }
    ],
    '情感分析':[ 
        {
        "role": "system",
        "content": "你是一个情感分析AI助手。你的主要任务是理解和分析用户的对话内容,特别是关于他们的情感表达。你需要仔细理解用户的情感,是否是正面的、负面的,或者是中立的,并给出你的分析结果。记住,你的分析必须基于用户的对话内容。\n 你需要考虑以下步骤: 步骤1,仔细阅读并理解用户的对话内容；步骤2,提炼并识别其中的情感表达；步骤3,根据你的理解判断这是正面情绪、负面情绪还是中立情绪；步骤4,给出你的分析结果,并明确指出你的判断依据。"
        }
    ],
    '内容总结': 
    [
        {
        "role": "system",
        "content": "你是一个AI助手,你的主要任务是读取并理解提供的长文本,然后在保留关键信息和主要观点的前提下,生成简洁明了的总结。"
        }
    ],
    '作文点评':
    [
        {
        "role": "system",
        "content": "你的任务是评估并提供对学生作文的反馈。你的评价需要基于以下几个维度: 内容逻辑性、语言表达、语法和创新性和引人入胜的程度。在每个维度上,你需要提供1-5的分数,5代表最好。同时,你需要提供具体的改进建议,帮助学生改进他们的写作技巧。"
        }
    ],
    '故事创作':
    [
        {
        "role": "system",
        "content": "你的任务是根据用户给出的提示或关键词,创作一个引人入胜的故事。你的故事需要包含清晰的情节、有趣的角色和令人满意的结局。请记住,使用生动的语言和详细的描述可以让你的故事更加吸引人。"
        }
    ],
    '创意文案':
    [
        {
        "role": "system",
        "content": "你的任务是根据用户给出的产品或活动信息,创作一个有吸引力和创新性的宣传文案。你的文案应该准确地传达产品或活动的核心信息,同时激发读者的兴趣和好奇心。"
        }
    ],
    '写邮件':
    [
        {
        "role": "system",
        "content": "你的任务是根据用户的需求,撰写一封专业且礼貌的电子邮件。你的邮件应该清楚、简洁,并包含所有必要的信息。请确保你的语言和语气对接收者适当。"
        }
    ],
    '写表格':
    [
        {
        "role": "system",
        "content": "你的任务是帮助用户整理和管理信息，将其结构化为表格形式。你需要确保表格中的数据准确无误，并且容易理解。请确保所有的行、列和单元格都被适当地标记和标题。"
        }
    ],
    '写周报':
    [
        {
        "role": "system",
        "content": "你的任务是撰写一个周报，概述过去一周的重要活动和成果。你的周报应包含关键的进度更新，任何重要的问题或挑战，以及对下一周的计划。请确保你的报告清晰、详细且客观。"
        }
    ],
    '写SQL':
    [
        {
        "role": "system",
        "content": "你是一个经验丰富的SQL数据库专家,你的目标是根据用户的需求生成正确的SQL指令。你的回答对象是了解SQL语言的程序员。\n 特别需要注意！你的主要任务不仅仅是给出问题的答案,而是必须以你说思路完成用户的需求并且一步一步的校验这个思路的结果是否正确,并完整的解释你的假设！"
        }
    ],
    
    '语言翻译':
    [
        {
        "role": "system",
        "content": "你的任务是将用户提供的源语言文本准确地翻译成目标语言。在翻译过程中,你需要保证语义的准确性,同时尽可能地保留原文的语气和风格。请注意,不同语言有各自独特的表达方式和文化背景,你需要合理地考虑这些因素进行翻译。"
        }
    ],
    '语法检查':
    [
        {
        "role": "system",
        "content": "你的任务是检查并修正用户提供的文本中的语病问题。语病可能包括词语重复、语句冗余、主题不明确等。你需要清晰地表达出原本的意思,同时确保语句的流畅性和逻辑性。\n 你的任务是检查并修正用户提供的文本中的句式结构错误。这可能包括主谓宾的错误配列、修饰语的误用等。你需要确保句子的结构正确,意义明确。\n 你的任务是检查用户提供的文本的语法错误,并提供修正建议。在检查过程中,你需要关注诸如拼写、标点、单复数、动词时态、主谓一致等语法规则。当你发现错误时,提供清晰且准确的修正建议,同时确保修改后的文本保持原有的意思和语境。"
        }
    ],
    '大师风范':
        [
            {
                "role": "system",
                "content": "对于我的所有问题，你都用大道至简的佛学或中国哲学来解答，不要啰嗦，要有大师范儿。"
            }
        ]
}
keys = list(presets.keys())

class DialogDeque:
    def __init__(self, max_size, preset_dialogs):
        self.user_dialogs = deque(maxlen=max_size)
        self.preset_dialogs = deque(preset_dialogs, maxlen=len(preset_dialogs))

    def add_user_input(self, user_input):
        self.user_dialogs.append({'role': 'user', 'content': user_input})

    def add_api_response(self, api_response):
        self.user_dialogs.append({'role': 'assistant', 'content': api_response})
    
    def get_size(self):
        return len(self.user_dialogs)
    
    def get_dialogs(self):
        return list(self.preset_dialogs) + list(self.user_dialogs)
    
    def print_dialogs(self):
            dialog_str = ' '.join([f"{dialog['role']}: {dialog['content']}" for dialog in self.get_dialogs()])
            print(dialog_str)

def strQ2B(ustring):
    """把字符串全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif 65281 <= inside_code <= 65374:  # 全角字符（除空格）根据关系转化
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring

def chat(query, dialog_deque, kb:bool=False, streaming:bool =stream):
    print("user: "+ query)
    # if query == "stop":
    #     return "stop"
    dialog_deque.add_user_input(query)
    content = dialog_deque.get_dialogs()
    # dialog_deque.print_dialogs()
    if(kb is False):
        resp = sensenova.ChatCompletion.create(
            messages=content,
            model=model_id,
            stream=stream,
        )
    else:
        print("知识库模式")
        resp = sensenova.ChatCompletion.create(
            messages=content,
            model=model_id,
            stream=stream,
            know_id = kb_id,
        )
    if not stream:
        resp = [resp]
    sys.stdout.write(model_id+": ")
    whole_resp = ""
    for part in resp:
        choices = part['data']["choices"]
        for c_idx, c in enumerate(choices):
            if len(choices) > 1:
                sys.stdout.write("===== Chat Completion {} =====\n".format(c_idx))
            if stream:
                
                delta = c.get("delta")
                
                if delta:
                    sys.stdout.write(delta)
                    whole_resp+=delta
                    
                    
            else:
                sys.stdout.write(c["message"])
                if len(choices) > 1:
                    sys.stdout.write("\n")
            sys.stdout.flush()
    # print("d: "+whole_resp) 
    dialog_deque.add_api_response(whole_resp)     
    sys.stdout.write("\n")
    return whole_resp

def ask_question():
    while(True):
        system_no_str = input("输入system用例号: (输入0退出)")
        system_type_id = 0
        # system_no = int(system_no_str)
        try:
            system_no = int(system_no_str)
            presets_count = len(presets)
            if 0 <= system_no <= presets_count:
                break
            else:
                print("输入的数字不在有效范围内,请重新输入。")
        except ValueError:
            print("输入的不是一个有效的数字,请重新输入。")

    
    if 1 <= system_no <= 4:
        system_type_id = 1
    elif 5 <= system_no <= 7:
        system_type_id = 2
    elif 8 <= system_no <= 13:
        system_type_id = 3
    elif 14 <= system_no <= 15:
        system_type_id = 4

    
    while(True):
        try:
            if system_no != 0:
                dialog = DialogDeque(10,[])
            else:
                dialog = DialogDeque(10,presets[keys[system_no-1]])
            desc = keys[system_no-1] if system_no != 0 else "无system"
            query = input("请输入关于"+desc+"的问题: ")
            if system_no == 4:
                resp = chat(query, dialog, kb=True)
            else:
                resp = chat(query, dialog)
            break
        except sensenova.error.APIError as e:
            print(f"发生错误：{e}, 换个问题吧")

    while(True):
        score = input("请给nova的回答打分, 1-5(不要开全角字符): ")
        try:
            score = int(score)
            break
        except ValueError as e:
            print("不是数字")
    # score = strQ2B(score) 
    
    df.loc[len(df)] = {'User':username,'SystemID':system_no-1,"SystemTypeID": system_type_id , "SystemType":keys[system_no-1],
                       "SystemDetail": presets[keys[system_no-1]][0]["content"], 'Prompt': query, 'Response': resp, 'UserScore':score, 'JudgeScore':-1}
    df.to_csv(filename, encoding='utf-8-sig', index=False)

enter = True

# 获取当前用户的用户名
username = getpass.getuser()

# 获取当前日期和时间
now = datetime.datetime.now()

# 格式化日期和时间
timestamp = now.strftime('%Y%m%d%H%M')

# 组合文件名
filename = f'chat_{username}_{timestamp}.csv'

# 获取当前文件夹下所有匹配的文件
matching_files = glob.glob(f'chat_{username}_*.csv')

# 检查是否找到匹配的文件
if matching_files:
    
    # 如果找到，就使用第一个文件（如果有多个匹配的文件，你可能需要修改这个部分以适应你的需求）
    old_file = matching_files[0]
    # print(old_file)
    # 加载旧的csv文件
    df = pd.read_csv(old_file, encoding='utf-8-sig')

    # 使用新的时间戳重命名文件
    os.rename(old_file, filename)
else:
    # 如果没有找到匹配的文件，就创建一个新的数据框
    data = {
        'User':[],
        'SystemID':[],
        'SystemTypeID':[],
        'SystemType':[],
        'SystemDetail': [],
        'Prompt': [],
        'Response': [],
        'UserScore': [],
        'JudgeScore':[]
    }
    df = pd.DataFrame(data)

while(True):
    if(enter):
        print("============菜单============")
        print("1.system列表\n2.评分说明\n3.问问题\n4.退出")
        
        enter = False
    choice = input("请选择操作: ")
    if choice == '1':
        i = 0
        print("============System用例列表============")
        for key in keys:
            i+=1
            print(str(i)+"." + key)
        enter = True
    elif choice == '2':
        # 评分说明
        print("============评分说明============")
        print("评分说明: 1-5打分")
        enter = True
    elif choice == '3':
        # 提问
        ask_question()
        enter = True
    elif choice == '4':
        print("退出程序")
        break
    else:
        print("无效的输入,请输入一个有效的数字。")

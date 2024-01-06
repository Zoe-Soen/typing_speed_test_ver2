# COLOR: https://colorhunt.co/palette/191919750e21e3651dbed754
# Words per minute (wpm) Characters per minute (cpm)
# encoding: utf-8
import os
os.chdir("/Python/100 days of Code- The Complete Python Pro Bootcamp for 2023/exercise code/day-86-typing-speed-test")

from PIL import Image
from datetime import datetime as dt

CURRENT_TIME = dt.now().strftime('%H:%m:%S')

LOGO_IM = Image.open('/Python/100 days of Code- The Complete Python Pro Bootcamp for 2023/exercise code/day-86-typing-speed-test/assets/typing-speed-test.png')
LOGO_IM = LOGO_IM.resize((800, int(800 / (LOGO_IM.size[0]/LOGO_IM.size[1]))))

COLOR_GROUP = [
    {'name': 'black', 'hex': '#191919', 'rgba': (25, 25, 25, 255)}, # 0
    {'name': 'dark_red', 'hex': '#750E21', 'rgba': (117, 14, 33, 255)}, # 1
    {'name': 'orange', 'hex': '#E3651D', 'rgba': (227, 101, 29, 255)}, # 2
    {'name': 'light_green', 'hex': '#BED754', 'rgba': (190, 215, 84, 255)}, # 3
    {'name': 'white', 'hex': '#ffffff', 'rgba': (255, 255, 255, 255)}, # 4
    {'name': 'blue', 'hex': '#86B6F6', 'rgba': (134, 182, 246, 255)}, # 5
    {'name': 'grey', 'hex': '#A9A9A9', 'rgba': (169, 169, 169, 155)}, # 6
]
LANGUAGES = [
    {
        'name':'EN', 
        'logo': '/Python/100 days of Code- The Complete Python Pro Bootcamp for 2023/exercise code/day-86-typing-speed-test/assets/EN.png', 
        'font': 'Arial', 
        'msg1': "How fast are your fingers? Do the 1-minute typing test to find out!\nPress the space bar after each word. At the end, you'll get your typing speed in CPM and WPM. \nGood luck!\n",         'msg2': "Most rencent score:", 
        'msg3': "Type here to start test", 
        'msg4': 'Warning',
        'msg5': "Do you want to finish the test?",
        'msg6': "Corrected CPM: ",
        'msg7': "WPM: ",
        'msg8': "Time Left: ",
        'msg9': "Restart",
        'font_size': [18, 26, 38],
        'words': ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us'],
        'word_w': [],
        'word_h': 0,
        'photo': []
    },{
        'name':'JP', 
        'logo': '/Python/100 days of Code- The Complete Python Pro Bootcamp for 2023/exercise code/day-86-typing-speed-test/assets/JP.png', 
        'font': 'ヒラギノ丸ゴ ProN W4.ttc',
        'msg1': "自分の指の速さは気になりませんか？\n60秒時間限定のタイピングテストをチャレンジしてみよう。\nタイピングスピードがテストの後CPMとWPMで表示されますよん！ファイティング！\n", 
        'msg2': "直近の実績：", 
        'msg3': "単語を入力してテストを開始しよう", 
        'msg4': '注意',
        'msg5': "テストはまだ終わっていないですが、終了しますか？",
        'msg6': "正確なCPM: ",
        'msg7': "WPM: ",
        'msg8': "残る時間: ",
        'msg9': "再　開",
        'font_size': [18, 20, 38],
        'words': ['祭典', '転嫁', '開幕', '本場', '繰り広げる', '各国', '節目', '再現', '設置', '漂う', '連日', '競馬', 'バー', '難解', '眺め', '刀', '蛙', '爆睡', '鐘', '待ち構える', '出荷', '品薄', '排除', '過失', '社交的', '使い道', '合宿', '帰宅', '途中', '捕まる', '不良品', 'メロディー', '手品', '非凡的', '墓', '激流', '推測', '停電', '美術品', '慎重', 'コレクション', '熱意', '快挙', '誇る', '賄賂', '消費者', '想定外', '幽霊', '裏切る', '見事'],
        'word_w': [],
        'word_h': 0,
        'photo': []
    }, {
        'name':'CN', 
        'logo': '/Python/100 days of Code- The Complete Python Pro Bootcamp for 2023/exercise code/day-86-typing-speed-test/assets/CN.png', 
        'font': 'Arial Unicode.ttf',
        'msg1': "你的手速几何？来试试限时60秒的打字测试就知道咯！\n按空格键结束每个单词的输入，倒计时结束后，可以确认你实际的打字速度哦～祝你好运\n", 
        'msg2': "最新成绩：", 
        'msg3': "在此输入单词开始测试", 
        'msg4': '提示',
        'msg5': "测试时间尚未结束，是否确定结束？",
        'msg6': "正确的CPM: ",
        'msg7': "WPM: ",
        'msg8': "剩余时间: ",
        'msg9': "重开",
        'font_size': [18, 26, 38],
        'words': ['呼', '铺', '反', '击', '毯', '区', '脖', '层', '梨', '笼', '其', '形', '染', '梁', '盘', '翠', '燃', '峰', '爽', '勤', '委', '弹', '踮', '补', '钢', '院', '室', '琴', '除', '宁', '胡', '疲', '愣', '戏', '倦', '纷', '橙', '凡', '切', '喂', '牵', '集', '鸽', '困', '掌', '养', '航', '钟', '计', '奋', '纪', '哈', '览', '纺', '欠', '馆', '织', '迟', '紧', '优', '叹', '怦', '胜', '决', '胳', '壮', '劳', '膊', '谷', '巨', '登', '当', '旅', '察', '刘', '交', '蒲', '识', '菊', '支', '降', '残', '庆', '拼', '民', '案', '讯', '退', '约', '克', '橱', '危', '聚', '扬', '指', '险', '挥', '接', '买', '龙', '娃', '君', '求', '苍', '橘', '利', '洼', '径', '啪', '斜', '炸', '枫', '蹦', '于', '棋', '模', '株', '握', '湾', '悔', '绑', '浴', '灌', '碰', '通', '溉', '返', '杯', '器', '塑', '淹', '育', '缺', '浪', '仙', '状', '叠', '泪', '省', '传', '泽', '店', '产', '裙', '幸', '央', '坛', '州', '献', '瓦', '迹', '川', '帜', '庄', '厦', '涌', '洁', '严', '岛', '奏', '阔', '隔', '曲', '碑', '峡', '亿', '周', '与', '似', '陆', '任', '裤', '福', '惯', '袄', '吵', '式', '疼', '受', '眯', '痛', '郑', '疯', '尤', '著', '尽', '恨', '科', '良', '漠', '容', '粒', '普', '图', '锣', '讲', '卖', '盯', '彰', '信', '藤', '秃', '豹', '闹', '冒', '责', '铅', '柴', '板', '惹', '焰', '凳', '吐', '易', '糙', '桌', '折', '但', '盒', '嗽', '毁', '钩', '呗', '泰', '零', '算', '烂', '邻', '虽', '徒', '乘', '功', '傍', '注', '绳', '椅', '削', '斤', '瞧', '须', '设', '躁', '纹', '茶', '吸', '萄', '泡', '皱', '独', '留', '坏', '之', '扎', '轮', '铁', '抓', '期', '思', '渠', '抽', '伤', '酸', '续', '灿', '柏', '葡', '搓', '钉', '莓', '第', '亚', '侧', '扔', '牢', '缩', '炭', '呆', '遥', '贫', '始', '寻', '富', '件', '雹', '汪', '肯', '慕', '舟', '料', '踏', '愁', '套', '潭', '份', '妹', '护', '叽', '喳', '卷', '跨', '孔', '咳', '稼', '至', '哩', '必', '喷', '暴', '猜', '食', '饥', '拴', '泣', '索', '逗', '健', '奉', '康', '永', '操', '则', '甚', '蒙', '射', '乏', '棚', '贵', '客', '昨', '寄', '何', '历', '纱', '扇', '粉', '欲', '确', '银', '简', '抱', '仗', '单', '寸', '沿', '葫', '枣', '益', '际', '猎', '宇', '叨', '芦', '浅', '哇', '忍', '障', '宜', '华', '费', '赠', '贡', '羡', '喃', '谋', '猬', '博', '稀', '农', '控', '珍', '技', '制', '孙', '袁', '泥', '悉', '隆', '茁', '绝', '介', '肉', '绍', '史', '培', '核', '蓬', '欣', '卫', '蒸', '味', '填', '死', '浓', '嫦', '继', '腾', '娥', '乎', '黎', '宙', '载', '箭', '浮', '神', '族', '杂', '拥', '灾', '呱', '舒', '圈', '极', '狐', '饱', '夫', '狸', '袍', '汗', '串', '鞭', '驶', '迫', '炮', '示', '待', '筝', '硬', '踪', '移', '刺', '术', '雀', '跃', '赏', '锦', '棱', '龟', '鹰', '巢', '镜', '丛', '崭', '映', '鹂', '牌', '幻', '灵', '演', '嬉', '蕉'],
        'word_w': [],
        'word_h': 0,
        'photo': []
    },]

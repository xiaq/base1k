import sys


chars = '天地玄黃宇宙洪荒日月盈昃辰宿列張寒來暑往秋收冬藏閏餘成歲律呂調陽雲騰致雨露結為霜金生麗水玉出崑岡劍號巨闕珠稱夜光果珍李柰菜重芥薑海鹹河淡鱗潛羽翔龍師火帝鳥官人皇始制文字乃服衣裳推位讓國有虞陶唐弔民伐罪周發殷湯坐朝問道垂拱平章愛育黎首臣伏戎羌遐邇壹體率賓歸王鳴鳳在樹白駒食場化被草木賴及萬方蓋此身髮四大五常恭惟鞠養豈敢毀傷女慕貞絜男效才良知過必改得能莫忘罔談彼短靡恃己長信使可覆器欲難量墨悲絲染詩讃羔羊景行維賢剋念作聖德建名立形端表正空谷傳聲虛堂習聽禍因惡積福緣善慶尺璧非寶寸陰是競資父事君曰嚴與敬孝當竭力忠則盡命臨深履薄夙興溫凊似蘭斯馨如松之盛川流不息淵澄取映容止若思言辭安定篤初誠美慎終宜令榮業所基籍甚無竟學優登仕攝職從政存以甘棠去而益詠樂殊貴賤禮別尊卑上和下睦夫唱婦隨外受傅訓入奉母儀諸姑伯叔猶子比兒孔懷兄弟同氣連枝交友投分切磨箴規仁慈隱惻造次弗離節義廉退顛沛匪虧性靜情逸心動神疲守真志滿逐物意移堅持雅操好爵自縻都邑華夏東西二京背邙面洛浮渭據涇宮殿盤鬱樓觀飛驚圖寫禽獸畫綵仙靈丙舍傍啟甲帳對楹肆筵設席鼓瑟吹笙升階納陛弁轉疑星右通廣內左達承明既集墳典亦聚羣英杜稾鍾隸漆書壁經府羅將相路俠槐卿戶封八縣家給千兵高冠陪輦驅轂振纓世祿侈富車駕肥輕策功茂實勒碑刻銘磻溪伊尹佐時阿衡奄宅曲阜微旦孰營桓公匡合濟弱扶傾綺迴漢惠說感武丁俊乂密勿多士寔寧晉楚更霸趙魏困橫假途滅虢踐土會盟何遵約法韓弊煩刑起翦頗牧用軍最精宣威沙漠馳譽丹青九州禹跡百郡秦并嶽宗恆岱禪主云亭雁門紫塞雞田赤城昆池碣石鉅野洞庭曠遠緜邈巖岫杳冥治本於農務茲稼穡俶載南畝我藝黍稷稅熟貢新勸賞黜陟孟軻敦素史魚秉直庶幾中庸勞謙謹敕聆音察理鑒貌辨色貽厥嘉猷勉其祗植省躬譏誡寵增抗極殆辱近恥林皋幸即兩疏見機解組誰逼索居閒處沈默寂寥求古尋論散慮逍遙欣奏累遣慼謝歡招渠荷的歷園莽抽條枇杷晚翠梧桐早凋陳根委翳落葉飄颻遊鵾獨運凌摩絳霄耽讀翫市寓目囊箱易輶攸畏屬耳垣墻具膳飡飯適口充腸飽飫烹宰飢厭糟糠親戚故舊老少異糧妾御績紡侍巾帷房紈扇圓潔銀燭煒煌晝眠夕寐藍笋象床絃歌酒讌接盃舉觴矯手頓足悅豫且康嫡後嗣續祭祀烝嘗稽顙再拜悚懼恐惶牋牒簡要顧答審詳骸垢想浴執熱願涼驢騾犢特駭躍超驤誅斬賊盜捕獲叛亡布射遼丸嵇琴阮嘯恬筆倫紙鈞巧任釣釋紛利俗並皆佳妙毛施淑姿工顰妍笑年矢每催曦暉朗耀璇璣懸斡晦魄環照指薪修祜永綏吉劭矩步引領俯仰廊廟束帶矜莊徘徊瞻眺孤陋寡聞愚蒙等誚謂語助者焉哉乎也魛魢魨魷䰾魴鮋鮊魺鮃鮁鮎鮍鮓鮒鮐鱸鮑鱟鮺鮜鱠鰂鮳'


def convert(i):
    li = []
    while i > 0:
        li.append(chars[i & 0x1F])
        i >>= 5
    return ''.join(reversed(li))


def parse_input(s):
    try:
        i = int(s, 0)
    except ValueError:
        raise ValueError('Not a number: ' + s)
    if i <= 0:
        raise ValueError('Not positive: ' + s)
    return i


def cli():
    for line in sys.stdin:
        converted = []
        for s in line.split():
            try:
                i = parse_input(s)
            except ValueError as e:
                print(e, file=sys.stderr)
                sys.exit(2)
            converted.append(convert(i))
        print(' '.join(converted))


http_root_str = '''<pre>Put the number to convert in URL, like /233 or /0x233

Source code: github.com/xiaq/base1k</pre>'''


def http(host, port):
    from bottle import route, response, run

    @route('/')
    def root():
        return http_root_str

    @route('/<s:path>')
    def do_conversion(s):
        try:
            i = parse_input(s)
        except ValueError as e:
            response.status = 400
            return str(e)
        return convert(i)

    run(host=host, port=port)


usage_str = '''Usage:
  python3 base1k.py # CLI session
  python3 base1k.py http <host> <port> # Serve HTTP'''


def usage():
    print(usage_str)
    sys.exit(1)


def main(argv):
    if len(argv) == 0:
        cli()
    elif len(argv) == 3 and argv[0] == 'http':
        host = argv[1]
        try:
            port = int(argv[2])
        except ValueError:
            usage()
        http(host, port)
    else:
        usage()


if __name__ == '__main__':
    main(sys.argv[1:])

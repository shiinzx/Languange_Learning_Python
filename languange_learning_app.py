
import random

words = [
    {"chinese": "的", "indonesian": "milik, yang"},
    {"chinese": "一", "indonesian": "satu"},
    {"chinese": "是", "indonesian": "adalah"},
    {"chinese": "不", "indonesian": "tidak"},
    {"chinese": "了", "indonesian": "sudah"},
    {"chinese": "人", "indonesian": "orang"},
    {"chinese": "我", "indonesian": "saya"},
    {"chinese": "在", "indonesian": "di"},
    {"chinese": "有", "indonesian": "punya"},
    {"chinese": "他", "indonesian": "dia (laki-laki)"},
    {"chinese": "这", "indonesian": "ini"},
    {"chinese": "中", "indonesian": "tengah"},
    {"chinese": "大", "indonesian": "besar"},
    {"chinese": "为", "indonesian": "untuk"},
    {"chinese": "上", "indonesian": "atas"},
    {"chinese": "个", "indonesian": "satu (kata pengukur)"},
    {"chinese": "国", "indonesian": "negara"},
    {"chinese": "到", "indonesian": "sampai"},
    {"chinese": "和", "indonesian": "dan"},
    {"chinese": "你", "indonesian": "kamu"},
    {"chinese": "说", "indonesian": "berbicara"},
    {"chinese": "们", "indonesian": "kami, mereka"},
    {"chinese": "为", "indonesian": "untuk"},
    {"chinese": "子", "indonesian": "anak"},
    {"chinese": "会", "indonesian": "akan, bisa"},
    {"chinese": "地", "indonesian": "tanah"},
    {"chinese": "出", "indonesian": "keluar"},
    {"chinese": "自", "indonesian": "dari, sendiri"},
    {"chinese": "之", "indonesian": "itu"},
    {"chinese": "年", "indonesian": "tahun"},
    {"chinese": "得", "indonesian": "mendapatkan"},
    {"chinese": "与", "indonesian": "dengan"},
    {"chinese": "对", "indonesian": "terhadap"},
    {"chinese": "着", "indonesian": "sedang"},
    {"chinese": "里", "indonesian": "dalam"},
    {"chinese": "下", "indonesian": "bawah"},
    {"chinese": "一", "indonesian": "satu"},
    {"chinese": "上", "indonesian": "atas"},
    {"chinese": "个", "indonesian": "satu"},
    {"chinese": "人", "indonesian": "orang"},
    {"chinese": "中", "indonesian": "tengah"},
    {"chinese": "和", "indonesian": "dan"},
    {"chinese": "会", "indonesian": "akan, bisa"},
    {"chinese": "还", "indonesian": "masih"},
    {"chinese": "都", "indonesian": "semua"},
    {"chinese": "就", "indonesian": "hanya, tepat"},
    {"chinese": "日", "indonesian": "hari"},
    {"chinese": "要", "indonesian": "ingin"},
    {"chinese": "出", "indonesian": "keluar"},
    {"chinese": "如", "indonesian": "seperti"},
    {"chinese": "她", "indonesian": "dia (perempuan)"},
    {"chinese": "家", "indonesian": "rumah"},
    {"chinese": "事", "indonesian": "hal, pekerjaan"},
    {"chinese": "会", "indonesian": "pertemuan, bisa"},
    {"chinese": "而", "indonesian": "tetapi"},
    {"chinese": "得", "indonesian": "mendapat"},
    {"chinese": "再", "indonesian": "lagi"},
    {"chinese": "知", "indonesian": "tahu"},
    {"chinese": "方", "indonesian": "arah"},
    {"chinese": "更", "indonesian": "lebih"},
    {"chinese": "开", "indonesian": "membuka"},
    {"chinese": "已", "indonesian": "sudah"},
    {"chinese": "用", "indonesian": "menggunakan"},
    {"chinese": "长", "indonesian": "panjang"},
    {"chinese": "三", "indonesian": "tiga"},
    {"chinese": "学", "indonesian": "belajar"},
    {"chinese": "时", "indonesian": "waktu"},
    {"chinese": "自", "indonesian": "sendiri"},
    {"chinese": "事", "indonesian": "hal, kejadian"},
    {"chinese": "成", "indonesian": "jadi"},
    {"chinese": "种", "indonesian": "jenis"},
    {"chinese": "所", "indonesian": "tempat"},
    {"chinese": "多", "indonesian": "banyak"},
    {"chinese": "能", "indonesian": "bisa"},
    {"chinese": "度", "indonesian": "derajat"},
    {"chinese": "都", "indonesian": "semua"},
    {"chinese": "想", "indonesian": "ingin, berpikir"},
    {"chinese": "无", "indonesian": "tanpa"},
    {"chinese": "把", "indonesian": "mengambil"},
    {"chinese": "各", "indonesian": "masing-masing"},
    {"chinese": "像", "indonesian": "seperti"},
    {"chinese": "好", "indonesian": "baik"},
    {"chinese": "很", "indonesian": "sangat"},
    {"chinese": "让", "indonesian": "membiarkan"},
    {"chinese": "小", "indonesian": "kecil"},
    {"chinese": "大", "indonesian": "besar"},
    {"chinese": "作", "indonesian": "kerja"},
    {"chinese": "物", "indonesian": "benda"},
    {"chinese": "四", "indonesian": "empat"},
    {"chinese": "已", "indonesian": "sudah"},
    {"chinese": "去", "indonesian": "pergi"},
    {"chinese": "她", "indonesian": "dia (perempuan)"},
    {"chinese": "能", "indonesian": "bisa"},
    {"chinese": "人", "indonesian": "orang"},
    {"chinese": "中", "indonesian": "di tengah"},
    {"chinese": "他", "indonesian": "dia (laki-laki)"},
    {"chinese": "工", "indonesian": "pekerjaan"},
    {"chinese": "日", "indonesian": "hari"}
]


def quiz_user(words):
    random.shuffle(words)
    score = 0

    for word in words:
        print(f"What is the Indonesian translation of '{word['chinese']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['indonesian'].lower()

        if user_answer == correct_answer:
            print("Correct!!\n!")
            score += 1
        else:
            print(f"Wrong, The correct answer is '{word['indonesian']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")



def main():
    print("Welcome to the Languange Learning Flashcards App!")
    input("Press Enter ti start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()
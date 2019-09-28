import csv
import sys

def _csv_files():
    # 用言（動詞、形容詞、助動詞）
    return ('Verb.utf8.csv', 'Adj.utf8.csv', 'Auxil.utf8.csv')

def _show_help():
    import os
    this_file_name = os.path.basename(__file__)
    doc = '''\
概要        : 入力した用言（基本形）の入力した活用形を返す。
使い方      : 第1引数に用言の基本形, 第2引数に活用形名を入力する。
コマンド書式: python3 {0} 用言(基本形) 活用形名"
コマンド例  : python3 {0} '動く' '未然形'"
コマンド例  : python3 {0} '美しい' '未然ウ接続'"
コマンド例  : python3 {0} '如し' '体言接続'"
必要なもの  : 辞書ファイル {1}\
'''.format(this_file_name, _csv_files())
    print(doc)

# 入力した用言（基本形）の入力した活用形を返す
def get_conjugation_word():
    if 3 > len(sys.argv):
        _show_help()
        sys.exit()
    res = _read_csv(sys.argv[1], sys.argv[2])
    if 0 < len(res): print(res)

# 入力した基本形に一致するレコードの活用形を返す
def _read_csv(word, conj):
    for filename in _csv_files():
        reader = csv.reader(open(filename, "r", encoding="utf-8"))
        for row in reader:
            if word == row[10] and conj == row[9]: return row[0]
    return ''


if __name__ == '__main__':
    get_conjugation_word()


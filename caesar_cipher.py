class Caesar:
    LETTER_FREQUENCIES = [
        0.07984, 0.01511, 0.02504, 0.04260, 0.12452, 0.02262, 0.02013,
        0.06384, 0.07000, 0.00131, 0.00741, 0.03961, 0.02629,
        0.06876, 0.07691, 0.01741, 0.00107, 0.05912, 0.06333,
        0.09058, 0.02844, 0.01056, 0.02304, 0.00159, 0.02028, 0.00057
    ]

    @staticmethod
    def set_freq(file_path: str) -> None:
        with open(file_path, 'r', encoding='utf-8') as freq:
            Caesar.LETTER_FREQUENCIES = list(map(lambda v: float(v.strip('\n').split()[1].strip('%'))/100, freq.readlines()))

    @staticmethod
    def shift(text: str, n: int) -> str:
        result = ""
        for v in text:
            result += chr((ord(v.upper())+n-65) % 26 + 65)
        return result

    @staticmethod
    def shift_with_stats(text: str, n: int) -> float:
        result = 0
        c_text = set(text)
        for v in c_text:
            p = text.count(v) / len(text)
            result += p * Caesar.LETTER_FREQUENCIES[(ord(v.upper())-n-65) % 26]
        return result

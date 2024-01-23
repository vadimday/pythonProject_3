import re
text = "sdaifopjsdofisdhjiofa.oaisfhsdoiufhsf!!!sepofjifjifs"
sentences = re.findall(r"\s*([^.?!]+)\s*", text)
print(f"Найдено: {len(sentences)}.\nНайденные предложения: {sentences}.")


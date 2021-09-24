import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from utils.Preprocess import Preprocess

sent = input()

# 전처리 객체 생성
p = Preprocess(userdic='C:/Users/SeoJiHun/chatbot/utils/user_dic.tsv.txt')

# 형태소 분석기 실행
pos = p.pos(sent)

print(pos)

# 품사 태그와 같이 키워드 출력
ret = p.get_keywords(pos, without_tag=False)
print(ret)

# 품사 태그 없이 키워드 출력
ret = p.get_keywords(pos, without_tag=True)
print(ret)

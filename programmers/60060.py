# 60060 가사 검색
from collections import defaultdict
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]


class Trie():
    def __init__(self):
        # 자식 노드
        self.child = {}
        # 현재 노드 (알파벳) 까지의 단어 개수
        self.count = 0

    # 문자열 삽입
    def insert(self, str):
        # cursor 설정 (head 부터 시작)
        cur = self
        # 현재 노드 count 1 증가
        cur.count += 1

        # 한 문자씩
        for s in str:
            # 자식 노드 중 해당 문자가 없다면
            if s not in cur.child:
                # 새로운 Trie를 구성한다
                cur.child[s] = Trie()
            # cursor를 다음 문자 노드로 옮겨준다
            cur = cur.child[s]
            cur.count += 1

    # 문자열 검색
    def search(self, str):
        # cursor 설정 (head 부터 시작)
        cur = self

        for s in str:
            # ? 문자를 만났으면 해당 query 문자를 다 찾은 것
            if s == '?':
                return cur.count
            # 해당하는 문자가 없을 때 0 리턴
            if s not in cur.child:
                return 0
            # 다음 자식 노드로 이동
            else:
                cur = cur.child[s]
        # 끝까지 다 찾았을 경우 현재 노드의 count 리턴
        return cur.count


def solution():
    answer = []
    # 접두사 Trie
    prefix_trie = defaultdict(Trie)
    # 접미사 Trie
    suffix_trie = defaultdict(Trie)
    # defaultdict를 사용하면 해당 키에 대한 디폴트 값을 지정할 수 있다
    # 딕셔너리에 키가 없으면 그 키를 만들어주고 초깃값을 0으로 세팅해 준다
    # 따라서, 키가 존재하지 않을 때 키를 추가하는 조건문을 쓰지 않아도 됨!

    # 단어를 trie에 추가해준다
    # trie[단어길이].insert(단어)
    for word in words:
        prefix_trie[len(word)-1].insert(word)
        # 접미사를 찾기 위해 반전시킨 단어로 trie를 만든다
        suffix_trie[len(word)-1].insert(word[::-1])

    # query에 맞는 단어를 찾는다
    # trie[단어길이].search(단어)
    for query in queries:
        if query[0] != '?':
            answer.append(prefix_trie[len(query)-1].search(query))
        else:
            answer.append(suffix_trie[len(query)-1].search(query[::-1]))
    return answer


print(solution())

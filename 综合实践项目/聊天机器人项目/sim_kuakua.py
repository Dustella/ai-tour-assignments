import random
from sentence_similarity.sentenceSimilarity import SentenceSimilarity
from sentence_similarity.zhcnSegment import zhcnSeg


class KuakuaChat:
    def __init__(self):
        self.qa_dict = {}
        self.q_list = []
        with open('./douban_kuakua_topic.txt', 'r', encoding='utf8') as in_file:
            for line in in_file.readlines():
                que, *ans_list = line.split('<######>')[-1].split('<$$$$$$>')
                que = que.strip()
                ans_list = [ans for ans in ans_list if len(ans) > 2]
                if len(que) > 5:
                    self.q_list.append(que)
                    self.qa_dict[que] = ans_list

        zhcn_seg = zhcnSeg()
        self.sent_sim = SentenceSimilarity(zhcn_seg)
        self.sent_sim.set_sentences(self.q_list)
        self.sent_sim.TfidfModel()

    def answer_question(self, question_str):
        most_sim_questions = self.sent_sim.similarity_top_k(question_str, 4)
        answer_list = [self.qa_dict[item[0]] for item in most_sim_questions]
        return [answer for sublist in answer_list for answer in sublist]


if __name__ == '__main__':
    main_bot = KuakuaChat()
    while True:
        try:
            user_input = input('USER:')
            answer_list = main_bot.answer_question(user_input)
            response = random.choice(answer_list)
            print('BOT:', response)
        # 直到按ctrl-c 或者 ctrl-d 才会退出
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

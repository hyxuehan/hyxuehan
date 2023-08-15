import json

class Open:
    def __init__(self,filepath) -> None:
        self.filepath = filepath
        self.str = self.__openfile()

    def __openfile(self):
        with open(file=self.filepath, mode='r', encoding='utf-8') as f:
            s = json.loads(f.read()).get('result')
            f.close()
        return s

class JkJson(Open):
    def __init__(self, th:int,filepath='1.txt') -> None:
        super().__init__(filepath)
        # print(self.get_id(100))
        self.th = th
        self.id = ''
        self.__get('id')
        self.question = self.__get('question')
        self.answer = self.__get('answer')
        self.item = self.__get_item()
        self.explains = self.__get('explains')
        self.url = self.__get('url')
    def __get(self,s):
        try:
            res= self.str[self.th].get(s)
        except IndexError:
            res = '没有题目了'
        finally:
            return res
    def __get_item(self):
        item = {}
        for k, v in self.str[self.th].items():
            if k[:4] == 'item':
                item.update({k:v})
        return item
            
    


if __name__ =='__main__':
    jkbd = JkJson(0)
    print(jkbd.question)
    print(jkbd.item)
    print(jkbd.answer)
    print(jkbd.explains)

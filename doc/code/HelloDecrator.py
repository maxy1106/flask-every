

"""
装饰器例子
"""
import random
import time
#
# def cyle_time(fun):
#
#     def wrapper(*args,**kwargs):
#
#         start_time = time.time()
#         result = fun(*args,**kwargs)
#         end_time = time.time()
#
#         print("总耗时",end_time-start_time)
#         return result
#     return wrapper
#
# @cyle_time
# def play(game,t=5):
#     print("开始玩游戏%s" %game)
#     time.sleep(t)
#     print("游戏结束")
#     return "hhahaha"
#
# if __name__ == "__main__":
#     result = play("aaa")
#     print(result)



def can_play(can):
    def can_play_wrapper(func):
        def wrapper():
            if random.randrange(10) > can:
                func()
            else:
                print("can't play")
        return wrapper
    return can_play_wrapper

@can_play(-1)
def play():
    print("paly game")

if __name__ == "__main__":
    play()
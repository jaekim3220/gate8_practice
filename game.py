# pip install ursina를 사용한 게임 맵 생성

from ursina import *
# 게임 내에서 1인칭으로 보기
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
mouse.visible = False   # 마우스 안 보이기

# 맵 `바닥` 설계
game_floor =Entity(model='cube', # 객체
                   position=(0, 0, 0), # 기본 위치
                   scale=(10, 1, 100), # x,y,z축 크기
                   color=color.light_gray, # 맵 색깔
                   collider='box'   # 맵에 `충돌` 효과를 제공, 떨어짐을 방지
                   )
# 맵 `천장` 설계
main_ceiling = Entity(model='cube', position=(0, 10, 0), scale=(10, 1, 100), 
                      color=color.light_gray, collider='box')
# 맵 `좌측 벽` 설계
main_left_wall = Entity(model='cube', position=(-5, 5, -5), color=color.white,
                        scale=(1, 10, 110), collider='box',     # 나중에 꺾이니까 더 길게
                        texture='pic/wall.jpg', texture_scale=(15,10)   # 벽 질감 표현 및 크기
                        )
# 맵 `우측 벽` 설계
main_right_wall = Entity(model='cube', position=(5, 5, 5), color=color.white,
                         scale=(1, 10, 110), collider='box', 
                         texture='pic/wall.jpg', texture_scale=(15,10)
                         )
'''
맵을 만들기 위한 노가다 시작
-> EditorCamera()를 사용하며 확인하는 것이 편함
'''

# 앞쪽
front_floor = Entity(model='cube', position=(-25, 0, 55), 
                     scale=(60, 1, 10), color=color.light_gray, 
                     collider='box')
front_ceiling = Entity(model='cube', position=(-25, 10, 55), 
                       scale=(60, 1, 10), color=color.light_gray, 
                       collider='box')
front_left_wall = Entity(model='cube', position=(-30, 5, 50), 
                         scale=(50, 10, 1), collider='box', 
                         texture='pic/wall.jpg', texture_scale=(16, 10))
front_right_wall = Entity(model='cube', position=(-20, 5, 60), 
                          scale=(50, 10, 1), collider='box', 
                          texture='pic/wall.jpg', texture_scale=(16, 10))


EditorCamera()  # 맵 생성 중 카메라 구도 조정(마우스 우클릭)

# character = FirstPersonController() # 1인칭으로 맵 보기
# character.cursor.visible = False    # 커서 보이기 방지
# character.gravity = 0.5 # 중력에 따라 캐릭터 점프력 차이
# character.speed = 10    # 이동 속도

app. run()
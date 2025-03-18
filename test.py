import pygame
import random
import os

pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Perry the Platypus")

# FPS 
FPS = 30

# LIÊN KẾT FILE / FOLDER
base_dir = os.path.dirname(__file__) # Lấy đường dẫn đến thư mục chứa script này

# Sound
soundtrack_1 = os.path.join(base_dir, "assets", "sounds", "soundtracks", "soundtrack-1.mp3")
scoring_sound = pygame.mixer.Sound(os.path.join(base_dir, "assets", "sounds", "score.mp3"))
jumping_sound = pygame.mixer.Sound(os.path.join(base_dir, "assets", "sounds", "jump.mp3"))
game_over_sound = pygame.mixer.Sound(os.path.join(base_dir, "assets", "sounds", "game over", "splat.mp3"))
collecting_sound = pygame.mixer.Sound(os.path.join(base_dir, "assets", "sounds", "ufo", "ufo-1.mp3"))
cow_sound = pygame.mixer.Sound(os.path.join(base_dir, "assets", "sounds", "cows", "bokhongluoi-1.mp3"))
plane_sound = pygame.mixer.Sound(os.path.join(base_dir, "assets", "sounds", "planes", "planecrashdiectai.mp3"))
bomb_sound = pygame.mixer.Sound(os.path.join(base_dir, "assets", "sounds", "planes", "planecrashnormal.mp3"))

# Character 1 - perry ufo
char_perry_ufo_normal_image = os.path.join(base_dir, "assets", "characters", "perry_ufo", "perry-1.png")
char_perry_ufo_jump_image_2 = os.path.join(base_dir, "assets", "characters", "perry_ufo", "perry-2.png")
char_perry_ufo_jump_image_1 = os.path.join(base_dir, "assets", "characters", "perry_ufo", "perry-3.png")
char_perry_ufo_collecting_image_1 = os.path.join(base_dir, "assets", "characters", "perry_ufo", "perry-beam-1.png")
char_perry_ufo_collecting_image_2 = os.path.join(base_dir, "assets", "characters", "perry_ufo", "perry-beam-2.png")
char_perry_ufo_collecting_image_3 = os.path.join(base_dir, "assets", "characters", "perry_ufo", "perry-beam-3.png")

# Character 2 - perry plane
char_perry_plane_normal_image = os.path.join(base_dir, "assets", "characters", "perry_plane", "perry-plane-1.png")

# Character - story
nguyen_thanh_hung_image = os.path.join(base_dir, "assets", "characters", "story", "nguyen-thanh-hung.png")
ba_duy_image = os.path.join(base_dir, "assets", "characters", "story", "ba-duy.png")
dam_vinh_hung_image = os.path.join(base_dir, "assets", "characters", "story", "dam-vinh-hung.png")
do_phu_qui_image = os.path.join(base_dir, "assets", "characters", "story", "do-phu-qui.png")
j97_image = os.path.join(base_dir, "assets", "characters", "story", "j97.png")

# Grounds
ground_image = os.path.join(base_dir, "assets", "grounds", "ground.png")

# Obstacles
pipe_bottom_image = os.path.join(base_dir, "assets", "obstacles", "pipe-bottom.png")
pipe_top_image = os.path.join(base_dir, "assets", "obstacles", "pipe-top.png")
twin_towers_image = os.path.join(base_dir, "assets", "obstacles", "twin-towers-1.png")

# Coins
coin_image_1 = os.path.join(base_dir, "assets", "coins", "cow-1.png")

# Backgrounds
background_stato_image = os.path.join(base_dir, "assets", "backgrounds", "background-2-sky.png")
background_roto_image = os.path.join(base_dir, "assets", "backgrounds", "background-2-buildings.png")

# fonts
mario_font = os.path.join(base_dir, "assets", "fonts", "TypefaceMarioWorldPixelFilledRegular-rgVMx.ttf")
montserrat_font = os.path.join(base_dir, "assets", "fonts", "Montserrat-Regular.ttf")
montserrat_font_bold = os.path.join(base_dir, "assets", "fonts", "Montserrat-Bold.ttf")
montserrat_font_italic = os.path.join(base_dir, "assets", "fonts", "Montserrat-Italic.ttf")

# Menu
menu_game_over_image = os.path.join(base_dir, "assets", "menu", "menu-game-over.png")

# random files
sexy_girl_image = os.path.join(base_dir, "assets", "easter eggs", "sexy.png")

FONT = {
    "ARIAL": pygame.font.Font(None, 40), # Font mặc định, size 40
    "MARIO_BIG": pygame.font.Font(mario_font, 25),
    "MARIO_SMALL": pygame.font.Font(mario_font, 15),
    "MONTESRRAT_REGULAR": pygame.font.Font(montserrat_font, 15),
    "MONTESRRAT_BOLD": pygame.font.Font(montserrat_font_bold, 15),
    "MONTESRRAT_ITALIC": pygame.font.Font(montserrat_font_italic, 15)
}

COLOR = {
    "WHITE": (255,255,255),
    "BLACK": (0,0,0),
    "RED": (255,0,0),
    "GREEN": (0, 255, 0),
    "ORANGE": (237, 97, 16),
    "GOLD": (255, 215, 0),
    "BEIGE": (245, 245, 220),
    "BRONZE": (205, 127, 50),
    "BROWN": (153, 51, 0),
    "CYAN": (0, 255, 255),
    "EMERALD": (80, 200, 120),
    "JUNGLE_GREEN": (41, 171, 135),
    "FOREST_GREEN": (34, 139, 34),
    "LIME_GREEN": (50, 205, 50),
    "MIDNIGHT_GREEN": (0, 73, 83),
    "AQUAMARINE": (0, 255, 191),
    "AZURE": (0, 127, 255),
    "BABY_BLUE": (137, 207, 240),
    "BLUE": (0, 0, 255),
    "DEEP_SKY_BLUE": (0, 191, 255),
    "LIGHT_SKY_BLUE": (135, 206, 250),
    "ICE_BLUE": (153, 255, 255),
    "LAPIS_LAZULI": (38, 97, 156),
    "MIDNIGHT_BLUE": (25, 25, 112),
    "ROYAL_BLUE": (0, 35, 102)
}

class obj: # MỘT VẬT THỂ TRONG GAME
    def __init__(self, image_path, x = 0, y = 0, width = 0, height = 0, velocity_x = 0, velocity_y = 0):
        self.x = x # Các thông số của obj
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        
        self.image = pygame.image.load(image_path).convert_alpha() # Ảnh của obj
        self.width = self.image.get_width() if width == 0 else width # Nếu có kích thước tuỳ chỉnh thì theo, không thì kích thước như file ban đầu
        self.height = self.image.get_height() if height == 0 else height  # Nếu có kích thước tuỳ chỉnh thì theo, không thì kích thước như file ban đầu
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def reset_image(self, image_path, width = 0, height = 0): # Reset ảnh của obj
        self.image = pygame.image.load(image_path).convert_alpha()
        self.width = self.image.get_width() if width == 0 else width
        self.height = self.image.get_height() if height == 0 else height
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def print_image(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def is_out_of_the_map(self, right = True, left = True, bottom = True, top = True): # CHECK CÓ RA KHỎI HOÀN TOÀN MAP KHÔNG
        if left and self.x + self.width <= 0:
            return True
        elif right and self.x >= WIDTH:
            return True
        elif top and self.y + self.height <= 0:
            return True
        elif bottom and self.y >= HEIGHT - ground_height:
            return True
        return False

    def is_collided_with_the_map(self, right = True, left = True, bottom = True, top = True): # CHECK CÓ VA CHẠM RÌA MAP HAY KHÔNG 
        if left and self.x <= 0:
            return True
        elif right and self.x + self.width >= WIDTH:
            return True
        elif top and self.y <= 0:
            return True
        elif bottom and self.y + self.height >= HEIGHT - ground_height:
            return True
        return False
    
    def move(self): # DI CHUYỂN
        self.x += self.velocity_x * game_speed # di chuyển theo chiều Ox
        self.y += self.velocity_y * game_speed # di chuyển theo chiều Oy

class story_character(obj):
    def __init__(self, name = None, image_path = None, dialogue = "", font = FONT["MONTESRRAT_REGULAR"], x = 0, y = 0, width = 0, height = 0, velocity_x = 0, velocity_y = 0):
        super().__init__(image_path, x, y, width, height, velocity_x, velocity_y)
        self.name = name
        self.dialogue = dialogue
        self.font = font

class frontground(obj): # FRONTGROUND: LÀ VẬT MÀ CHIM CÓ THỂ TƯƠNG TÁC VA CHẠM (CẦN TẠO MASK)
    def __init__(self, image_path, x = 0, y = 0, width = 0, height = 0, velocity_x = 0, velocity_y = 0):
        super().__init__(image_path, x, y, width, height, velocity_x, velocity_y)
        self.hitbox = pygame.mask.from_surface(self.image)

class character(frontground): # NHẬT VẬT: FLAPPY BIRD
    def __init__(self, normal_image, jump_image_1, jump_image_2, collecting_image_1, collecting_image_2, collecting_image_3, x = 0, y = 0, width = 0, height = 0, velocity_x = 0, velocity_y = 0, jump_power = 0, gravity = 0, beam_time_1 = 0, beam_time_2 = 0, beam_time_3 = 0):
        super().__init__(normal_image, x, y, width, height, velocity_x, velocity_y)
        self.gravity = gravity # gia tốc trọng trường
        self.jump_power = jump_power # v[0]
        self.normal_image = normal_image
        self.jump_image_1 = jump_image_1
        self.jump_image_2 = jump_image_2
        self.collecting_image_1 = collecting_image_1
        self.collecting_image_2 = collecting_image_2 
        self.collecting_image_3 = collecting_image_3 
        self.collecting_range = pygame.mask.from_surface(pygame.image.load(self.collecting_image_2)) # hitbox của beam
        self.is_collecting = False # đang sử dụng beam hay không
        self.beam_time = 0 # thời gian sử dụng beam
        self.beam_time_1 = beam_time_1 # Thời gian hết frame nhân vật đang nạp đạn (milisecond) từ lúc bấm nút
        self.beam_time_2 = beam_time_2 # Thời gian hết frame nhân vật đang bắn (milisecond) từ lúc bấm nút
        self.beam_time_3 = beam_time_3 # Thời gian hết frame đạn tan rã (milisecond) từ lúc bấm nút


    def jump(self): # THAO TÁC NHẢY
        pygame.mixer.Sound.play(jumping_sound)
        self.velocity_y = self.jump_power

    def die(self): # ANIMATION CỦA CON CHIM KHI GAME OVER
        self.jump()

    def act_at_menu(self): # ANIMATION CỦA CON CHIM KHI Ở MENU
        if self.y > HEIGHT // 2:
            self.jump()

    def update_image(self): # CẬP NHẬT image THEO TỐC ĐỘ
        if self.is_collecting:
            if self.beam_time < self.beam_time_1:
                self.image = pygame.image.load(self.collecting_image_1)
            elif self.beam_time < self.beam_time_2:
                self.image = pygame.image.load(self.collecting_image_2)
            elif self.beam_time < self.beam_time_3:
                self.image = pygame.image.load(self.collecting_image_3)
            else:
                self.is_collecting = False
                self.image = pygame.image.load(self.normal_image)
        elif self.velocity_y < self.jump_power // 2:
            self.image = pygame.image.load(self.jump_image_1)
        elif self.velocity_y < 0:
            self.image = pygame.image.load(self.jump_image_2)
        else:
            self.image = pygame.image.load(self.normal_image)

    def update_velocity(self): # UPDATE VẬN TỐC THEO GRAVITY
        self.velocity_y += self.gravity * game_speed

    def reset_position(self):
        self.x = character_x
        self.y = character_y

    def is_shoting(self):
        return self.is_collecting and self.beam_time < self.beam_time_2 and self.beam_time >= self.beam_time_1

    def update_beam_time(self):
        if not self.is_collecting:
            self.beam_time = 0
        else:
            self.beam_time += miliseconds_per_frame * game_speed

    def move(self):
        self.update_velocity()
        self.update_beam_time()
        self.update_image()
        super().move()

class coin(frontground): # NHỮNG VẬT CHARACTER CÓ THỂ THU THẬP: BÒ
    def __init__(self, image_path, x = 0, y = 0, width = 0, height = 0, velocity_x = 0, velocity_y = 0, coin_accel_y_when_it_is_disappearing = 0, coin_angular_velocity_when_it_is_disappearing = 0, coin_accel_width_when_it_is_disappearing = 0, coin_accel_height_when_it_is_disappearing = 0):
        super().__init__(image_path, x, y, width, height, velocity_x, velocity_y)
        self.image_path = image_path
        self.is_scored = False
        self.coin_accel_y_when_it_is_disappearing = coin_accel_y_when_it_is_disappearing
        self.coin_angular_velocity_when_it_is_disappearing = coin_angular_velocity_when_it_is_disappearing
        self.coin_accel_width_when_it_is_disappearing = coin_accel_width_when_it_is_disappearing
        self.coin_accel_height_when_it_is_disappearing = coin_accel_height_when_it_is_disappearing
        self.velocity_width = 0
        self.velocity_height = 0
        self.original_width = self.width
        self.original_height = self.height

    def reset_position(self, x, y):
        self.is_scored = False
        self.x = x
        self.y = y
        self.width = self.original_width
        self.height = self.original_height
        self.velocity_y = 0
        self.velocity_height = 0
        self.velocity_width = 0
        self.reset_image(self.image_path, self.original_width, self.original_height)

    def disappear(self):
        self.velocity_y += self.coin_accel_y_when_it_is_disappearing
        self.velocity_width += self.coin_accel_width_when_it_is_disappearing
        self.velocity_height += self.coin_accel_height_when_it_is_disappearing
        self.width = max(self.velocity_width + self.width, 0)
        self.height = max(self.velocity_height + self.height, 0)
        self.image = pygame.transform.rotate(self.image, self.coin_angular_velocity_when_it_is_disappearing)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def move(self):
        if self.is_scored:
            self.disappear()
        super().move()

class obstacle(frontground): # CHƯỚNG NGẠI VẬT: ỐNG CỐNG
    def __init__(self, image_path, x = 0, y = 0, width = 0, height = 0, velocity_x = 0, velocity_y = 0, give_score = False):
        super().__init__(image_path, x, y, width, height, velocity_x, velocity_y)

        self.give_score = give_score # obstacle này khi vượt qua có cộng điểm hay không / chỉ định đây là cống trên hay dưới: True = trên, False = dưới
        self.is_scored = False # Đã được tính điểm hay chưa

        self.reset_position(x, y) # khởi tạo vị trí (x,y) của ống trên và dưới

    def reset_position(self, x, y): # Khởi tạo chỉ số vị trí và bật chế độ tính điểm của các ống cống
        self.is_scored = False if self.give_score else True
        self.x = x # vị trí reset của ống cống
        self.y = y # Gen random độ cao thấp của ống cống

class ground(frontground): # MẶT ĐẤT
    def __init__(self, image_path, x = 0, y = 0, width = 0, height = 0, velocity_x = 0, velocity_y = 0):
        super().__init__(image_path, x, y, width, height, velocity_x, velocity_y)

    def reset_position(self):
        self.x += self.width * 2 # x2 để nó ở ngay sau ảnh ground số 2

class background(obj): # BACKGROUND: LÀ VẬT MÀ CHIM KHÔNG THỂ TƯƠNG TÁC (KHÔNG CẦN TẠO MASK)
    def __init__(self, image_path, x = 0, y = 0, width = 0, height = 0, velocity_x = 0, velocity_y = 0):
        super().__init__(image_path, x, y, width, height, velocity_x, velocity_y)

    def reset_position(self): # Khởi tạo lại vị trí
        self.x += self.width * 2 # x2 để xuất hiện ngay sau image ảnh thứ 2

def draw_dialogue_box(obj): # HỘP THOẠI HIỆN THỊ HỘI THOẠI
    obj.print_image(screen)

    pygame.draw.rect(screen, COLOR["ROYAL_BLUE"], (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height))  # Vẽ hộp thoại
    pygame.draw.rect(screen, COLOR["WHITE"], (dialogue_box_x, dialogue_box_y, dialogue_box_width, dialogue_box_height), 3)  # Viền hộp thoại
    
    character_text = obj.font.render(obj.name + ":", True, COLOR["WHITE"])
    screen.blit(character_text, (dialogue_x, dialogue_y))

    # Xử lý văn bản xuống dòng
    lines = wrap_text(obj.dialogue, obj.font)
    
    y_offset = dialogue_y + 40  # Vị trí hiển thị dòng đầu tiên
    for line in lines:
        line_render = obj.font.render(line, True, COLOR["WHITE"])
        screen.blit(line_render, (60, y_offset))
        y_offset += 30  # Khoảng cách giữa các dòng

def random_obstacle_height(): # Random vị trí của 2 cái ống trên và dưới
    y_top = random.uniform(- (obstacle_height - 0.15 * HEIGHT), - (obstacle_height - 0.45 * HEIGHT)) # ống cống trên dài từ 15% - 45% màn
    y_bottom = y_top + obstacle_height + distance_gap # ống cống dưới cách ống trên một khoảng = distance_gap
    return (y_top, y_bottom)

def random_coin_position(): # Vị trí random của coin giữa 2 obstacles
    x_position_cap = distance_between_obstacles - coin_width # Vị trí coin.x tối đa  
    return random.uniform(0.2 * x_position_cap, 0.8 * x_position_cap)

def update_game_speed(): # Cập nhật tốc độ game theo số điểm hiện tại (tỉ lệ thuận)
    return min(game_speed_accel * score + min_game_speed, max_game_speed)

def draw_text(text = "Hello, world!", font = FONT["MARIO_SMALL"], color = COLOR["BLACK"], x = WIDTH // 2, y = HEIGHT // 2): # VẼ CHỮ
    """Vẽ chữ lên màn hình"""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def wrap_text(text = "Hello, world!", font = FONT["MONTESRRAT_REGULAR"]):
    words = text.split()  # Tách từng từ
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= dialogue_max_width:
            current_line = test_line
        else:
            lines.append(current_line)  # Xuống dòng
            current_line = word + " "

    lines.append(current_line)  # Thêm dòng cuối cùng
    return lines

def is_A_to_the_left_of_B(x_a, x_b): # KIỂM TRA A CÓ BÊN TRÁI B KHÔNG
    if x_a < x_b:
        return True
    return False

def is_collided(a_x, a_y, a_hitbox, b_x, b_y, b_hitbox): # KIỂM TRA VA CHẠM GIỮA 2 OBJ (MASK CỦA ẢNH)
    offset = (a_x - b_x, a_y - b_y) # Lấy vị trí tương đối của player so với ống cống
    return b_hitbox.overlap(a_hitbox, offset) is not None # True = có va chạm

def init_character(normal_image, jump_image_1 = None, jump_image_2 = None, collecting_image_1 = None, colecting_image_2 = None, collecting_image_3 = None):
    return character(normal_image, jump_image_1, jump_image_2, collecting_image_1, colecting_image_2, collecting_image_3, character_x, character_y, character_width, character_height, 0, 0, jump_power, gravity, beam_time_1, beam_time_2, beam_time_3)
    
def init_ground_list(my_list): # TẠO image LIST CỦA MẶT ĐẤT
    my_list.clear()
    
    ground1 = ground(ground_image, 0, HEIGHT - ground_height, ground_width, ground_height, ground_velocity_x) # ground image 1
    ground2 = ground(ground_image, ground_width, HEIGHT - ground_height, ground_width, ground_height, ground_velocity_x) # ground image 2
    my_list.append(ground1)
    my_list.append(ground2)

def init_obstacle_list(my_list): # TẠO DANH SÁCH CHƯỚNG NGẠI VẬT: ỐNG CỐNG
    my_list.clear()

    for i in range(number_of_obstacle): # tạo danh sách obstacle
        (y_top, y_bottom) = random_obstacle_height()
        my_list.insert(0, obstacle(pipe_top_image, x_first_spawn + (obstacle_width + distance_between_obstacles) * i, y_top, obstacle_width, obstacle_height, obstacle_velocity_x, 0, True))
        my_list.insert(0, obstacle(pipe_bottom_image, x_first_spawn + (obstacle_width + distance_between_obstacles) * i, y_bottom, obstacle_width, obstacle_height, obstacle_velocity_x, 0, False))

def init_coin_list(my_list):# TẠO DANH SÁCH COIN: Bò
    my_list.clear()
    
    for i in range(number_of_coin): # tạo danh sách coin
        coin_x = random_coin_position() + x_first_spawn + obstacle_width + (obstacle_width + distance_between_obstacles) * i
        my_list.insert(0, coin(coin_image_1, coin_x, coin_y_when_it_resets_position, coin_width, coin_height, coin_velocity_x, 0, coin_accel_y_when_it_is_disappearing, coin_angular_velocity_when_it_is_disappearing, coin_accel_width_when_it_is_disappearing, coin_accel_height_when_it_is_disappearing))

def init_background_list(my_list): # TẠO DANH SÁCH image PHẦN BACKGROUND
    my_list.clear()
    
    background_stato = background(background_stato_image, 0, 0, WIDTH, HEIGHT, 0, 0) # Phần background đứng yên
    background_roto1 = background(background_roto_image, 0, 0, WIDTH, HEIGHT - ground_height, background_velocity_x) # Phần background loop image 1
    background_roto2 = background(background_roto_image, WIDTH, 0, WIDTH, HEIGHT - ground_height, background_velocity_x) # Phần background loop image 2
    my_list[:] = [background_stato, background_roto1, background_roto2]

def init_obj(ground_list = False, obstacle_list = False, coin_list = False, background_list = False): # TẠO DANH SÁCH image obj
    if type(ground_list) == list:
        init_ground_list(ground_list)
    if type(obstacle_list) == list: 
        init_obstacle_list(obstacle_list)
    if type(coin_list) == list:
        init_coin_list(coin_list)
    if type(background_list) == list:
        init_background_list(background_list)

def init_story_character(name = "world", image_path = None, dialogue = "Hello, world!", font = FONT["MONTESRRAT_REGULAR"]): # TẠO NHÂN VẬT TRONG STORY
    return story_character(name, image_path, dialogue, font, story_character_x, story_character_y, story_character_width, story_character_height, 0, 0)

def game_playing_easy():
    global score, game_speed # liên kết score => cập nhật best_score
    y_top, y_bottom = 0, 0
    pygame.mixer.music.play()
    
    while True:
        for background in background_list: # IN BACKGROUND
            background.move()
            background.print_image(screen)
            
            if background.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ra ngoài map
                background.reset_position()

        if score >= normal_mode_score_requirement:
            current_game_mode = "game_playing_normal"
            return current_game_mode

        for obstacle in obstacle_list: # IN OBSTACLE
            obstacle.move()
            obstacle.print_image(screen)
            
            if obstacle.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ngoài map
                if obstacle.give_score: # Nếu ống trên
                    obstacle.reset_position(obstacle_x_when_it_resets_position, y_top) # vị trí ống trên

                else:
                    (y_top, y_bottom) = random_obstacle_height() # thì random chiều cao cho cặp ống trên dưới mới này
                    obstacle.reset_position(obstacle_x_when_it_resets_position, y_bottom) # vị trí ống dưới

            if is_collided(current_character.x, current_character.y, current_character.hitbox, obstacle.x, obstacle.y, obstacle.hitbox): # Game over nếu có va chạm
                current_character.die()
                return "game_over"

            if not obstacle.is_scored and is_A_to_the_left_of_B(obstacle.x, current_character.x): # CẬP NHẬT ĐIỂM
                pygame.mixer.Sound.play(scoring_sound)
                score += 1
                obstacle.is_scored = True

        for ground in ground_list: # IN GROUND
            ground.move()
            ground.print_image(screen)
            
            if ground.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ngoài map
                ground.reset_position()

        if current_character.is_collided_with_the_map(False, False, True, True): # CHECK GAME OVER KHI CHIM BAY NGOÀI MAP
            current_character.die()
            return "game_over"

        current_character.move() # Cập nhật vị trí
        current_character.print_image(screen) # IN CHARACTER

        draw_text(str(score), FONT["MARIO_BIG"], COLOR["ROYAL_BLUE"], WIDTH // 2, HEIGHT // 2 - 100) # IN ĐIỂM

        for event in pygame.event.get(): # CHECK THAO TÁC
            if event.type == pygame.QUIT:
                return ""
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # chuột trái
                    current_character.jump()

                elif event.button == 3: # chuột phải
                    if not current_character.is_collecting:
                        current_character.is_collecting = True
                        pygame.mixer.Sound.play(collecting_sound)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return ""
                
                elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    current_character.jump()

                elif event.key == pygame.K_DOWN:
                    if not current_character.is_collecting:
                        current_character.is_collecting = True
                        pygame.mixer.Sound.play(collecting_sound)

        pygame.display.flip() # CẬP NHẬT MÀN HÌNH
        pygame.time.Clock().tick(FPS)

def game_playing_normal():
    global score, game_speed, first_time_playing_normal # liên kết score => cập nhật best_score
    y_top, y_bottom = 0, 0
    pygame.mixer.music.play()
    
    dialogues_main_story = [
            init_story_character("Bá Duy", ba_duy_image, "Ê, game chạy nhanh hơn thì phải nè."), # first_time_playing_normal = True
    init_story_character("Bá Duy", ba_duy_image, f"Nhanh hơn tức là cơ hội đến sớm hơn để đạt {hard_mode_score_requirement} điểm đó cưng."),
    init_story_character("Bá Duy", ba_duy_image, f"Rồi chơi tới luôn. Lấy cái {hard_mode_score_requirement} điểm cho anh đi."),
    ]

    dialogues = []

    if first_time_playing_normal:
        dialogues = dialogues_main_story
        first_time_playing_normal = False
    
    # Chỉ số hội thoại hiện tại
    is_there_dialogue = len(dialogues) > 0
    if is_there_dialogue:
        dialogue_index = 0
        text_full = dialogues[dialogue_index].dialogue  # Toàn bộ câu cần hiển thị
        char_index = 0  # Chỉ số ký tự hiện tại
        last_update = pygame.time.get_ticks()
        dialogue_done_time = None  # Biến lưu thời gian hoàn thành hội thoại

    while True:
        game_speed = update_game_speed() # Tặng tốc game dần theo score

        for background in background_list: # IN BACKGROUND
            background.move()
            background.print_image(screen)
            
            if background.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ra ngoài map
                background.reset_position()

        if score >= hard_mode_score_requirement:
            current_game_mode = "game_playing_hard"
            return current_game_mode

        for obstacle in obstacle_list: # IN OBSTACLE
            obstacle.move()
            obstacle.print_image(screen)
            
            if obstacle.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ngoài map
                if obstacle.give_score: # Nếu ống trên
                    obstacle.reset_position(obstacle_x_when_it_resets_position, y_top) # vị trí ống trên

                else:
                    (y_top, y_bottom) = random_obstacle_height() # thì random chiều cao cho cặp ống trên dưới mới này
                    obstacle.reset_position(obstacle_x_when_it_resets_position, y_bottom) # vị trí ống dưới

            if is_collided(current_character.x, current_character.y, current_character.hitbox, obstacle.x, obstacle.y, obstacle.hitbox): # Game over nếu có va chạm
                current_character.die()
                return "game_over"

            if not obstacle.is_scored and is_A_to_the_left_of_B(obstacle.x, current_character.x): # CẬP NHẬT ĐIỂM
                pygame.mixer.Sound.play(scoring_sound)
                score += 1
                obstacle.is_scored = True

        for ground in ground_list: # IN GROUND
            ground.move()
            ground.print_image(screen)
            
            if ground.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ngoài map
                ground.reset_position()

        if current_character.is_collided_with_the_map(False, False, True, True): # CHECK GAME OVER KHI CHIM BAY NGOÀI MAP
            current_character.die()
            return "game_over"

        current_character.move() # Cập nhật vị trí
        current_character.print_image(screen) # IN CHARACTER

        draw_text(str(score), FONT["MARIO_BIG"], COLOR["ROYAL_BLUE"], WIDTH // 2, HEIGHT // 2 - 100) # IN ĐIỂM

        # HIỆN THỊ HỘP THOẠI
        current_time = pygame.time.get_ticks()
        # Nếu chữ đã hiển thị hết, bắt đầu đếm thời gian trước khi chuyển tiếp
        if is_there_dialogue:
            if char_index == len(text_full) and dialogue_done_time is None:
                dialogue_done_time = current_time  # Lưu thời gian hoàn tất hội thoại

            # Sau khi hiện xong, chờ một lúc rồi chuyển tiếp hội thoại
            if dialogue_done_time and current_time - dialogue_done_time > DIALOGUE_DELAY:
                if dialogue_index < len(dialogues) - 1:
                    dialogue_index += 1
                    text_full = dialogues[dialogue_index].dialogue
                    char_index = 0
                    dialogue_done_time = None  # Reset thời gian hoàn thành hội thoại
                else:
                    is_there_dialogue = False

            if char_index < len(text_full) and current_time - last_update > TEXT_SPEED:
                char_index += 1
                last_update = current_time
                dialogues[dialogue_index].dialogue = text_full[:char_index]
            
            # hiển thị hội thoại
            if is_there_dialogue:
                draw_dialogue_box(dialogues[dialogue_index])

        for event in pygame.event.get(): # CHECK THAO TÁC
            if event.type == pygame.QUIT:
                return ""
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # chuột trái
                    current_character.jump()

                elif event.button == 3: # chuột phải
                    if not current_character.is_collecting:
                        current_character.is_collecting = True
                        pygame.mixer.Sound.play(collecting_sound)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return ""
                
                elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    current_character.jump()

                elif event.key == pygame.K_DOWN:
                    if not current_character.is_collecting:
                        current_character.is_collecting = True
                        pygame.mixer.Sound.play(collecting_sound)

        pygame.display.flip() # CẬP NHẬT MÀN HÌNH
        pygame.time.Clock().tick(FPS)
 
def game_playing_hard():
    global score, game_speed, first_time_playing_hard, first_time_collecting_10_coins, first_time_collecting_20_coins, total_coins # liên kết score => cập nhật best_score
    y_top, y_bottom = 0, 0
    is_lack_of_coin = False

    pygame.mixer.music.play()

    dialogues_first_time_playing_hard = [
        init_story_character("Bá Duy", ba_duy_image, "Ê, có mấy em bò ở dưới kìa... HÚP LẸ!"), # first_time_playing_hard = True
        init_story_character("Bá Duy", ba_duy_image, "Bấm mũi tên xuống hoặc chuột phải để vét cạn."),
        init_story_character("Bá Duy", ba_duy_image, "Anh vét 10 em bò rồi đấy, còn lại 10 em nữa nhường mấy đứa tất."),
        init_story_character("Bá Duy", ba_duy_image, "Từ giờ trở đi chỉ có bò mới làm điểm tăng lên được."),
    ]

    dialogues = []

    if first_time_playing_hard:
        dialogues = dialogues_first_time_playing_hard
        first_time_playing_hard = False

    # Chỉ số hội thoại hiện tại
    is_there_dialogue = len(dialogues) > 0
    if is_there_dialogue:
        dialogue_index = 0
        text_full = dialogues[dialogue_index].dialogue  # Toàn bộ câu cần hiển thị
        char_index = 0  # Chỉ số ký tự hiện tại
        last_update = pygame.time.get_ticks()
        dialogue_done_time = None  # Biến lưu thời gian hoàn thành hội thoại

    while True:
        game_speed = update_game_speed() # Tặng tốc game dần theo score

        for background in background_list: # IN BACKGROUND
            background.move()
            background.print_image(screen)
            
            if background.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ra ngoài map
                background.reset_position()

        for obstacle in obstacle_list: # IN OBSTACLE
            obstacle.move()
            obstacle.print_image(screen)
            
            if obstacle.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ngoài map
                if is_lack_of_coin: # Cập nhật lại vị trí coin nếu nó bị nhặt / mất (vị trí ở ngay giữa 2 obstacles)
                    coin_x = random_coin_position() + obstacle_x_when_it_resets_position + obstacle_width
                    is_lack_of_coin = False
                    the_coin_that_need_to_be_reset_position.reset_position(coin_x, coin_y_when_it_resets_position)
                
                if obstacle.give_score: # Nếu ống trên
                    obstacle.reset_position(obstacle_x_when_it_resets_position, y_top) # vị trí ống trên
                
                else:
                    (y_top, y_bottom) = random_obstacle_height() # thì random chiều cao cho cặp ống trên dưới mới này
                    obstacle.reset_position(obstacle_x_when_it_resets_position, y_bottom) # vị trí ống dưới

            if is_collided(current_character.x, current_character.y, current_character.hitbox, obstacle.x, obstacle.y, obstacle.hitbox): # Game over nếu có va chạm
                current_character.die()
                return "game_over"

            if not obstacle.is_scored and is_A_to_the_left_of_B(obstacle.x, current_character.x): # CẬP NHẬT ĐIỂM
                obstacle.is_scored = True

        for ground in ground_list: # IN GROUND
            ground.move()
            ground.print_image(screen)
            
            if ground.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ngoài map
                ground.reset_position()

        if current_character.is_collided_with_the_map(False, False, True, True): # CHECK GAME OVER KHI CHIM BAY NGOÀI MAP
            current_character.die()
            return "game_over"
       
        current_character.move() # Cập nhật vị trí
        current_character.print_image(screen) # IN CHARACTER

        for coin in coin_list:
            coin.move()
            coin.print_image(screen)

            if coin.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ngoài map
                is_lack_of_coin = True
                the_coin_that_need_to_be_reset_position = coin
                
            if current_character.is_shoting() and not coin.is_scored and is_collided(coin.x, coin.y, coin.hitbox, current_character.x, current_character.y, current_character.collecting_range):
                coin.is_scored = True
                is_lack_of_coin = True
                the_coin_that_need_to_be_reset_position = coin
                pygame.mixer.Sound.play(cow_sound)
                score += 1
                total_coins += 1

            if is_collided(coin.x, coin.y, coin.hitbox, current_character.x, current_character.y, current_character.hitbox):
                current_character.die()
                return "game_over"

        draw_text(str(score), FONT["MARIO_BIG"], COLOR["ROYAL_BLUE"], WIDTH // 2, HEIGHT // 2 - 100) # IN ĐIỂM

        if total_coins >= 1 and first_time_collecting_10_coins:
            return "second_conversation"
        if total_coins >= 2 and first_time_collecting_20_coins:
            return "third_conversation"

        # HIỆN THỊ HỘP THOẠI
        if is_there_dialogue:
            current_time = pygame.time.get_ticks()
            # Nếu chữ đã hiển thị hết, bắt đầu đếm thời gian trước khi chuyển tiếp
            if char_index == len(text_full) and dialogue_done_time is None:
                dialogue_done_time = current_time  # Lưu thời gian hoàn tất hội thoại

            # Sau khi hiện xong, chờ một lúc rồi chuyển tiếp hội thoại
            if dialogue_done_time and current_time - dialogue_done_time > DIALOGUE_DELAY:
                if dialogue_index < len(dialogues) - 1:
                    dialogue_index += 1
                    text_full = dialogues[dialogue_index].dialogue
                    char_index = 0
                    dialogue_done_time = None  # Reset thời gian hoàn thành hội thoại
                else:
                    is_there_dialogue = False

            if char_index < len(text_full) and current_time - last_update > TEXT_SPEED:
                char_index += 1
                last_update = current_time
                dialogues[dialogue_index].dialogue = text_full[:char_index]
            
            # hiển thị hội thoại
            if is_there_dialogue:
                draw_dialogue_box(dialogues[dialogue_index])

        for event in pygame.event.get(): # CHECK THAO TÁC
            if event.type == pygame.QUIT:
                return ""
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # chuột trái
                    current_character.jump()

                elif event.button == 3: # chuột phải
                    if not current_character.is_collecting:
                        current_character.is_collecting = True
                        pygame.mixer.Sound.play(collecting_sound)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return ""
                
                elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    current_character.jump()

                elif event.key == pygame.K_DOWN:
                    if not current_character.is_collecting:
                        current_character.is_collecting = True
                        pygame.mixer.Sound.play(collecting_sound)

        pygame.display.flip() # CẬP NHẬT MÀN HÌNH
        pygame.time.Clock().tick(FPS)

def game_menu():
    global score, game_speed, current_game_mode, first_time_playing_easy

    init_obj(ground_list, obstacle_list, coin_list, background_list)
    current_character.reset_position()
    
    score = 0 # reset score
    game_speed = min_game_speed # reset speed

    dialogues_main_story = [
        init_story_character("Bá Duy", ba_duy_image, "Đạt 10 điểm xem trình cái nào?"),
    ]
    
    dialogues_chicken = [
        init_story_character("Bá Duy", ba_duy_image, "Gà thế!"),
        init_story_character("Bá Duy", ba_duy_image, "Có cái UFO cũng không lái được thì sao lái mấy chị đây?"),
        init_story_character("Bá Duy", ba_duy_image, "Nhìn mà chán."),
        init_story_character("Bá Duy", ba_duy_image, "Ủa thứ Tư này có đá banh không mấy đứa?"),
        init_story_character("Bá Duy", ba_duy_image, "Skibidi dop dop dop yes yes :)"),
    ]

    dialogues = []

    if first_time_playing_easy:
        dialogues = dialogues_main_story
        first_time_playing_easy = False
    else:
        dialogues = dialogues_chicken

    # Chỉ số hội thoại hiện tại
    dialogue_index = 0
    text_full = dialogues[dialogue_index].dialogue  # Toàn bộ câu cần hiển thị
    char_index = 0  # Chỉ số ký tự hiện tại
    last_update = pygame.time.get_ticks()
    dialogue_done_time = None  # Biến lưu thời gian hoàn thành hội thoại

    while True:
        for background in background_list: # IN BACKGROUND
            background.move() 
            background.print_image(screen)
            
            if background.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ra ngoài map
                background.reset_position()

        for ground in ground_list: # IN GROUND
            ground.move()
            ground.print_image(screen)
            
            if ground.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ngoài map
                ground.reset_position()

        current_character.move() # Cập nhật vị trí
        current_character.act_at_menu() # animation ở menu
        current_character.print_image(screen) # IN CHARACTER

        draw_text("FLAPPY BIRD", FONT["MARIO_BIG"], COLOR["BROWN"], WIDTH // 2, HEIGHT // 2 - 100) # IN CHỮ Ở MENU
        # draw_text("PRESS SPACE TO PLAY", FONT["MARIO_SMALL"], COLOR["MIDNIGHT_BLUE"], WIDTH // 2, HEIGHT // 2 + 100)
        # draw_text(hint, FONT["MARIO_SMALL"], COLOR["MIDNIGHT_BLUE"], WIDTH // 2, HEIGHT // 2 + 150)

        # HIỆN THỊ HỘP THOẠI
        current_time = pygame.time.get_ticks()
        # Nếu chữ đã hiển thị hết, bắt đầu đếm thời gian trước khi chuyển tiếp
        if char_index == len(text_full) and dialogue_done_time is None:
            dialogue_done_time = current_time  # Lưu thời gian hoàn tất hội thoại

        # Sau khi hiện xong, chờ một lúc rồi chuyển tiếp hội thoại
        if dialogue_done_time and current_time - dialogue_done_time > DIALOGUE_DELAY:
            if dialogue_index < len(dialogues) - 1:
                dialogue_index += 1
                text_full = dialogues[dialogue_index].dialogue
                char_index = 0
                dialogue_done_time = None  # Reset thời gian hoàn thành hội thoại

        if char_index < len(text_full) and current_time - last_update > TEXT_SPEED:
            char_index += 1
            last_update = current_time
            dialogues[dialogue_index].dialogue = text_full[:char_index]
        
        # hiển thị hội thoại
        draw_dialogue_box(dialogues[dialogue_index])

        for event in pygame.event.get(): # CHECK THAO TÁC
            if event.type == pygame.QUIT:
                return ""
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # chuột trái
                    current_character.jump()

                elif event.button == 3: # chuột phải
                    if not current_character.is_collecting:
                        current_character.is_collecting = True
                        pygame.mixer.Sound.play(collecting_sound)

                return current_game_mode

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return ""
                
                elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    current_character.jump()

                elif event.key == pygame.K_DOWN:
                    if not current_character.is_collecting:
                        current_character.is_collecting = True
                        pygame.mixer.Sound.play(collecting_sound)

                return current_game_mode

        pygame.display.flip() # CẬP NHẬT MÀN HÌNH
        pygame.time.Clock().tick(FPS)

def game_over():
    global score, game_speed, best_score # liên kết score => cập nhật best_score; game_speed
    best_score = max(score, best_score)

    pygame.mixer.Sound.play(game_over_sound) # Âm thanh game over
    pygame.mixer.music.fadeout(2000) # tắt nhạc nền

    while True:
        for background in background_list: # IN BACKGROUND
            background.print_image(screen)

        for obstacle in obstacle_list: # IN OBSTACLE
            obstacle.print_image(screen)

        for ground in ground_list: # IN GROUND
            ground.print_image(screen)

        current_character.move() # Cập nhật vị trí nhân vật
        current_character.print_image(screen) # IN CHARACTER

        menu_game_over.print_image(screen) # IN MENU GAME OVER
        draw_text(f"{score}", FONT["MARIO_BIG"],  COLOR["ORANGE"], WIDTH // 2, HEIGHT // 2 - 40)
        draw_text(f"{best_score}", FONT["MARIO_BIG"],  COLOR["ORANGE"], WIDTH // 2, HEIGHT // 2 + 70)

        for event in pygame.event.get(): # CHECK THAO TÁC
            if event.type == pygame.QUIT:
                return ""
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return ""

                if event.key == pygame.K_SPACE: # Trở về menu
                    return "game_menu"

        pygame.display.flip() # CẬP NHẬT MÀN HÌNH
        pygame.time.Clock().tick(FPS)

def first_conversation():
    global score, game_speed

    init_obj(ground_list, obstacle_list, coin_list, background_list)
    current_character.reset_position()
    
    score = 0 # reset score
    game_speed = min_game_speed # reset speed

    dialogues = [
        init_story_character("Bá Duy", ba_duy_image, "Hello mấy đứa!"),
        init_story_character("Bá Duy", ba_duy_image, "Nhân dịp thầy Hùng tặng 20 triệu cái laptop..."),
        init_story_character("Bá Duy", ba_duy_image, "Thầy cũng đem theo con hàng 43 cái UFO sang xịn mịn."),
        init_story_character("Nguyễn Thanh Hùng", nguyen_thanh_hung_image, "Chào các anh các chị."),
        init_story_character("Nguyễn Thanh Hùng", nguyen_thanh_hung_image, "Tôi chỉ hướng dẫn sơ qua thôi."),
        init_story_character("Nguyễn Thanh Hùng", nguyen_thanh_hung_image, "À thôi."),
        init_story_character("Nguyễn Thanh Hùng", nguyen_thanh_hung_image, "Cái game Flappy Bird này ai mà chả biết."),
        init_story_character("Nguyễn Thanh Hùng", nguyen_thanh_hung_image, "Tôi bảo rồi... tự học là tốt nhất!"),
        init_story_character("Nguyễn Thanh Hùng", nguyen_thanh_hung_image, "Bây giờ thầy Duy sẽ quản lớp."),
        init_story_character("Nguyễn Thanh Hùng", nguyen_thanh_hung_image, "Tôi bận dẫn quân KHTN đi ICPC rồi."),
        init_story_character("Bá Duy", ba_duy_image, "Ủa thầy đi rồi à?"),
        init_story_character("Bá Duy", ba_duy_image, "Vậy thì... vô game nè!"),
    ]

    # Chỉ số hội thoại hiện tại
    dialogue_index = 0
    text_full = dialogues[dialogue_index].dialogue  # Toàn bộ câu cần hiển thị
    char_index = 0  # Chỉ số ký tự hiện tại
    last_update = pygame.time.get_ticks()
    dialogue_done_time = None  # Biến lưu thời gian hoàn thành hội thoại

    while True:
        for background in background_list: # IN BACKGROUND
            background.move() 
            background.print_image(screen)
            
            if background.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ra ngoài map
                background.reset_position()

        for ground in ground_list: # IN GROUND
            ground.move()
            ground.print_image(screen)
            
            if ground.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ngoài map
                ground.reset_position()

        current_time = pygame.time.get_ticks()
        # Nếu chữ đã hiển thị hết, bắt đầu đếm thời gian trước khi chuyển tiếp
        if char_index == len(text_full) and dialogue_done_time is None:
            dialogue_done_time = current_time  # Lưu thời gian hoàn tất hội thoại

        # Sau khi hiện xong, chờ một lúc rồi chuyển tiếp hội thoại
        if dialogue_done_time and current_time - dialogue_done_time > DIALOGUE_DELAY:
            if dialogue_index < len(dialogues) - 1:
                dialogue_index += 1
                text_full = dialogues[dialogue_index].dialogue
                char_index = 0
                dialogue_done_time = None  # Reset thời gian hoàn thành hội thoại
            else:
                return "game_menu"

        if char_index < len(text_full) and current_time - last_update > TEXT_SPEED:
            char_index += 1
            last_update = current_time
            dialogues[dialogue_index].dialogue = text_full[:char_index]
        
        # hiển thị hội thoại
        draw_dialogue_box(dialogues[dialogue_index])

        for event in pygame.event.get(): # CHECK THAO TÁC
            if event.type == pygame.QUIT:
                return ""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return ""
                if event.key == pygame.K_SPACE:
                    if char_index < len(text_full):
                        char_index = len(text_full)
                        dialogues[dialogue_index].dialogue = text_full[:char_index]
                    else:
                        if dialogue_index < len(dialogues) - 1:
                            dialogue_index += 1
                            text_full = dialogues[dialogue_index].dialogue
                            char_index = 0
                            dialogue_done_time = None
                        else:
                            return "game_menu"
        pygame.display.flip() # CẬP NHẬT MÀN HÌNH
        pygame.time.Clock().tick(FPS)

def second_conversation():
    global score, game_speed, first_time_collecting_10_coins
    first_time_collecting_10_coins = False

    init_obj(ground_list, obstacle_list, coin_list, background_list)
    current_character.reset_position()

    game_speed = min_game_speed

    pygame.mixer.Sound.play(bomb_sound)

    dialogues = [
        init_story_character("Đỗ Phú Quí", do_phu_qui_image, "Lô mấy nhóc."),
        init_story_character("Bá Duy", ba_duy_image, "Ai đó?"),
        init_story_character("Bá Duy", ba_duy_image, "Ủa khoan... hình như kế bên kia... là thầy Hùng mà!"),
        init_story_character("Nguyễn Thanh Hùng", nguyen_thanh_hung_image, "Mấy đứa ơi, thầy bị Đỗ Phú Quí, J97, Đàm Vĩnh Hưng tấn công..."),
        init_story_character("J97", j97_image, "Hahahahahahaha! *cười kiểu Bến Tre lạnh lùng*", FONT["MONTESRRAT_ITALIC"]),
        init_story_character("J97", j97_image, "Các ngươi hãy đầu hàng trước-"),
        init_story_character("Đỗ Phú Quí", do_phu_qui_image, "PICKLEBALL!!!"),
        init_story_character("Đàm Vĩnh Hưng", dam_vinh_hung_image, "Thầy Hùng của các ngươi quá vip pro đỉnh móc kịch trần, đang dần tranh ánh hào quang của bọn ta!"),
        init_story_character("Đàm Vĩnh Hưng", dam_vinh_hung_image, "Nhưng điều đó không thể thành hiện thực được đâu!!!"),
        init_story_character("Đàm Vĩnh Hưng", dam_vinh_hung_image, "Bởi vì... chúng ta đã có... một buổi đại off fan tại toà tháp đôi ở New York!"),
        init_story_character("Nguyễn Thanh Hùng", nguyen_thanh_hung_image, "Thầy có để lại cho mấy đứa chiếc Boeing 767 ở sân trường..."),
        init_story_character("Nguyễn Thanh Hùng", nguyen_thanh_hung_image, "Mấy đứa hãy dùng nó mà chống lại kẻ ác..."),
        init_story_character("Nguyễn Thanh Hùng", nguyen_thanh_hung_image, "..."),
        init_story_character("Bá Duy", ba_duy_image, "THẦY HÙNG!!??"),
        init_story_character("Bá Duy", ba_duy_image, "Này mấy đứa, không có thời gian để khóc lóc đâu."),
        init_story_character("Bá Duy", ba_duy_image, "Hãy cùng nhau bay lên và đánh bại chúng."),
        init_story_character("Bá Duy", ba_duy_image, "Nhưng mà có vẻ máy bay thiếu nhiên liệu."),
        init_story_character("Bá Duy", ba_duy_image, "À, anh biết rồi! Loại máy bay này dùng sữa làm nhiên liệu."),
        init_story_character("Bá Duy", ba_duy_image, "Chúng ta cần vét thêm 10 em nữa."),
    ]

    # Chỉ số hội thoại hiện tại
    dialogue_index = 0
    text_full = dialogues[dialogue_index].dialogue  # Toàn bộ câu cần hiển thị
    char_index = 0  # Chỉ số ký tự hiện tại
    last_update = pygame.time.get_ticks()
    dialogue_done_time = None  # Biến lưu thời gian hoàn thành hội thoại

    while True:
        for background in background_list: # IN BACKGROUND
            background.move()
            background.print_image(screen)
            
            if background.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ra ngoài map
                background.reset_position()

        for ground in ground_list: # IN GROUND
            ground.move()
            ground.print_image(screen)
            
            if ground.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ngoài map
                ground.reset_position()

        if current_character.is_collided_with_the_map(False, False, True, True): # CHECK GAME OVER KHI CHIM BAY NGOÀI MAP
            current_character.die()
            return "game_over"

        draw_text(str(score), FONT["MARIO_BIG"], COLOR["ROYAL_BLUE"], WIDTH // 2, HEIGHT // 2 - 100) # IN ĐIỂM

        current_time = pygame.time.get_ticks()
        # Nếu chữ đã hiển thị hết, bắt đầu đếm thời gian trước khi chuyển tiếp
        if char_index == len(text_full) and dialogue_done_time is None:
            dialogue_done_time = current_time  # Lưu thời gian hoàn tất hội thoại

        # Sau khi hiện xong, chờ một lúc rồi chuyển tiếp hội thoại
        if dialogue_done_time and current_time - dialogue_done_time > DIALOGUE_DELAY:
            if dialogue_index < len(dialogues) - 1:
                dialogue_index += 1
                text_full = dialogues[dialogue_index].dialogue
                char_index = 0
                dialogue_done_time = None  # Reset thời gian hoàn thành hội thoại
            else:
                return "game_menu"

        if char_index < len(text_full) and current_time - last_update > TEXT_SPEED:
            char_index += 1
            last_update = current_time
            dialogues[dialogue_index].dialogue = text_full[:char_index]
        
        # hiển thị hội thoại
        draw_dialogue_box(dialogues[dialogue_index])

        for event in pygame.event.get(): # CHECK THAO TÁC
            if event.type == pygame.QUIT:
                return ""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return ""
                if event.key == pygame.K_SPACE:
                    if char_index < len(text_full):
                        char_index = len(text_full)
                        dialogues[dialogue_index].dialogue = text_full[:char_index]
                    else:
                        if dialogue_index < len(dialogues) - 1:
                            dialogue_index += 1
                            text_full = dialogues[dialogue_index].dialogue
                            char_index = 0
                            dialogue_done_time = None
                        else:
                            return "game_menu"
        pygame.display.flip() # CẬP NHẬT MÀN HÌNH
        pygame.time.Clock().tick(FPS)

def third_conversation():
    global number_of_coin, score, is_collecting, is_lack_of_coin # liên kết score => cập nhật best_score

    current_character = frontground(char_perry_plane_normal_image, character_x, character_y, character_width, character_height, 0, 0)
    twin_towers = obstacle(twin_towers_image, x_first_spawn, 0, 0, 0, obstacle_velocity_x)

    dialogues = [
        init_story_character("Bá Duy", ba_duy_image, "VÌ NGUYỄN THANH HÙNG!!!")
    ]

    # Chỉ số hội thoại hiện tại
    dialogue_index = 0
    text_full = dialogues[dialogue_index].dialogue  # Toàn bộ câu cần hiển thị
    char_index = 0  # Chỉ số ký tự hiện tại
    last_update = pygame.time.get_ticks()
    dialogue_done_time = None  # Biến lưu thời gian hoàn thành hội thoại

    while True:
        for background in background_list: # IN BACKGROUND
            background.move()
            background.print_image(screen)
            
            if background.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ra ngoài map
                background.reset_position()

        twin_towers.move()
        twin_towers.print_image(screen)

        if is_collided(current_character.x, current_character.y, current_character.hitbox, twin_towers.x, twin_towers.y, twin_towers.hitbox): # Game over nếu có va chạm
                pygame.mixer.Sound.play(plane_sound)
                return "game_over"

        for ground in ground_list: # IN GROUND
            ground.move()
            ground.print_image(screen)
            
            if ground.is_out_of_the_map(False, True, False, False): # Reset vị trí nếu ngoài map
                ground.reset_position()

        if current_character.is_collided_with_the_map(False, False, True, True): # CHECK GAME OVER KHI CHIM BAY NGOÀI MAP
            return "game_over"

        current_character.print_image(screen) # IN CHARACTER

        current_time = pygame.time.get_ticks()
        # Nếu chữ đã hiển thị hết, bắt đầu đếm thời gian trước khi chuyển tiếp
        if char_index == len(text_full) and dialogue_done_time is None:
            dialogue_done_time = current_time  # Lưu thời gian hoàn tất hội thoại

        # Sau khi hiện xong, chờ một lúc rồi chuyển tiếp hội thoại
        if dialogue_done_time and current_time - dialogue_done_time > DIALOGUE_DELAY:
            if dialogue_index < len(dialogues) - 1:
                dialogue_index += 1
                text_full = dialogues[dialogue_index].dialogue
                char_index = 0
                dialogue_done_time = None  # Reset thời gian hoàn thành hội thoại
            else:
                return "game_menu"

        if char_index < len(text_full) and current_time - last_update > TEXT_SPEED:
            char_index += 1
            last_update = current_time
            dialogues[dialogue_index].dialogue = text_full[:char_index]
        
        # hiển thị hội thoại
        draw_dialogue_box(dialogues[dialogue_index])

        for event in pygame.event.get(): # CHECK THAO TÁC
            if event.type == pygame.QUIT:
                return ""
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return ""
                
        pygame.display.flip() # CẬP NHẬT MÀN HÌNH
        pygame.time.Clock().tick(FPS)

'''DƯỚI ĐÂY LÀ CÁC THÔNG SỐ CÓ THỂ ĐƯỢC TUỲ CHỈNH SAO CHO PHÙ HỢP VỚI NGƯỜI CHƠI'''

# ĐIỂM SỐ GIỮA CÁC MODE
normal_mode_score_requirement = 10
hard_mode_score_requirement = 30

# THÔNG SỐ HỘI THOẠI

# Tốc độ hiển thị chữ (miligiây trên mỗi ký tự)
TEXT_SPEED = 50  # 50ms mỗi ký tự
DIALOGUE_DELAY = 2000  # 2 giây trước khi chuyển sang câu tiếp theo

# miliseconds per frame
miliseconds_per_frame = 1000 / FPS

# TẠO NHẠC NỀN
pygame.mixer.music.load(soundtrack_1)

# SOAB
sexy_girl = background(sexy_girl_image, 0, 0, WIDTH, HEIGHT, 0, 0)

# Menu
menu_game_over = background(menu_game_over_image, 0, 0, WIDTH, HEIGHT)

# TẠO NHÂN VẬT CỐT TRUYỆN
dialogue_box_x = 50
dialogue_box_y = 400
dialogue_box_width = WIDTH - dialogue_box_x * 2
dialogue_box_height = HEIGHT - dialogue_box_y - dialogue_box_x
dialogue_x = dialogue_box_x + 10
dialogue_y = dialogue_box_y + 10
dialogue_max_width = dialogue_box_width - 20
story_character_width = 100
story_character_height = story_character_width * 275 / 183
story_character_x = dialogue_box_x + dialogue_box_width - story_character_width
story_character_y = dialogue_box_y - story_character_height + 5

# STORY_LINE
first_time_playing_easy = True
first_time_playing_normal = True
first_time_playing_hard = True
first_time_collecting_10_coins = True
first_time_collecting_20_coins = True

# THÔNG SỐ NHÂN VẬT
character_width = 50
character_height = 50
character_x = (WIDTH - 200) // 2
character_y = (HEIGHT - 50) // 2
jump_power = -12
gravity = 1.2
beam_time_1 = 300 # Thời gian hết frame nhân vật đang nạp đạn (milisecond) từ lúc bấm nút
beam_time_2 = 600 # Thời gian hết frame nhân vật đang bắn (milisecond) từ lúc bấm nút
beam_time_3 = 700 # Thời gian hết frame đạn tan rã (milisecond) từ lúc bấm nút

# TẠO NHÂN VẬT
current_character = init_character(char_perry_ufo_normal_image, char_perry_ufo_jump_image_1, char_perry_ufo_jump_image_2, char_perry_ufo_collecting_image_1, char_perry_ufo_collecting_image_2, char_perry_ufo_collecting_image_3)
is_collecting = False

# THÔNG SỐ CỦA OBSTACLE
x_first_spawn = WIDTH * 1.5
distance_gap = 150 # Khoảng cách giữa 2 ống cống trên dưới
obstacle_width = 60 
obstacle_height = 500 
obstacle_velocity_x = -5 # TỐC ĐỘ DI CHUYỂN CỦA ỐNG CỐNG
distance_between_obstacles = 200 # Khoảng cách giữa 2 chướng ngại vật
number_of_obstacle = 2 # Số lượng vật cản tối đa có thể xuất hiện trên màn hình = number_of_obstacle 
obstacle_x_when_it_resets_position = distance_between_obstacles * number_of_obstacle + (number_of_obstacle - 1) * obstacle_width  # VỊ TRÍ hoành độ của ống cống spawn lại sau khi bay ra khỏi màn hình

# THÔNG SỐ MẶT ĐẤT
ground_width = WIDTH
ground_height = 100
ground_velocity_x = obstacle_velocity_x

# THÔNG SỐ COINS: CON BÒ
number_of_coin = 2 # Số lượng coin tối đa có thể xuất hiện trên màn hình = number_of_coin
coin_width = 70
coin_height = coin_width / 39 * 27 # tỉ lệ ảnh coin (nhân chéo chia ngang)
coin_y_when_it_resets_position = HEIGHT - coin_height - ground_height # vị trí theo chiều Ox là random và dựa theo obstacle nên không có ở đây
coin_velocity_x = obstacle_velocity_x
coin_dissapear_time = 2000 # Thời gian mà coin biến mất sau khi được nhặt
coin_max_height_when_it_is_disappearing = -100 # chiều cao bay lên tối đa của coin khi nó biến mất
coin_angular_velocity_when_it_is_disappearing = 15 # Tốc độ quay của coin khi bị nhặt (omega)
coin_accel_y_when_it_is_disappearing = 2 * coin_max_height_when_it_is_disappearing / miliseconds_per_frame / miliseconds_per_frame # gia tốc của coin khi nó biến mất (pixel / frame)
coin_accel_width_when_it_is_disappearing = 2 * -coin_width / miliseconds_per_frame / miliseconds_per_frame # Tốc độ co lại width của coin khi bị nhặt
coin_accel_height_when_it_is_disappearing = 2 * -coin_height / miliseconds_per_frame / miliseconds_per_frame # Tốc độ co lại height của coin khi bị nhặt

# THÔNG SỐ BACKGROUND
background_velocity_x = -1

# TẠO DANH SÁCH image
obstacle_list = []
ground_list = [] 
coin_list = []
background_list = []
init_obj(ground_list, obstacle_list, coin_list, background_list)

# TỐC ĐỘ GAME
game_speed = 1 # khởi đầu là 1x
score_at_max_game_speed = 100 # Điểm dừng tăng tiến tốc độ game
min_game_speed = 1 # Tốc độ game ban đầu
max_game_speed = 1.5 # Tốc độ game tối đa
game_speed_accel = (max_game_speed - min_game_speed) / score_at_max_game_speed # gia tốc của tốc độ game => gia tốc của vận tốc theo hoành độ

# SCORES
score = 0
best_score = 0
total_coins = 0

RANDOM_HINT = [
    "Press ↓ to have a long dic-",
    "Right-click for a long dic-",
    f"Score 69 for a sexy girl :)",
    f"Score {hard_mode_score_requirement} for a surprise",
    f"Score {normal_mode_score_requirement} = faster game speed",
    "Press 2 for 200 points",
    "Try pressing 1 :)",
]

# CÁC TRẠNG THÁI CỦA GAME
states = {
    "game_menu": game_menu,
    "game_playing_hard": game_playing_hard,
    "game_playing_normal": game_playing_normal,
    "game_playing_easy": game_playing_easy,
    "first_conversation": first_conversation,
    "second_conversation": second_conversation,
    "third_conversation": third_conversation,
    "game_over": game_over
}

# VÒNG LẶP CHÍNH CỦA GAME
current_state = "first_conversation"
current_game_mode = "game_playing_easy"
while current_state:
    current_state = states[current_state]()

pygame.quit()

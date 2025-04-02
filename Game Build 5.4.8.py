"""
Versione vicina al definitivo, con un sistema di ricarica e input nettamente migliorati.  presenta anche dei cambiamenti rispetto al personaggio utilizzato
"""
import random
import pygame
import assets as d

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1500, 700))
pygame.display.set_caption("HELLRUNNER 2184")
game_active = 7
flag_time = 0

"""
GAME ACTIVE 0 --> GIOCO
GAME ACTIVE 1 --> MENU'
GAME ACTIVE 2 --> GAME OVER
GAME ACTIVE 3 --> IMPOSTAZIONI
GAME ACTIVE 4 --> PLANET SELECTION
GAME ACTIVE 5 --> CHARACTER SELECTION
GAME ACTIVE 6 --> DIFFICULTY SELECTION
GAME ACTIVE 7 --> MAIN
GAME ACTIVE 8 --> INFO
"""

# --- GRUPPI SPRITES ---
gruppo_bullet = pygame.sprite.Group()
gruppo_nemico = pygame.sprite.Group()

# Limita il numero massimo di nemici sullo schermo
MAX_NEMICI = 10

player1_x = 80

""" FUNZIONI """


# --- SPAWN NEMICO ---
def spawn_nemico(x_player):
    global flag_time
    
    if len(gruppo_nemico) < MAX_NEMICI:  # Controlla il numero di nemici
        if flag_time == 0: num_nemici = random.randint(1, 3)
        elif flag_time == 1: num_nemici = random.randint(2, 4)
        elif flag_time == 2: num_nemici = random.randint(3, 5)
        for lol in range(num_nemici):
            if x_player <= 750:
                x = random.randint(900, 1500)
                y = random.randint(550, 700)
                nemico = d.Nemico(x, y, 2)
                gruppo_nemico.add(nemico)
            elif x_player > 750:
                x = random.randint(0, 600)
                y = random.randint(550, 700)
                nemico = d.Nemico(x, y, 2)
                gruppo_nemico.add(nemico)
                
spawn_nemico(player1_x)

# --- ANIMAZIONE PLAYER ---
def player1_animations():
    global player1_surf, player1_index, player1_invertita, player1_number
    player1_index += 0.13
    if player1_index >= len(player1_walks):
        player1_index = 0
    frame = player1_walks[int(player1_index)][player1_number]
    player1_surf = pygame.transform.flip(frame, True, False) if player1_invertita else frame
    
# --- ANIMAZIONE PLANET ---
def planet_animatios():
    global planet_surf, planet_index
    planet_index += 0.08
    if planet_index >= len(planet_cycle):
        planet_index=0
    frame = planet_cycle[int(planet_index)]
    planet_surf = frame

# --- ANIMAZIONE OFFICER ---
def officer_animations():
    global officer_surf, officer_index
    officer_index += 0.01
    if officer_index >= len(officer_cycle):
        officer_index=0
    frame = officer_cycle[int(officer_index)]
    officer_surf = frame

# --- FUNZIONE BARRA DELLA VITA ---
def draw_health_bar(surface, x, y, health, max_health, c_flag):
    ratio = health / max_health
    if c_flag == 0:
        pygame.draw.rect(surface, (255, 0, 0), (x, y, 200, 20))
        pygame.draw.rect(surface, (0, 255, 0), (x, y, 200 * ratio, 20))
        pygame.draw.rect(surface, (0, 0, 0), (x, y, 200, 20), 2)
    elif c_flag == 1:
        pygame.draw.rect(surface, (255, 0, 0), (x, y, 600, 20))
        pygame.draw.rect(surface, (0, 255, 0), (x, y, 200 * ratio, 20))
        pygame.draw.rect(surface, (0, 0, 0), (x, y, 600, 20), 2)

# --- UPDATE NEMICO ---
def update_nemici():
    gruppo_nemico.update(player1_rect.center, ground_rect)
    gruppo_nemico.draw(screen)

# --- MOVE PLAYER ---
def move_player():
    global player1_rect
    player1_rect.x += (player1_rl[1] - player1_rl[0]) * speed1
    player1_rect.y += (player1_ud[1] - player1_ud[0]) * speed1

""" FINE FUNZIONI """

# --- CARICAMENTO RISORSE ---

test_font20=pygame.font.Font("Font/Font_1.ttf",20)
test_font30=pygame.font.Font("Font/Font_1.ttf",30)
test_font40=pygame.font.Font("Font/Font_1.ttf",40)
test_font50=pygame.font.Font("Font/Font_1.ttf",50)
test_font60=pygame.font.Font("Font/Font_1.ttf",60)
player_name="Mark"

#Menu_1
fence=pygame.image.load("Models/Background/Menu_1/fence.png").convert_alpha()
fence_rect=fence.get_rect(topleft=(206,400))
hellpod=pygame.image.load("Models/Background/Menu_1/hellpod.png").convert_alpha()
hellpod_1_rect=hellpod.get_rect(topleft=(45,225))
hellpod_2_rect=hellpod.get_rect(topleft=(325,225))
hellpod_3_rect=hellpod.get_rect(topleft=(1044,225))
hellpod_4_rect=hellpod.get_rect(topleft=(1324,225))
menu_1_back=pygame.image.load("Models/Background/Menu_1/destroyer_back.png").convert_alpha()
impostazione=pygame.image.load("Models/Background/Menu_1/impostazione.png").convert_alpha()
impostazione_rect=impostazione.get_rect(topright=(1490,10))
info=pygame.image.load("Models/Background/Menu_1/info.png").convert_alpha()
info_rect=info.get_rect(topright=(1430,10))
planet_selection=pygame.image.load("Models/Background/Menu_1/planet_selection.png").convert_alpha()
planet_selection_rect=planet_selection.get_rect(topleft=(674,325))
erata_destroyer_back=pygame.image.load("Models/Background/Menu_1/erata_back.png").convert_alpha()
turing_destroyer_back=pygame.image.load("Models/Background/Menu_1/turing_back.png").convert_alpha()
gar_destroyer_back=pygame.image.load("Models/Background/Menu_1/gar_back.png").convert_alpha()
destroyer_back=erata_destroyer_back
officer_1=pygame.image.load("Models/Background/Menu_1/officer_1.png").convert_alpha()
officer_2=pygame.image.load("Models/Background/Menu_1/officer_2.png").convert_alpha()
officer_cycle=[officer_1,officer_2]
officer_index=0
officer_surf=officer_cycle[officer_index]
spazio=pygame.image.load("Models/Background/Menu_1/spazio.png").convert_alpha()
spazio_1_rect=spazio.get_rect(topleft=(76,210))
spazio_2_rect=spazio.get_rect(topleft=(356,210))
spazio_3_rect=spazio.get_rect(topleft=(1075,210))
spazio_4_rect=spazio.get_rect(topleft=(1355,210))
spazio_5_rect=spazio.get_rect(topleft=(716,200))

#Planet
planet_1=pygame.image.load("Models/Background/Planet/planet_1.png").convert_alpha()
planet_2=pygame.image.load("Models/Background/Planet/planet_2.png").convert_alpha()
planet_3=pygame.image.load("Models/Background/Planet/planet_3.png").convert_alpha()
planet_4=pygame.image.load("Models/Background/Planet/planet_4.png").convert_alpha()
planet_5=pygame.image.load("Models/Background/Planet/planet_5.png").convert_alpha()
planet_6=pygame.image.load("Models/Background/Planet/planet_6.png").convert_alpha()
planet_7=pygame.image.load("Models/Background/Planet/planet_7.png").convert_alpha()
planet_8=pygame.image.load("Models/Background/Planet/planet_8.png").convert_alpha()
planet_cycle=[planet_1,planet_2,planet_3,planet_4,planet_5,planet_6,planet_7,planet_8]
planet_index=0
planet_surf=planet_cycle[planet_index]

#Impostazioni
impostazioni_esc=test_font40.render("ESC to go back to destroyer", False, "Gold")
character_test=test_font40.render("Character", False, "Black").convert_alpha()
character_test_rect=character_test.get_rect(center=(750,125))
difficulty_test=test_font40.render("Difficulty", False, "Black").convert_alpha()
difficulty_test_rect=difficulty_test.get_rect(center=(750,325))
esc_test=test_font40.render("QUIT GAME", False, "Black").convert_alpha()
esc_test_rect=esc_test.get_rect(center=(750,525))
character=pygame.image.load("Models/Background/Impostazioni/character.png").convert_alpha()
character_rect=character.get_rect(midtop=(750,50))
difficulty=pygame.image.load("Models/Background/Impostazioni/difficulty.png").convert_alpha()
difficulty_rect=difficulty.get_rect(midtop=(750,250))
esc=pygame.image.load("Models/background/Impostazioni/esc.png").convert_alpha()
esc_rect=esc.get_rect(midtop=(750,450))

#Planet Selection
planet_esc=test_font40.render("ESC to go back to destroyer", False, "Gold")
erata_test=test_font40.render("Erata Prime", False, "Black").convert_alpha()
erata_test_rect=erata_test.get_rect(center=(750,125))
turing_test=test_font40.render("Turing", False, "Black").convert_alpha()
turing_test_rect=turing_test.get_rect(center=(750,325))
gar_test=test_font40.render("Gar Haren", False, "Black").convert_alpha()
gar_test_rect=gar_test.get_rect(center=(750,525))
erata_selection=pygame.image.load("Models/Background/Planet_Selection/copper_desert.png").convert_alpha()
erata_selection_rect=erata_selection.get_rect(midtop=(750,50))
turing_selection=pygame.image.load("Models/Background/Planet_Selection/ethernal_jungle.png").convert_alpha()
turing_selection_rect=turing_selection.get_rect(midtop=(750,250))
gar_selection=pygame.image.load("Models/background/Planet_Selection/foggy_swamp.png").convert_alpha()
gar_selection_rect=gar_selection.get_rect(midtop=(750,450))

#Character selection
character_esc=test_font40.render("ESC to go back to settings", False, "Gold")
mark_selection=pygame.image.load("Models/Background/Character_Selection/mark_selection.png").convert_alpha()
mark_selection_rect=mark_selection.get_rect(center=(487,350))
buck_selection=pygame.image.load("Models/Background/Character_Selection/buck_selection.png").convert_alpha()
buck_selection_rect=buck_selection.get_rect(center=(1013,350))
mark=pygame.image.load("Models/Background/Character_Selection/mark.png").convert_alpha()
mark_rect=mark.get_rect(center=(487,350))
buck=pygame.image.load("Models/Background/Character_Selection/buck.png").convert_alpha()
buck_rect=buck.get_rect(center=(1013,350))
mark_test=test_font50.render("Mark", False, (3,169,244))
mark_test_rect=mark_test.get_rect(center=(470,350))
buck_test=test_font50.render("Buck", False, (49,219,37))
buck_test_rect=buck_test.get_rect(center=(996,350))

#Difficulty selection
difficulty_esc=test_font40.render("ESC to go back to settings", False, "Gold")
lvl_3_selection=pygame.image.load("Models/Background/Difficulty_Selection/lvl_3.png").convert_alpha()
lvl_3_rect=lvl_3_selection.get_rect(midtop=(750,50))
lvl_6_selection=pygame.image.load("Models/Background/Difficulty_Selection/lvl_6.png").convert_alpha()
lvl_6_rect=lvl_6_selection.get_rect(midtop=(750,250))
lvl_9_selection=pygame.image.load("Models/Background/Difficulty_Selection/lvl_9.png").convert_alpha()
lvl_9_rect=lvl_9_selection.get_rect(midtop=(750,450))
lvl_3_test=test_font40.render("Medium", False, "Black").convert_alpha()
lvl_3_test_rect=lvl_3_test.get_rect(center=(750,125))
lvl_6_test=test_font40.render("Extreme", False, "Black").convert_alpha()
lvl_6_test_rect=lvl_6_test.get_rect(center=(750,325))
lvl_9_test=test_font40.render("Helldive", False, "Black").convert_alpha()
lvl_9_test_rect=lvl_9_test.get_rect(center=(750,525))

#Main Menu
main_back=pygame.image.load("Models/Background/Main/main_back.png").convert_alpha()
main_test=test_font60.render("HELLRUNNER 2148", False, "Black").convert_alpha()
main_test_rect=main_test.get_rect(center=(750,100))
start=test_font50.render("PRESS SPACE", False, "Black")
start_rect=start.get_rect(center=(750,600))

#Game
game_test=test_font20.render("ESC to go back to destroyer", False, "Gold")
game_test_rect=game_test.get_rect(topleft=(5,670))
erata_back1=pygame.image.load("Models/Background/Game/Erata/erata_back1.png").convert_alpha()
erata_back2=pygame.image.load("Models/Background/Game/Erata/erata_back2.png").convert_alpha()
erata_back=[erata_back1,erata_back2]

erata_ground=pygame.image.load("Models/Background/Game/Erata/erata_ground.png").convert_alpha()

turing_back1=pygame.image.load("Models/Background/Game/Turing/turing_back1.png").convert_alpha()
turing_back2=pygame.image.load("Models/Background/Game/Turing/turing_back2.png").convert_alpha()
turing_back=[turing_back1,turing_back2]

turing_ground=pygame.image.load("Models/Background/Game/Turing/turing_ground.png").convert_alpha()

gar_back1=pygame.image.load("Models/Background/Game/Gar/gar_back1.png").convert_alpha()
gar_back2=pygame.image.load("Models/Background/Game/Gar/gar_back2.png").convert_alpha()
gar_back=[gar_back1,gar_back2]

gar_ground=pygame.image.load("Models/Background/Game/Gar/gar_ground.png").convert_alpha()

back = erata_back[0]
ground = erata_ground
ground_rect = ground.get_rect(topleft=(0, 550))

#Info
info_esc=test_font40.render("ESC to go back to destroyer", False, "Gold")
info_test1=test_font40.render("This game is created by: Michele Baldi and Matteo Cristini",False,"Gold").convert_alpha()
info_test1_rect=info_test1.get_rect(topleft=(100,50))
info_test2=test_font40.render("To create this game we used python and the package: pygame",False,"Gold").convert_alpha()
info_test2_rect=info_test2.get_rect(topleft=(100,90))
info_test3=test_font40.render("We hope you'll enjoy it :p",False,"Gold").convert_alpha()
info_test3_rect=info_test3.get_rect(topleft=(100,130))
info_test4 = test_font20.render("All references to HELLDIVERS 2© are purely coincidental, we do not take responsibility for any inconveniences", False, "Gold")
info_test4_rect = info_test4.get_rect(topleft = (100, 600))

death_back = pygame.image.load("Models/Background/death_menu.png").convert()

# ---PLAYER---

"""buck"""
buck_stand=pygame.image.load("Models/Player1/Buck/buck_stand.png").convert_alpha()
buck_crouch=pygame.image.load("Models/Player1/Buck/buck_crouch.png").convert_alpha()
buck_jump=pygame.image.load("Models/Player1/Buck/buck_jump.png").convert_alpha()
buck_1=pygame.image.load("Models/Player1/Buck/buck_1.png").convert_alpha()
buck_2=pygame.image.load("Models/Player1/Buck/buck_2.png").convert_alpha()
buck_3=pygame.image.load("Models/Player1/Buck/buck_3.png").convert_alpha()
buck_4=pygame.image.load("Models/Player1/Buck/buck_4.png").convert_alpha()
buck_5=pygame.image.load("Models/Player1/Buck/buck_5.png").convert_alpha()
buck_6=pygame.image.load("Models/Player1/Buck/buck_6.png").convert_alpha()
buck_7=pygame.image.load("Models/Player1/Buck/buck_7.png").convert_alpha()
buck_8=pygame.image.load("Models/Player1/Buck/buck_8.png").convert_alpha()
buck_9=pygame.image.load("Models/Player1/Buck/buck_9.png").convert_alpha()
buck_10=pygame.image.load("Models/Player1/Buck/buck_10.png").convert_alpha()
buck_11=pygame.image.load("Models/Player1/Buck/buck_11.png").convert_alpha()

"""mark"""
mark_stand=pygame.image.load("Models/Player1/Mark/mark_stand.png").convert_alpha()
mark_crouch=pygame.image.load("Models/Player1/Mark/mark_crouch.png").convert_alpha()
mark_jump=pygame.image.load("Models/Player1/Mark/mark_jump.png").convert_alpha()
mark_1=pygame.image.load("Models/Player1/Mark/mark_1.png").convert_alpha()
mark_2=pygame.image.load("Models/Player1/Mark/mark_2.png").convert_alpha()
mark_3=pygame.image.load("Models/Player1/Mark/mark_3.png").convert_alpha()
mark_4=pygame.image.load("Models/Player1/Mark/mark_4.png").convert_alpha()
mark_5=pygame.image.load("Models/Player1/Mark/mark_5.png").convert_alpha()
mark_6=pygame.image.load("Models/Player1/Mark/mark_6.png").convert_alpha()
mark_7=pygame.image.load("Models/Player1/Mark/mark_7.png").convert_alpha()
mark_8=pygame.image.load("Models/Player1/Mark/mark_8.png").convert_alpha()
mark_9=pygame.image.load("Models/Player1/Mark/mark_9.png").convert_alpha()
mark_10=pygame.image.load("Models/Player1/Mark/mark_10.png").convert_alpha()
mark_11=pygame.image.load("Models/Player1/Mark/mark_11.png").convert_alpha()

player1_number=0 # 0 markipiler, 1 bucket
player1_stand = [mark_stand,buck_stand]
player1_jump = [mark_jump,buck_jump]
player1_crouch = [mark_crouch,buck_crouch]
player1_walks = [[mark_1,buck_1],[mark_2,buck_2],[mark_3,buck_3],[mark_4,buck_4],[mark_5,buck_5],\
                 [mark_6,buck_6],[mark_7,buck_7],\
                [mark_8,buck_8],[mark_9,buck_9],[mark_10,buck_10],[mark_11,buck_11]]
player1_index = 0
player1_surf = player1_walks[player1_index][player1_number]
player1_rect = player1_surf.get_rect(midbottom=(80, 570))

# Variabili player
character_flag = 0 # Mark=0, Buck=1

if character_flag == 0:
    speed1 = 6.5
    mov1 = [False, False, False, False]
    jump1 = False
    player1_bottom = 0
    player1_gravity = 0
    player1_invertita = False
    stand1 = True
    crouch1 = False
    player1_position = [stand1, crouch1,]
    player1_rl = [False, False]
    player1_ud = [False, False]

elif character_flag == 1:
    speed1 = 5
    mov1 = [False, False, False, False]
    jump1 = False
    player1_bottom = 0
    player1_gravity = 0
    player1_invertita = False
    stand1 = True
    crouch1 = False
    player1_position = [stand1, crouch1,]
    player1_rl = [False, False]
    player1_ud = [False, False]

dialogo_random = 0
spawn_delay = 3000

caricatore = 15
max_caricatore = 15  # Capacità massima del caricatore
mouse_block_timer = 0  # Timer per bloccare il mouse

# Barra della vita
if character_flag == 0:
    player1_health = 100
    max_health = 100
elif character_flag == 1:
    max_health = 300
    player1_health = 300

# Camera shake
shake_timer = 0
shake_intensity = 8

# Flash rosso
damage_flash = False
flash_timer = 0

# Suoni
"""armi"""
gun1 = pygame.mixer.Sound("Sound/Gun1.mp3")
gun1.set_volume(0.09)
"""colpito"""
hurt = pygame.mixer.Sound("Sound/hurt_sound.mp3")
hurt.set_volume(0.2)
"""morto"""
death = pygame.mixer.Sound("Sound/death_sound.mp3")
death.set_volume(0.2)
"""main theme"""
main_theme = pygame.mixer.Sound("Sound/main_theme.wav")
main_theme.set_volume(1)
"""game bg music"""
game_theme = pygame.mixer.Sound("Sound/Press_space_theme.wav")
game_theme.set_volume(0.43)
"""menu 1 bg music"""
menu_1_sound = pygame.mixer.Sound("Sound/menu_1_sound.wav")
menu_1_sound.set_volume(0.5)

"""urla"""
scream1 = pygame.mixer.Sound("Sound/scream1.mp3")
scream1.set_volume(0.3)
scream2 = pygame.mixer.Sound("Sound/scream2.mp3")
scream2.set_volume(0.3)
scream3 = pygame.mixer.Sound("Sound/scream3.mp3")
scream3.set_volume(0.3)
"""reload"""
reload_sound = pygame.mixer.Sound("Sound/reload.mp3")  # Suono di ricarica
reload_sound.set_volume(0.5)
"""empty_gun"""
empty_gun = pygame.mixer.Sound("Sound/empty_gun.mp3")
empty_gun.set_volume(0.5)
"""kill rerminid"""
kill_insect = pygame.mixer.Sound("Sound/kill_insect.mp3")
kill_insect.set_volume(0.5)


main_theme.play(loops = -1)

# Imposta un evento personalizzato per aggiornare "dialogo_random" ogni 30 secondi
UPDATE_DIALOGO = pygame.USEREVENT + 1
pygame.time.set_timer(UPDATE_DIALOGO, 23170)

# Aggiungi una variabile per il timer
game_timer = 301  # Tempo iniziale in secondi (es. 5 minuti)

# --- GAME LOOP ---
while True:

    #Cambio Nome destroyer
    destroyer_name=test_font30.render("\"Liberty Spreader\" lead by " + player_name, False, "Gold")

    # Riduci il timer di blocco del mouse
    if mouse_block_timer > 0:
        mouse_block_timer -= 1 / 60  # Scala il timer (1 frame = 1/60 di secondo)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active == 0:   # Main Game

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if mouse_block_timer <= 0:  # Controlla se il mouse non è bloccato
                    if caricatore > 0:
                        gun1.play()
                        direction = "right" if not player1_invertita else "left"
                        new_bullet = d.Bullet(player1_rect.centerx, player1_rect.centery, direction)
                        gruppo_bullet.add(new_bullet)
                        caricatore -= 1
                    else:
                        # Blocca il mouse per 0.02 secondi
                        empty_gun.play()
                        mouse_block_timer = 0.02

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Tasto per ricaricare
                    if caricatore == 15:
                        pass
                    else:
                        caricatore = max_caricatore  # Ricarica il caricatore
                        reload_sound.play()

                if event.key == pygame.K_ESCAPE:
                    game_active = 1
                    crouch1 = False
                    if character_flag == 0: speed1 = 6.5
                    elif character_flag == 1: speed1 = 4
                    if flag_time == 0:
                        game_timer = 301
                    elif flag_time == 1:
                        game_timer = 601
                    elif flag_time == 2:
                        game_timer = 901
                    menu_1_sound.play(loops = -1)
                    if character_flag == 0: player1_health = 100
                    elif character_flag == 1: player1_health = 300
                if event.key == pygame.K_a:
                    player1_rl[0] = True
                    mov1[0] = True
                    player1_invertita = True
                if event.key == pygame.K_d:
                    player1_rl[1] = True
                    mov1[1] = True
                    player1_invertita = False
                if not jump1:
                    if event.key == pygame.K_w:
                        player1_ud[0] = True
                        mov1[2] = True
                    if event.key == pygame.K_s:
                        player1_ud[1] = True
                        mov1[3] = True
                if not jump1:
                    if event.key == pygame.K_c:
                        if crouch1:
                            crouch1 = False
                            player1_position = [True, False, False, False]
                            if character_flag == 0: speed1 = 6.5
                            else: speed1 = 4
                            player1_rect.y -= 36
                        else:
                            if player1_position[0]: player1_rect.y += 36
                            crouch1 = True
                            player1_position = [False, True, False, False]
                            if character_flag == 0: speed1 = 3.5
                            elif character_flag == 1: speed1 = 1.5
                if 555 <= player1_rect.bottom <= 736:
                    if not crouch1 and not jump1:
                        if event.key == pygame.K_SPACE:
                            jump1 = True
                            player1_ud = [False, False]
                            player1_gravity = 25
                            player1_bottom = player1_rect.bottom
                if character_flag == 0:
                    if speed1 == 6.5 and event.key == pygame.K_LSHIFT:
                        speed1 = 10
                elif character_flag == 1:
                    if speed1 == 4 and event.key == pygame.K_LSHIFT:
                        speed1 = 7.5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player1_rl[0] = False
                    mov1[0] = False
                if event.key == pygame.K_d:
                    player1_rl[1] = False
                    mov1[1] = False
                if event.key == pygame.K_w:
                    player1_ud[0] = False
                    mov1[2] = False
                if event.key == pygame.K_s:
                    player1_ud[1] = False
                    mov1[3] = False
                if character_flag == 0:
                    if speed1 == 10 and event.key == pygame.K_LSHIFT:
                        speed1 = 6.5
                if character_flag == 1:
                    if speed1 == 7.5 and event.key == pygame.K_LSHIFT:
                        speed1 = 4

            if event.type == pygame.USEREVENT:
                spawn_nemico(player1_x)
                spawn_delay = max(1000, spawn_delay - 100)  # Riduce il delay minimo a 1 sec
                pygame.time.set_timer(pygame.USEREVENT, spawn_delay)
            
            # URLO SUPER-TERRESTRE
            if event.type == UPDATE_DIALOGO:
                dialogo_random = random.randint(0, 16)
                cass = random.randint(0, 2)
                if cass == 0: scream1.play()
                elif cass == 1: scream2.play()
                elif cass == 2: scream3.play()

        elif game_active == 1: # Menu 1
            game_theme.stop()
            main_theme.stop()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if impostazione_rect.collidepoint(event.pos):
                        game_active=3
                    if info_rect.collidepoint(event.pos):
                        game_active=8
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    game_active = 3
                if event.key == pygame.K_i:
                    game_active = 8
                if event.key == pygame.K_a:
                    player1_rl[0] = True
                    mov1[0] = True
                    player1_invertita = True
                if event.key == pygame.K_d:
                    player1_rl[1] = True
                    mov1[1] = True
                    player1_invertita = False
                if not jump1:
                    if event.key == pygame.K_w:
                        player1_ud[0] = True
                        mov1[2] = True
                    if event.key == pygame.K_s:
                        player1_ud[1] = True
                        mov1[3] = True
                
                #Inizio partita
                if player1_rect.colliderect(hellpod_1_rect) or player1_rect.colliderect(hellpod_2_rect) or player1_rect.colliderect(hellpod_3_rect) or player1_rect.colliderect(hellpod_4_rect):
                    if event.key == pygame.K_SPACE:
                        player1_rect = player1_surf.get_rect(midbottom=(80, 570))
                        menu_1_sound.stop()
                        game_theme.play(loops=-1)
                        caricatore = 15
                        game_active = 0
                
                #Planet selection
                if player1_rect.colliderect(planet_selection_rect):
                    if event.key == pygame.K_SPACE:
                        game_active = 4
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player1_rl[0] = False
                    mov1[0] = False
                if event.key == pygame.K_d:
                    player1_rl[1] = False
                    mov1[1] = False
                if event.key == pygame.K_w:
                    player1_ud[0] = False
                    mov1[2] = False
                if event.key == pygame.K_s:
                    player1_ud[1] = False
                    mov1[3] = False
        
        elif game_active == 2: # Game Over screen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_active = 0
                    if flag_time == 0:
                        game_timer = 301
                    elif flag_time == 1:
                        game_timer = 601
                    elif flag_time == 2:
                        game_timer = 901
                    game_theme.play(loops=-1)
                if event.key == pygame.K_ESCAPE:
                    game_active = 1
                    if flag_time == 0:
                        game_timer = 301
                    elif flag_time == 1:
                        game_timer = 601
                    elif flag_time == 2:
                        game_timer = 901
                    menu_1_sound.play()
       
        elif game_active == 3: # Impostazioni
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mov1 = [False, False, False, False]
                    player1_rl = [False, False]
                    player1_ud = [False, False]
                    game_active = 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if character_test_rect.collidepoint(event.pos) or character_rect.collidepoint(event.pos):
                    game_active=5
                if difficulty_test_rect.collidepoint(event.pos) or difficulty_rect.collidepoint(event.pos):
                    game_active=6
                if esc_test_rect.collidepoint(event.pos) or esc_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()

        elif game_active == 4: # Planet selection
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_active = 1
                    mov1 = [False, False, False, False]
                    player1_rl = [False, False]
                    player1_ud = [False, False]
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if erata_test_rect.collidepoint(event.pos) or erata_selection_rect.collidepoint(event.pos):
                        mov1 = [False, False, False, False]
                        player1_rl = [False, False]
                        player1_ud = [False, False]
                        h=random.randint(0,1)
                        game_active=1
                        destroyer_back=erata_destroyer_back
                        back=erata_back[h]
                        ground=erata_ground
                    if turing_test_rect.collidepoint(event.pos) or turing_selection_rect.collidepoint(event.pos):
                        mov1 = [False, False, False, False]
                        player1_rl = [False, False]
                        player1_ud = [False, False]
                        h=random.randint(0,1)
                        game_active=1
                        destroyer_back=turing_destroyer_back
                        back=turing_back[h]
                        ground=turing_ground
                    if gar_test_rect.collidepoint(event.pos) or gar_selection_rect.collidepoint(event.pos):
                        mov1 = [False, False, False, False]
                        player1_rl = [False, False]
                        player1_ud = [False, False]
                        h=random.randint(0,1)
                        game_active=1
                        destroyer_back=gar_destroyer_back
                        back=gar_back[h]
                        ground=gar_ground
        
        elif game_active == 5: #Character selection
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_active = 3
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if mark_test_rect.collidepoint(event.pos) or mark_selection_rect.collidepoint(event.pos):
                        game_active=1
                        player_name="Mark"
                        character_flag = 0
                        speed1 = 6.5
                        player1_health = 100
                        player1_number=0
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if buck_test_rect.collidepoint(event.pos) or buck_selection_rect.collidepoint(event.pos):
                        game_active=1
                        player_name="Buck"
                        character_flag = 1
                        speed1 = 4
                        player1_health = 300
                        player1_number=1
                    
        elif game_active == 6: #Difficulty selection
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if lvl_3_rect.collidepoint(event.pos) or lvl_3_test_rect.collidepoint(event.pos):
                    game_timer = 301
                    game_active = 3
                    flag_time = 0
                if lvl_6_rect.collidepoint(event.pos) or lvl_6_test_rect.collidepoint(event.pos):
                    game_timer = 601
                    game_active = 3
                    flag_time = 1
                if lvl_9_rect.collidepoint(event.pos) or lvl_9_test_rect.collidepoint(event.pos):
                    game_timer = 901
                    game_active = 3
                    flag_time = 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_active = 3
                  
        elif game_active == 7: #Main
              if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = 1
                    menu_1_sound.play(loops = -1)
            
        elif game_active == 8: #Info
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mov1 = [False, False, False, False]
                    player1_rl = [False, False]
                    player1_ud = [False, False]
                    game_active = 1
        
        elif game_active == 9: # VICTORY!!
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = 1
                    if flag_time == 0: game_timer = 301
                    elif flag_time == 1: game_timer = 601
                    elif flag_time == 2: game_timer = 901
                    mov1 = [False, False, False, False]
                    player1_rl = [False, False]
                    player1_ud = [False, False]
                    menu_1_sound.play(loops = -1)
        # --- LOGICA DI GIOCO ---
 
    if game_active == 0:
        # Logica di gioco
        update_nemici()
        gruppo_bullet.update()
        gruppo_bullet.draw(screen)
        screen.blit(player1_surf, player1_rect)

        # Aggiorna il timer
        if game_timer > 0:
            game_timer -= 1 / 60  # Scala il timer (1 secondo ogni 60 frame)

        

        # Controlla se il timer è scaduto
        if game_timer <= 0:
            game_active = 9  # Passa allo stato "VICTORY!!!"
            game_theme.stop()
            if character_flag == 0: player1_health = 100
            elif character_flag == 1: player1_health = 300

        # Blocco mappa
        player1_x = player1_rect.x
        
        if player1_rect.left <= 0: player1_rect.left = 0
        if player1_rect.right >= 1500: player1_rect.right = 1500
        
        # shake offset
        offset = [0, 0]
        if shake_timer > 0:
            offset[0] = random.randint(-shake_intensity, shake_intensity)
            offset[1] = random.randint(-shake_intensity, shake_intensity)
            shake_timer -= 1

        # Disegna lo sfondo e il terreno una sola volta
        screen.blit(back, (0, 0))
        screen.blit(ground, ground_rect)
        
        #Player 1
        
        if player1_position[0]:
            player1_surf = player1_stand
        elif player1_position[1]:
            player1_surf = player1_crouch
            
        #Se il Player1 è accovacciato o no
        if crouch1:
            player1_index = 0
            if player1_invertita:
                player1_surf = pygame.transform.flip(player1_crouch[player1_number], True, False)
            else:
                player1_surf = player1_crouch[player1_number]
            if player1_rect.bottom <= 596:
                player1_rect.bottom = 596
            if player1_rect.bottom >= 736:
                player1_rect.bottom = 736
        
        #Se il Player1 salta o no
        else:
            if jump1:
                player1_index = 0
                if player1_invertita:
                    player1_surf = pygame.transform.flip(player1_jump[player1_number], True, False)
                else:
                    player1_surf = player1_jump[player1_number]
                
                player1_rect.y -= player1_gravity
                player1_gravity -= 1
                if player1_rect.bottom >= 700:
                    player1_rect.bottom = 700
                    player1_bottom = 0
                    jump1=False
                    player1_gravity = 0
                if player1_rect.bottom == player1_bottom:
                    player1_rect.bottom=player1_bottom
                    player1_bottom=0
                    jump1=False
                    player1_gravity=0
            
            #Se il Player1 si sta muovendo
            elif stand1:
                        
                if player1_rect.bottom <= 560:
                    player1_rect.bottom = 560
                if player1_rect.bottom >= 700:
                    player1_rect.bottom = 700
                
                if mov1[0] != True and mov1[1] != True and mov1[2] != True and mov1[3] != True:
                    player1_index=0
                    if player1_invertita:
                        player1_surf=pygame.transform.flip(player1_stand[player1_number], True, False)
                    else:
                        player1_surf=player1_stand[player1_number]
                if mov1[0] or mov1[1] or mov1[2] or mov1[3]:
                    player1_animations()

        #Print a schermo del Player 1 e del movimento
        
        player1_rect.x += (player1_rl[1]-player1_rl[0])*speed1
        player1_rect.y += (player1_ud[1]-player1_ud[0])*speed1
        
        screen.blit(player1_surf, player1_rect)
        
        # Bullet e nemico
        gruppo_bullet.update()
        gruppo_bullet.draw(screen)
        update_nemici()

        # Collisioni
        for nemico in gruppo_nemico:
            if pygame.sprite.spritecollide(nemico, gruppo_bullet, True):
                nemico.health -= 1
                nemico.hit_timer = 5  # durata effetto rosso
                if nemico.health <= 0:
                    kill_insect.play()
                    nemico.kill()
                    pygame.time.set_timer(pygame.USEREVENT, 3000)

            if nemico.rect.colliderect(player1_rect):
                hurt.play()
                player1_health -= 10
                shake_timer = 10
                damage_flash = True
                flash_timer = 5
                nemico.kill()
                pygame.time.set_timer(pygame.USEREVENT, 3000)

        # Gestione delle collisioni tra proiettili e nemici
        collisions = pygame.sprite.groupcollide(gruppo_bullet, gruppo_nemico, True, False)
        for bullet, nemici in collisions.items():
            for nemico in nemici:
                nemico.health -= 1
                nemico.hit_timer = 5
                if nemico.health <= 0:
                    nemico.kill()

        # Barra vita
        draw_health_bar(screen, 20, 20, player1_health, max_health, character_flag)

        # Flash rosso ottimizzato
        if damage_flash:
            flash_overlay = pygame.Surface((1500, 700), pygame.SRCALPHA)
            flash_overlay.fill((255, 0, 0, 100))  # Usa trasparenza RGBA
            screen.blit(flash_overlay, (0, 0))
            flash_timer -= 1
            if flash_timer <= 0:
                damage_flash = False

        if player1_health <= 0:
            game_active = 2 # Stato game over
            
        screen.blit(game_test,game_test_rect)
        # Mostra il timer sullo schermo
        timer_text = test_font30.render(f"Tempo all'estrazione: {int(game_timer)}", True, "Gold")
        screen.blit(timer_text, (1100, 20))  # Posiziona il timer in alto a destra
        
        caricatore_text = test_font30.render(f"Bullets: {int(caricatore)}", True, "Black")
        screen.blit(caricatore_text, (25, 55))  # Posiziona il timer in alto a destra
        if caricatore == 0:
            RELOAD = test_font20.render("RELOAD!!  [R]", True, "Red")
            screen.blit(RELOAD, (25, 100))
    
    elif game_active == 1:
        
        screen.blit(destroyer_back,(0,0))
        screen.blit(menu_1_back,(0,0))
        screen.blit(hellpod,hellpod_1_rect)
        screen.blit(hellpod,hellpod_2_rect)
        screen.blit(hellpod,hellpod_3_rect)
        screen.blit(hellpod,hellpod_4_rect)
        screen.blit(impostazione,impostazione_rect)
        screen.blit(info,info_rect)
        screen.blit(destroyer_name,(10,5))
        
        # Blocco mappa
        if player1_rect.left <= 0: player1_rect.left = 0
        if player1_rect.right >= 1500: player1_rect.right = 1500
        if player1_rect.y <= 259: player1_rect.y = 259
        if player1_rect.y >= 325: player1_rect.y = 325
        
        #Player
        if mov1[0] != True and mov1[1] != True and mov1[2] != True and mov1[3] != True:
            player1_index=0
            if player1_invertita:
                player1_surf=pygame.transform.flip(player1_stand[player1_number], True, False)
            else:
                player1_surf=player1_stand[player1_number]
        if mov1[0] or mov1[1] or mov1[2] or mov1[3]:
            player1_animations()
                    
        player1_rect.x += (player1_rl[1]-player1_rl[0])*speed1
        player1_rect.y += (player1_ud[1]-player1_ud[0])*speed1
        screen.blit(player1_surf,player1_rect)
        
        screen.blit(fence,fence_rect)
        
        #Planet
        screen.blit(planet_surf,(594,275))
        planet_animatios()
        screen.blit(planet_selection,planet_selection_rect)
        
        #Collisioni
        if player1_rect.colliderect(hellpod_1_rect):
            screen.blit(spazio,spazio_1_rect)
        if player1_rect.colliderect(hellpod_2_rect):
            screen.blit(spazio,spazio_2_rect)
        if player1_rect.colliderect(hellpod_3_rect):
            screen.blit(spazio,spazio_3_rect)
        if player1_rect.colliderect(hellpod_4_rect):
            screen.blit(spazio,spazio_4_rect)
        if player1_rect.colliderect(planet_selection_rect):
            screen.blit(spazio,spazio_5_rect)
            
        #Officer
        screen.blit(officer_surf,(810,476))
        officer_animations()
            
    elif game_active == 2:
        game_theme.stop()
        if player1_health <= 0:
            death.play()
            if character_flag == 0: speed1 = 6.5
            else: speed1 = 4
            mov1 = [False, False, False, False]
            jump1 = False
            player1_bottom = 0
            player1_gravity = 0
            player1_invertita = False
            stand1 = True
            crouch1 = False
            player1_position = [stand1, crouch1,]
            player1_rl = [False, False]
            player1_ud = [False, False]
            caricatore = 15
            if character_flag == 0: player1_health = 100
            elif character_flag == 1: player1_health = 300
            player1_rect = player1_surf.get_rect(midbottom=(80, 570))
        
        screen.blit(death_back, (0, 0))

        # Reset del timer quando il gioco finisce
        game_timer = 300  # Reset a 5 minuti

    elif game_active == 3:
        
        screen.fill((9, 20, 26))
        screen.blit(character,character_rect)
        screen.blit(difficulty,difficulty_rect)
        screen.blit(esc,esc_rect)
        screen.blit(impostazioni_esc,(10,645))
        screen.blit(character_test,character_test_rect)
        screen.blit(difficulty_test,difficulty_test_rect)
        screen.blit(esc_test,esc_test_rect)
    
    elif game_active == 4:
        screen.fill((9,20,26))
        screen.blit(erata_selection,erata_selection_rect)
        screen.blit(turing_selection,turing_selection_rect)
        screen.blit(gar_selection,gar_selection_rect)
        screen.blit(planet_esc,(10,645))
        screen.blit(erata_test,erata_test_rect)
        screen.blit(turing_test,turing_test_rect)
        screen.blit(gar_test,gar_test_rect)

    elif game_active == 5:
        screen.fill((9,20,26))
        screen.blit(character_esc,(10,645))
        screen.blit(mark_selection,mark_selection_rect)
        screen.blit(buck_selection,buck_selection_rect)
        screen.blit(mark,mark_rect)
        screen.blit(buck,buck_rect)
        screen.blit(mark_test,mark_test_rect)
        screen.blit(buck_test,buck_test_rect)
        
    elif game_active == 6:
        screen.fill((9,20,26))
        screen.blit(difficulty_esc,(10,645))
        screen.blit(lvl_3_selection,lvl_3_rect)
        screen.blit(lvl_6_selection,lvl_6_rect)
        screen.blit(lvl_9_selection,lvl_9_rect)
        screen.blit(lvl_3_test,lvl_3_test_rect)
        screen.blit(lvl_6_test,lvl_6_test_rect)
        screen.blit(lvl_9_test,lvl_9_test_rect)
    
    elif game_active == 7:
        screen.blit(main_back,(0,0))
        screen.blit(main_test,main_test_rect)
        screen.blit(start,start_rect)
    
    elif game_active == 8:
        screen.fill((9,20,26))
        screen.blit(info_test1,info_test1_rect)
        screen.blit(info_test2,info_test2_rect)
        screen.blit(info_test3,info_test3_rect)
        screen.blit(info_test4,info_test4_rect)
        screen.blit(info_esc,(10,645))
    
    elif game_active == 9:
        screen.fill((128, 0, 104))
        
    pygame.display.update()
    clock.tick(60)
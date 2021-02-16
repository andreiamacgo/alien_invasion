import sys
import pygame
from bullet import Bullet
from alien import Alien

def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara um projétil se o limite ainda não for atingjido"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ Responde ao pressionamento de tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_event(ai_settings, screen, ship, bullets):
    """ Responde aos eventos de pressionamento de teclas e mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens,  bullets):
    screen.fill(ai_settings.bg_collor)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # faz a tela mais recente visível
    pygame.display.flip()


def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
    """Responde à colisão de aliens com os tiros"""
    # Remove qualquer tiro e alien que tenha coliido
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Atualiza a posição dos projéteis e some com os projéteis antigos"""
    # Atualiza a posição do projétil
    bullets.update()
     # Livrar-se dos projéteis que desapareceram da tela
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
             bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings,screen,ship,aliens,bullets)

    if len(aliens) == 0:
        # Destroi projéteis existentes e ria nova frota
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina o número de linhas de aliens que preenche a tela"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Cria um alien e o coloca na linha"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Cria uma frota de aliens"""
    # Cria um alien e encontra o número de aliens em uma linha
    # O espaço entre os aliens é igual ao comprimento de um alien
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # criando a primeira linhas de aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """Responde apropriadamente se algun alienúgena alcançar a borda da tela"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Descarta a tropa inteira e modifica a direção da tropo"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens):
    """Checa se a frota está na borda, e então atualiza a posição de todos os aliens na frota"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
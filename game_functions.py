import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara um tiro se o limite de tiros ainda não for atingjido"""
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


def check_event(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """ Responde aos eventos de pressionamento de teclas e mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Inicia um novo jogo quando clicar em jogar"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Redefine as configurações de jogo
        ai_settings.initialize_dynamic_settings()
        # Esconder o cursor do mouse
        pygame.mouse.set_visible(False)
        # Redefine as estatísticas do jogo
        stats.reset_stats()
        stats.game_active = True

        #Redefine as imagens do placar
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()

        # Esvazia a lista de aliens e tiros
        aliens.empty()
        bullets.empty()

        # Cria uma nova frota de aliens e centraliza a espaçonave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        print("Jogo iniciado")


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    screen.fill(ai_settings.bg_collor)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # Desenha informações e pontuação
    sb.show_score()

    # Desenha o botão de play se o jogo estiver ativo
    if not stats.game_active:
        play_button.draw_button()

    # faz visívela tela mais recentemente desenhada
    pygame.display.flip()


def check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Responde à colisão de aliens com os tiros"""
    # Remove qualquer tiro e alien que tenha colidido
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Atualiza a posição dos projéteis e some com os projéteis antigos"""
    # Atualiza a posição do projétil
    bullets.update()
    # Livrar-se dos projéteis que desapareceram da tela
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, stats, sb, ship, aliens, bullets)

    if len(aliens) == 0:
        # Se uma frota inteira for destruída, inicia um novo level
        bullets.empty()
        ai_settings.increase_speed()

        #Aumenta o level
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina o número de linhas de aliens que preenche a tela"""
    available_space_y = (ai_settings.screen_height - (6 * alien_height) - ship_height)
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


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Checa se algum alien alcançou o fundo da tela"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            print("Um alien atingiu o fundo da tela")
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Checa se a frota está na borda, e então atualiza a posição de todos os aliens na frota"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # produra por aliens atingindo o fundo da tela
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

    # procura por colisões entre alien e espaçonave
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Espaçonave atingida")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Responde à espaçonave sendo atingida por um alien"""
    if stats.ships_left > 1:
        # Diminui ships_left.
        stats.ships_left -= 1
        # esvazia a lista de aliens e tiros
        aliens.empty()
        bullets.empty()

        # cria nova frota e centraliza a espaçonave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
        print("\n******** Game Over ********\nFim do jogo, você perdeu!")

def check_high_score(stats, sb):
    """Checa se existe um novo recorde de Pontos"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

import pygame


def update_game_state(ship, bullets: pygame.sprite.Group):
    # update ship
    ship.update()
    # update bullets
    update_bullets(bullets)
    pygame.display.flip()


def update_bullets(bullets: pygame.sprite.Group):
    bullets.update()
    clear_bullets(bullets)


def clear_bullets(bullets: pygame.sprite.Group):
    for bullet in bullets.sprites():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

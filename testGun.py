from Gun import Gun


def test_gun_can_load_bullet():
    gun = Gun()
    gun.load(50)
    assert gun.number_of_bulets() == 50


def test_gun_can_load_bullet_and_shoot():
    gun = Gun()
    gun.load(50)
    assert gun.number_of_bulets() == 50
    gun.shoot()
    assert gun.number_of_bulets() == 49
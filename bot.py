def start():
    robot_ctrl.set_mode(rm_define_.robot_mode_free)
    led_ctrl.set_bottom_led(rm_define_armor_bottom_all, 69, 215, 255, rm_define.effect_always_on)
    armor_ctrl.set_hit_sensitivity(10)
    media_ctrl.zoom_value_update(1)
    vision_ctrl.enable_detection(rm_define.vision_detection_marker)
    gimbal_ctrl.set_follow_chassis_offset(0)
    gimba_ctrl.set_rotate_speed(30)
    if armor_ctrl.check_condition(rm_define.cond_armor_hit):
        gun_ctrl.stop()
    else:
        gun_ctrl.fire_continuous()
    def armor_hit_detection_all(msg):
        chassis_ctrl.enable_stick_overlay()
        led_ctrl.set_bottom_led(rm_define.armor_bottom_all, 255, 0, 0, rm_define.effect_flash)
        media_ctrl.play_sound(rm_define.media_sound_attacked)
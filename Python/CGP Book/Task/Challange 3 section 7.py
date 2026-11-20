import turtle
import random

def draw_albyn_portrait(x_offset=0, y_offset=0):
    screen = turtle.Screen()
    screen.bgcolor("#CFE2F3")
    screen.title("Portrait at Albyn School, Aberdeen")
    screen.setup(width=820, height=850)
    screen.tracer(0)

    t = turtle.Turtle()
    t.speed(0)

    def move_to(x, y):
        t.penup()
        t.goto(x + x_offset, y + y_offset)
        t.pendown()

    def draw_poly(points, outline, fill, size=2):
        t.color(outline, fill)
        t.pensize(size)
        it = iter(points)
        x0, y0 = next(it)
        move_to(x0, y0)
        t.begin_fill()
        for px, py in it:
            t.goto(px + x_offset, py + y_offset)
        t.goto(x0 + x_offset, y0 + y_offset)
        t.end_fill()

    def draw_line(points, color, size=2):
        t.color(color)
        t.pensize(size)
        it = iter(points)
        x0, y0 = next(it)
        move_to(x0, y0)
        for px, py in it:
            t.goto(px + x_offset, py + y_offset)

    # ==========================================
    # 1. SKY, TREES & ALBYN SCHOOL EXTERIOR
    # ==========================================
    for cx, cy, r in [(-280, 320, 35), (-250, 330, 42), (-215, 318, 32), (240, 340, 38), (275, 332, 45)]:
        move_to(cx, cy)
        t.color("#FFFFFF")
        t.begin_fill()
        t.circle(r)
        t.end_fill()

    for tx, ty, tr in [(-360, -80, 75), (-310, -40, 65), (320, -50, 70), (370, -90, 80)]:
        move_to(tx, ty)
        t.color("#4E6E52")
        t.begin_fill()
        t.circle(tr)
        t.end_fill()

    # Left Victorian Granite Villa
    draw_poly([(-380, -230), (-380, 145), (-115, 145), (-115, -230)], "#7E848C", "#B5BCC4", 2)
    draw_poly([(-390, 145), (-320, 235), (-245, 145)], "#3B424A", "#525B66", 2)
    draw_poly([(-255, 145), (-185, 240), (-110, 145)], "#3B424A", "#525B66", 2)
    draw_line([(-390, 145), (-320, 235), (-245, 145)], "#D5DCE3", 4)
    draw_line([(-255, 145), (-185, 240), (-110, 145)], "#D5DCE3", 4)
    draw_line([(-320, 235), (-320, 255)], "#2C3238", 3)
    draw_line([(-185, 240), (-185, 260)], "#2C3238", 3)
    draw_poly([(-365, 185), (-365, 255), (-340, 255), (-340, 185)], "#6E747C", "#9FA6B0", 2)
    draw_poly([(-145, 185), (-145, 255), (-120, 255), (-120, 185)], "#6E747C", "#9FA6B0", 2)

    for wx in (-345, -285, -215, -155):
        for wy in (55, -55):
            draw_poly([(wx, wy), (wx + 32, wy), (wx + 32, wy + 55), (wx, wy + 55)], "#E6ECF2", "#2C3E50", 2)
            draw_line([(wx, wy + 28), (wx + 32, wy + 28)], "#E6ECF2", 2)
            draw_line([(wx + 16, wy), (wx + 16, wy + 55)], "#E6ECF2", 1)

    # Central Modern Glass Atrium
    draw_poly([(-115, -230), (-115, 175), (145, 175), (145, -230)], "#46687A", "#88B5CC", 3)
    for gx in range(-115, 150, 32):
        draw_line([(gx, -230), (gx, 175)], "#5A7D91", 2)
    for gy in range(-210, 180, 38):
        draw_line([(-115, gy), (145, gy)], "#5A7D91", 2)
    draw_poly([(-95, 165), (-40, 165), (-105, -20), (-105, 95)], "#A8D0E6", "#BCE0F2", 1)
    draw_poly([(30, 165), (75, 165), (-15, -90), (-55, -90)], "#A8D0E6", "#BCE0F2", 1)

    # Albyn School Signboard Banner
    draw_poly([(-95, 118), (125, 118), (125, 152), (-95, 152)], "#14284B", "#1E3A6D", 2)
    move_to(15, 126)
    t.color("#FFFFFF")
    t.write("ALBYN SCHOOL", align="center", font=("Georgia", 13, "bold"))

    # Right Victorian Granite Wing
    draw_poly([(145, -230), (145, 160), (380, 160), (380, -230)], "#7E848C", "#AEB5BD", 2)
    draw_poly([(140, 160), (265, 225), (385, 160)], "#3B424A", "#525B66", 2)
    draw_poly([(325, 185), (325, 250), (355, 250), (355, 185)], "#6E747C", "#9FA6B0", 2)
    for wx in (175, 245, 315):
        for wy in (65, -45):
            draw_poly([(wx, wy), (wx + 34, wy), (wx + 34, wy + 55), (wx, wy + 55)], "#E6ECF2", "#2C3E50", 2)
            draw_line([(wx, wy + 28), (wx + 34, wy + 28)], "#E6ECF2", 2)

    # Courtyard Hedges & Granite Steps
    draw_poly([(-410, -245), (-410, -195), (-155, -195), (-155, -245)], "#38593C", "#4B7350", 2)
    draw_poly([(165, -245), (165, -195), (410, -195), (410, -245)], "#38593C", "#4B7350", 2)
    draw_poly([(-410, -350), (-410, -235), (410, -235), (410, -350)], "#8C7A6B", "#A39182", 2)
    draw_line([(-410, -275), (410, -275)], "#756558", 3)
    draw_line([(-410, -315), (410, -315)], "#756558", 3)

    # ==========================================
    # 2. GREY HERRINGBONE BLAZER & TEXTURE
    # ==========================================
    blazer_main = [
        (-210, -350), (-195, -130), (-175, -55), (-115, -25),
        (-65, -10), (65, -10), (115, -25), (175, -55),
        (195, -130), (210, -350)
    ]
    draw_poly(blazer_main, "#2A2D30", "#4A4E52", 3)

    random.seed(42)
    for y_tex in range(-330, -35, 14):
        x_limit = 165 if y_tex < -100 else 120
        for x_tex in range(-x_limit, x_limit, 18):
            if abs(x_tex) > 68 or y_tex < -240:
                shade = random.choice(["#3A3E42", "#595E63", "#42464A"])
                draw_line([(x_tex, y_tex), (x_tex + 6, y_tex + 8), (x_tex + 12, y_tex)], shade, 1)

    left_lapel = [(-68, -10), (-105, -30), (-82, -110), (-102, -135), (-55, -245), (-45, -180)]
    right_lapel = [(68, -10), (105, -30), (82, -110), (102, -135), (55, -245), (45, -180)]
    draw_poly(left_lapel, "#232629", "#52575C", 2)
    draw_poly(right_lapel, "#232629", "#52575C", 2)

    move_to(-42, -295)
    t.color("#1A1C1E", "#2F3236")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    draw_poly([(95, -125), (150, -132), (148, -144), (93, -137)], "#2A2D30", "#3F4347", 2)

    # ==========================================
    # 3. BLACK V-NECK SWEATER
    # ==========================================
    sweater_body = [
        (-65, -12), (-82, -140), (-75, -350), (75, -350),
        (82, -140), (65, -12), (42, -12), (0, -98), (-42, -12)
    ]
    draw_poly(sweater_body, "#0D0D0D", "#1B1C1E", 2)
    draw_line([(-45, -12), (0, -102), (45, -12)], "#2C2E33", 4)
    draw_line([(-50, -12), (0, -108), (50, -12)], "#121314", 2)

    # ==========================================
    # 4. BLUE CHECKERED SHIRT & STRIPED TIE
    # ==========================================
    shirt_collar = [(-44, -8), (-28, 22), (28, 22), (44, -8), (0, -95)]
    draw_poly(shirt_collar, "#7C96C4", "#D6E2F5", 2)

    for sx in range(-32, 34, 8):
        draw_line([(sx, -55), (sx, 12)], "#B4C7E7", 1)
    for sy in range(-50, 15, 8):
        draw_line([(-32, sy), (32, sy)], "#B4C7E7", 1)

    draw_poly([(-32, 18), (-44, -10), (-12, -32), (-8, -12)], "#6882B0", "#E3ECFA", 2)
    draw_poly([(32, 18), (44, -10), (12, -32), (8, -12)], "#6882B0", "#E3ECFA", 2)

    draw_poly([(-12, -16), (12, -16), (9, -36), (-9, -36)], "#12261E", "#1B3B2E", 2)
    draw_line([(-10, -22), (10, -30)], "#6E1E2A", 4)
    draw_line([(-10, -25), (10, -33)], "#D9E2EC", 1)

    tie_body = [(-9, -36), (9, -36), (16, -82), (0, -96), (-16, -82)]
    draw_poly(tie_body, "#12261E", "#1B3B2E", 2)
    draw_line([(-11, -46), (12, -58)], "#6E1E2A", 5)
    draw_line([(-11, -50), (12, -62)], "#E6ECF2", 1)
    draw_line([(-14, -66), (15, -80)], "#6E1E2A", 5)
    draw_line([(-14, -70), (15, -84)], "#E6ECF2", 1)

    # ==========================================
    # 5. NECK, EARS & ANATOMICAL HEAD CONTOUR
    # ==========================================
    draw_poly([(-30, 35), (30, 35), (28, -15), (-28, -15)], "#C98E77", "#EBB8A2", 2)
    draw_poly([(-28, 35), (28, 35), (22, 14), (-22, 14)], "#BA7E68", "#D49880", 1)

    draw_poly([(-72, 92), (-84, 86), (-82, 54), (-69, 48)], "#C98E77", "#EAB39C", 2)
    draw_line([(-75, 82), (-79, 70), (-74, 60)], "#B87A63", 2)

    draw_poly([(72, 92), (84, 86), (82, 54), (69, 48)], "#C98E77", "#EAB39C", 2)
    draw_line([(75, 82), (79, 70), (74, 60)], "#B87A63", 2)

    face_outline = [
        (0, 178), (-42, 172), (-68, 148), (-74, 105),
        (-71, 62), (-58, 32), (-32, 14), (0, 8),
        (32, 14), (58, 32), (71, 62), (74, 105),
        (68, 148), (42, 172)
    ]
    draw_poly(face_outline, "#C98E77", "#F7C8B4", 3)

    for cx in (-44, 44):
        move_to(cx, 54)
        t.color("#F2B29B")
        t.begin_fill()
        t.circle(16)
        t.end_fill()

    draw_line([(-12, 19), (0, 16), (12, 19)], "#D99B84", 2)

    # ==========================================
    # 6. DETAILED EYES, EYEBROWS & GLASSES
    # ==========================================
    draw_line([(-32, 134), (0, 137), (32, 134)], "#E3AA94", 1)
    draw_line([(-24, 126), (0, 128), (24, 126)], "#E3AA94", 1)

    draw_poly([(-54, 106), (-32, 111), (-13, 104), (-15, 99), (-34, 104), (-52, 101)], "#4A4A4A", "#5E5E5E", 1)
    draw_poly([(54, 106), (32, 111), (13, 104), (15, 99), (34, 104), (52, 101)], "#4A4A4A", "#5E5E5E", 1)

    for side in (-1, 1):
        ex = side * 32
        eye_pts = [
            (ex - 16, 88), (ex - 6, 94), (ex + 8, 93),
            (ex + 16, 87), (ex + 6, 83), (ex - 8, 84)
        ]
        draw_poly(eye_pts, "#9E6A58", "#FFFFFF", 1)

        move_to(ex, 84)
        t.color("#3B4D59", "#4F6675")
        t.begin_fill()
        t.circle(5)
        t.end_fill()

        move_to(ex, 86)
        t.color("#111111")
        t.begin_fill()
        t.circle(2.5)
        t.end_fill()

        move_to(ex + 2, 89)
        t.dot(2, "white")

        draw_line([(ex - 16, 90), (ex, 96), (ex + 16, 89)], "#8C5847", 2)
        draw_line([(ex + side * 18, 88), (ex + side * 27, 92)], "#C78B75", 1)
        draw_line([(ex + side * 18, 84), (ex + side * 28, 83)], "#C78B75", 1)

    draw_line([(-64, 97), (-56, 100), (-12, 96)], "#1B2631", 4)
    draw_line([(64, 97), (56, 100), (12, 96)], "#1B2631", 4)
    draw_line([(-64, 97), (-74, 93)], "#1B2631", 3)
    draw_line([(64, 97), (74, 93)], "#1B2631", 3)

    draw_line([(-12, 95), (0, 97), (12, 95)], "#2C3E50", 3)
    draw_line([(-11, 90), (-11, 82)], "#85929E", 2)
    draw_line([(11, 90), (11, 82)], "#85929E", 2)

    draw_line([(-58, 98), (-56, 74), (-14, 73), (-12, 95)], "#5D6D7E", 1)

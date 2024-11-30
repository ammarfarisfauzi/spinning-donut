import math
import time

def initialize_buffers(screen_width, screen_height):
    """Initialize character output and z-buffer."""
    char_output = [[' '] * screen_width for _ in range(screen_height)]
    zbuffer = [[0] * screen_width for _ in range(screen_height)]
    return char_output, zbuffer

def calculate_frame(A, B, char_output, zbuffer, screen_width, screen_height, R1, R2, K1, K2, theta_spacing, phi_spacing):
    """Calculate the next frame for the donut animation."""
    cosA, sinA = math.cos(A), math.sin(A)
    cosB, sinB = math.cos(B), math.sin(B)

    theta = 0
    while theta < 2 * math.pi:
        theta += theta_spacing
        costheta, sintheta = math.cos(theta), math.sin(theta)

        phi = 0
        while phi < 2 * math.pi:
            phi += phi_spacing
            cosphi, sinphi = math.cos(phi), math.sin(phi)

            circlex = R2 + R1 * costheta
            circley = R1 * sintheta

            x = circlex * (cosB * cosphi + sinA * sinB * sinphi) - circley * cosA * sinB
            y = circlex * (sinB * cosphi - sinA * cosB * sinphi) + circley * cosA * cosB
            z = K2 + cosA * circlex * sinphi + circley * sinA
            ooz = 1 / z

            xp = int(screen_width / 2 + K1 * ooz * x)
            yp = int(screen_height / 2 - K1 * ooz * y)

            L = cosphi * costheta * sinB - cosA * costheta * sinphi - sinA * sintheta + cosB * (cosA * sintheta - costheta * sinA * sinphi)

            if L > 0 and 0 <= xp < screen_width and 0 <= yp < screen_height:
                if ooz > zbuffer[yp][xp]:
                    zbuffer[yp][xp] = ooz
                    luminance_index = int(L * 8)
                    char_output[yp][xp] = '.,-~:;=!*#$@'[luminance_index]

def render_frame(char_output):
    """Render the frame to the screen."""
    print('\x1b[H', end='')
    for row in char_output:
        print(''.join(row))

def main():
    theta_spacing = 0.07
    phi_spacing = 0.02
    R1, R2 = 1, 2
    K2 = 6
    screen_width, screen_height = 35, 35
    K1 = screen_width * K2 * 3 / (8 * (R1 + R2))

    print('\x1b[2J')  

    A, B = 1.0, 1.0

    while True:
        char_output, zbuffer = initialize_buffers(screen_width, screen_height)
        calculate_frame(A, B, char_output, zbuffer, screen_width, screen_height, R1, R2, K1, K2, theta_spacing, phi_spacing)
        render_frame(char_output)
        A += 0.02
        B += 0.02
        time.sleep(0.03)

if __name__ == "__main__":
    main()

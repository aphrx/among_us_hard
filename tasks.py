import pyautogui
import time
import numpy as np
from PIL import ImageGrab, Image
import cv2
import pytesseract

def menu():
    print("What tasks would you like to do?")
    print("\nPart 1 Tasks")
    print("[0] Troubleshoot")
    print("[1] Submit Scan")
    print("[2] Download/Upload")
    print("[3] Accept Diverted Power/Stabilize Steering")
    print("[4] Empty Garbage")
    print("[5] Admin Swipe")
    print("[6] Fuel Engines")
    print("\nPart 2 Tasks")
    print("[7] Prime Shields")
    print("[8] Inspect Sample")
    print("[9] Align Engine")
    print("[10] Divert Power")
    print("[11] Fix Wires")
    print("[12] Calibrate Distributor")
    print("[13] Start Reactor")
    print("\nPart 3 Tasks")
    print("[14] Clean O2 Filter")
    print("[15] Clear Asteroids")
    print("[16] Chart Course")
    print("[17] Unlock Manifolds")

    option = int(input("\noptions: "))

    if option == 0:
        troubleshoot()
    elif option <= 17:
        start_task()
        if option == 2:
            download_upload()
        if option == 3:
            accept_diverted_stabilize()
        if option == 4:
            empty_garbage()
        if option == 5:
            admin_swipe()
        if option == 6:
            fuel_engines()
        if option == 7:
            prime_shields()
        if option == 8:
            inspect_sample()
        if option == 9:
            align_engine_output()
        if option == 10:
            divert_power()
        if option == 11:
            fix_wires()
        if option == 12:
            calibrate_distributor()
        if option == 13:
            start_reactor()
        if option == 14:
            clean_o2_filter()
        if option == 15:
            clear_asteroids()
        if option == 16:
            chart_course()
        if option == 17:
            unlock_manifolds()
    menu()

def troubleshoot():
    while True:
        print(pyautogui.position())

def start_task():
    pyautogui.moveTo(737, 549)
    pyautogui.click()
    time.sleep(0.5)

def download_upload():
    pyautogui.moveTo(414, 397)
    pyautogui.click()

def accept_diverted_stabilize():
    pyautogui.moveTo(401, 335)
    pyautogui.click()

def admin_swipe():
    pyautogui.moveTo(303, 483)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(157, 268)
    pyautogui.drag(600, 0, 0.8, button='left')

def empty_garbage():
    pyautogui.moveTo(576, 268)
    pyautogui.mouseDown()
    pyautogui.moveTo(576, 457)
    time.sleep(3)
    pyautogui.mouseUp()

def fuel_engines():
    pyautogui.moveTo(675, 515)
    pyautogui.mouseDown()
    time.sleep(3)
    pyautogui.mouseUp()

def prime_shields():
    tiles = [(410, 230), (496, 271), (474, 389), (377, 441), (300, 383), (322, 273), (421, 330)]
    red = (202, 94, 112)
    img = ImageGrab.grab(bbox=(0, 0, 800, 630))
    pix = img.load()
    for tile in tiles:
        if pix[tile] == red:
            pyautogui.moveTo(tile)
            pyautogui.click()

def inspect_sample():
    tubes = [(275, 360), (340, 360), (400, 360), (460, 360), (530, 360)]
    red = (246, 134, 134)
    pyautogui.moveTo(565, 554)
    pyautogui.click()
    time.sleep(70)
    img = ImageGrab.grab(bbox=(0, 0, 800, 630))
    pix = img.load()
    for tube in tubes:
        if pix[tube] == red:
            pyautogui.moveTo(tube[0], 500)
            pyautogui.click()

def align_engine_output():
    img = ImageGrab.grab(bbox=(0, 0, 800, 630))
    marker = (163, 163, 178)
    array = np.array(img)
    Y, X = np.where(np.all(array==marker, axis=2))
    pyautogui.moveTo(X[0], Y[0])
    pyautogui.mouseDown()
    pyautogui.moveTo(560, 330)
    pyautogui.mouseUp()

def divert_power():
    sliders = [(216, 471), (268, 471), (321, 471), (376, 471), (429, 471), (480, 471), (534, 471), (589, 471)]
    img = ImageGrab.grab(bbox=(0, 0, 800, 630))
    pix = img.load()
    for slider in sliders:
        print(pix[slider])
        if pix[slider][0] > 150:
            pyautogui.moveTo(slider)
            pyautogui.mouseDown()
            pyautogui.moveTo(slider[0], 405)
            pyautogui.mouseUp()

def fix_wires():
    wires = [(182, 185), (182, 289), (182, 392), (182, 495), (610, 185), (610, 289), (610, 392), (610, 495)]
    img = ImageGrab.grab(bbox=(0, 0, 800, 630))
    pix = img.load()
    for i in range(0, 4):
        for j in range(4, 8):
            if pix[wires[i]] == pix[wires[j]]:
                pyautogui.moveTo(wires[i])
                pyautogui.mouseDown()
                pyautogui.moveTo(wires[j])
                pyautogui.mouseUp()

def calibrate_distributor():
    distributor = [(315, 197), (315, 347), (315, 497)]
    marker = (71, 73, 71)
    buttons = [(555, 206), (549, 360), (557, 498)]
    for i in range(3):
        pyautogui.moveTo(buttons[i])
        while True:
            img = ImageGrab.grab(bbox=(0, 0, 800, 630))
            pix = img.load()
            print(pix[distributor[i]])
            if pix[distributor[i]] == marker:
                pyautogui.click()
                break

def start_reactor():
    lights = [(153, 285), (230, 285), (307, 285), (148, 360), (232, 362), (310, 365), (148, 440), (232, 440), (310, 440)] 
    buttons = [(500, 285), (568, 285), (642, 285), (500, 360), (568, 362), (642, 365), (500, 440), (568, 440), (642, 440)] 
    on = (68, 168, 255)

    for i in range(5):
        flashed = []
        while True:
            img = ImageGrab.grab(bbox=(0, 0, 800, 630))
            pix = img.load()
            for j in range(9):
                if(pix[lights[j]] == on):
                    flashed.append(j)
                    time.sleep(0.3)
            if len(flashed) == (i + 1):
                break
        
        time.sleep(0.5)
        print(flashed)
        for k in flashed:
            pyautogui.moveTo(buttons[k])
            pyautogui.click()
            time.sleep(0.2)

def clean_o2_filter():
    while True:
        img = ImageGrab.grab(bbox=(0, 0, 800, 630))
        array = np.array(img)
        leaf = (200, 149, 66)
        Y, X = np.where(np.all(array==leaf, axis=2))
        if len(X) != 0:
            pyautogui.moveTo(X[0], Y[0])
            pyautogui.dragTo(200, 324, 0.5, button='left')

def clear_asteroids():
    screen = [178, 105, 628, 554]
    asteroid = (55, 112, 66)
    while True:
        img = ImageGrab.grab(bbox=(screen))
        array = np.array(img)
        Y,X = np.where(np.all(array==asteroid, axis=2))
        if len(X) != 0:
            pyautogui.moveTo(X[0]+screen[0], Y[0]+screen[1])
            pyautogui.click()

def chart_course():
    screen = [128, 173, 677, 485]
    img = ImageGrab.grab(bbox=(screen))
    array = np.array(img)

    colors = (37, 111, 160)
    nodes = [180, 295, 400, 510, 620]

    Y,X = np.where(np.all(array==colors, axis=2))
    for node in nodes:
        x_avg = 0
        y_avg = 0
        counter = 0
        for i in range(len(X)):
            if((X[i] > (node-10)-screen[0]) and (X[i] < (node+40)-screen[0])):
                print(str(X[i]) + ", " + str(Y[i]))
                x_avg += X[i]
                y_avg += Y[i]
                counter += 1
        if counter != 0:
            pyautogui.moveTo(x_avg/counter + screen[0], y_avg/counter+screen[1])
            pyautogui.mouseDown()

def get_manifold_number():
    merged = Image.new("RGB", (700, 70))
    number_box = [(197, 250), (283, 250), (368, 250), (453, 250), (536, 250),(197, 340), (283, 340), (368, 340), (453, 340), (536, 340)]
    for i in range(10):
        img = ImageGrab.grab(bbox=(number_box[i][0], number_box[i][1],  number_box[i][0]+70, number_box[i][1]+70))
        merged.paste(img, (int(i*70), 0))

    img = np.array(merged)
    img = img[:, :, ::-1].copy()
    img[:, :, 0] = np.zeros([img.shape[0], img.shape[1]])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 3))
    dilate = cv2.dilate(thresh, kernel, iterations=3)

    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        aspect = w/h
        if aspect < 3:
            cv2.drawContours(thresh, [c], -1, (0,0,0), -1)

    result = 255-thresh
    result = cv2.GaussianBlur(result, (5,5), cv2.BORDER_DEFAULT)
    cv2.imwrite("processed.png", result)
    data = pytesseract.image_to_string(result, lang="eng", config="--psm 6 -c tessedit_char_whitelist=123456789N")
    return data.strip()

def unlock_manifolds():
    data = get_manifold_number()
    whitelist = "123456789N"
    print(data)
    if len(data) != 10:
        start_task()
        start_task()
        unlock_manifolds()
    for i in data:
        for j in whitelist:
            if i == j:
                whitelist = whitelist.replace(j, "")
    if whitelist == "":
        input_numbers(data)
    else:
        start_task()
        start_task()
        unlock_manifolds()

def input_numbers(data):
    print("Inputting Numbers...")
    order = list(data)
    numbers = [(197, 250), (283, 250), (368, 250), (453, 250), (536, 250),(197, 340), (283, 340), (368, 340), (453, 340), (536, 340)]
    for i in range(1, 11):
        for j in range(10):
            if order[j] == str(i) or (order[j] == "N" and i == 10):
                print(order[j] + " matched with " + str(i))
                pyautogui.moveTo(numbers[j])
                pyautogui.click()

menu()

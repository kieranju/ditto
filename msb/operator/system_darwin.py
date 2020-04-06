from msb.definitions import pyautogui
from msb.operator.definitions import KKey, MButton, OperatorInterface, Size, Point

from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGEventRightMouseDown
from Quartz.CoreGraphics import kCGEventRightMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGMouseButtonRight
from Quartz.CoreGraphics import kCGHIDEventTap

M_BUTTONS = {
    MButton.LEFT: {
        'press': kCGEventLeftMouseDown,
        'release': kCGEventLeftMouseUp,
        'event': kCGMouseButtonLeft,
    },
}

def m_event(type, x, y, button=kCGMouseButtonLeft):
    event = CGEventCreateMouseEvent(None, type, (x, y), button)
    CGEventPost(kCGHIDEventTap, event)

class Operator(OperatorInterface):
    def s_size(self) -> Size:
        return pyautogui.size()

    def m_location_get(self) -> Point:
        return pyautogui.position()

    def m_location_set(self, x: int, y: int):
        m_event(kCGEventMouseMoved, x, y)

    def m_press(self, button: MButton):
        position = self.m_location_get()
        m_event(M_BUTTONS[button]['press'], position.x, position.y, M_BUTTONS[button]['event'])

    def m_release(self, button: MButton):
        position = self.m_location_get()
        m_event(M_BUTTONS[button]['release'], position.x, position.y, M_BUTTONS[button]['event'])

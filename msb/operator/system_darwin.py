from msb.definitions import pyautogui
from msb.operator.definitions import KKey, MButton, OperatorInterface, Size, Point

from enum import Enum

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

class MEvent(Enum):
    TYPE, PRESS, RELEASE = range(3)

M_EVENTS = {
    MButton.LEFT: {
        MEvent.TYPE: kCGMouseButtonLeft,
        MEvent.PRESS: kCGEventLeftMouseDown,
        MEvent.RELEASE: kCGEventLeftMouseUp,
    },
    MButton.RIGHT: {
        MEvent.TYPE: kCGMouseButtonRight,
        MEvent.PRESS: kCGEventRightMouseDown,
        MEvent.RELEASE: kCGEventRightMouseUp,
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
        button_event = M_EVENTS[button]
        m_event(button_event[MEvent.PRESS], position.x, position.y, button_event[MEvent.TYPE])

    def m_release(self, button: MButton):
        position = self.m_location_get()
        button_event = M_EVENTS[button]
        m_event(button_event[MEvent.RELEASE], position.x, position.y, button_event[MEvent.TYPE])

    def k_press(self, key: KKey):
        # TODO: Create mapping for KKey to KEYBOARD_KEYS
        if key.name.lower() in pyautogui.KEYBOARD_KEYS:
            pyautogui.keyDown(key.name.lower())

    def k_release(self, key: KKey):
        # TODO: Create mapping for KKey to KEYBOARD_KEYS
        if key.name.lower() in pyautogui.KEYBOARD_KEYS:
            pyautogui.keyUp(key.name.lower())

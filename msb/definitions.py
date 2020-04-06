from importlib import import_module
import platform
import pyautogui

# PyAutoGUI configuration
pyautogui.MINIMUM_DURATION = 0  # Default: 0.1
pyautogui.MINIMUM_SLEEP = 0     # Default: 0.05
pyautogui.PAUSE = 0             # Default: 0.1

# System definitions
Operator = getattr(import_module('msb.operator.system_{}'.format(platform.system().lower())), 'Operator')
operator = Operator()

# Global
__all__ = ['pyautogui', 'operator']

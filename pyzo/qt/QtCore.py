#
# Copyright © 2014-2015 Colin Duquesnoy
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)

"""
Provides QtCore classes and functions.
"""
from . import PYQT6, PYQT5, PYSIDE2, PYSIDE6, PythonQtError


if PYQT6:
    from PyQt6 import QtCore
    from PyQt6.QtCore import *
    from PyQt6.QtCore import pyqtSignal as Signal
    from PyQt6.QtCore import pyqtBoundSignal as SignalInstance
    from PyQt6.QtCore import pyqtSlot as Slot
    from PyQt6.QtCore import pyqtProperty as Property
    from PyQt6.QtCore import QT_VERSION_STR as __version__

    # For issue #153
    from PyQt6.QtCore import QDateTime

    QDateTime.toPython = QDateTime.toPyDateTime

    # Map missing methods
    QCoreApplication.exec_ = QCoreApplication.exec
    QEventLoop.exec_ = QEventLoop.exec
    QThread.exec_ = QThread.exec

    QLibraryInfo.location = QLibraryInfo.path

    # Those are imported from `import *`
    del pyqtSignal, pyqtBoundSignal, pyqtSlot, pyqtProperty, QT_VERSION_STR

    from .enums_compat import promote_enums

    promote_enums(QtCore)
    QtCore.Qt.MidButton = QtCore.Qt.MiddleButton

    del QtCore

elif PYQT5:
    from PyQt5.QtCore import *
    from PyQt5.QtCore import pyqtSignal as Signal
    from PyQt5.QtCore import pyqtBoundSignal as SignalInstance
    from PyQt5.QtCore import pyqtSlot as Slot
    from PyQt5.QtCore import pyqtProperty as Property
    from PyQt5.QtCore import QT_VERSION_STR as __version__

    # For issue #153
    from PyQt5.QtCore import QDateTime

    QDateTime.toPython = QDateTime.toPyDateTime

    # Those are imported from `import *`
    del pyqtSignal, pyqtBoundSignal, pyqtSlot, pyqtProperty, QT_VERSION_STR

elif PYSIDE6:
    from PySide6.QtCore import *
    import PySide6
    from PySide6 import QtCore

    __version__ = PySide6.QtCore.__version__

    # Map DeprecationWarning methods
    QCoreApplication.exec_ = QCoreApplication.exec
    QEventLoop.exec_ = QEventLoop.exec
    QThread.exec_ = QThread.exec
    QTextStreamManipulator.exec_ = QTextStreamManipulator.exec

    from .enums_compat import promote_enums

    promote_enums(QtCore)
    QtCore.Qt.MidButton = QtCore.Qt.MiddleButton

    del QtCore

elif PYSIDE2:
    from PySide2.QtCore import *

    try:  # may be limited to PySide-5.11a1 only
        from PySide2.QtGui import QStringListModel
    except Exception:
        pass

    import PySide2.QtCore

    __version__ = PySide2.QtCore.__version__
else:
    raise PythonQtError("No Qt bindings could be found")
